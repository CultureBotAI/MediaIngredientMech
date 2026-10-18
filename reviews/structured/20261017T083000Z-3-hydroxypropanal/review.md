# Per-record structured review: 3-Hydroxypropanal (data/ingredients/mapped/3-Hydroxypropanal.yaml)

- Review: 20261017T083000Z-3-hydroxypropanal
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-Hydroxypropanal (data/ingredients/mapped/3-Hydroxypropanal.yaml, record-1b1a5d45f88628d3, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-Hydroxypropanal.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-Hydroxypropanal.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1b1a5d45f88628d3 | data/ingredients/mapped/3-Hydroxypropanal.yaml | maintained | 3-Hydroxypropanal |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1b1a5d45f88628d3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1b1a5d45f88628d3 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1b1a5d45f88628d3 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1b1a5d45f88628d3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1b1a5d45f88628d3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:56:39Z; reviewed SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100; current SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100; hash_changed=False. Reports=["reports/yaml_record_review/3-Hydroxypropanal.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active residual grounding to CHEBI:17871, occurrence count, SSSOM, and aggregate pass, but ingredient_type and ChEBI chemistry are missing.

## Findings

### rec-f-69195cfb2bf4d691: Historical review coverage and residual narrative: 3-Hydroxypropanal

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1b1a5d45f88628d3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:56:39Z; reviewed SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100; current SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100; hash_changed=False. Reports=["reports/yaml_record_review/3-Hydroxypropanal.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active residual grounding to CHEBI:17871, occurrence count, SSSOM, and aggregate pass, but ingredient_type and ChEBI chemistry are missing.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4a49d350f1ecc894 | data/ingredients/mapped/3-Hydroxypropanal.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2527],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17871","line":2529,"mapping_status":"MAPPED","ontology_id":"CHEBI:17871","preferred_term":"3-Hydroxypropanal"}],"identifier":"CHEBI:17871","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:17871","ontology_label":"3-hydroxypropanal","ontology_source":"CHEBI"},"preferred_term":"3-Hydroxypropanal","sssom_rows":[{"data_row":123,"object_id":"CHEBI:17871","object_label":"3-hydroxypropanal","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-Hydroxypropanal","synonym_count":0} |
| ev-0e8ccbf9e3c6dbc3 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2527] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-57687895a8161e25 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-Hydroxypropanal; data-row positions=[123] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":123,"object_id":"CHEBI:17871","object_label":"3-hydroxypropanal","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:3-Hydroxypropanal","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-d646479f8b5d435d | docs/data/mapped_ingredients.csv; CSV lines=[2529] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17871","line":2529,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:17871","preferred_term":"3-Hydroxypropanal","total_occurrences":"1"}] |
| ev-9507c7de180fb4c0 | reports/yaml_record_review/3-Hydroxypropanal.md; &#96;data/ingredients/mapped/3-Hydroxypropanal.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:36; Completeness:49; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cf4668c75df5b133 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[103] | context_only | [{"current_record_sha256":"57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100","finding_id":"SEM:2ddb3dd43d252687d4a5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-hydroxypropanal
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-Hydroxypropanal (data/ingredients/mapped/3-Hydroxypropanal.yaml)'
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
summary: Per-record structured review for 3-Hydroxypropanal (data/ingredients/mapped/3-Hydroxypropanal.yaml,
  record-1b1a5d45f88628d3, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-Hydroxypropanal.yaml
    sha256: 57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100
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
  - path: reports/yaml_record_review/3-Hydroxypropanal.md
    sha256: 1d9844edfb22e8e00f7b33c383450c809276607d5ac23b63a570bd1624679cb5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1b1a5d45f88628d3
  path: data/ingredients/mapped/3-Hydroxypropanal.yaml
  label: 3-Hydroxypropanal
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-Hydroxypropanal.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-Hydroxypropanal.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-Hydroxypropanal.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1b1a5d45f88628d3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1b1a5d45f88628d3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1b1a5d45f88628d3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1b1a5d45f88628d3
evidence:
- evidence_id: ev-4a49d350f1ecc894
  kind: record_content
  reference: data/ingredients/mapped/3-Hydroxypropanal.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2527],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17871","line":2529,"mapping_status":"MAPPED","ontology_id":"CHEBI:17871","preferred_term":"3-Hydroxypropanal"}],"identifier":"CHEBI:17871","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:17871","ontology_label":"3-hydroxypropanal","ontology_source":"CHEBI"},"preferred_term":"3-Hydroxypropanal","sssom_rows":[{"data_row":123,"object_id":"CHEBI:17871","object_label":"3-hydroxypropanal","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-Hydroxypropanal","synonym_count":0}'
  snapshot_sha256: 57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100
- evidence_id: ev-0e8ccbf9e3c6dbc3
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2527]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-57687895a8161e25
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-Hydroxypropanal; data-row positions=[123]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":123,"object_id":"CHEBI:17871","object_label":"3-hydroxypropanal","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:3-Hydroxypropanal","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d646479f8b5d435d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2529]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17871","line":2529,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:17871","preferred_term":"3-Hydroxypropanal","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9507c7de180fb4c0
  kind: prior_review
  reference: reports/yaml_record_review/3-Hydroxypropanal.md
  locator: '`data/ingredients/mapped/3-Hydroxypropanal.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:36; Completeness:49; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1d9844edfb22e8e00f7b33c383450c809276607d5ac23b63a570bd1624679cb5
  quote: "Recommended Edits:\n1. Set `ingredient_type: SINGLE_INGREDIENT`.\n2. Backfill\
    \ formula `C3H6O2`, InChI, and SMILES from ChEBI.\n3. Regenerate `data/curated/mapped_ingredients.yaml`,\n\
    \   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.\n\
    4. Re-run the focused strict/LinkML validators, `just qc-sssom`, and\n   `just\
    \ qc-flat-coverage` after those edits."
- evidence_id: ev-cf4668c75df5b133
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[103]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100","finding_id":"SEM:2ddb3dd43d252687d4a5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-5ab7c82c7a5252e1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1b1a5d45f88628d3
  evidence_ids:
  - ev-4a49d350f1ecc894
  - ev-0e8ccbf9e3c6dbc3
  - ev-57687895a8161e25
  - ev-d646479f8b5d435d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-20273487f4cb1397
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1b1a5d45f88628d3
  evidence_ids:
  - ev-9507c7de180fb4c0
  - ev-4a49d350f1ecc894
  - ev-cf4668c75df5b133
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:56:39Z;
    reviewed SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100;
    current SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100;
    hash_changed=False. Reports=["reports/yaml_record_review/3-Hydroxypropanal.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active residual
    grounding to CHEBI:17871, occurrence count, SSSOM, and aggregate pass, but ingredient_type
    and ChEBI chemistry are missing.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9507c7de180fb4c0
    - ev-4a49d350f1ecc894
  - name: legacy-native-ids
    value: '["SEM:2ddb3dd43d252687d4a5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4a49d350f1ecc894
    - ev-9507c7de180fb4c0
    - ev-cf4668c75df5b133
findings:
- finding_id: rec-f-69195cfb2bf4d691
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1b1a5d45f88628d3
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 3-Hydroxypropanal'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:56:39Z;
    reviewed SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100;
    current SHA-256=57371b55b90b1eb9206906a66c75449b7f0cd8641f617d2a04db94304caf0100;
    hash_changed=False. Reports=["reports/yaml_record_review/3-Hydroxypropanal.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active residual
    grounding to CHEBI:17871, occurrence count, SSSOM, and aggregate pass, but ingredient_type
    and ChEBI chemistry are missing.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1b1a5d45f88628d3
  evidence_ids:
  - ev-9507c7de180fb4c0
  - ev-4a49d350f1ecc894
  - ev-cf4668c75df5b133
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-Hydroxypropanal.yaml
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
