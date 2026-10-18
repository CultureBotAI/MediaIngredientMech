# Per-record structured review: Na2hpo4_X_12_H2o (data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml)

- Review: 20261017T083000Z-na2hpo4-x-12-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2hpo4_X_12_H2o (data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml, record-9e6009e25d9e9636, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9e6009e25d9e9636 | data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml | maintained | Na2hpo4_X_12_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9e6009e25d9e9636 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9e6009e25d9e9636 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9e6009e25d9e9636 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9e6009e25d9e9636.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9e6009e25d9e9636.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z; reviewed SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05; current SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05; hash_changed=False. Reports=["reports/yaml_record_review/Na2hpo4_X_12_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:91259 dodecahydrate identity passes, but final other has anhydrous-parent labels and the stored structure is anhydrous.

## Findings

### rec-f-13a318102fa47ba1: Historical review coverage and residual narrative: Na2hpo4_X_12_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9e6009e25d9e9636.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z; reviewed SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05; current SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05; hash_changed=False. Reports=["reports/yaml_record_review/Na2hpo4_X_12_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:91259 dodecahydrate identity passes, but final other has anhydrous-parent labels and the stored structure is anhydrous.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-241aa7364ff2aaa2 | data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1489],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91259","line":1491,"mapping_status":"MAPPED","ontology_id":"CHEBI:91259","preferred_term":"Na2HPO4 x 12 H2O"}],"identifier":"CHEBI:91259","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":159,"total_occurrences":159},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91259","ontology_label":"disodium hydrogenphosphate dodecahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2HPO4 x 12 H2O","sssom_rows":[{"data_row":1997,"object_id":"CHEBI:91259","object_label":"disodium hydrogenphosphate dodecahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2hpo4_X_12_H2o","synonym_count":16} |
| ev-dae7d188e431ea9a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1489] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-abe74b3bc7f1ee34 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2hpo4_X_12_H2o; data-row positions=[1997] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1997,"object_id":"CHEBI:91259","object_label":"disodium hydrogenphosphate dodecahydrate","other":"Na2HPO4 . 12H2O&#124;Na2HPO4.12H2O&#124;Na2HPO4\u00b712H2O&#124;Na2HPO4 \u00d7 12 H2O&#124;disodium acid orthophosphate&#124;disodium monohydrogen phosphate&#124;disodium orthophosphate&#124;CAS:10039-32-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2hpo4_X_12_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-3219a8f32f842b90 | docs/data/mapped_ingredients.csv; CSV lines=[1491] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:91259","line":1491,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"159","ontology_id":"CHEBI:91259","preferred_term":"Na2HPO4 x 12 H2O","total_occurrences":"159"}] |
| ev-38c0a2ad08416b62 | reports/yaml_record_review/Na2hpo4_X_12_H2o.md; &#96;data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml&#96;:2; Verdict:4; Identity:13; Validation:23; Evidence:31; Completeness:56; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-51df1af6397a829a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[996] | context_only | [{"current_record_sha256":"cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05","finding_id":"SEM:8cbb8d222f9e3e87d107","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2hpo4-x-12-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2hpo4_X_12_H2o (data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml)'
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
summary: Per-record structured review for Na2hpo4_X_12_H2o (data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml,
  record-9e6009e25d9e9636, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml
    sha256: cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05
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
  - path: reports/yaml_record_review/Na2hpo4_X_12_H2o.md
    sha256: 378bdbb1db776ead890ccadc1f12a9594d93d30f073b0e4c7cfabcdf1d7bdb8b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9e6009e25d9e9636
  path: data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml
  label: Na2hpo4_X_12_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9e6009e25d9e9636
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9e6009e25d9e9636
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9e6009e25d9e9636
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9e6009e25d9e9636
evidence:
- evidence_id: ev-241aa7364ff2aaa2
  kind: record_content
  reference: data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1489],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91259","line":1491,"mapping_status":"MAPPED","ontology_id":"CHEBI:91259","preferred_term":"Na2HPO4
    x 12 H2O"}],"identifier":"CHEBI:91259","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":159,"total_occurrences":159},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91259","ontology_label":"disodium
    hydrogenphosphate dodecahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2HPO4
    x 12 H2O","sssom_rows":[{"data_row":1997,"object_id":"CHEBI:91259","object_label":"disodium
    hydrogenphosphate dodecahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2hpo4_X_12_H2o","synonym_count":16}'
  snapshot_sha256: cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05
- evidence_id: ev-dae7d188e431ea9a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1489]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-abe74b3bc7f1ee34
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2hpo4_X_12_H2o; data-row positions=[1997]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1997,"object_id":"CHEBI:91259","object_label":"disodium
    hydrogenphosphate dodecahydrate","other":"Na2HPO4 . 12H2O|Na2HPO4.12H2O|Na2HPO4\u00b712H2O|Na2HPO4
    \u00d7 12 H2O|disodium acid orthophosphate|disodium monohydrogen phosphate|disodium
    orthophosphate|CAS:10039-32-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2hpo4_X_12_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3219a8f32f842b90
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1491]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:91259","line":1491,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"159","ontology_id":"CHEBI:91259","preferred_term":"Na2HPO4
    x 12 H2O","total_occurrences":"159"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-38c0a2ad08416b62
  kind: prior_review
  reference: reports/yaml_record_review/Na2hpo4_X_12_H2o.md
  locator: '`data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml`:2; Verdict:4; Identity:13;
    Validation:23; Evidence:31; Completeness:56; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 378bdbb1db776ead890ccadc1f12a9594d93d30f073b0e4c7cfabcdf1d7bdb8b
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml`,\
    \ mark the three\n  anhydrous-parent labels as `REJECTED_LABEL` or otherwise keep\
    \ them\n  provenance-only, then rebuild final SSSOM and rerun the final SSSOM\
    \ plus\n  product label validators.\n- Major: replace the inherited anhydrous\
    \ InChI and SMILES with structure values\n  that include twelve waters of hydration.\n\
    - Minor: prune or explicitly mark the superseded registry-mint and close-match\n\
    \  `ontology_mapping.evidence` notes so the active exact ChEBI mapping carries\n\
    \  only current evidence."
- evidence_id: ev-51df1af6397a829a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[996]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05","finding_id":"SEM:8cbb8d222f9e3e87d107","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e101036b9d2e51ee
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9e6009e25d9e9636
  evidence_ids:
  - ev-241aa7364ff2aaa2
  - ev-dae7d188e431ea9a
  - ev-abe74b3bc7f1ee34
  - ev-3219a8f32f842b90
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c66190014b2608b1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9e6009e25d9e9636
  evidence_ids:
  - ev-38c0a2ad08416b62
  - ev-241aa7364ff2aaa2
  - ev-51df1af6397a829a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z;
    reviewed SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05;
    current SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2hpo4_X_12_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:91259 dodecahydrate identity passes, but final other has anhydrous-parent
    labels and the stored structure is anhydrous.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-38c0a2ad08416b62
    - ev-241aa7364ff2aaa2
  - name: legacy-native-ids
    value: '["SEM:8cbb8d222f9e3e87d107"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-241aa7364ff2aaa2
    - ev-38c0a2ad08416b62
    - ev-51df1af6397a829a
findings:
- finding_id: rec-f-13a318102fa47ba1
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9e6009e25d9e9636
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2hpo4_X_12_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:14:57Z;
    reviewed SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05;
    current SHA-256=cd257bc36c2fff1d5cb48b640b2146dbca2804e4b67a9e125af1029ee234ca05;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2hpo4_X_12_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:91259 dodecahydrate identity passes, but final other has anhydrous-parent
    labels and the stored structure is anhydrous.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9e6009e25d9e9636
  evidence_ids:
  - ev-38c0a2ad08416b62
  - ev-241aa7364ff2aaa2
  - ev-51df1af6397a829a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_12_H2o.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
