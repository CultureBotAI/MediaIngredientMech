# Per-record structured review: Znso4_X_7_H2o (data/ingredients/mapped/Znso4_X_7_H2o.yaml)

- Review: 20261017T083000Z-znso4-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Znso4_X_7_H2o (data/ingredients/mapped/Znso4_X_7_H2o.yaml, record-98cb1d7d228701e5, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Znso4_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Znso4_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-98cb1d7d228701e5 | data/ingredients/mapped/Znso4_X_7_H2o.yaml | maintained | Znso4_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-98cb1d7d228701e5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-98cb1d7d228701e5 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-98cb1d7d228701e5 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-98cb1d7d228701e5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-98cb1d7d228701e5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:46:27Z; reviewed SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791; current SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791; hash_changed=False. Reports=["reports/yaml_record_review/Znso4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI zinc sulfate heptahydrate identity and source-backed trace-element role pass, but final SSSOM exports an impossible Zn2SO4 formula synonym.

## Findings

### rec-f-f3f86585feaa442b: Historical review coverage and residual narrative: Znso4_X_7_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-98cb1d7d228701e5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:46:27Z; reviewed SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791; current SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791; hash_changed=False. Reports=["reports/yaml_record_review/Znso4_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI zinc sulfate heptahydrate identity and source-backed trace-element role pass, but final SSSOM exports an impossible Zn2SO4 formula synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a6b794241631a7df | data/ingredients/mapped/Znso4_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2080],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32312","line":2082,"mapping_status":"MAPPED","ontology_id":"CHEBI:32312","preferred_term":"ZnSO4 x 7 H2O"}],"identifier":"CHEBI:32312","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2407,"edge_count":2407,"occurrences":2410},"occurrence_statistics":{"media_count":2407,"total_occurrences":2410},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32312","ontology_label":"zinc sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"ZnSO4 x 7 H2O","sssom_rows":[{"data_row":2964,"object_id":"CHEBI:32312","object_label":"zinc sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Znso4_X_7_H2o","synonym_count":26} |
| ev-3530885e2f5a0bd6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2080] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ba0127e8916b4704 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Znso4_X_7_H2o; data-row positions=[2964] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2964,"object_id":"CHEBI:32312","object_label":"zinc sulfate heptahydrate","other":"Zn2SO4\u00b77H2O&#124;ZnSO4 . 7H2O&#124;ZnSO4 .7H2O&#124;ZnSO4 x 7H2O&#124;ZnSO4 \u00b7 7H2O&#124;ZnSO4 \u22c5 7H2O&#124;ZnSO4.7H2O&#124;ZnSO4\u00b77H2O&#124;ZnSO4\u22c57H2O&#124;ZnSO4\u30fb7H2O&#124;zinc sulfate (1:1) heptahydrate&#124;zinc sulfate heptahydrate (1:1:7)&#124;ZnSO4-7H2O&#124;zinc(2+) sulfate heptahydrate&#124;ZnSO4 \u00d7 7H2O&#124;ZnSO4*7 H2O&#124;ZnSO4*7H2O&#124;ZnSO4\u22197H2O&#124;ZnSO4\uff657H2O&#124;zinc(2+) sulfate--water (1/7)&#124;CAS:7446-20-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Znso4_X_7_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-69d9f546e07faead | docs/data/mapped_ingredients.csv; CSV lines=[2082] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32312","line":2082,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2407","ontology_id":"CHEBI:32312","preferred_term":"ZnSO4 x 7 H2O","total_occurrences":"2410"}] |
| ev-04c6cf0646047c3b | reports/yaml_record_review/Znso4_X_7_H2o.md; &#96;data/ingredients/mapped/Znso4_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:28; Evidence:39; Issues:48; Completeness:54; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bc599bec9eae8ca0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1364] | context_only | [{"current_record_sha256":"2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791","finding_id":"SEM:d5702393a6f68bb02098","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-znso4-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Znso4_X_7_H2o (data/ingredients/mapped/Znso4_X_7_H2o.yaml)'
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
summary: Per-record structured review for Znso4_X_7_H2o (data/ingredients/mapped/Znso4_X_7_H2o.yaml,
  record-98cb1d7d228701e5, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Znso4_X_7_H2o.yaml
    sha256: 2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791
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
  - path: reports/yaml_record_review/Znso4_X_7_H2o.md
    sha256: 08ac13c0a77cc649cdb8f6296066848d1632e4e3b68bb04e6627057c7dfcdb7e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-98cb1d7d228701e5
  path: data/ingredients/mapped/Znso4_X_7_H2o.yaml
  label: Znso4_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Znso4_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Znso4_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Znso4_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-98cb1d7d228701e5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-98cb1d7d228701e5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-98cb1d7d228701e5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-98cb1d7d228701e5
evidence:
- evidence_id: ev-a6b794241631a7df
  kind: record_content
  reference: data/ingredients/mapped/Znso4_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2080],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32312","line":2082,"mapping_status":"MAPPED","ontology_id":"CHEBI:32312","preferred_term":"ZnSO4
    x 7 H2O"}],"identifier":"CHEBI:32312","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2407,"edge_count":2407,"occurrences":2410},"occurrence_statistics":{"media_count":2407,"total_occurrences":2410},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32312","ontology_label":"zinc
    sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"ZnSO4 x 7 H2O","sssom_rows":[{"data_row":2964,"object_id":"CHEBI:32312","object_label":"zinc
    sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Znso4_X_7_H2o","synonym_count":26}'
  snapshot_sha256: 2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791
- evidence_id: ev-3530885e2f5a0bd6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2080]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ba0127e8916b4704
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Znso4_X_7_H2o; data-row positions=[2964]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2964,"object_id":"CHEBI:32312","object_label":"zinc
    sulfate heptahydrate","other":"Zn2SO4\u00b77H2O|ZnSO4 . 7H2O|ZnSO4 .7H2O|ZnSO4
    x 7H2O|ZnSO4 \u00b7 7H2O|ZnSO4 \u22c5 7H2O|ZnSO4.7H2O|ZnSO4\u00b77H2O|ZnSO4\u22c57H2O|ZnSO4\u30fb7H2O|zinc
    sulfate (1:1) heptahydrate|zinc sulfate heptahydrate (1:1:7)|ZnSO4-7H2O|zinc(2+)
    sulfate heptahydrate|ZnSO4 \u00d7 7H2O|ZnSO4*7 H2O|ZnSO4*7H2O|ZnSO4\u22197H2O|ZnSO4\uff657H2O|zinc(2+)
    sulfate--water (1/7)|CAS:7446-20-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Znso4_X_7_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-69d9f546e07faead
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2082]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32312","line":2082,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2407","ontology_id":"CHEBI:32312","preferred_term":"ZnSO4
    x 7 H2O","total_occurrences":"2410"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-04c6cf0646047c3b
  kind: prior_review
  reference: reports/yaml_record_review/Znso4_X_7_H2o.md
  locator: '`data/ingredients/mapped/Znso4_X_7_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:28; Evidence:39; Issues:48; Completeness:54; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 08ac13c0a77cc649cdb8f6296066848d1632e4e3b68bb04e6627057c7dfcdb7e
  quote: "Issues:\n- Major: the final SSSOM `other` field exports an impossible\n\
    \  `Zn2SO4`-prefixed heptahydrate formula as an exact synonym for zinc sulfate\n\
    \  heptahydrate.\n\nRecommended Edits:\n- Remove or suppress the `Zn2SO4`-prefixed\
    \ hydrate synonym from final SSSOM\n  `other`.\n- Rebuild SSSOM and rerun strict\
    \ validation plus SSSOM invariant validation."
- evidence_id: ev-bc599bec9eae8ca0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1364]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791","finding_id":"SEM:d5702393a6f68bb02098","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-3401269e6de44096
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-98cb1d7d228701e5
  evidence_ids:
  - ev-a6b794241631a7df
  - ev-3530885e2f5a0bd6
  - ev-ba0127e8916b4704
  - ev-69d9f546e07faead
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a5994549fd971308
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-98cb1d7d228701e5
  evidence_ids:
  - ev-04c6cf0646047c3b
  - ev-a6b794241631a7df
  - ev-bc599bec9eae8ca0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:46:27Z;
    reviewed SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791;
    current SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791;
    hash_changed=False. Reports=["reports/yaml_record_review/Znso4_X_7_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    zinc sulfate heptahydrate identity and source-backed trace-element role pass,
    but final SSSOM exports an impossible Zn2SO4 formula synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-04c6cf0646047c3b
    - ev-a6b794241631a7df
  - name: legacy-native-ids
    value: '["SEM:d5702393a6f68bb02098"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a6b794241631a7df
    - ev-04c6cf0646047c3b
    - ev-bc599bec9eae8ca0
findings:
- finding_id: rec-f-f3f86585feaa442b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-98cb1d7d228701e5
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Znso4_X_7_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:46:27Z;
    reviewed SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791;
    current SHA-256=2a8b07050006f6d9d0d167997107fbb3b3c453657c98c0b512276e182f4bc791;
    hash_changed=False. Reports=["reports/yaml_record_review/Znso4_X_7_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    zinc sulfate heptahydrate identity and source-backed trace-element role pass,
    but final SSSOM exports an impossible Zn2SO4 formula synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-98cb1d7d228701e5
  evidence_ids:
  - ev-04c6cf0646047c3b
  - ev-a6b794241631a7df
  - ev-bc599bec9eae8ca0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Znso4_X_7_H2o.yaml
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
