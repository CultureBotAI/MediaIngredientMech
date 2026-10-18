# Per-record structured review: White_Wine (data/ingredients/mapped/White_Wine.yaml)

- Review: 20261017T083000Z-white-wine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for White_Wine (data/ingredients/mapped/White_Wine.yaml, record-05b748da1e731a52, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/White_Wine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/White_Wine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-05b748da1e731a52 | data/ingredients/mapped/White_Wine.yaml | maintained | White_Wine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-05b748da1e731a52 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-05b748da1e731a52 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-05b748da1e731a52 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-05b748da1e731a52.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-05b748da1e731a52.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:17:04Z; reviewed SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7; current SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7; hash_changed=False. Reports=["reports/yaml_record_review/White_Wine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT White Wine identity passes, but the fermented beverage is classified as a SINGLE_INGREDIENT.

## Findings

### rec-f-41a72f7133f96b52: Historical review coverage and residual narrative: White_Wine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-05b748da1e731a52.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:17:04Z; reviewed SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7; current SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7; hash_changed=False. Reports=["reports/yaml_record_review/White_Wine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT White Wine identity passes, but the fermented beverage is classified as a SINGLE_INGREDIENT.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2cde73aa903e6cb2 | data/ingredients/mapped/White_Wine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2059],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C84877","line":2061,"mapping_status":"MAPPED","ontology_id":"NCIT:C84877","preferred_term":"White wine"}],"identifier":"NCIT:C84877","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C84877","ontology_label":"White Wine","ontology_source":"NCIT"},"preferred_term":"White wine","sssom_rows":[{"data_row":2925,"object_id":"NCIT:C84877","object_label":"White Wine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:White_Wine","synonym_count":0} |
| ev-b3d168a015aa16c1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2059] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-62e3ee06e8bfac5b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:White_Wine; data-row positions=[2925] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2925,"object_id":"NCIT:C84877","object_label":"White Wine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:White_Wine","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-5291e6161f0a4344 | docs/data/mapped_ingredients.csv; CSV lines=[2061] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C84877","line":2061,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"NCIT:C84877","preferred_term":"White wine","total_occurrences":"5"}] |
| ev-cb178edb9ee372cd | reports/yaml_record_review/White_Wine.md; &#96;data/ingredients/mapped/White_Wine.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Issues:39; Completeness:46; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5c552afaa956b3b6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1347] | context_only | [{"current_record_sha256":"805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7","finding_id":"SEM:fcac1f2cf8ff76282357","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-white-wine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: White_Wine (data/ingredients/mapped/White_Wine.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for White_Wine (data/ingredients/mapped/White_Wine.yaml,
  record-05b748da1e731a52, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/White_Wine.yaml
    sha256: 805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7
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
  - path: reports/yaml_record_review/White_Wine.md
    sha256: 96f8d3dd9d32a3e74ec4c7c8fa18e70b7b2597dff4df5cfcd301dcf04f954fa5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-05b748da1e731a52
  path: data/ingredients/mapped/White_Wine.yaml
  label: White_Wine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/White_Wine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/White_Wine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/White_Wine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-05b748da1e731a52
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-05b748da1e731a52
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-05b748da1e731a52
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-05b748da1e731a52
evidence:
- evidence_id: ev-2cde73aa903e6cb2
  kind: record_content
  reference: data/ingredients/mapped/White_Wine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2059],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C84877","line":2061,"mapping_status":"MAPPED","ontology_id":"NCIT:C84877","preferred_term":"White
    wine"}],"identifier":"NCIT:C84877","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C84877","ontology_label":"White
    Wine","ontology_source":"NCIT"},"preferred_term":"White wine","sssom_rows":[{"data_row":2925,"object_id":"NCIT:C84877","object_label":"White
    Wine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:White_Wine","synonym_count":0}'
  snapshot_sha256: 805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7
- evidence_id: ev-b3d168a015aa16c1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2059]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-62e3ee06e8bfac5b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:White_Wine; data-row positions=[2925]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2925,"object_id":"NCIT:C84877","object_label":"White
    Wine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:White_Wine","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5291e6161f0a4344
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2061]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C84877","line":2061,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"NCIT:C84877","preferred_term":"White
    wine","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cb178edb9ee372cd
  kind: prior_review
  reference: reports/yaml_record_review/White_Wine.md
  locator: '`data/ingredients/mapped/White_Wine.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:31; Issues:39; Completeness:46; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 96f8d3dd9d32a3e74ec4c7c8fa18e70b7b2597dff4df5cfcd301dcf04f954fa5
  quote: "Issues:\n- Major: `ingredient_type: SINGLE_INGREDIENT` is incompatible with\
    \ the mapped\n  NCIT identity for a fermented white-grape beverage. The schema\
    \ reserves\n  `SINGLE_INGREDIENT` for pure compounds or single ingredients, while\
    \ white\n  wine is a complex mixture.\n\nRecommended Edits:\n- Reclassify this\
    \ record as `UNDEFINED_MIXTURE` unless a more specific local\n  stock-solution\
    \ treatment is intended.\n- Rerun strict validation and SSSOM invariant validation\
    \ after curation."
- evidence_id: ev-5c552afaa956b3b6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1347]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7","finding_id":"SEM:fcac1f2cf8ff76282357","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0b5f02b45bf6b0ff
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-05b748da1e731a52
  evidence_ids:
  - ev-2cde73aa903e6cb2
  - ev-b3d168a015aa16c1
  - ev-62e3ee06e8bfac5b
  - ev-5291e6161f0a4344
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-555db570f488c7cb
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-05b748da1e731a52
  evidence_ids:
  - ev-cb178edb9ee372cd
  - ev-2cde73aa903e6cb2
  - ev-5c552afaa956b3b6
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:17:04Z;
    reviewed SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7;
    current SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7;
    hash_changed=False. Reports=["reports/yaml_record_review/White_Wine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact NCIT
    White Wine identity passes, but the fermented beverage is classified as a SINGLE_INGREDIENT.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cb178edb9ee372cd
    - ev-2cde73aa903e6cb2
  - name: legacy-native-ids
    value: '["SEM:fcac1f2cf8ff76282357"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2cde73aa903e6cb2
    - ev-cb178edb9ee372cd
    - ev-5c552afaa956b3b6
findings:
- finding_id: rec-f-41a72f7133f96b52
  issue_key: mim-reconciliation-historical-review-coverage-and-r-05b748da1e731a52
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: White_Wine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:17:04Z;
    reviewed SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7;
    current SHA-256=805255a381f26e5786c98e54bc8213d36bb3a744460266b91f72785df56019a7;
    hash_changed=False. Reports=["reports/yaml_record_review/White_Wine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact NCIT
    White Wine identity passes, but the fermented beverage is classified as a SINGLE_INGREDIENT.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-05b748da1e731a52
  evidence_ids:
  - ev-cb178edb9ee372cd
  - ev-2cde73aa903e6cb2
  - ev-5c552afaa956b3b6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/White_Wine.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
