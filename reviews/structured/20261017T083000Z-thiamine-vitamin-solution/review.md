# Per-record structured review: Thiamine_Vitamin_Solution (data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml)

- Review: 20261017T083000Z-thiamine-vitamin-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Thiamine_Vitamin_Solution (data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml, record-f790d2e32ec35d95, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f790d2e32ec35d95 | data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml | maintained | Thiamine_Vitamin_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f790d2e32ec35d95 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-f790d2e32ec35d95 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f790d2e32ec35d95 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f790d2e32ec35d95.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f790d2e32ec35d95.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z; reviewed SHA-256=4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c; current SHA-256=4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c; hash_changed=False. Reports=["reports/yaml_record_review/Thiamine_Vitamin_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity and final SSSOM rows pass, but the stock lacks components and VITAMIN_SOURCE is still provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-f790d2e32ec35d95.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5388cc135dbd82a4: Reassess prediction-only role support: Thiamine Vitamin Solution

major / open / confirmed; issue key: mim-reconciliation-role-support-f790d2e32ec35d95.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5388cc135dbd82a4

Reassess prediction-only role support: Thiamine Vitamin Solution

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c37dbb2afd12453d | data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1957],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","line":1959,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Thiamine Vitamin Solution"}],"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin solution","ontology_source":"MICRO"},"preferred_term":"Thiamine Vitamin Solution","sssom_rows":[{"data_row":2765,"object_id":"MICRO:0000460","object_label":"vitamin solution","predicate_id":"skos:closeMatch"},{"data_row":2766,"object_id":"kgmicrobe.ingredient:thiamine_vitamin_solution","object_label":"Thiamine Vitamin Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine_Vitamin_Solution","synonym_count":1} |
| ev-e28d5f27c3bb52a5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1957] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-05dd0611d99af1b5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Thiamine_Vitamin_Solution; data-row positions=[2765, 2766] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2765,"object_id":"MICRO:0000460","object_label":"vitamin solution","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Thiamine_Vitamin_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2766,"object_id":"kgmicrobe.ingredient:thiamine_vitamin_solution","object_label":"Thiamine Vitamin Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamine_Vitamin_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-375524556dbf7624 | docs/data/mapped_ingredients.csv; CSV lines=[1959] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","line":1959,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"14","ontology_id":"MICRO:0000460","preferred_term":"Thiamine Vitamin Solution","total_occurrences":"14"}] |
| ev-4f4f5a468f84d07d | reports/yaml_record_review/Thiamine_Vitamin_Solution.md; &#96;data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:35; Completeness:49; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-718abfd1f2d696b3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1284,2084] | context_only | [{"current_record_sha256":"4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c","finding_id":"SEM:9e9066a5b501b490c4ab","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c","finding_id":"SEM:59ffb6c0d2eaa6c94d02","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c9209afd00539792 | data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1957],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","line":1959,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Thiamine Vitamin Solution"}],"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin solution","ontology_source":"MICRO"},"preferred_term":"Thiamine Vitamin Solution","sssom_rows":[{"data_row":2765,"object_id":"MICRO:0000460","object_label":"vitamin solution","predicate_id":"skos:closeMatch"},{"data_row":2766,"object_id":"kgmicrobe.ingredient:thiamine_vitamin_solution","object_label":"Thiamine Vitamin Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine_Vitamin_Solution","synonym_count":1} |
| ev-243ae6ffb6fcd651 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-5388cc135dbd82a4] | context_only | Predecessor structured review finding f-5388cc135dbd82a4 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-thiamine-vitamin-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Thiamine_Vitamin_Solution (data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml)'
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
summary: Per-record structured review for Thiamine_Vitamin_Solution (data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml,
  record-f790d2e32ec35d95, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
    sha256: 4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Thiamine_Vitamin_Solution.md
    sha256: 6bce3bdd62d3ff97cdbd97943c7ba9825439ece3df122fbb73a9c0bb60813d4d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f790d2e32ec35d95
  path: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
  label: Thiamine_Vitamin_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f790d2e32ec35d95
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-c37dbb2afd12453d
  - ev-e28d5f27c3bb52a5
  - ev-05dd0611d99af1b5
  - ev-375524556dbf7624
  - ev-c9209afd00539792
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-c37dbb2afd12453d
  - ev-718abfd1f2d696b3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-4f4f5a468f84d07d
  - ev-718abfd1f2d696b3
  - ev-243ae6ffb6fcd651
evidence:
- evidence_id: ev-c37dbb2afd12453d
  kind: record_content
  reference: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1957],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","line":1959,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Thiamine
    Vitamin Solution"}],"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin
    solution","ontology_source":"MICRO"},"preferred_term":"Thiamine Vitamin Solution","sssom_rows":[{"data_row":2765,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","predicate_id":"skos:closeMatch"},{"data_row":2766,"object_id":"kgmicrobe.ingredient:thiamine_vitamin_solution","object_label":"Thiamine
    Vitamin Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine_Vitamin_Solution","synonym_count":1}'
  snapshot_sha256: 4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c
- evidence_id: ev-e28d5f27c3bb52a5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1957]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-05dd0611d99af1b5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Thiamine_Vitamin_Solution; data-row positions=[2765, 2766]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2765,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Thiamine_Vitamin_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2766,"object_id":"kgmicrobe.ingredient:thiamine_vitamin_solution","object_label":"Thiamine
    Vitamin Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Thiamine_Vitamin_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-375524556dbf7624
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1959]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","line":1959,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"14","ontology_id":"MICRO:0000460","preferred_term":"Thiamine
    Vitamin Solution","total_occurrences":"14"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4f4f5a468f84d07d
  kind: prior_review
  reference: reports/yaml_record_review/Thiamine_Vitamin_Solution.md
  locator: '`data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml`:2; Verdict:4;
    Identity:11; Validation:24; Evidence:35; Completeness:49; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6bce3bdd62d3ff97cdbd97943c7ba9825439ece3df122fbb73a9c0bb60813d4d
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml`,\
    \ curate\n  the stock recipe into `components` plus `component_assertion` if the\n\
    \  underlying source defines its ingredients. If the source really only names\
    \ an\n  opaque stock, annotate that bounded absence explicitly.\n- Major: replace\
    \ or remove the provisional `VITAMIN_SOURCE` role evidence.\n  Then rerun strict\
    \ validation, SSSOM publication, unknown-term triage,\n  component partonomy validation,\
    \ and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-718abfd1f2d696b3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1284,2084]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c","finding_id":"SEM:9e9066a5b501b490c4ab","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c","finding_id":"SEM:59ffb6c0d2eaa6c94d02","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c9209afd00539792
  kind: record_content
  reference: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1957],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","line":1959,"mapping_status":"MAPPED","ontology_id":"MICRO:0000460","preferred_term":"Thiamine
    Vitamin Solution"}],"identifier":"kgmicrobe.ingredient:thiamine_vitamin_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":14,"total_occurrences":14},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"MICRO:0000460","ontology_label":"vitamin
    solution","ontology_source":"MICRO"},"preferred_term":"Thiamine Vitamin Solution","sssom_rows":[{"data_row":2765,"object_id":"MICRO:0000460","object_label":"vitamin
    solution","predicate_id":"skos:closeMatch"},{"data_row":2766,"object_id":"kgmicrobe.ingredient:thiamine_vitamin_solution","object_label":"Thiamine
    Vitamin Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thiamine_Vitamin_Solution","synonym_count":1}'
  snapshot_sha256: 4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c
- evidence_id: ev-243ae6ffb6fcd651
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-5388cc135dbd82a4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5388cc135dbd82a4 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-df5e3720a1f6b217
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-c37dbb2afd12453d
  - ev-e28d5f27c3bb52a5
  - ev-05dd0611d99af1b5
  - ev-375524556dbf7624
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5e44175d903a00bd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-4f4f5a468f84d07d
  - ev-c37dbb2afd12453d
  - ev-718abfd1f2d696b3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:37:37Z;
    reviewed SHA-256=4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c;
    current SHA-256=4c48be23fcd0f01a354028889258574c342481c16d92fa546d3d10eb9bab6d8c;
    hash_changed=False. Reports=["reports/yaml_record_review/Thiamine_Vitamin_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity and final SSSOM rows pass, but the stock lacks components and VITAMIN_SOURCE
    is still provisional name-pattern evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4f4f5a468f84d07d
    - ev-c37dbb2afd12453d
  - name: legacy-native-ids
    value: '["SEM:9e9066a5b501b490c4ab","SEM:59ffb6c0d2eaa6c94d02"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c37dbb2afd12453d
    - ev-4f4f5a468f84d07d
    - ev-718abfd1f2d696b3
- assessment_id: a-c9209afd00539792
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-4f4f5a468f84d07d
  - ev-c9209afd00539792
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4f4f5a468f84d07d
    - ev-c9209afd00539792
findings:
- finding_id: rec-f-5388cc135dbd82a4
  issue_key: mim-reconciliation-role-support-f790d2e32ec35d95
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Thiamine Vitamin Solution'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f790d2e32ec35d95
  evidence_ids:
  - ev-4f4f5a468f84d07d
  - ev-c9209afd00539792
  - ev-243ae6ffb6fcd651
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-5388cc135dbd82a4
actions:
- action_id: rec-action-5388cc135dbd82a4
  description: 'Reassess prediction-only role support: Thiamine Vitamin Solution'
  finding_ids:
  - rec-f-5388cc135dbd82a4
  target_ids:
  - record-f790d2e32ec35d95
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thiamine_Vitamin_Solution.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
