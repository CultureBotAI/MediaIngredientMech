# Per-record structured review: Na2wo4_X_2_H2o (data/ingredients/mapped/Na2wo4_X_2_H2o.yaml)

- Review: 20261017T083000Z-na2wo4-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2wo4_X_2_H2o (data/ingredients/mapped/Na2wo4_X_2_H2o.yaml, record-3caced37c68a8c8e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2wo4_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2wo4_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3caced37c68a8c8e | data/ingredients/mapped/Na2wo4_X_2_H2o.yaml | maintained | Na2wo4_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3caced37c68a8c8e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3caced37c68a8c8e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3caced37c68a8c8e | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3caced37c68a8c8e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3caced37c68a8c8e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z; reviewed SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9; current SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9; hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63939 sodium tungstate dihydrate identity passes, but final other has concentration, malformed, and anhydrous-parent labels.

## Findings

### rec-f-9e4706b8d72ebb39: Historical review coverage and residual narrative: Na2wo4_X_2_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3caced37c68a8c8e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z; reviewed SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9; current SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9; hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63939 sodium tungstate dihydrate identity passes, but final other has concentration, malformed, and anhydrous-parent labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e06c6ae0d12c7516 | data/ingredients/mapped/Na2wo4_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1513],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63939","line":1515,"mapping_status":"MAPPED","ontology_id":"CHEBI:63939","preferred_term":"Na2WO4 x 2 H2O"}],"identifier":"CHEBI:63939","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1640,"edge_count":1640,"occurrences":1642},"occurrence_statistics":{"media_count":1640,"total_occurrences":1642},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63939","ontology_label":"sodium tungstate dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2WO4 x 2 H2O","sssom_rows":[{"data_row":2022,"object_id":"CHEBI:63939","object_label":"sodium tungstate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2wo4_X_2_H2o","synonym_count":25} |
| ev-7816b61e48cf2908 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1513] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d0a7228407db9baa | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2wo4_X_2_H2o; data-row positions=[2022] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2022,"object_id":"CHEBI:63939","object_label":"sodium tungstate dihydrate","other":"Na2WO4 . 2H2O&#124;Na2WO4 x 2 H2O (0.1% w/v)&#124;Na2WO4.2H2O&#124;Na2WO4\u00b72H2O&#124;Na2WO4\u30fb2H2O&#124;NaWO4\u00b72H2O&#124;Na-tungstate x 2 H2O&#124;Tungstic acid, sodium salt, dihydrate&#124;sodium orthotungstate dihydrate&#124;sodium tungstate(VI) dihydrate&#124;Na2WO4 \u00d7 2H2O&#124;Na2WO4*2H2O&#124;sodium dioxido(dioxo)tungsten--water (1/2)&#124;Na2WO2 x 2 H2O&#124;Na2WO4\u20222H2O&#124;Disodium tetraoxotungstate&#124;Na2WO2.2H2O&#124;Sodium tungstate(VI)&#124;Sodium tungsten oxide&#124;Sodium wolframate&#124;Tungstic acid, disodium salt&#124;sodium tetraoxotungstate(VI)&#124;CAS:10213-10-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2wo4_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-7b4d21fe7030a95a | docs/data/mapped_ingredients.csv; CSV lines=[1515] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63939","line":1515,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1640","ontology_id":"CHEBI:63939","preferred_term":"Na2WO4 x 2 H2O","total_occurrences":"1642"}] |
| ev-46a314fcc14f9bd4 | reports/yaml_record_review/Na2wo4_X_2_H2o.md; &#96;data/ingredients/mapped/Na2wo4_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7f7246ce64a6dcab | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1019] | context_only | [{"current_record_sha256":"b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9","finding_id":"SEM:477d3e4544224f5f805a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2wo4-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2wo4_X_2_H2o (data/ingredients/mapped/Na2wo4_X_2_H2o.yaml)'
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
summary: Per-record structured review for Na2wo4_X_2_H2o (data/ingredients/mapped/Na2wo4_X_2_H2o.yaml,
  record-3caced37c68a8c8e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2wo4_X_2_H2o.yaml
    sha256: b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9
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
  - path: reports/yaml_record_review/Na2wo4_X_2_H2o.md
    sha256: abdf3d32d738960b7e9ecc252b2c3ce58c6529c3c202b27320a98101700b03ac
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3caced37c68a8c8e
  path: data/ingredients/mapped/Na2wo4_X_2_H2o.yaml
  label: Na2wo4_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2wo4_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2wo4_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2wo4_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3caced37c68a8c8e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3caced37c68a8c8e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3caced37c68a8c8e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3caced37c68a8c8e
evidence:
- evidence_id: ev-e06c6ae0d12c7516
  kind: record_content
  reference: data/ingredients/mapped/Na2wo4_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1513],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63939","line":1515,"mapping_status":"MAPPED","ontology_id":"CHEBI:63939","preferred_term":"Na2WO4
    x 2 H2O"}],"identifier":"CHEBI:63939","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1640,"edge_count":1640,"occurrences":1642},"occurrence_statistics":{"media_count":1640,"total_occurrences":1642},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63939","ontology_label":"sodium
    tungstate dihydrate","ontology_source":"CHEBI"},"preferred_term":"Na2WO4 x 2 H2O","sssom_rows":[{"data_row":2022,"object_id":"CHEBI:63939","object_label":"sodium
    tungstate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2wo4_X_2_H2o","synonym_count":25}'
  snapshot_sha256: b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9
- evidence_id: ev-7816b61e48cf2908
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1513]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d0a7228407db9baa
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2wo4_X_2_H2o; data-row positions=[2022]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2022,"object_id":"CHEBI:63939","object_label":"sodium
    tungstate dihydrate","other":"Na2WO4 . 2H2O|Na2WO4 x 2 H2O (0.1% w/v)|Na2WO4.2H2O|Na2WO4\u00b72H2O|Na2WO4\u30fb2H2O|NaWO4\u00b72H2O|Na-tungstate
    x 2 H2O|Tungstic acid, sodium salt, dihydrate|sodium orthotungstate dihydrate|sodium
    tungstate(VI) dihydrate|Na2WO4 \u00d7 2H2O|Na2WO4*2H2O|sodium dioxido(dioxo)tungsten--water
    (1/2)|Na2WO2 x 2 H2O|Na2WO4\u20222H2O|Disodium tetraoxotungstate|Na2WO2.2H2O|Sodium
    tungstate(VI)|Sodium tungsten oxide|Sodium wolframate|Tungstic acid, disodium
    salt|sodium tetraoxotungstate(VI)|CAS:10213-10-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2wo4_X_2_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7b4d21fe7030a95a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1515]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63939","line":1515,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1640","ontology_id":"CHEBI:63939","preferred_term":"Na2WO4
    x 2 H2O","total_occurrences":"1642"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-46a314fcc14f9bd4
  kind: prior_review
  reference: reports/yaml_record_review/Na2wo4_X_2_H2o.md
  locator: '`data/ingredients/mapped/Na2wo4_X_2_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: abdf3d32d738960b7e9ecc252b2c3ce58c6529c3c202b27320a98101700b03ac
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2wo4_X_2_H2o.yaml`,\
    \ demote the\n  concentration-qualified, malformed, and bullet-dot raw labels\
    \ that should not\n  publish as exact `CHEBI:63939` synonyms.\n- Major: remove\
    \ the anhydrous `CHEBI:63940` aliases from the dihydrate record\n  or retype them\
    \ as rejected parent-term provenance. Rebuild final SSSOM and\n  rerun final SSSOM\
    \ validation plus product label validation."
- evidence_id: ev-7f7246ce64a6dcab
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1019]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9","finding_id":"SEM:477d3e4544224f5f805a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-aa1aaf6844fe2a72
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3caced37c68a8c8e
  evidence_ids:
  - ev-e06c6ae0d12c7516
  - ev-7816b61e48cf2908
  - ev-d0a7228407db9baa
  - ev-7b4d21fe7030a95a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-263ad7c1332217ab
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3caced37c68a8c8e
  evidence_ids:
  - ev-46a314fcc14f9bd4
  - ev-e06c6ae0d12c7516
  - ev-7f7246ce64a6dcab
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z;
    reviewed SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9;
    current SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:63939 sodium tungstate dihydrate identity passes, but final other has concentration,
    malformed, and anhydrous-parent labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-46a314fcc14f9bd4
    - ev-e06c6ae0d12c7516
  - name: legacy-native-ids
    value: '["SEM:477d3e4544224f5f805a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e06c6ae0d12c7516
    - ev-46a314fcc14f9bd4
    - ev-7f7246ce64a6dcab
findings:
- finding_id: rec-f-9e4706b8d72ebb39
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3caced37c68a8c8e
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2wo4_X_2_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:39:25Z;
    reviewed SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9;
    current SHA-256=b66951aba30cde0c3efe3b5ae2080a8d3445aebdffbd04b748e554f28358ffa9;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2wo4_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:63939 sodium tungstate dihydrate identity passes, but final other has concentration,
    malformed, and anhydrous-parent labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3caced37c68a8c8e
  evidence_ids:
  - ev-46a314fcc14f9bd4
  - ev-e06c6ae0d12c7516
  - ev-7f7246ce64a6dcab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2wo4_X_2_H2o.yaml
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
