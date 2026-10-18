# Per-record structured review: Garden_Soil (data/ingredients/mapped/Garden_Soil.yaml)

- Review: 20261017T083000Z-garden-soil
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Garden_Soil (data/ingredients/mapped/Garden_Soil.yaml, record-e4a9b0c1642c8cf6, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Garden_Soil.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Garden_Soil.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e4a9b0c1642c8cf6 | data/ingredients/mapped/Garden_Soil.yaml | maintained | Garden_Soil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e4a9b0c1642c8cf6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e4a9b0c1642c8cf6 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e4a9b0c1642c8cf6 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e4a9b0c1642c8cf6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e4a9b0c1642c8cf6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:30:33Z; reviewed SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1; current SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1; hash_changed=False. Reports=["reports/yaml_record_review/Garden_Soil.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ENVO garden-soil identity passes, but top-level notes remain stale original import text.

## Findings

### rec-f-08f4d9aa3b874f80: Historical review coverage and residual narrative: Garden_Soil

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e4a9b0c1642c8cf6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:30:33Z; reviewed SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1; current SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1; hash_changed=False. Reports=["reports/yaml_record_review/Garden_Soil.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ENVO garden-soil identity passes, but top-level notes remain stale original import text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-61c73968dd91484b | data/ingredients/mapped/Garden_Soil.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1041],"raw_equal":true},"docs_rows":[{"identifier":"ENVO:00002263","line":1043,"mapping_status":"MAPPED","ontology_id":"ENVO:00002263","preferred_term":"Garden soil"}],"identifier":"ENVO:00002263","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"ENVO:00002263","ontology_label":"garden soil","ontology_source":"ENVO"},"preferred_term":"Garden soil","sssom_rows":[{"data_row":1284,"object_id":"ENVO:00002263","object_label":"garden soil","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Garden_Soil","synonym_count":1} |
| ev-7e934157e25f2627 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1041] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ff8e812b60adf99a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Garden_Soil; data-row positions=[1284] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1284,"object_id":"ENVO:00002263","object_label":"garden soil","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Garden_Soil","validation_method":"OLS:envo&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-589dedce3346a314 | docs/data/mapped_ingredients.csv; CSV lines=[1043] | supports | Published identity and count rows inspected: [{"identifier":"ENVO:00002263","line":1043,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"ENVO:00002263","preferred_term":"Garden soil","total_occurrences":"5"}] |
| ev-83c8540af07d7859 | reports/yaml_record_review/Garden_Soil.md; &#96;data/ingredients/mapped/Garden_Soil.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:33; Completeness:57; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-eb686c6722483531 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[652] | context_only | [{"current_record_sha256":"311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1","finding_id":"SEM:7f60bbc9f86d9578758c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-garden-soil
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Garden_Soil (data/ingredients/mapped/Garden_Soil.yaml)'
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
summary: Per-record structured review for Garden_Soil (data/ingredients/mapped/Garden_Soil.yaml,
  record-e4a9b0c1642c8cf6, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Garden_Soil.yaml
    sha256: 311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Garden_Soil.md
    sha256: 82f4a2064e686705bc04e1b4945e4098a05b75de27c38aa6c4694ad004e3c4b9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e4a9b0c1642c8cf6
  path: data/ingredients/mapped/Garden_Soil.yaml
  label: Garden_Soil
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Garden_Soil.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Garden_Soil.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Garden_Soil.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e4a9b0c1642c8cf6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e4a9b0c1642c8cf6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e4a9b0c1642c8cf6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e4a9b0c1642c8cf6
evidence:
- evidence_id: ev-61c73968dd91484b
  kind: record_content
  reference: data/ingredients/mapped/Garden_Soil.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1041],"raw_equal":true},"docs_rows":[{"identifier":"ENVO:00002263","line":1043,"mapping_status":"MAPPED","ontology_id":"ENVO:00002263","preferred_term":"Garden
    soil"}],"identifier":"ENVO:00002263","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"ENVO:00002263","ontology_label":"garden
    soil","ontology_source":"ENVO"},"preferred_term":"Garden soil","sssom_rows":[{"data_row":1284,"object_id":"ENVO:00002263","object_label":"garden
    soil","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Garden_Soil","synonym_count":1}'
  snapshot_sha256: 311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1
- evidence_id: ev-7e934157e25f2627
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1041]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ff8e812b60adf99a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Garden_Soil; data-row positions=[1284]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1284,"object_id":"ENVO:00002263","object_label":"garden
    soil","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Garden_Soil","validation_method":"OLS:envo|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-589dedce3346a314
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1043]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"ENVO:00002263","line":1043,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"ENVO:00002263","preferred_term":"Garden
    soil","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-83c8540af07d7859
  kind: prior_review
  reference: reports/yaml_record_review/Garden_Soil.md
  locator: '`data/ingredients/mapped/Garden_Soil.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:33; Completeness:57; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 82f4a2064e686705bc04e1b4945e4098a05b75de27c38aa6c4694ad004e3c4b9
  quote: "Recommended Edits:\n- Minor: replace the top-level `notes` value with text\
    \ that describes the\n  current exact ENVO garden-soil identity, or remove the\
    \ stale note if the\n  mapping evidence and curation history are sufficient."
- evidence_id: ev-eb686c6722483531
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[652]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1","finding_id":"SEM:7f60bbc9f86d9578758c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-6030c06ca5c24d88
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e4a9b0c1642c8cf6
  evidence_ids:
  - ev-61c73968dd91484b
  - ev-7e934157e25f2627
  - ev-ff8e812b60adf99a
  - ev-589dedce3346a314
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a2911c9fc17887b0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e4a9b0c1642c8cf6
  evidence_ids:
  - ev-83c8540af07d7859
  - ev-61c73968dd91484b
  - ev-eb686c6722483531
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:30:33Z;
    reviewed SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1;
    current SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1;
    hash_changed=False. Reports=["reports/yaml_record_review/Garden_Soil.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ENVO
    garden-soil identity passes, but top-level notes remain stale original import
    text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-83c8540af07d7859
    - ev-61c73968dd91484b
  - name: legacy-native-ids
    value: '["SEM:7f60bbc9f86d9578758c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-61c73968dd91484b
    - ev-83c8540af07d7859
    - ev-eb686c6722483531
findings:
- finding_id: rec-f-08f4d9aa3b874f80
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e4a9b0c1642c8cf6
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Garden_Soil'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:30:33Z;
    reviewed SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1;
    current SHA-256=311b253c5f14ecabb27c644d2ed1493f307e2ddafb815306d849f126d584dec1;
    hash_changed=False. Reports=["reports/yaml_record_review/Garden_Soil.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ENVO
    garden-soil identity passes, but top-level notes remain stale original import
    text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e4a9b0c1642c8cf6
  evidence_ids:
  - ev-83c8540af07d7859
  - ev-61c73968dd91484b
  - ev-eb686c6722483531
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Garden_Soil.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
