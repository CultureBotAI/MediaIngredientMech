# Per-record structured review: L-alanylglycine (data/ingredients/mapped/L-alanylglycine.yaml)

- Review: 20261017T083000Z-l-alanylglycine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-alanylglycine (data/ingredients/mapped/L-alanylglycine.yaml, record-27d19d0976f9f6e8, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-alanylglycine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-alanylglycine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-27d19d0976f9f6e8 | data/ingredients/mapped/L-alanylglycine.yaml | maintained | L-alanylglycine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-27d19d0976f9f6e8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-27d19d0976f9f6e8 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-27d19d0976f9f6e8 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-27d19d0976f9f6e8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-27d19d0976f9f6e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:36:49Z; reviewed SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c; current SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c; hash_changed=False. Reports=["reports/yaml_record_review/L-alanylglycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI synonym identity, structure, empty final other field, and SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.

## Findings

### rec-f-27ceaca1d3dc7578: Historical review coverage and residual narrative: L-alanylglycine

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-27d19d0976f9f6e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:36:49Z; reviewed SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c; current SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c; hash_changed=False. Reports=["reports/yaml_record_review/L-alanylglycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI synonym identity, structure, empty final other field, and SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-070a2334a2fd7005 | data/ingredients/mapped/L-alanylglycine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[248],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:73757","line":250,"mapping_status":"MAPPED","ontology_id":"CHEBI:73757","preferred_term":"L-alanylglycine"}],"identifier":"CHEBI:73757","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":6,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:73757","ontology_label":"Ala-Gly","ontology_source":"CHEBI"},"preferred_term":"L-alanylglycine","sssom_rows":[{"data_row":1596,"object_id":"CHEBI:73757","object_label":"Ala-Gly","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-alanylglycine","synonym_count":1} |
| ev-8146cc3c3e8dc673 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [248] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1a1f50298a600614 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-alanylglycine; data-row positions=[1596] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1596,"object_id":"CHEBI:73757","object_label":"Ala-Gly","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:L-alanylglycine","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-04"}] |
| ev-50eb756f29917975 | docs/data/mapped_ingredients.csv; CSV lines=[250] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:73757","line":250,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73757","preferred_term":"L-alanylglycine","total_occurrences":"0"}] |
| ev-f3a8543107361abb | reports/yaml_record_review/L-alanylglycine.md; &#96;data/ingredients/mapped/L-alanylglycine.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:27; Completeness:44; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-98ffcffa82094b5b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[804] | context_only | [{"current_record_sha256":"be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c","finding_id":"SEM:04a26800bad22404b690","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-alanylglycine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-alanylglycine (data/ingredients/mapped/L-alanylglycine.yaml)'
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
summary: Per-record structured review for L-alanylglycine (data/ingredients/mapped/L-alanylglycine.yaml,
  record-27d19d0976f9f6e8, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-alanylglycine.yaml
    sha256: be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-alanylglycine.md
    sha256: d9c48a7cd60ca281e1eb6eb9140d846899c37d288ccb1ceaf7223847ce7b12c0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-27d19d0976f9f6e8
  path: data/ingredients/mapped/L-alanylglycine.yaml
  label: L-alanylglycine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-alanylglycine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-alanylglycine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-alanylglycine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-27d19d0976f9f6e8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-27d19d0976f9f6e8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-27d19d0976f9f6e8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-27d19d0976f9f6e8
evidence:
- evidence_id: ev-070a2334a2fd7005
  kind: record_content
  reference: data/ingredients/mapped/L-alanylglycine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[248],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:73757","line":250,"mapping_status":"MAPPED","ontology_id":"CHEBI:73757","preferred_term":"L-alanylglycine"}],"identifier":"CHEBI:73757","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":6,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:73757","ontology_label":"Ala-Gly","ontology_source":"CHEBI"},"preferred_term":"L-alanylglycine","sssom_rows":[{"data_row":1596,"object_id":"CHEBI:73757","object_label":"Ala-Gly","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-alanylglycine","synonym_count":1}'
  snapshot_sha256: be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c
- evidence_id: ev-8146cc3c3e8dc673
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [248]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1a1f50298a600614
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-alanylglycine; data-row positions=[1596]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1596,"object_id":"CHEBI:73757","object_label":"Ala-Gly","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:L-alanylglycine","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-50eb756f29917975
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[250]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:73757","line":250,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73757","preferred_term":"L-alanylglycine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f3a8543107361abb
  kind: prior_review
  reference: reports/yaml_record_review/L-alanylglycine.md
  locator: '`data/ingredients/mapped/L-alanylglycine.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:27; Completeness:44; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d9c48a7cd60ca281e1eb6eb9140d846899c37d288ccb1ceaf7223847ce7b12c0
  quote: "Recommended Edits:\n- Minor: update the stale top-level `notes` in\n  `data/ingredients/mapped/L-alanylglycine.yaml`\
    \ and the aggregate copy the\n  next time the record is touched so the current\
    \ review text does not imply\n  that the CHEBI search is still unresolved."
- evidence_id: ev-98ffcffa82094b5b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[804]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c","finding_id":"SEM:04a26800bad22404b690","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-995821cfbd5df987
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-27d19d0976f9f6e8
  evidence_ids:
  - ev-070a2334a2fd7005
  - ev-8146cc3c3e8dc673
  - ev-1a1f50298a600614
  - ev-50eb756f29917975
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cd6748b31ea7c4f5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-27d19d0976f9f6e8
  evidence_ids:
  - ev-f3a8543107361abb
  - ev-070a2334a2fd7005
  - ev-98ffcffa82094b5b
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:36:49Z;
    reviewed SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c;
    current SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c;
    hash_changed=False. Reports=["reports/yaml_record_review/L-alanylglycine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI
    synonym identity, structure, empty final other field, and SSSOM row pass, but
    stale importer notes still say no CHEBI/NCIT match was found.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f3a8543107361abb
    - ev-070a2334a2fd7005
  - name: legacy-native-ids
    value: '["SEM:04a26800bad22404b690"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-070a2334a2fd7005
    - ev-f3a8543107361abb
    - ev-98ffcffa82094b5b
findings:
- finding_id: rec-f-27ceaca1d3dc7578
  issue_key: mim-reconciliation-historical-review-coverage-and-r-27d19d0976f9f6e8
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-alanylglycine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:36:49Z;
    reviewed SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c;
    current SHA-256=be592fbf7c4c0713b0962fb7db4c100d07ebeb53eac160ef4a93adff0f4df93c;
    hash_changed=False. Reports=["reports/yaml_record_review/L-alanylglycine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI
    synonym identity, structure, empty final other field, and SSSOM row pass, but
    stale importer notes still say no CHEBI/NCIT match was found.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-27d19d0976f9f6e8
  evidence_ids:
  - ev-f3a8543107361abb
  - ev-070a2334a2fd7005
  - ev-98ffcffa82094b5b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-alanylglycine.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
