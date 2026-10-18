# Per-record structured review: Yeastolate_BD_2_autoclaved (data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml)

- Review: 20261017T083000Z-yeastolate-bd-2-autoclaved
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Yeastolate_BD_2_autoclaved (data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml, record-ebe50f4af493dc3c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ebe50f4af493dc3c | data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml | maintained | Yeastolate_BD_2_autoclaved |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ebe50f4af493dc3c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-ebe50f4af493dc3c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ebe50f4af493dc3c | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ebe50f4af493dc3c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ebe50f4af493dc3c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z; reviewed SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937; current SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937; hash_changed=False. Reports=["reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic MicrO Yeastolate class is too broad for a BD, two-percent, autoclaved source label, and final SSSOM exports a Difco catalog variant.

## Findings

### rec-f-07de2e661daf8567: Historical review coverage and residual narrative: Yeastolate_BD_2_autoclaved

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-ebe50f4af493dc3c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z; reviewed SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937; current SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937; hash_changed=False. Reports=["reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic MicrO Yeastolate class is too broad for a BD, two-percent, autoclaved source label, and final SSSOM exports a Difco catalog variant.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-efefc8037ae1f3b1 | data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2621],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000522","line":2623,"mapping_status":"MAPPED","ontology_id":"MICRO:0000522","preferred_term":"Yeastolate (BD; 2%, autoclaved)"}],"identifier":"MICRO:0000522","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"MICRO:0000522","ontology_label":"Yeastolate","ontology_source":"MICRO"},"preferred_term":"Yeastolate (BD; 2%, autoclaved)","sssom_rows":[{"data_row":2955,"object_id":"MICRO:0000522","object_label":"Yeastolate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeastolate_BD_2_autoclaved","synonym_count":1} |
| ev-c015237b90c233df | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2621] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9f161920a2a333b0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Yeastolate_BD_2_autoclaved; data-row positions=[2955] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2955,"object_id":"MICRO:0000522","object_label":"Yeastolate","other":"Yeastolate (Difco)","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeastolate_BD_2_autoclaved","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-8be4e802bd0c4bbc | docs/data/mapped_ingredients.csv; CSV lines=[2623] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000522","line":2623,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"MICRO:0000522","preferred_term":"Yeastolate (BD; 2%, autoclaved)","total_occurrences":"4"}] |
| ev-b30559a2bc58c7a7 | reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md; &#96;data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:36; Issues:44; Completeness:53; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f944c5a462b76288 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1360] | context_only | [{"current_record_sha256":"4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937","finding_id":"SEM:3dd4f46b459f3e25269e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-yeastolate-bd-2-autoclaved
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Yeastolate_BD_2_autoclaved (data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml)'
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
summary: Per-record structured review for Yeastolate_BD_2_autoclaved (data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml,
  record-ebe50f4af493dc3c, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
    sha256: 4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937
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
  - path: reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md
    sha256: 4ac36615c0ff78c2182add0b7c1b6ba0034d4c76010a571770d41b188c955d51
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ebe50f4af493dc3c
  path: data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
  label: Yeastolate_BD_2_autoclaved
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ebe50f4af493dc3c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ebe50f4af493dc3c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-ebe50f4af493dc3c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ebe50f4af493dc3c
evidence:
- evidence_id: ev-efefc8037ae1f3b1
  kind: record_content
  reference: data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2621],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000522","line":2623,"mapping_status":"MAPPED","ontology_id":"MICRO:0000522","preferred_term":"Yeastolate
    (BD; 2%, autoclaved)"}],"identifier":"MICRO:0000522","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"MICRO:0000522","ontology_label":"Yeastolate","ontology_source":"MICRO"},"preferred_term":"Yeastolate
    (BD; 2%, autoclaved)","sssom_rows":[{"data_row":2955,"object_id":"MICRO:0000522","object_label":"Yeastolate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeastolate_BD_2_autoclaved","synonym_count":1}'
  snapshot_sha256: 4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937
- evidence_id: ev-c015237b90c233df
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2621]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9f161920a2a333b0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Yeastolate_BD_2_autoclaved; data-row positions=[2955]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2955,"object_id":"MICRO:0000522","object_label":"Yeastolate","other":"Yeastolate
    (Difco)","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeastolate_BD_2_autoclaved","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8be4e802bd0c4bbc
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2623]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000522","line":2623,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"MICRO:0000522","preferred_term":"Yeastolate
    (BD; 2%, autoclaved)","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b30559a2bc58c7a7
  kind: prior_review
  reference: reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md
  locator: '`data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml`:2; Verdict:4;
    Identity:12; Validation:24; Evidence:36; Issues:44; Completeness:53; Recommended
    Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4ac36615c0ff78c2182add0b7c1b6ba0034d4c76010a571770d41b188c955d51
  quote: "Issues:\n- Major: `Yeastolate (BD; 2%, autoclaved)` has vendor, two-percent\n\
    \  concentration, and heat-treatment qualifiers, so it is a narrower processed\n\
    \  catalog ingredient rather than an exact synonym of generic MicrO Yeastolate.\n\
    - Major: final SSSOM exports `Yeastolate (Difco)` as an `other` synonym on the\n\
    \  generic Yeastolate exact-match row, even though that label is catalog\n  qualified.\n\
    \nRecommended Edits:\n- Reground this record to a local MIM identifier for the\
    \ BD, two-percent,\n  autoclaved preparation.\n- Move `MICRO:0000522` to an appropriate\
    \ parent or component assertion if the\n  source label is known to be Yeastolate-based.\n\
    - Suppress `Yeastolate (Difco)` from final SSSOM `other` on the generic MicrO\n\
    \  exact row.\n- Rebuild SSSOM, then rerun strict validation, SSSOM invariant\
    \ validation, and\n  the cross-record `other` synonym audit."
- evidence_id: ev-f944c5a462b76288
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1360]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937","finding_id":"SEM:3dd4f46b459f3e25269e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-7cee9150ff282484
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ebe50f4af493dc3c
  evidence_ids:
  - ev-efefc8037ae1f3b1
  - ev-c015237b90c233df
  - ev-9f161920a2a333b0
  - ev-8be4e802bd0c4bbc
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9e1ab2e31ebeab45
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ebe50f4af493dc3c
  evidence_ids:
  - ev-b30559a2bc58c7a7
  - ev-efefc8037ae1f3b1
  - ev-f944c5a462b76288
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z;
    reviewed SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937;
    current SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937;
    hash_changed=False. Reports=["reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The generic
    MicrO Yeastolate class is too broad for a BD, two-percent, autoclaved source label,
    and final SSSOM exports a Difco catalog variant.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b30559a2bc58c7a7
    - ev-efefc8037ae1f3b1
  - name: legacy-native-ids
    value: '["SEM:3dd4f46b459f3e25269e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-efefc8037ae1f3b1
    - ev-b30559a2bc58c7a7
    - ev-f944c5a462b76288
findings:
- finding_id: rec-f-07de2e661daf8567
  issue_key: mim-reconciliation-historical-review-coverage-and-r-ebe50f4af493dc3c
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Yeastolate_BD_2_autoclaved'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z;
    reviewed SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937;
    current SHA-256=4cc7aec4170d4ac7ce274b8e8dc4ab75fb3aa2997aeed46aa14b592b59d4d937;
    hash_changed=False. Reports=["reports/yaml_record_review/Yeastolate_BD_2_autoclaved.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The generic
    MicrO Yeastolate class is too broad for a BD, two-percent, autoclaved source label,
    and final SSSOM exports a Difco catalog variant.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ebe50f4af493dc3c
  evidence_ids:
  - ev-b30559a2bc58c7a7
  - ev-efefc8037ae1f3b1
  - ev-f944c5a462b76288
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeastolate_BD_2_autoclaved.yaml
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
