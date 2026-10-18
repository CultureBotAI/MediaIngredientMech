# Per-record structured review: Glycylglycylglycine (data/ingredients/mapped/Glycylglycylglycine.yaml)

- Review: 20261017T083000Z-glycylglycylglycine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycylglycylglycine (data/ingredients/mapped/Glycylglycylglycine.yaml, record-b142df48f6f55d5e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycylglycylglycine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycylglycylglycine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b142df48f6f55d5e | data/ingredients/mapped/Glycylglycylglycine.yaml | maintained | Glycylglycylglycine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b142df48f6f55d5e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b142df48f6f55d5e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b142df48f6f55d5e | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b142df48f6f55d5e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b142df48f6f55d5e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:32:48Z; reviewed SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb; current SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb; hash_changed=False. Reports=["reports/yaml_record_review/Glycylglycylglycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The glycyl-glycyl-glycine synonym match and final SSSOM row pass, but the top-level note still says no CHEBI or NCIT match exists.

## Findings

### rec-f-6800450a63edbebe: Historical review coverage and residual narrative: Glycylglycylglycine

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b142df48f6f55d5e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:32:48Z; reviewed SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb; current SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb; hash_changed=False. Reports=["reports/yaml_record_review/Glycylglycylglycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The glycyl-glycyl-glycine synonym match and final SSSOM row pass, but the top-level note still says no CHEBI or NCIT match exists.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-316dcbbb86cf1df5 | data/ingredients/mapped/Glycylglycylglycine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[249],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63961","line":251,"mapping_status":"MAPPED","ontology_id":"CHEBI:63961","preferred_term":"Glycylglycylglycine"}],"identifier":"CHEBI:63961","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:63961","ontology_label":"glycyl-glycyl-glycine","ontology_source":"CHEBI"},"preferred_term":"Glycylglycylglycine","sssom_rows":[{"data_row":1354,"object_id":"CHEBI:63961","object_label":"glycyl-glycyl-glycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycylglycylglycine","synonym_count":1} |
| ev-d32581cf523ec372 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [249] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7cbd40701d99ab64 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycylglycylglycine; data-row positions=[1354] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1354,"object_id":"CHEBI:63961","object_label":"glycyl-glycyl-glycine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycylglycylglycine","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-04"}] |
| ev-0171a5995b60397a | docs/data/mapped_ingredients.csv; CSV lines=[251] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63961","line":251,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:63961","preferred_term":"Glycylglycylglycine","total_occurrences":"0"}] |
| ev-d70f564a6f951e87 | reports/yaml_record_review/Glycylglycylglycine.md; &#96;data/ingredients/mapped/Glycylglycylglycine.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:29; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6a25584fa33d1c26 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[702] | context_only | [{"current_record_sha256":"f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb","finding_id":"SEM:8f0f8704491379a4f914","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycylglycylglycine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycylglycylglycine (data/ingredients/mapped/Glycylglycylglycine.yaml)'
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
summary: Per-record structured review for Glycylglycylglycine (data/ingredients/mapped/Glycylglycylglycine.yaml,
  record-b142df48f6f55d5e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycylglycylglycine.yaml
    sha256: f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb
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
  - path: reports/yaml_record_review/Glycylglycylglycine.md
    sha256: d2b3d2c9a2869f9eb5c9d3186d2af32a2881a45698aa6c00e6ab5c97b0869b72
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b142df48f6f55d5e
  path: data/ingredients/mapped/Glycylglycylglycine.yaml
  label: Glycylglycylglycine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycylglycylglycine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycylglycylglycine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycylglycylglycine.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b142df48f6f55d5e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b142df48f6f55d5e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b142df48f6f55d5e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b142df48f6f55d5e
evidence:
- evidence_id: ev-316dcbbb86cf1df5
  kind: record_content
  reference: data/ingredients/mapped/Glycylglycylglycine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[249],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63961","line":251,"mapping_status":"MAPPED","ontology_id":"CHEBI:63961","preferred_term":"Glycylglycylglycine"}],"identifier":"CHEBI:63961","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:63961","ontology_label":"glycyl-glycyl-glycine","ontology_source":"CHEBI"},"preferred_term":"Glycylglycylglycine","sssom_rows":[{"data_row":1354,"object_id":"CHEBI:63961","object_label":"glycyl-glycyl-glycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycylglycylglycine","synonym_count":1}'
  snapshot_sha256: f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb
- evidence_id: ev-d32581cf523ec372
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [249]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7cbd40701d99ab64
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycylglycylglycine; data-row positions=[1354]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1354,"object_id":"CHEBI:63961","object_label":"glycyl-glycyl-glycine","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycylglycylglycine","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0171a5995b60397a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[251]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63961","line":251,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:63961","preferred_term":"Glycylglycylglycine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d70f564a6f951e87
  kind: prior_review
  reference: reports/yaml_record_review/Glycylglycylglycine.md
  locator: '`data/ingredients/mapped/Glycylglycylglycine.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:29; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d2b3d2c9a2869f9eb5c9d3186d2af32a2881a45698aa6c00e6ab5c97b0869b72
  quote: "Recommended Edits:\n- Minor: replace the stale top-level `notes` text in\n\
    \  `data/ingredients/mapped/Glycylglycylglycine.yaml` with a current note saying\n\
    \  the MicrobeDecoder residual label was reviewed and promoted to a ChEBI\n  synonym\
    \ match."
- evidence_id: ev-6a25584fa33d1c26
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[702]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb","finding_id":"SEM:8f0f8704491379a4f914","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-fc1dd6d4008e146a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b142df48f6f55d5e
  evidence_ids:
  - ev-316dcbbb86cf1df5
  - ev-d32581cf523ec372
  - ev-7cbd40701d99ab64
  - ev-0171a5995b60397a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d305b25899f21ab2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b142df48f6f55d5e
  evidence_ids:
  - ev-d70f564a6f951e87
  - ev-316dcbbb86cf1df5
  - ev-6a25584fa33d1c26
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:32:48Z;
    reviewed SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb;
    current SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycylglycylglycine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The glycyl-glycyl-glycine
    synonym match and final SSSOM row pass, but the top-level note still says no CHEBI
    or NCIT match exists.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d70f564a6f951e87
    - ev-316dcbbb86cf1df5
  - name: legacy-native-ids
    value: '["SEM:8f0f8704491379a4f914"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-316dcbbb86cf1df5
    - ev-d70f564a6f951e87
    - ev-6a25584fa33d1c26
findings:
- finding_id: rec-f-6800450a63edbebe
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b142df48f6f55d5e
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glycylglycylglycine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T18:32:48Z;
    reviewed SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb;
    current SHA-256=f63e5a69409786eda00ff318d1a478df48d218404008f18ebf1868ff86c2d9bb;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycylglycylglycine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The glycyl-glycyl-glycine
    synonym match and final SSSOM row pass, but the top-level note still says no CHEBI
    or NCIT match exists.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b142df48f6f55d5e
  evidence_ids:
  - ev-d70f564a6f951e87
  - ev-316dcbbb86cf1df5
  - ev-6a25584fa33d1c26
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycylglycylglycine.yaml
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
