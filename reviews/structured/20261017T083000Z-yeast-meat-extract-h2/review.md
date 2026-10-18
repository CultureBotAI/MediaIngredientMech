# Per-record structured review: Yeast_Meat_Extract_H2 (data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml)

- Review: 20261017T083000Z-yeast-meat-extract-h2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Yeast_Meat_Extract_H2 (data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml, record-efcfe3f13183bfaa, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-efcfe3f13183bfaa | data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml | maintained | Yeast_Meat_Extract_H2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-efcfe3f13183bfaa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-efcfe3f13183bfaa | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-efcfe3f13183bfaa | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-efcfe3f13183bfaa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-efcfe3f13183bfaa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z; reviewed SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad; current SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad; hash_changed=False. Reports=["reports/yaml_record_review/Yeast_Meat_Extract_H2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local fallback identity and final row pass, but the decomposition has a stale unresolved Yeast component.

## Findings

### rec-f-450d27ab2c129875: Historical review coverage and residual narrative: Yeast_Meat_Extract_H2

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-efcfe3f13183bfaa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z; reviewed SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad; current SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad; hash_changed=False. Reports=["reports/yaml_record_review/Yeast_Meat_Extract_H2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local fallback identity and final row pass, but the decomposition has a stale unresolved Yeast component.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-695925991c2ca346 | data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[71],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:yeast_meat_extract_h2","line":73,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","preferred_term":"Yeast + Meat Extract + H2"}],"identifier":"kgmicrobe.ingredient:yeast_meat_extract_h2","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","ontology_label":"Yeast + Meat Extract + H2","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Yeast + Meat Extract + H2","sssom_rows":[{"data_row":2954,"object_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","object_label":"Yeast + Meat Extract + H2","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Meat_Extract_H2","synonym_count":1} |
| ev-d53308a7a4f15738 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [71] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8dcee51b5a6c4cec | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Yeast_Meat_Extract_H2; data-row positions=[2954] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2954,"object_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","object_label":"Yeast + Meat Extract + H2","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeast_Meat_Extract_H2","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-1e81b325b95887cb | docs/data/mapped_ingredients.csv; CSV lines=[73] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:yeast_meat_extract_h2","line":73,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","preferred_term":"Yeast + Meat Extract + H2","total_occurrences":"0"}] |
| ev-890b7c665c3d3962 | reports/yaml_record_review/Yeast_Meat_Extract_H2.md; &#96;data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:38; Issues:51; Completeness:56; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9c2146f0adb0e6be | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1359] | context_only | [{"current_record_sha256":"532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad","finding_id":"SEM:870e68d3c55393c022b7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-yeast-meat-extract-h2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Yeast_Meat_Extract_H2 (data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml)'
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
summary: Per-record structured review for Yeast_Meat_Extract_H2 (data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml,
  record-efcfe3f13183bfaa, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml
    sha256: 532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad
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
  - path: reports/yaml_record_review/Yeast_Meat_Extract_H2.md
    sha256: cc2e602d3328cc0bc921cd33757412ee786563f1b491e163f0546afca00ca46b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-efcfe3f13183bfaa
  path: data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml
  label: Yeast_Meat_Extract_H2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-efcfe3f13183bfaa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-efcfe3f13183bfaa
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-efcfe3f13183bfaa
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-efcfe3f13183bfaa
evidence:
- evidence_id: ev-695925991c2ca346
  kind: record_content
  reference: data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[71],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:yeast_meat_extract_h2","line":73,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","preferred_term":"Yeast
    + Meat Extract + H2"}],"identifier":"kgmicrobe.ingredient:yeast_meat_extract_h2","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","ontology_label":"Yeast
    + Meat Extract + H2","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Yeast
    + Meat Extract + H2","sssom_rows":[{"data_row":2954,"object_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","object_label":"Yeast
    + Meat Extract + H2","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Yeast_Meat_Extract_H2","synonym_count":1}'
  snapshot_sha256: 532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad
- evidence_id: ev-d53308a7a4f15738
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [71]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8dcee51b5a6c4cec
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Yeast_Meat_Extract_H2; data-row positions=[2954]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2954,"object_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","object_label":"Yeast
    + Meat Extract + H2","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Yeast_Meat_Extract_H2","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1e81b325b95887cb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[73]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:yeast_meat_extract_h2","line":73,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:yeast_meat_extract_h2","preferred_term":"Yeast
    + Meat Extract + H2","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-890b7c665c3d3962
  kind: prior_review
  reference: reports/yaml_record_review/Yeast_Meat_Extract_H2.md
  locator: '`data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml`:2; Verdict:4; Identity:11;
    Validation:27; Evidence:38; Issues:51; Completeness:56; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cc2e602d3328cc0bc921cd33757412ee786563f1b491e163f0546afca00ca46b
  quote: "Issues:\n- Major: the first component should be linked to the existing MIM\
    \ Yeast record\n  instead of remaining an `UNMAPPED` component without a `component_id`.\n\
    \nRecommended Edits:\n- Set the `Yeast` component to `component_id: FOODON:03411345`\
    \ with\n  `reference_scope: MIM_CATALOG`.\n- Add curation history documenting\
    \ the component repair.\n- Rerun strict validation, SSSOM invariant validation,\
    \ and component-partonomy\n  validation."
- evidence_id: ev-9c2146f0adb0e6be
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1359]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad","finding_id":"SEM:870e68d3c55393c022b7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b1bfa1272228d5db
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-efcfe3f13183bfaa
  evidence_ids:
  - ev-695925991c2ca346
  - ev-d53308a7a4f15738
  - ev-8dcee51b5a6c4cec
  - ev-1e81b325b95887cb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-884962b653f44557
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-efcfe3f13183bfaa
  evidence_ids:
  - ev-890b7c665c3d3962
  - ev-695925991c2ca346
  - ev-9c2146f0adb0e6be
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z;
    reviewed SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad;
    current SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad;
    hash_changed=False. Reports=["reports/yaml_record_review/Yeast_Meat_Extract_H2.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    fallback identity and final row pass, but the decomposition has a stale unresolved
    Yeast component.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-890b7c665c3d3962
    - ev-695925991c2ca346
  - name: legacy-native-ids
    value: '["SEM:870e68d3c55393c022b7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-695925991c2ca346
    - ev-890b7c665c3d3962
    - ev-9c2146f0adb0e6be
findings:
- finding_id: rec-f-450d27ab2c129875
  issue_key: mim-reconciliation-historical-review-coverage-and-r-efcfe3f13183bfaa
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Yeast_Meat_Extract_H2'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T21:36:19Z;
    reviewed SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad;
    current SHA-256=532680aa187d87f37cdb6afcb3e0d3011f44bb3e6dc63795d8620507e83dd2ad;
    hash_changed=False. Reports=["reports/yaml_record_review/Yeast_Meat_Extract_H2.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    fallback identity and final row pass, but the decomposition has a stale unresolved
    Yeast component.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-efcfe3f13183bfaa
  evidence_ids:
  - ev-890b7c665c3d3962
  - ev-695925991c2ca346
  - ev-9c2146f0adb0e6be
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Yeast_Meat_Extract_H2.yaml
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
