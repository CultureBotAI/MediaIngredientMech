# Per-record structured review: 5-trimethoxybenzoate (data/ingredients/mapped/5-trimethoxybenzoate.yaml)

- Review: 20261017T083000Z-5-trimethoxybenzoate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 5-trimethoxybenzoate (data/ingredients/mapped/5-trimethoxybenzoate.yaml, record-52671dadd3e9394a, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/5-trimethoxybenzoate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/5-trimethoxybenzoate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-52671dadd3e9394a | data/ingredients/mapped/5-trimethoxybenzoate.yaml | maintained | 5-trimethoxybenzoate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-52671dadd3e9394a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-52671dadd3e9394a | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-52671dadd3e9394a | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-52671dadd3e9394a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-52671dadd3e9394a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:43:15Z; reviewed SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30; current SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30; hash_changed=False. Reports=["reports/yaml_record_review/5-trimethoxybenzoate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The corrected exact CHEBI 3,4,5-trimethoxybenzoate identity passes, but the grade is still CLOSE_MATCH, chemistry is missing, and two non-exact raw labels are exported as SSSOM other surfaces.

## Findings

### rec-f-208c4f0d6098f950: Historical review coverage and residual narrative: 5-trimethoxybenzoate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-52671dadd3e9394a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:43:15Z; reviewed SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30; current SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30; hash_changed=False. Reports=["reports/yaml_record_review/5-trimethoxybenzoate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The corrected exact CHEBI 3,4,5-trimethoxybenzoate identity passes, but the grade is still CLOSE_MATCH, chemistry is missing, and two non-exact raw labels are exported as SSSOM other surfaces.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-932e4cb64ccb5931 | data/ingredients/mapped/5-trimethoxybenzoate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[174],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:58989","line":176,"mapping_status":"MAPPED","ontology_id":"CHEBI:58989","preferred_term":"3,4,5-trimethoxybenzoate"}],"identifier":"CHEBI:58989","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:58989","ontology_label":"3,4,5-trimethoxybenzoate","ontology_source":"CHEBI"},"preferred_term":"3,4,5-trimethoxybenzoate","sssom_rows":[{"data_row":238,"object_id":"CHEBI:58989","object_label":"3,4,5-trimethoxybenzoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:5-trimethoxybenzoate","synonym_count":2} |
| ev-5e837c1a01d77f71 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [174] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c184c79f485fa651 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:5-trimethoxybenzoate; data-row positions=[238] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":238,"object_id":"CHEBI:58989","object_label":"3,4,5-trimethoxybenzoate","other":"5-trimethoxybenzoate&#124;Trimethoxybenzoate","predicate_id":"skos:exactMatch","subject_id":"MIM:5-trimethoxybenzoate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-60c81c9999dc8bd3 | docs/data/mapped_ingredients.csv; CSV lines=[176] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:58989","line":176,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:58989","preferred_term":"3,4,5-trimethoxybenzoate","total_occurrences":"0"}] |
| ev-9b43114f23c82b1d | reports/yaml_record_review/5-trimethoxybenzoate.md; &#96;data/ingredients/mapped/5-trimethoxybenzoate.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:36; Completeness:57; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0c9586710e7e0e68 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[168] | context_only | [{"current_record_sha256":"f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30","finding_id":"SEM:fa04961fd358d5acc2f5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-5-trimethoxybenzoate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 5-trimethoxybenzoate (data/ingredients/mapped/5-trimethoxybenzoate.yaml)'
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
summary: Per-record structured review for 5-trimethoxybenzoate (data/ingredients/mapped/5-trimethoxybenzoate.yaml,
  record-52671dadd3e9394a, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/5-trimethoxybenzoate.yaml
    sha256: f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/5-trimethoxybenzoate.md
    sha256: 2722c7e1a1344e40ba97c933805c4da5d8f8263ac306ac94850cf4c63d89b40d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-52671dadd3e9394a
  path: data/ingredients/mapped/5-trimethoxybenzoate.yaml
  label: 5-trimethoxybenzoate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-trimethoxybenzoate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/5-trimethoxybenzoate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/5-trimethoxybenzoate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-52671dadd3e9394a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-52671dadd3e9394a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-52671dadd3e9394a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-52671dadd3e9394a
evidence:
- evidence_id: ev-932e4cb64ccb5931
  kind: record_content
  reference: data/ingredients/mapped/5-trimethoxybenzoate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[174],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:58989","line":176,"mapping_status":"MAPPED","ontology_id":"CHEBI:58989","preferred_term":"3,4,5-trimethoxybenzoate"}],"identifier":"CHEBI:58989","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:58989","ontology_label":"3,4,5-trimethoxybenzoate","ontology_source":"CHEBI"},"preferred_term":"3,4,5-trimethoxybenzoate","sssom_rows":[{"data_row":238,"object_id":"CHEBI:58989","object_label":"3,4,5-trimethoxybenzoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:5-trimethoxybenzoate","synonym_count":2}'
  snapshot_sha256: f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30
- evidence_id: ev-5e837c1a01d77f71
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [174]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c184c79f485fa651
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:5-trimethoxybenzoate; data-row positions=[238]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":238,"object_id":"CHEBI:58989","object_label":"3,4,5-trimethoxybenzoate","other":"5-trimethoxybenzoate|Trimethoxybenzoate","predicate_id":"skos:exactMatch","subject_id":"MIM:5-trimethoxybenzoate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-60c81c9999dc8bd3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[176]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:58989","line":176,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:58989","preferred_term":"3,4,5-trimethoxybenzoate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9b43114f23c82b1d
  kind: prior_review
  reference: reports/yaml_record_review/5-trimethoxybenzoate.md
  locator: '`data/ingredients/mapped/5-trimethoxybenzoate.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:36; Completeness:57; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2722c7e1a1344e40ba97c933805c4da5d8f8263ac306ac94850cf4c63d89b40d
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/5-trimethoxybenzoate.yaml`,\
    \ change\n  `ontology_mapping.mapping_quality` from `CLOSE_MATCH` to `EXACT_MATCH`.\n\
    - Remove `5-trimethoxybenzoate` and `Trimethoxybenzoate` from `synonyms`, or\n\
    \  move them to source-occurrence-only provenance that will not be exported as\n\
    \  exact SSSOM `other` values.\n- Backfill `chemical_properties` from `CHEBI:58989`\
    \ without adding the neutral\n  acid's CAS RN; rebuild `mappings/ingredient_mappings.sssom.tsv`\
    \ and\n  `data/curated/mapped_ingredients.yaml`, then rerun strict validation,\
    \ SSSOM\n  invariants, and the id/label correspondence gate."
- evidence_id: ev-0c9586710e7e0e68
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[168]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30","finding_id":"SEM:fa04961fd358d5acc2f5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-7c2589495a583ded
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-52671dadd3e9394a
  evidence_ids:
  - ev-932e4cb64ccb5931
  - ev-5e837c1a01d77f71
  - ev-c184c79f485fa651
  - ev-60c81c9999dc8bd3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-810f8f443db046db
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-52671dadd3e9394a
  evidence_ids:
  - ev-9b43114f23c82b1d
  - ev-932e4cb64ccb5931
  - ev-0c9586710e7e0e68
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:43:15Z;
    reviewed SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30;
    current SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30;
    hash_changed=False. Reports=["reports/yaml_record_review/5-trimethoxybenzoate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The corrected
    exact CHEBI 3,4,5-trimethoxybenzoate identity passes, but the grade is still CLOSE_MATCH,
    chemistry is missing, and two non-exact raw labels are exported as SSSOM other
    surfaces.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9b43114f23c82b1d
    - ev-932e4cb64ccb5931
  - name: legacy-native-ids
    value: '["SEM:fa04961fd358d5acc2f5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-932e4cb64ccb5931
    - ev-9b43114f23c82b1d
    - ev-0c9586710e7e0e68
findings:
- finding_id: rec-f-208c4f0d6098f950
  issue_key: mim-reconciliation-historical-review-coverage-and-r-52671dadd3e9394a
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 5-trimethoxybenzoate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:43:15Z;
    reviewed SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30;
    current SHA-256=f448316b3399201e1ee2da1d339fdfa39a326fb6f01595a498d4ec6d2a10da30;
    hash_changed=False. Reports=["reports/yaml_record_review/5-trimethoxybenzoate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The corrected
    exact CHEBI 3,4,5-trimethoxybenzoate identity passes, but the grade is still CLOSE_MATCH,
    chemistry is missing, and two non-exact raw labels are exported as SSSOM other
    surfaces.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-52671dadd3e9394a
  evidence_ids:
  - ev-9b43114f23c82b1d
  - ev-932e4cb64ccb5931
  - ev-0c9586710e7e0e68
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-trimethoxybenzoate.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
