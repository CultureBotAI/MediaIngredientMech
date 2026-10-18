# Per-record structured review: Ki (data/ingredients/mapped/Ki.yaml)

- Review: 20261017T083000Z-ki
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Ki (data/ingredients/mapped/Ki.yaml, record-57b162c1eb307490, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Ki.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Ki.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-57b162c1eb307490 | data/ingredients/mapped/Ki.yaml | maintained | Ki |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-57b162c1eb307490 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-57b162c1eb307490 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-57b162c1eb307490 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-57b162c1eb307490.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-57b162c1eb307490.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:49:17Z; reviewed SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a; current SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a; hash_changed=False. Reports=["reports/yaml_record_review/Ki.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact potassium iodide identity, CAS value, structure fields, occurrence count, curated KJ alias, and mineral-source role pass, but final SSSOM exports a concentration label as a synonym.

## Findings

### rec-f-446389f9cacc231e: Historical review coverage and residual narrative: Ki

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-57b162c1eb307490.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:49:17Z; reviewed SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a; current SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a; hash_changed=False. Reports=["reports/yaml_record_review/Ki.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact potassium iodide identity, CAS value, structure fields, occurrence count, curated KJ alias, and mineral-source role pass, but final SSSOM exports a concentration label as a synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b4149db66ec5a0d3 | data/ingredients/mapped/Ki.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1205],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:8346","line":1207,"mapping_status":"MAPPED","ontology_id":"CHEBI:8346","preferred_term":"KI"}],"identifier":"CHEBI:8346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":186,"edge_count":186,"occurrences":186},"occurrence_statistics":{"media_count":186,"total_occurrences":186},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:8346","ontology_label":"potassium iodide","ontology_source":"CHEBI"},"preferred_term":"KI","sssom_rows":[{"data_row":1549,"object_id":"CHEBI:8346","object_label":"potassium iodide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ki","synonym_count":7} |
| ev-10949771712173c7 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1205] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-327c41a9b3bf1e74 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Ki; data-row positions=[1549] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1549,"object_id":"CHEBI:8346","object_label":"potassium iodide","other":"Kaliumiodid&#124;KJ&#124;Kaliumjodid&#124;KI (0.01% w/v)&#124;CAS:7681-11-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Ki","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d790ac9d39dcc997 | docs/data/mapped_ingredients.csv; CSV lines=[1207] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:8346","line":1207,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"186","ontology_id":"CHEBI:8346","preferred_term":"KI","total_occurrences":"186"}] |
| ev-965e6ae6e8e6000f | reports/yaml_record_review/Ki.md; &#96;data/ingredients/mapped/Ki.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:58; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d71f6c2ad12dd091 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[776] | context_only | [{"current_record_sha256":"46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a","finding_id":"SEM:c0f37d82035dbcbb0fe2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-ki
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Ki (data/ingredients/mapped/Ki.yaml)'
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
summary: Per-record structured review for Ki (data/ingredients/mapped/Ki.yaml, record-57b162c1eb307490,
  mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Ki.yaml
    sha256: 46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Ki.md
    sha256: c99766ff2316e9811d814964993f8049359b77d064950b2c70969d2150db7929
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-57b162c1eb307490
  path: data/ingredients/mapped/Ki.yaml
  label: Ki
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ki.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Ki.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/Ki.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-57b162c1eb307490
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-57b162c1eb307490
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-57b162c1eb307490
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-57b162c1eb307490
evidence:
- evidence_id: ev-b4149db66ec5a0d3
  kind: record_content
  reference: data/ingredients/mapped/Ki.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1205],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:8346","line":1207,"mapping_status":"MAPPED","ontology_id":"CHEBI:8346","preferred_term":"KI"}],"identifier":"CHEBI:8346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":186,"edge_count":186,"occurrences":186},"occurrence_statistics":{"media_count":186,"total_occurrences":186},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:8346","ontology_label":"potassium
    iodide","ontology_source":"CHEBI"},"preferred_term":"KI","sssom_rows":[{"data_row":1549,"object_id":"CHEBI:8346","object_label":"potassium
    iodide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Ki","synonym_count":7}'
  snapshot_sha256: 46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a
- evidence_id: ev-10949771712173c7
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1205]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-327c41a9b3bf1e74
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Ki; data-row positions=[1549]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1549,"object_id":"CHEBI:8346","object_label":"potassium
    iodide","other":"Kaliumiodid|KJ|Kaliumjodid|KI (0.01% w/v)|CAS:7681-11-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Ki","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d790ac9d39dcc997
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1207]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:8346","line":1207,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"186","ontology_id":"CHEBI:8346","preferred_term":"KI","total_occurrences":"186"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-965e6ae6e8e6000f
  kind: prior_review
  reference: reports/yaml_record_review/Ki.md
  locator: '`data/ingredients/mapped/Ki.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:32; Completeness:58; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c99766ff2316e9811d814964993f8049359b77d064950b2c70969d2150db7929
  quote: "Recommended Edits:\n- Major: remove or demote `KI (0.01% w/v)` in\n  `data/ingredients/mapped/Ki.yaml`,\
    \ then regenerate the aggregate and final\n  SSSOM so it disappears from `mappings/ingredient_mappings.sssom.tsv`;\
    \ rerun\n  strict, term, round-trip, component, and SSSOM validation."
- evidence_id: ev-d71f6c2ad12dd091
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[776]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a","finding_id":"SEM:c0f37d82035dbcbb0fe2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c9dec18872089add
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-57b162c1eb307490
  evidence_ids:
  - ev-b4149db66ec5a0d3
  - ev-10949771712173c7
  - ev-327c41a9b3bf1e74
  - ev-d790ac9d39dcc997
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fbb3937ed99388c4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-57b162c1eb307490
  evidence_ids:
  - ev-965e6ae6e8e6000f
  - ev-b4149db66ec5a0d3
  - ev-d71f6c2ad12dd091
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:49:17Z;
    reviewed SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a;
    current SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a;
    hash_changed=False. Reports=["reports/yaml_record_review/Ki.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact potassium iodide
    identity, CAS value, structure fields, occurrence count, curated KJ alias, and
    mineral-source role pass, but final SSSOM exports a concentration label as a synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-965e6ae6e8e6000f
    - ev-b4149db66ec5a0d3
  - name: legacy-native-ids
    value: '["SEM:c0f37d82035dbcbb0fe2"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b4149db66ec5a0d3
    - ev-965e6ae6e8e6000f
    - ev-d71f6c2ad12dd091
findings:
- finding_id: rec-f-446389f9cacc231e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-57b162c1eb307490
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Ki'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:49:17Z;
    reviewed SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a;
    current SHA-256=46d38e549c32f9dcc80d19580c3aced0c41307894af886cffe1f0f85103b459a;
    hash_changed=False. Reports=["reports/yaml_record_review/Ki.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact potassium iodide
    identity, CAS value, structure fields, occurrence count, curated KJ alias, and
    mineral-source role pass, but final SSSOM exports a concentration label as a synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-57b162c1eb307490
  evidence_ids:
  - ev-965e6ae6e8e6000f
  - ev-b4149db66ec5a0d3
  - ev-d71f6c2ad12dd091
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Ki.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
