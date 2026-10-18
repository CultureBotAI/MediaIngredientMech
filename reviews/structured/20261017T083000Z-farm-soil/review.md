# Per-record structured review: Farm_soil (data/ingredients/mapped/Farm_soil.yaml)

- Review: 20261017T083000Z-farm-soil
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Farm_soil (data/ingredients/mapped/Farm_soil.yaml, record-f174435924b82bd2, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Farm_soil.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Farm_soil.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f174435924b82bd2 | data/ingredients/mapped/Farm_soil.yaml | maintained | Farm_soil |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f174435924b82bd2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f174435924b82bd2 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f174435924b82bd2 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f174435924b82bd2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f174435924b82bd2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:05:10Z; reviewed SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2; current SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2; hash_changed=False. Reports=["reports/yaml_record_review/Farm_soil.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ENVO farm soil identity and final SSSOM row pass, but ingredient_type should be backfilled.

## Findings

### rec-f-bd0cf13cc6d034c9: Historical review coverage and residual narrative: Farm_soil

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-f174435924b82bd2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:05:10Z; reviewed SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2; current SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2; hash_changed=False. Reports=["reports/yaml_record_review/Farm_soil.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ENVO farm soil identity and final SSSOM row pass, but ingredient_type should be backfilled.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9ee97fc3e406d844 | data/ingredients/mapped/Farm_soil.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2563],"raw_equal":true},"docs_rows":[{"identifier":"ENVO:00005749","line":2565,"mapping_status":"MAPPED","ontology_id":"ENVO:00005749","preferred_term":"farm soil"}],"identifier":"ENVO:00005749","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"ENVO:00005749","ontology_label":"farm soil","ontology_source":"ENVO"},"preferred_term":"farm soil","sssom_rows":[{"data_row":1163,"object_id":"ENVO:00005749","object_label":"farm soil","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Farm_soil","synonym_count":0} |
| ev-9099af2c82af5c36 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2563] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3d94e3cc79953454 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Farm_soil; data-row positions=[1163] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1163,"object_id":"ENVO:00005749","object_label":"farm soil","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Farm_soil","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-6c6964956d0bce7e | docs/data/mapped_ingredients.csv; CSV lines=[2565] | supports | Published identity and count rows inspected: [{"identifier":"ENVO:00005749","line":2565,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"ENVO:00005749","preferred_term":"farm soil","total_occurrences":"1"}] |
| ev-0d2aa9edd62e6c60 | reports/yaml_record_review/Farm_soil.md; &#96;data/ingredients/mapped/Farm_soil.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:29; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e548c4b2be8f894f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[581] | context_only | [{"current_record_sha256":"65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2","finding_id":"SEM:d9cd66c6bb67c1b5198a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-farm-soil
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Farm_soil (data/ingredients/mapped/Farm_soil.yaml)'
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
summary: Per-record structured review for Farm_soil (data/ingredients/mapped/Farm_soil.yaml,
  record-f174435924b82bd2, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Farm_soil.yaml
    sha256: 65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2
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
  - path: reports/yaml_record_review/Farm_soil.md
    sha256: c7828b585e8fafcafb0e16797e5763a394b0106295a039bd5451f6bc6b404889
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f174435924b82bd2
  path: data/ingredients/mapped/Farm_soil.yaml
  label: Farm_soil
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Farm_soil.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Farm_soil.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Farm_soil.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f174435924b82bd2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f174435924b82bd2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f174435924b82bd2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f174435924b82bd2
evidence:
- evidence_id: ev-9ee97fc3e406d844
  kind: record_content
  reference: data/ingredients/mapped/Farm_soil.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2563],"raw_equal":true},"docs_rows":[{"identifier":"ENVO:00005749","line":2565,"mapping_status":"MAPPED","ontology_id":"ENVO:00005749","preferred_term":"farm
    soil"}],"identifier":"ENVO:00005749","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"ENVO:00005749","ontology_label":"farm
    soil","ontology_source":"ENVO"},"preferred_term":"farm soil","sssom_rows":[{"data_row":1163,"object_id":"ENVO:00005749","object_label":"farm
    soil","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Farm_soil","synonym_count":0}'
  snapshot_sha256: 65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2
- evidence_id: ev-9099af2c82af5c36
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2563]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3d94e3cc79953454
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Farm_soil; data-row positions=[1163]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1163,"object_id":"ENVO:00005749","object_label":"farm
    soil","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Farm_soil","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6c6964956d0bce7e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2565]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"ENVO:00005749","line":2565,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"ENVO:00005749","preferred_term":"farm
    soil","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0d2aa9edd62e6c60
  kind: prior_review
  reference: reports/yaml_record_review/Farm_soil.md
  locator: '`data/ingredients/mapped/Farm_soil.yaml`:2; Verdict:4; Identity:10; Validation:22;
    Evidence:29; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c7828b585e8fafcafb0e16797e5763a394b0106295a039bd5451f6bc6b404889
  quote: "Recommended Edits:\n- Minor: set `ingredient_type: UNDEFINED_MIXTURE` on\n\
    \  `data/ingredients/mapped/Farm_soil.yaml`, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ and rerun strict validation."
- evidence_id: ev-e548c4b2be8f894f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[581]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2","finding_id":"SEM:d9cd66c6bb67c1b5198a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-67a08849845680fc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f174435924b82bd2
  evidence_ids:
  - ev-9ee97fc3e406d844
  - ev-9099af2c82af5c36
  - ev-3d94e3cc79953454
  - ev-6c6964956d0bce7e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-595c1264421182aa
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f174435924b82bd2
  evidence_ids:
  - ev-0d2aa9edd62e6c60
  - ev-9ee97fc3e406d844
  - ev-e548c4b2be8f894f
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:05:10Z;
    reviewed SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2;
    current SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2;
    hash_changed=False. Reports=["reports/yaml_record_review/Farm_soil.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ENVO
    farm soil identity and final SSSOM row pass, but ingredient_type should be backfilled.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0d2aa9edd62e6c60
    - ev-9ee97fc3e406d844
  - name: legacy-native-ids
    value: '["SEM:d9cd66c6bb67c1b5198a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9ee97fc3e406d844
    - ev-0d2aa9edd62e6c60
    - ev-e548c4b2be8f894f
findings:
- finding_id: rec-f-bd0cf13cc6d034c9
  issue_key: mim-reconciliation-historical-review-coverage-and-r-f174435924b82bd2
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Farm_soil'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:05:10Z;
    reviewed SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2;
    current SHA-256=65771db536e8dda29b993cc6a7e98f47b58c1b959111272de6c4681b5865abb2;
    hash_changed=False. Reports=["reports/yaml_record_review/Farm_soil.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ENVO
    farm soil identity and final SSSOM row pass, but ingredient_type should be backfilled.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f174435924b82bd2
  evidence_ids:
  - ev-0d2aa9edd62e6c60
  - ev-9ee97fc3e406d844
  - ev-e548c4b2be8f894f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Farm_soil.yaml
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
