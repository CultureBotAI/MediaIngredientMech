# Per-record structured review: Na3-citrate_X_2_H2o (data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml)

- Review: 20261017T083000Z-na3-citrate-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na3-citrate_X_2_H2o (data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml, record-aa6b49388cc41ecc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-aa6b49388cc41ecc | data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml | maintained | Na3-citrate_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-aa6b49388cc41ecc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-aa6b49388cc41ecc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-aa6b49388cc41ecc | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-aa6b49388cc41ecc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-aa6b49388cc41ecc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:44:03Z; reviewed SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10; current SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10; hash_changed=False. Reports=["reports/yaml_record_review/Na3-citrate_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:32142 sodium citrate dihydrate identity passes, but final other has malformed and hydrate-erasing labels.

## Findings

### rec-f-1634f09d1717f0f4: Historical review coverage and residual narrative: Na3-citrate_X_2_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-aa6b49388cc41ecc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:44:03Z; reviewed SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10; current SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10; hash_changed=False. Reports=["reports/yaml_record_review/Na3-citrate_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:32142 sodium citrate dihydrate identity passes, but final other has malformed and hydrate-erasing labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9ff50a568f9101e8 | data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1514],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32142","line":1516,"mapping_status":"MAPPED","ontology_id":"CHEBI:32142","preferred_term":"Na3-citrate x 2 H2O"}],"identifier":"CHEBI:32142","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":277,"edge_count":277,"occurrences":277},"occurrence_statistics":{"media_count":277,"total_occurrences":277},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32142","ontology_label":"sodium citrate dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na3-citrate x 2 H2O","sssom_rows":[{"data_row":2023,"object_id":"CHEBI:32142","object_label":"sodium citrate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na3-citrate_X_2_H2o","synonym_count":21} |
| ev-ee2d6b302e46e944 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1514] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a8cf0dbe15736f94 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na3-citrate_X_2_H2o; data-row positions=[2023] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2023,"object_id":"CHEBI:32142","object_label":"sodium citrate dihydrate","other":"2-hydroxy-1,2,3-propanetricarboxylic acid trisodium salt dihydrate&#124;Na2citrate x 2 H2O&#124;Na3-citrate x 2 H2O (0.6 g/l stock solution)&#124;Na3Citrate x 2 H2O&#124;Na3\u2010citrate x 2H2O&#124;Na3\u2010citrate\u00a0x\u00a02H2O&#124;Sodium citrate hydrate&#124;Trisodium Citrate Dihydrate&#124;trisodium 2-hydroxypropane-1,2,3-tricarboxylate--water (1/2)&#124;Trisodium citrate x 2 H2O&#124;Sodium Citrate&#124;Na2citrate&#124;Na3Citrate&#124;Sodiumcitrate&#124;Trisodium citrate dehydrate&#124;Trisodium citrate\u00b72H2O&#124;CAS:6132-04-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na3-citrate_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-3cc22785e9af4a3d | docs/data/mapped_ingredients.csv; CSV lines=[1516] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32142","line":1516,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"277","ontology_id":"CHEBI:32142","preferred_term":"Na3-citrate x 2 H2O","total_occurrences":"277"}] |
| ev-7edaefa969df8102 | reports/yaml_record_review/Na3-citrate_X_2_H2o.md; &#96;data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2ca4a36762f39d7a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1020] | context_only | [{"current_record_sha256":"3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10","finding_id":"SEM:6ff79ffdc4923527d8e4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na3-citrate-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na3-citrate_X_2_H2o (data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml)'
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
summary: Per-record structured review for Na3-citrate_X_2_H2o (data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml,
  record-aa6b49388cc41ecc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml
    sha256: 3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10
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
  - path: reports/yaml_record_review/Na3-citrate_X_2_H2o.md
    sha256: e467877f26d99be0dfeddee16bde66504c31905ee1e1fdf7d2fb8d885932402f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-aa6b49388cc41ecc
  path: data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml
  label: Na3-citrate_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-aa6b49388cc41ecc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-aa6b49388cc41ecc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-aa6b49388cc41ecc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-aa6b49388cc41ecc
evidence:
- evidence_id: ev-9ff50a568f9101e8
  kind: record_content
  reference: data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1514],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32142","line":1516,"mapping_status":"MAPPED","ontology_id":"CHEBI:32142","preferred_term":"Na3-citrate
    x 2 H2O"}],"identifier":"CHEBI:32142","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":277,"edge_count":277,"occurrences":277},"occurrence_statistics":{"media_count":277,"total_occurrences":277},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32142","ontology_label":"sodium
    citrate dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na3-citrate x
    2 H2O","sssom_rows":[{"data_row":2023,"object_id":"CHEBI:32142","object_label":"sodium
    citrate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na3-citrate_X_2_H2o","synonym_count":21}'
  snapshot_sha256: 3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10
- evidence_id: ev-ee2d6b302e46e944
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1514]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a8cf0dbe15736f94
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na3-citrate_X_2_H2o; data-row positions=[2023]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2023,"object_id":"CHEBI:32142","object_label":"sodium
    citrate dihydrate","other":"2-hydroxy-1,2,3-propanetricarboxylic acid trisodium
    salt dihydrate|Na2citrate x 2 H2O|Na3-citrate x 2 H2O (0.6 g/l stock solution)|Na3Citrate
    x 2 H2O|Na3\u2010citrate x 2H2O|Na3\u2010citrate\u00a0x\u00a02H2O|Sodium citrate
    hydrate|Trisodium Citrate Dihydrate|trisodium 2-hydroxypropane-1,2,3-tricarboxylate--water
    (1/2)|Trisodium citrate x 2 H2O|Sodium Citrate|Na2citrate|Na3Citrate|Sodiumcitrate|Trisodium
    citrate dehydrate|Trisodium citrate\u00b72H2O|CAS:6132-04-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na3-citrate_X_2_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3cc22785e9af4a3d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1516]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32142","line":1516,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"277","ontology_id":"CHEBI:32142","preferred_term":"Na3-citrate
    x 2 H2O","total_occurrences":"277"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7edaefa969df8102
  kind: prior_review
  reference: reports/yaml_record_review/Na3-citrate_X_2_H2o.md
  locator: '`data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e467877f26d99be0dfeddee16bde66504c31905ee1e1fdf7d2fb8d885932402f
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml`,\
    \ demote or reject\n  the malformed `Na2citrate` forms, the stock-solution label,\
    \ anhydrous/generic\n  citrate labels, and the `dehydrate` typo so they no longer\
    \ publish as exact\n  `CHEBI:32142` synonyms. Rebuild final SSSOM and rerun final\
    \ SSSOM validation\n  plus product label validation."
- evidence_id: ev-2ca4a36762f39d7a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1020]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10","finding_id":"SEM:6ff79ffdc4923527d8e4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-56e6ca27873c4eab
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-aa6b49388cc41ecc
  evidence_ids:
  - ev-9ff50a568f9101e8
  - ev-ee2d6b302e46e944
  - ev-a8cf0dbe15736f94
  - ev-3cc22785e9af4a3d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b51dcf70000e7243
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-aa6b49388cc41ecc
  evidence_ids:
  - ev-7edaefa969df8102
  - ev-9ff50a568f9101e8
  - ev-2ca4a36762f39d7a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:44:03Z;
    reviewed SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10;
    current SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10;
    hash_changed=False. Reports=["reports/yaml_record_review/Na3-citrate_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:32142 sodium citrate dihydrate identity passes, but final other has malformed
    and hydrate-erasing labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7edaefa969df8102
    - ev-9ff50a568f9101e8
  - name: legacy-native-ids
    value: '["SEM:6ff79ffdc4923527d8e4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9ff50a568f9101e8
    - ev-7edaefa969df8102
    - ev-2ca4a36762f39d7a
findings:
- finding_id: rec-f-1634f09d1717f0f4
  issue_key: mim-reconciliation-historical-review-coverage-and-r-aa6b49388cc41ecc
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na3-citrate_X_2_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:44:03Z;
    reviewed SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10;
    current SHA-256=3c1499ff6499f36840a5e3789a881515ef77b9db4781a38d4b2065b4838f8d10;
    hash_changed=False. Reports=["reports/yaml_record_review/Na3-citrate_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:32142 sodium citrate dihydrate identity passes, but final other has malformed
    and hydrate-erasing labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-aa6b49388cc41ecc
  evidence_ids:
  - ev-7edaefa969df8102
  - ev-9ff50a568f9101e8
  - ev-2ca4a36762f39d7a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na3-citrate_X_2_H2o.yaml
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
