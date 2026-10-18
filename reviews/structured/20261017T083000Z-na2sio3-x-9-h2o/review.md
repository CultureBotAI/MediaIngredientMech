# Per-record structured review: Na2sio3_X_9_H2o (data/ingredients/mapped/Na2sio3_X_9_H2o.yaml)

- Review: 20261017T083000Z-na2sio3-x-9-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2sio3_X_9_H2o (data/ingredients/mapped/Na2sio3_X_9_H2o.yaml, record-5d33bb3aede92fc4, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2sio3_X_9_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2sio3_X_9_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5d33bb3aede92fc4 | data/ingredients/mapped/Na2sio3_X_9_H2o.yaml | maintained | Na2sio3_X_9_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5d33bb3aede92fc4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-5d33bb3aede92fc4 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5d33bb3aede92fc4 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5d33bb3aede92fc4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5d33bb3aede92fc4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:35:01Z; reviewed SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b; current SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b; hash_changed=False. Reports=["reports/yaml_record_review/Na2sio3_X_9_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132108 sodium silicate nonahydrate identity passes, but final other has anhydrous, typoed, and catalog labels.

## Findings

### rec-f-f7e1cde19dd87af2: Historical review coverage and residual narrative: Na2sio3_X_9_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-5d33bb3aede92fc4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:35:01Z; reviewed SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b; current SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b; hash_changed=False. Reports=["reports/yaml_record_review/Na2sio3_X_9_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132108 sodium silicate nonahydrate identity passes, but final other has anhydrous, typoed, and catalog labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0bcbcd31639581bc | data/ingredients/mapped/Na2sio3_X_9_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1507],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132108","line":1509,"mapping_status":"MAPPED","ontology_id":"CHEBI:132108","preferred_term":"Na2SiO3 x 9 H2O"}],"identifier":"CHEBI:132108","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132108","ontology_label":"sodium silicate nonahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2SiO3 x 9 H2O","sssom_rows":[{"data_row":2016,"object_id":"CHEBI:132108","object_label":"sodium silicate nonahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2sio3_X_9_H2o","synonym_count":11} |
| ev-a36d3e179dc28d58 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1507] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b47ff53f049d7f31 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2sio3_X_9_H2o; data-row positions=[2016] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2016,"object_id":"CHEBI:132108","object_label":"sodium silicate nonahydrate","other":"Na2SiO3.9H2O&#124;Na2SiO3\u00b79H2O&#124;Na2SiO3\u30fb9H2O&#124;Na2SiO3\u22199H2O&#124;Na2SiO3\u20229H2O&#124;Na2SiO3\u20229H2O(CAS: 13517-24-3)&#124;Na2SiO3\u20229H2O(Sigma 307815)&#124;sodium oxosilanebis(olate)--water (1/9)&#124;Na2SiO3&#124;Na2SiO3 x 9 H20&#124;CAS:13517-24-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2sio3_X_9_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-73ec34bf1b8a30b8 | docs/data/mapped_ingredients.csv; CSV lines=[1509] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:132108","line":1509,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"36","ontology_id":"CHEBI:132108","preferred_term":"Na2SiO3 x 9 H2O","total_occurrences":"36"}] |
| ev-422eb7297f1c3564 | reports/yaml_record_review/Na2sio3_X_9_H2o.md; &#96;data/ingredients/mapped/Na2sio3_X_9_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:45; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-da37922899b18c96 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1013] | context_only | [{"current_record_sha256":"f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b","finding_id":"SEM:6a26e19438140a71ad2a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2sio3-x-9-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2sio3_X_9_H2o (data/ingredients/mapped/Na2sio3_X_9_H2o.yaml)'
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
summary: Per-record structured review for Na2sio3_X_9_H2o (data/ingredients/mapped/Na2sio3_X_9_H2o.yaml,
  record-5d33bb3aede92fc4, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2sio3_X_9_H2o.yaml
    sha256: f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b
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
  - path: reports/yaml_record_review/Na2sio3_X_9_H2o.md
    sha256: c5663a5f72827255b57b69383496a31bdf4030a5885437c3c3d8661d75415648
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5d33bb3aede92fc4
  path: data/ingredients/mapped/Na2sio3_X_9_H2o.yaml
  label: Na2sio3_X_9_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2sio3_X_9_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2sio3_X_9_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2sio3_X_9_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5d33bb3aede92fc4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5d33bb3aede92fc4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-5d33bb3aede92fc4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5d33bb3aede92fc4
evidence:
- evidence_id: ev-0bcbcd31639581bc
  kind: record_content
  reference: data/ingredients/mapped/Na2sio3_X_9_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1507],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132108","line":1509,"mapping_status":"MAPPED","ontology_id":"CHEBI:132108","preferred_term":"Na2SiO3
    x 9 H2O"}],"identifier":"CHEBI:132108","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":36,"edge_count":36,"occurrences":36},"occurrence_statistics":{"media_count":36,"total_occurrences":36},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132108","ontology_label":"sodium
    silicate nonahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2SiO3 x 9
    H2O","sssom_rows":[{"data_row":2016,"object_id":"CHEBI:132108","object_label":"sodium
    silicate nonahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2sio3_X_9_H2o","synonym_count":11}'
  snapshot_sha256: f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b
- evidence_id: ev-a36d3e179dc28d58
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1507]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b47ff53f049d7f31
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2sio3_X_9_H2o; data-row positions=[2016]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2016,"object_id":"CHEBI:132108","object_label":"sodium
    silicate nonahydrate","other":"Na2SiO3.9H2O|Na2SiO3\u00b79H2O|Na2SiO3\u30fb9H2O|Na2SiO3\u22199H2O|Na2SiO3\u20229H2O|Na2SiO3\u20229H2O(CAS:
    13517-24-3)|Na2SiO3\u20229H2O(Sigma 307815)|sodium oxosilanebis(olate)--water
    (1/9)|Na2SiO3|Na2SiO3 x 9 H20|CAS:13517-24-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2sio3_X_9_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-73ec34bf1b8a30b8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1509]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:132108","line":1509,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"36","ontology_id":"CHEBI:132108","preferred_term":"Na2SiO3
    x 9 H2O","total_occurrences":"36"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-422eb7297f1c3564
  kind: prior_review
  reference: reports/yaml_record_review/Na2sio3_X_9_H2o.md
  locator: '`data/ingredients/mapped/Na2sio3_X_9_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:45; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c5663a5f72827255b57b69383496a31bdf4030a5885437c3c3d8661d75415648
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2sio3_X_9_H2o.yaml`,\
    \ demote or reject the\n  anhydrous `Na2SiO3`, the typoed `Na2SiO3 x 9 H20`, and\
    \ the CAS/vendor\n  decorated CultureMech raw labels so they no longer publish\
    \ as exact\n  `CHEBI:132108` synonyms. Rebuild final SSSOM and rerun final SSSOM\
    \ validation\n  plus product label validation."
- evidence_id: ev-da37922899b18c96
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1013]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b","finding_id":"SEM:6a26e19438140a71ad2a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a0ee74249321ca70
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5d33bb3aede92fc4
  evidence_ids:
  - ev-0bcbcd31639581bc
  - ev-a36d3e179dc28d58
  - ev-b47ff53f049d7f31
  - ev-73ec34bf1b8a30b8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-000846967cf894e8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5d33bb3aede92fc4
  evidence_ids:
  - ev-422eb7297f1c3564
  - ev-0bcbcd31639581bc
  - ev-da37922899b18c96
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:35:01Z;
    reviewed SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b;
    current SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2sio3_X_9_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:132108 sodium silicate nonahydrate identity passes, but final other has
    anhydrous, typoed, and catalog labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-422eb7297f1c3564
    - ev-0bcbcd31639581bc
  - name: legacy-native-ids
    value: '["SEM:6a26e19438140a71ad2a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0bcbcd31639581bc
    - ev-422eb7297f1c3564
    - ev-da37922899b18c96
findings:
- finding_id: rec-f-f7e1cde19dd87af2
  issue_key: mim-reconciliation-historical-review-coverage-and-r-5d33bb3aede92fc4
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2sio3_X_9_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:35:01Z;
    reviewed SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b;
    current SHA-256=f4d860dd443582074583a911491db43130dd92efe57488228012c85da842798b;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2sio3_X_9_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:132108 sodium silicate nonahydrate identity passes, but final other has
    anhydrous, typoed, and catalog labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5d33bb3aede92fc4
  evidence_ids:
  - ev-422eb7297f1c3564
  - ev-0bcbcd31639581bc
  - ev-da37922899b18c96
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2sio3_X_9_H2o.yaml
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
