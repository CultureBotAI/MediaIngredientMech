# Per-record structured review: Glucose_Xylose (data/ingredients/mapped/Glucose_Xylose.yaml)

- Review: 20261017T083000Z-glucose-xylose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucose_Xylose (data/ingredients/mapped/Glucose_Xylose.yaml, record-2dce8d2b72b3aa6b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucose_Xylose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucose_Xylose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2dce8d2b72b3aa6b | data/ingredients/mapped/Glucose_Xylose.yaml | maintained | Glucose_Xylose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2dce8d2b72b3aa6b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2dce8d2b72b3aa6b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2dce8d2b72b3aa6b | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2dce8d2b72b3aa6b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2dce8d2b72b3aa6b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z; reviewed SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f; current SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Xylose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local glucose plus xylose decomposition and final SSSOM row pass, but stale notes need cleanup.

## Findings

### rec-f-ded1ad93daaa6225: Historical review coverage and residual narrative: Glucose_Xylose

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2dce8d2b72b3aa6b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z; reviewed SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f; current SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Xylose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local glucose plus xylose decomposition and final SSSOM row pass, but stale notes need cleanup.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f4f89378a3faa446 | data/ingredients/mapped/Glucose_Xylose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[38],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:glucose_xylose","line":40,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:glucose_xylose","preferred_term":"Glucose + Xylose"}],"identifier":"kgmicrobe.ingredient:glucose_xylose","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:glucose_xylose","ontology_label":"Glucose + Xylose","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Glucose + Xylose","sssom_rows":[{"data_row":1315,"object_id":"kgmicrobe.ingredient:glucose_xylose","object_label":"Glucose + Xylose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucose_Xylose","synonym_count":1} |
| ev-9c0b092fcf37dc84 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [38] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0420c31b2ffb8f9e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucose_Xylose; data-row positions=[1315] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1315,"object_id":"kgmicrobe.ingredient:glucose_xylose","object_label":"Glucose + Xylose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucose_Xylose","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-1547e383ffc194a4 | docs/data/mapped_ingredients.csv; CSV lines=[40] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:glucose_xylose","line":40,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:glucose_xylose","preferred_term":"Glucose + Xylose","total_occurrences":"0"}] |
| ev-c161494c3b06d79a | reports/yaml_record_review/Glucose_Xylose.md; &#96;data/ingredients/mapped/Glucose_Xylose.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:35; Completeness:60; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-51886ce0431512c1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[675] | context_only | [{"current_record_sha256":"bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f","finding_id":"SEM:7c98929be346c4d2ec69","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucose-xylose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucose_Xylose (data/ingredients/mapped/Glucose_Xylose.yaml)'
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
summary: Per-record structured review for Glucose_Xylose (data/ingredients/mapped/Glucose_Xylose.yaml,
  record-2dce8d2b72b3aa6b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucose_Xylose.yaml
    sha256: bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f
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
  - path: reports/yaml_record_review/Glucose_Xylose.md
    sha256: 773fe8bd275fbec2abafaa75814330ec1ca386e1d15c7ee753ab5a8d2220107d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2dce8d2b72b3aa6b
  path: data/ingredients/mapped/Glucose_Xylose.yaml
  label: Glucose_Xylose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_Xylose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucose_Xylose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucose_Xylose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2dce8d2b72b3aa6b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2dce8d2b72b3aa6b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2dce8d2b72b3aa6b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2dce8d2b72b3aa6b
evidence:
- evidence_id: ev-f4f89378a3faa446
  kind: record_content
  reference: data/ingredients/mapped/Glucose_Xylose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[38],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:glucose_xylose","line":40,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:glucose_xylose","preferred_term":"Glucose
    + Xylose"}],"identifier":"kgmicrobe.ingredient:glucose_xylose","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:glucose_xylose","ontology_label":"Glucose
    + Xylose","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Glucose
    + Xylose","sssom_rows":[{"data_row":1315,"object_id":"kgmicrobe.ingredient:glucose_xylose","object_label":"Glucose
    + Xylose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucose_Xylose","synonym_count":1}'
  snapshot_sha256: bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f
- evidence_id: ev-9c0b092fcf37dc84
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [38]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0420c31b2ffb8f9e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucose_Xylose; data-row positions=[1315]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1315,"object_id":"kgmicrobe.ingredient:glucose_xylose","object_label":"Glucose
    + Xylose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucose_Xylose","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1547e383ffc194a4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[40]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:glucose_xylose","line":40,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:glucose_xylose","preferred_term":"Glucose
    + Xylose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c161494c3b06d79a
  kind: prior_review
  reference: reports/yaml_record_review/Glucose_Xylose.md
  locator: '`data/ingredients/mapped/Glucose_Xylose.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:35; Completeness:60; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 773fe8bd275fbec2abafaa75814330ec1ca386e1d15c7ee753ab5a8d2220107d
  quote: "Recommended Edits:\n- Minor: refresh `notes` in\n  `data/ingredients/mapped/Glucose_Xylose.yaml`\
    \ so it describes the current\n  reviewed local fallback decomposition.\n- Minor:\
    \ replace the legacy `ingredient_type=DEFINED_MEDIUM` prose in\n  `ontology_mapping.evidence[0].notes`\
    \ with wording that either names the\n  current type or simply describes the two\
    \ defined components."
- evidence_id: ev-51886ce0431512c1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[675]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f","finding_id":"SEM:7c98929be346c4d2ec69","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-f4eb10753e6fe1b3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2dce8d2b72b3aa6b
  evidence_ids:
  - ev-f4f89378a3faa446
  - ev-9c0b092fcf37dc84
  - ev-0420c31b2ffb8f9e
  - ev-1547e383ffc194a4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-42a7e707f8685a1e
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2dce8d2b72b3aa6b
  evidence_ids:
  - ev-c161494c3b06d79a
  - ev-f4f89378a3faa446
  - ev-51886ce0431512c1
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z;
    reviewed SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f;
    current SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Xylose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    glucose plus xylose decomposition and final SSSOM row pass, but stale notes need
    cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c161494c3b06d79a
    - ev-f4f89378a3faa446
  - name: legacy-native-ids
    value: '["SEM:7c98929be346c4d2ec69"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f4f89378a3faa446
    - ev-c161494c3b06d79a
    - ev-51886ce0431512c1
findings:
- finding_id: rec-f-ded1ad93daaa6225
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2dce8d2b72b3aa6b
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glucose_Xylose'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z;
    reviewed SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f;
    current SHA-256=bfe6131c9ea1cd4558e93d984bbb63e4ae1ed1010b130b11847f4f299188260f;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Xylose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    glucose plus xylose decomposition and final SSSOM row pass, but stale notes need
    cleanup.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2dce8d2b72b3aa6b
  evidence_ids:
  - ev-c161494c3b06d79a
  - ev-f4f89378a3faa446
  - ev-51886ce0431512c1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_Xylose.yaml
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
