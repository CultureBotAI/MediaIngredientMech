# Per-record structured review: Glucose_Peptone-yeast_Extract (data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml)

- Review: 20261017T083000Z-glucose-peptone-yeast-extract
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucose_Peptone-yeast_Extract (data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml, record-8b821004982be482, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8b821004982be482 | data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml | maintained | Glucose_Peptone-yeast_Extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8b821004982be482 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-8b821004982be482 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8b821004982be482 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8b821004982be482.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8b821004982be482.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z; reviewed SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5; current SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local glucose plus peptone plus yeast extract decomposition and final SSSOM row pass, but the stale top-level note needs cleanup.

## Findings

### rec-f-a446d641312fe2f5: Historical review coverage and residual narrative: Glucose_Peptone-yeast_Extract

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-8b821004982be482.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z; reviewed SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5; current SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5; hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local glucose plus peptone plus yeast extract decomposition and final SSSOM row pass, but the stale top-level note needs cleanup.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-51a7753b3866939c | data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[37],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","line":39,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","preferred_term":"Glucose Peptone-yeast Extract"}],"identifier":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","ontology_label":"Glucose Peptone-yeast Extract","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Glucose Peptone-yeast Extract","sssom_rows":[{"data_row":1314,"object_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","object_label":"Glucose Peptone-yeast Extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucose_Peptone-yeast_Extract","synonym_count":1} |
| ev-106606cbe0d37ce2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [37] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-309f1de26b3aa126 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucose_Peptone-yeast_Extract; data-row positions=[1314] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1314,"object_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","object_label":"Glucose Peptone-yeast Extract","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucose_Peptone-yeast_Extract","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-5cbb99a371e85b19 | docs/data/mapped_ingredients.csv; CSV lines=[39] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","line":39,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","preferred_term":"Glucose Peptone-yeast Extract","total_occurrences":"0"}] |
| ev-e4b672d378ecefd5 | reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md; &#96;data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:38; Completeness:64; Recommended Edits:72 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a18f27a1b02104e1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[674] | context_only | [{"current_record_sha256":"e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5","finding_id":"SEM:d8f11900bf0f924ec7c6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucose-peptone-yeast-extract
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucose_Peptone-yeast_Extract (data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml)'
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
summary: Per-record structured review for Glucose_Peptone-yeast_Extract (data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml,
  record-8b821004982be482, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
    sha256: e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5
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
  - path: reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md
    sha256: c29dfa7ccc3f295339c8c9d7b32d19253c63db26e1c9a5565288fad60abd14e9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8b821004982be482
  path: data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
  label: Glucose_Peptone-yeast_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8b821004982be482
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8b821004982be482
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8b821004982be482
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8b821004982be482
evidence:
- evidence_id: ev-51a7753b3866939c
  kind: record_content
  reference: data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[37],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","line":39,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","preferred_term":"Glucose
    Peptone-yeast Extract"}],"identifier":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","ontology_label":"Glucose
    Peptone-yeast Extract","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Glucose
    Peptone-yeast Extract","sssom_rows":[{"data_row":1314,"object_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","object_label":"Glucose
    Peptone-yeast Extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucose_Peptone-yeast_Extract","synonym_count":1}'
  snapshot_sha256: e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5
- evidence_id: ev-106606cbe0d37ce2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [37]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-309f1de26b3aa126
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucose_Peptone-yeast_Extract; data-row positions=[1314]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1314,"object_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","object_label":"Glucose
    Peptone-yeast Extract","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucose_Peptone-yeast_Extract","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5cbb99a371e85b19
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[39]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","line":39,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:glucose_peptone_yeast_extract","preferred_term":"Glucose
    Peptone-yeast Extract","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e4b672d378ecefd5
  kind: prior_review
  reference: reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md
  locator: '`data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml`:2; Verdict:4;
    Identity:12; Validation:24; Evidence:38; Completeness:64; Recommended Edits:72'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c29dfa7ccc3f295339c8c9d7b32d19253c63db26e1c9a5565288fad60abd14e9
  quote: "Recommended Edits:\n- Minor: refresh `notes` in\n  `data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml`\
    \ so it describes\n  the current reviewed local fallback decomposition."
- evidence_id: ev-a18f27a1b02104e1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[674]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5","finding_id":"SEM:d8f11900bf0f924ec7c6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0f10dcce8867a098
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8b821004982be482
  evidence_ids:
  - ev-51a7753b3866939c
  - ev-106606cbe0d37ce2
  - ev-309f1de26b3aa126
  - ev-5cbb99a371e85b19
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2443849ad0aa4fae
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8b821004982be482
  evidence_ids:
  - ev-e4b672d378ecefd5
  - ev-51a7753b3866939c
  - ev-a18f27a1b02104e1
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z;
    reviewed SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5;
    current SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    glucose plus peptone plus yeast extract decomposition and final SSSOM row pass,
    but the stale top-level note needs cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e4b672d378ecefd5
    - ev-51a7753b3866939c
  - name: legacy-native-ids
    value: '["SEM:d8f11900bf0f924ec7c6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-51a7753b3866939c
    - ev-e4b672d378ecefd5
    - ev-a18f27a1b02104e1
findings:
- finding_id: rec-f-a446d641312fe2f5
  issue_key: mim-reconciliation-historical-review-coverage-and-r-8b821004982be482
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glucose_Peptone-yeast_Extract'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z;
    reviewed SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5;
    current SHA-256=e37175824a9e5c477fedd007a279b35056d89ab2b8c4ab5f8f8b9504e09794a5;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucose_Peptone-yeast_Extract.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    glucose plus peptone plus yeast extract decomposition and final SSSOM row pass,
    but the stale top-level note needs cleanup.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8b821004982be482
  evidence_ids:
  - ev-e4b672d378ecefd5
  - ev-51a7753b3866939c
  - ev-a18f27a1b02104e1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucose_Peptone-yeast_Extract.yaml
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
