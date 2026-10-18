# Per-record structured review: Hydrous_Ferric_Oxide (data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml)

- Review: 20261017T083000Z-hydrous-ferric-oxide
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hydrous_Ferric_Oxide (data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml, record-2301e05ad491f798, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2301e05ad491f798 | data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml | maintained | Hydrous_Ferric_Oxide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2301e05ad491f798 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2301e05ad491f798 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2301e05ad491f798 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2301e05ad491f798.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2301e05ad491f798.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:54:17Z; reviewed SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b; current SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b; hash_changed=False. Reports=["reports/yaml_record_review/Hydrous_Ferric_Oxide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The hydrous source label exact-matches anhydrous ferric oxide and exports anhydrous iron oxide synonyms.

## Findings

### rec-f-8859df2ab5d7c0c6: Historical review coverage and residual narrative: Hydrous_Ferric_Oxide

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2301e05ad491f798.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:54:17Z; reviewed SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b; current SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b; hash_changed=False. Reports=["reports/yaml_record_review/Hydrous_Ferric_Oxide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The hydrous source label exact-matches anhydrous ferric oxide and exports anhydrous iron oxide synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8126c4a924e86dcc | data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1145],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:50819","line":1147,"mapping_status":"MAPPED","ontology_id":"CHEBI:50819","preferred_term":"hydrous ferric oxide"}],"identifier":"CHEBI:50819","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":50,"edge_count":50,"occurrences":50},"occurrence_statistics":{"media_count":50,"total_occurrences":50},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:50819","ontology_label":"ferric oxide","ontology_source":"CHEBI"},"preferred_term":"hydrous ferric oxide","sssom_rows":[{"data_row":1454,"object_id":"CHEBI:50819","object_label":"ferric oxide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydrous_Ferric_Oxide","synonym_count":4} |
| ev-e768dc76d45edb07 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1145] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-25c8fa9a4f134cad | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hydrous_Ferric_Oxide; data-row positions=[1454] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1454,"object_id":"CHEBI:50819","object_label":"ferric oxide","other":"diiron trioxide&#124;iron(3+) oxide&#124;iron(III) oxide","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydrous_Ferric_Oxide","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-af17f5b02f5dc4d3 | docs/data/mapped_ingredients.csv; CSV lines=[1147] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:50819","line":1147,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"50","ontology_id":"CHEBI:50819","preferred_term":"hydrous ferric oxide","total_occurrences":"50"}] |
| ev-d10ad2bbfcae4047 | reports/yaml_record_review/Hydrous_Ferric_Oxide.md; &#96;data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:33; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9b90a3291782f8c8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[740] | context_only | [{"current_record_sha256":"198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b","finding_id":"SEM:fc7475516f628e56b62d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hydrous-ferric-oxide
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hydrous_Ferric_Oxide (data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml)'
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
summary: Per-record structured review for Hydrous_Ferric_Oxide (data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml,
  record-2301e05ad491f798, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml
    sha256: 198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b
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
  - path: reports/yaml_record_review/Hydrous_Ferric_Oxide.md
    sha256: 54960c4d7c3369a3f59c2ec03a260c2eb587a0dd9c9cbff3d923bdce3911ce6b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2301e05ad491f798
  path: data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml
  label: Hydrous_Ferric_Oxide
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2301e05ad491f798
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2301e05ad491f798
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2301e05ad491f798
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2301e05ad491f798
evidence:
- evidence_id: ev-8126c4a924e86dcc
  kind: record_content
  reference: data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1145],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:50819","line":1147,"mapping_status":"MAPPED","ontology_id":"CHEBI:50819","preferred_term":"hydrous
    ferric oxide"}],"identifier":"CHEBI:50819","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":50,"edge_count":50,"occurrences":50},"occurrence_statistics":{"media_count":50,"total_occurrences":50},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:50819","ontology_label":"ferric
    oxide","ontology_source":"CHEBI"},"preferred_term":"hydrous ferric oxide","sssom_rows":[{"data_row":1454,"object_id":"CHEBI:50819","object_label":"ferric
    oxide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydrous_Ferric_Oxide","synonym_count":4}'
  snapshot_sha256: 198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b
- evidence_id: ev-e768dc76d45edb07
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1145]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-25c8fa9a4f134cad
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hydrous_Ferric_Oxide; data-row positions=[1454]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1454,"object_id":"CHEBI:50819","object_label":"ferric
    oxide","other":"diiron trioxide|iron(3+) oxide|iron(III) oxide","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydrous_Ferric_Oxide","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-af17f5b02f5dc4d3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1147]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:50819","line":1147,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"50","ontology_id":"CHEBI:50819","preferred_term":"hydrous
    ferric oxide","total_occurrences":"50"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d10ad2bbfcae4047
  kind: prior_review
  reference: reports/yaml_record_review/Hydrous_Ferric_Oxide.md
  locator: '`data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:33; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 54960c4d7c3369a3f59c2ec03a260c2eb587a0dd9c9cbff3d923bdce3911ce6b
  quote: "Recommended Edits:\n- Major: remap hydrous ferric oxide to a distinct local\
    \ registry identifier, or\n  to an exact external hydrous-ferric-oxide term if\
    \ one is found, and keep\n  `CHEBI:50819` only as a broader or related anhydrous\
    \ oxide target if that\n  relationship is chemically justified; then regenerate\
    \ the SSSOM and rerun\n  strict, term, round-trip, id-label, component, and SSSOM\
    \ validation."
- evidence_id: ev-9b90a3291782f8c8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[740]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b","finding_id":"SEM:fc7475516f628e56b62d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bfaffc365eda0e8b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2301e05ad491f798
  evidence_ids:
  - ev-8126c4a924e86dcc
  - ev-e768dc76d45edb07
  - ev-25c8fa9a4f134cad
  - ev-af17f5b02f5dc4d3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6b17736982859782
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2301e05ad491f798
  evidence_ids:
  - ev-d10ad2bbfcae4047
  - ev-8126c4a924e86dcc
  - ev-9b90a3291782f8c8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:54:17Z;
    reviewed SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b;
    current SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b;
    hash_changed=False. Reports=["reports/yaml_record_review/Hydrous_Ferric_Oxide.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The hydrous
    source label exact-matches anhydrous ferric oxide and exports anhydrous iron oxide
    synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d10ad2bbfcae4047
    - ev-8126c4a924e86dcc
  - name: legacy-native-ids
    value: '["SEM:fc7475516f628e56b62d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8126c4a924e86dcc
    - ev-d10ad2bbfcae4047
    - ev-9b90a3291782f8c8
findings:
- finding_id: rec-f-8859df2ab5d7c0c6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2301e05ad491f798
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Hydrous_Ferric_Oxide'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:54:17Z;
    reviewed SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b;
    current SHA-256=198628f2fbdba927b28160d4e708d59e7e7ab62ebeb3da6204d1b1277a33b09b;
    hash_changed=False. Reports=["reports/yaml_record_review/Hydrous_Ferric_Oxide.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The hydrous
    source label exact-matches anhydrous ferric oxide and exports anhydrous iron oxide
    synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2301e05ad491f798
  evidence_ids:
  - ev-d10ad2bbfcae4047
  - ev-8126c4a924e86dcc
  - ev-9b90a3291782f8c8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydrous_Ferric_Oxide.yaml
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
