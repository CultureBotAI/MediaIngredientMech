# Per-record structured review: Soya_Pepton (data/ingredients/mapped/Soya_Pepton.yaml)

- Review: 20261017T083000Z-soya-pepton
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Soya_Pepton (data/ingredients/mapped/Soya_Pepton.yaml, record-86693bf933fc7455, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Soya_Pepton.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Soya_Pepton.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-86693bf933fc7455 | data/ingredients/mapped/Soya_Pepton.yaml | maintained | Soya_Pepton |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-86693bf933fc7455 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-86693bf933fc7455 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-86693bf933fc7455 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-86693bf933fc7455.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-86693bf933fc7455.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:05:00Z; reviewed SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c; current SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c; hash_changed=False. Reports=["reports/yaml_record_review/Soya_Pepton.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The misspelled soy-peptone surface is still an active duplicate of the canonical Soy_Peptone record.

## Findings

### rec-f-0a930222e069570c: Historical review coverage and residual narrative: Soya_Pepton

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-86693bf933fc7455.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:05:00Z; reviewed SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c; current SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c; hash_changed=False. Reports=["reports/yaml_record_review/Soya_Pepton.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The misspelled soy-peptone surface is still an active duplicate of the canonical Soy_Peptone record.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-216b00f866d5621a | data/ingredients/mapped/Soya_Pepton.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2093],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315720","line":2095,"mapping_status":"MAPPED","ontology_id":"FOODON:03315720","preferred_term":"Soya pepton"}],"identifier":"FOODON:03315720","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":833,"edge_count":833,"occurrences":1089},"occurrence_statistics":{"media_count":833,"total_occurrences":1089},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03315720","ontology_label":"vegetable protein, hydrolyzed","ontology_source":"FOODON"},"preferred_term":"Soya pepton","sssom_rows":[{"data_row":2623,"object_id":"FOODON:03315720","object_label":"vegetable protein, hydrolyzed","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Soya_Pepton","synonym_count":1} |
| ev-b69fc589eb742aa1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2093] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-019be018b8e3761e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Soya_Pepton; data-row positions=[2623] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2623,"object_id":"FOODON:03315720","object_label":"vegetable protein, hydrolyzed","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Soya_Pepton","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-e813c7548fc36b53 | docs/data/mapped_ingredients.csv; CSV lines=[2095] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03315720","line":2095,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"833","ontology_id":"FOODON:03315720","preferred_term":"Soya pepton","total_occurrences":"1089"}] |
| ev-199dd9cd5827ab46 | reports/yaml_record_review/Soya_Pepton.md; &#96;data/ingredients/mapped/Soya_Pepton.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:30; Completeness:39; Recommended Edits:46 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a63dede659c14c30 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1238] | context_only | [{"current_record_sha256":"941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c","finding_id":"SEM:5474b49bb60f188f1ca3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-soya-pepton
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Soya_Pepton (data/ingredients/mapped/Soya_Pepton.yaml)'
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
summary: Per-record structured review for Soya_Pepton (data/ingredients/mapped/Soya_Pepton.yaml,
  record-86693bf933fc7455, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Soya_Pepton.yaml
    sha256: 941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c
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
  - path: reports/yaml_record_review/Soya_Pepton.md
    sha256: 34e254ac985ce107cceda6d23c0a2290abd00167c89c0383dc2c92bc3941df32
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-86693bf933fc7455
  path: data/ingredients/mapped/Soya_Pepton.yaml
  label: Soya_Pepton
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Soya_Pepton.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Soya_Pepton.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Soya_Pepton.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-86693bf933fc7455
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-86693bf933fc7455
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-86693bf933fc7455
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-86693bf933fc7455
evidence:
- evidence_id: ev-216b00f866d5621a
  kind: record_content
  reference: data/ingredients/mapped/Soya_Pepton.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2093],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315720","line":2095,"mapping_status":"MAPPED","ontology_id":"FOODON:03315720","preferred_term":"Soya
    pepton"}],"identifier":"FOODON:03315720","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":833,"edge_count":833,"occurrences":1089},"occurrence_statistics":{"media_count":833,"total_occurrences":1089},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03315720","ontology_label":"vegetable
    protein, hydrolyzed","ontology_source":"FOODON"},"preferred_term":"Soya pepton","sssom_rows":[{"data_row":2623,"object_id":"FOODON:03315720","object_label":"vegetable
    protein, hydrolyzed","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Soya_Pepton","synonym_count":1}'
  snapshot_sha256: 941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c
- evidence_id: ev-b69fc589eb742aa1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2093]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-019be018b8e3761e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Soya_Pepton; data-row positions=[2623]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2623,"object_id":"FOODON:03315720","object_label":"vegetable
    protein, hydrolyzed","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Soya_Pepton","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e813c7548fc36b53
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2095]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03315720","line":2095,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"833","ontology_id":"FOODON:03315720","preferred_term":"Soya
    pepton","total_occurrences":"1089"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-199dd9cd5827ab46
  kind: prior_review
  reference: reports/yaml_record_review/Soya_Pepton.md
  locator: '`data/ingredients/mapped/Soya_Pepton.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:30; Completeness:39; Recommended Edits:46'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 34e254ac985ce107cceda6d23c0a2290abd00167c89c0383dc2c92bc3941df32
  quote: "Recommended Edits:\n- Major: merge `data/ingredients/mapped/Soya_Pepton.yaml`\
    \ into\n  `data/ingredients/mapped/Soy_Peptone.yaml`, retaining `Soya pepton`\
    \ as a raw\n  misspelling/provenance label and dropping the extra final SSSOM\
    \ subject."
- evidence_id: ev-a63dede659c14c30
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1238]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c","finding_id":"SEM:5474b49bb60f188f1ca3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-602b3b3b436849cf
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-86693bf933fc7455
  evidence_ids:
  - ev-216b00f866d5621a
  - ev-b69fc589eb742aa1
  - ev-019be018b8e3761e
  - ev-e813c7548fc36b53
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-03206d91bdd4e0f5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-86693bf933fc7455
  evidence_ids:
  - ev-199dd9cd5827ab46
  - ev-216b00f866d5621a
  - ev-a63dede659c14c30
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:05:00Z;
    reviewed SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c;
    current SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c;
    hash_changed=False. Reports=["reports/yaml_record_review/Soya_Pepton.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The misspelled
    soy-peptone surface is still an active duplicate of the canonical Soy_Peptone
    record.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-199dd9cd5827ab46
    - ev-216b00f866d5621a
  - name: legacy-native-ids
    value: '["SEM:5474b49bb60f188f1ca3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-216b00f866d5621a
    - ev-199dd9cd5827ab46
    - ev-a63dede659c14c30
findings:
- finding_id: rec-f-0a930222e069570c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-86693bf933fc7455
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Soya_Pepton'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:05:00Z;
    reviewed SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c;
    current SHA-256=941ffbb12746f06f0d1fcd7a7142947f77836b861ffc670ad0ec7c56696ba85c;
    hash_changed=False. Reports=["reports/yaml_record_review/Soya_Pepton.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The misspelled
    soy-peptone surface is still an active duplicate of the canonical Soy_Peptone
    record.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-86693bf933fc7455
  evidence_ids:
  - ev-199dd9cd5827ab46
  - ev-216b00f866d5621a
  - ev-a63dede659c14c30
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Soya_Pepton.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
