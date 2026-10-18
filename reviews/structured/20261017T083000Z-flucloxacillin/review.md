# Per-record structured review: Flucloxacillin (data/ingredients/mapped/Flucloxacillin.yaml)

- Review: 20261017T083000Z-flucloxacillin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Flucloxacillin (data/ingredients/mapped/Flucloxacillin.yaml, record-fd3757756aa2c093, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Flucloxacillin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Flucloxacillin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fd3757756aa2c093 | data/ingredients/mapped/Flucloxacillin.yaml | maintained | Flucloxacillin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fd3757756aa2c093 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-fd3757756aa2c093 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fd3757756aa2c093 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fd3757756aa2c093.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fd3757756aa2c093.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:48:26Z; reviewed SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9; current SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9; hash_changed=False. Reports=["reports/yaml_record_review/Flucloxacillin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CultureMech residual grounding and SSSOM provenance pass, but ingredient_type is missing.

## Findings

### rec-f-8bafc00f803c803a: Historical review coverage and residual narrative: Flucloxacillin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-fd3757756aa2c093.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:48:26Z; reviewed SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9; current SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9; hash_changed=False. Reports=["reports/yaml_record_review/Flucloxacillin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CultureMech residual grounding and SSSOM provenance pass, but ingredient_type is missing.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-28ebfb3c0805e539 | data/ingredients/mapped/Flucloxacillin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2566],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:5098","line":2568,"mapping_status":"MAPPED","ontology_id":"CHEBI:5098","preferred_term":"flucloxacillin"}],"identifier":"CHEBI:5098","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:5098","ontology_label":"flucloxacillin","ontology_source":"CHEBI"},"preferred_term":"flucloxacillin","sssom_rows":[{"data_row":1221,"object_id":"CHEBI:5098","object_label":"flucloxacillin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Flucloxacillin","synonym_count":0} |
| ev-ea2d9f294fe4fb00 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2566] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c0c1974f2b240906 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Flucloxacillin; data-row positions=[1221] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1221,"object_id":"CHEBI:5098","object_label":"flucloxacillin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Flucloxacillin","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-933c11c1e5a29798 | docs/data/mapped_ingredients.csv; CSV lines=[2568] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:5098","line":2568,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:5098","preferred_term":"flucloxacillin","total_occurrences":"1"}] |
| ev-c7f0984e195894ef | reports/yaml_record_review/Flucloxacillin.md; &#96;data/ingredients/mapped/Flucloxacillin.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:31; Completeness:50; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8cd3bc33f5114e01 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[622] | context_only | [{"current_record_sha256":"dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9","finding_id":"SEM:2807087cbddf4c607a4f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-flucloxacillin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Flucloxacillin (data/ingredients/mapped/Flucloxacillin.yaml)'
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
summary: Per-record structured review for Flucloxacillin (data/ingredients/mapped/Flucloxacillin.yaml,
  record-fd3757756aa2c093, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Flucloxacillin.yaml
    sha256: dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9
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
  - path: reports/yaml_record_review/Flucloxacillin.md
    sha256: af7b6efdb4b2bac3979a24c4a85ec577bbce3c693935604674d6b04a93ed4610
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fd3757756aa2c093
  path: data/ingredients/mapped/Flucloxacillin.yaml
  label: Flucloxacillin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Flucloxacillin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Flucloxacillin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Flucloxacillin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fd3757756aa2c093
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fd3757756aa2c093
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-fd3757756aa2c093
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fd3757756aa2c093
evidence:
- evidence_id: ev-28ebfb3c0805e539
  kind: record_content
  reference: data/ingredients/mapped/Flucloxacillin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2566],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:5098","line":2568,"mapping_status":"MAPPED","ontology_id":"CHEBI:5098","preferred_term":"flucloxacillin"}],"identifier":"CHEBI:5098","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:5098","ontology_label":"flucloxacillin","ontology_source":"CHEBI"},"preferred_term":"flucloxacillin","sssom_rows":[{"data_row":1221,"object_id":"CHEBI:5098","object_label":"flucloxacillin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Flucloxacillin","synonym_count":0}'
  snapshot_sha256: dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9
- evidence_id: ev-ea2d9f294fe4fb00
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2566]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c0c1974f2b240906
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Flucloxacillin; data-row positions=[1221]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1221,"object_id":"CHEBI:5098","object_label":"flucloxacillin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Flucloxacillin","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-933c11c1e5a29798
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2568]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:5098","line":2568,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:5098","preferred_term":"flucloxacillin","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c7f0984e195894ef
  kind: prior_review
  reference: reports/yaml_record_review/Flucloxacillin.md
  locator: '`data/ingredients/mapped/Flucloxacillin.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:31; Completeness:50; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: af7b6efdb4b2bac3979a24c4a85ec577bbce3c693935604674d6b04a93ed4610
  quote: "Recommended Edits:\n- Minor: set `ingredient_type: SINGLE_INGREDIENT` in\n\
    \  `data/ingredients/mapped/Flucloxacillin.yaml`, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ and rerun strict validation plus the\n  final SSSOM invariant gates."
- evidence_id: ev-8cd3bc33f5114e01
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[622]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9","finding_id":"SEM:2807087cbddf4c607a4f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a9c48c538e66d1d1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fd3757756aa2c093
  evidence_ids:
  - ev-28ebfb3c0805e539
  - ev-ea2d9f294fe4fb00
  - ev-c0c1974f2b240906
  - ev-933c11c1e5a29798
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5866029f037fe4d7
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fd3757756aa2c093
  evidence_ids:
  - ev-c7f0984e195894ef
  - ev-28ebfb3c0805e539
  - ev-8cd3bc33f5114e01
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:48:26Z;
    reviewed SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9;
    current SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9;
    hash_changed=False. Reports=["reports/yaml_record_review/Flucloxacillin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CultureMech residual grounding and SSSOM provenance pass, but ingredient_type
    is missing.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c7f0984e195894ef
    - ev-28ebfb3c0805e539
  - name: legacy-native-ids
    value: '["SEM:2807087cbddf4c607a4f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-28ebfb3c0805e539
    - ev-c7f0984e195894ef
    - ev-8cd3bc33f5114e01
findings:
- finding_id: rec-f-8bafc00f803c803a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-fd3757756aa2c093
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Flucloxacillin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:48:26Z;
    reviewed SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9;
    current SHA-256=dadfb6772f985982737129b47b3df1a3e312e5f0d63377ca44f48f2976b917e9;
    hash_changed=False. Reports=["reports/yaml_record_review/Flucloxacillin.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CultureMech residual grounding and SSSOM provenance pass, but ingredient_type
    is missing.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fd3757756aa2c093
  evidence_ids:
  - ev-c7f0984e195894ef
  - ev-28ebfb3c0805e539
  - ev-8cd3bc33f5114e01
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Flucloxacillin.yaml
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
