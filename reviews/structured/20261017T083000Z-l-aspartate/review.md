# Per-record structured review: L-aspartate (data/ingredients/mapped/L-aspartate.yaml)

- Review: 20261017T083000Z-l-aspartate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-aspartate (data/ingredients/mapped/L-aspartate.yaml, record-407c0dff68cff5a0, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-aspartate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-aspartate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-407c0dff68cff5a0 | data/ingredients/mapped/L-aspartate.yaml | maintained | L-aspartate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-407c0dff68cff5a0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-407c0dff68cff5a0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-407c0dff68cff5a0 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-407c0dff68cff5a0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-407c0dff68cff5a0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:42:39Z; reviewed SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766; current SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766; hash_changed=False. Reports=["reports/yaml_record_review/L-aspartate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI synonym identity, monoanion structure, occurrence count, empty final other field, and SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.

## Findings

### rec-f-ecbcc64e45227d47: Historical review coverage and residual narrative: L-aspartate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-407c0dff68cff5a0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:42:39Z; reviewed SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766; current SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766; hash_changed=False. Reports=["reports/yaml_record_review/L-aspartate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI synonym identity, monoanion structure, occurrence count, empty final other field, and SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1577b199b9b32b75 | data/ingredients/mapped/L-aspartate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[247],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29991","line":249,"mapping_status":"MAPPED","ontology_id":"CHEBI:29991","preferred_term":"L-aspartate"}],"identifier":"CHEBI:29991","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":21,"edge_count":21,"occurrences":21},"occurrence_statistics":{"media_count":21,"source_occurrences":[{"count":65,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":21},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:29991","ontology_label":"L-aspartate(1-)","ontology_source":"CHEBI"},"preferred_term":"L-aspartate","sssom_rows":[{"data_row":1603,"object_id":"CHEBI:29991","object_label":"L-aspartate(1-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-aspartate","synonym_count":1} |
| ev-5107271e159a7a1c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [247] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9da7a55c9bfdb54c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-aspartate; data-row positions=[1603] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1603,"object_id":"CHEBI:29991","object_label":"L-aspartate(1-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:L-aspartate","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-04"}] |
| ev-fe39d327a48cc035 | docs/data/mapped_ingredients.csv; CSV lines=[249] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29991","line":249,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"21","ontology_id":"CHEBI:29991","preferred_term":"L-aspartate","total_occurrences":"21"}] |
| ev-9a9aa0a7b05c5ed1 | reports/yaml_record_review/L-aspartate.md; &#96;data/ingredients/mapped/L-aspartate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:27; Completeness:42; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-363b3ef8361c7efe | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[807] | context_only | [{"current_record_sha256":"cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766","finding_id":"SEM:535045206f1690c6f83e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-aspartate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-aspartate (data/ingredients/mapped/L-aspartate.yaml)'
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
summary: Per-record structured review for L-aspartate (data/ingredients/mapped/L-aspartate.yaml,
  record-407c0dff68cff5a0, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-aspartate.yaml
    sha256: cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766
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
  - path: reports/yaml_record_review/L-aspartate.md
    sha256: 750f9303ec8373f00e85f70590bc4cf3d597c36e3de9720fe3f073e84c58a214
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-407c0dff68cff5a0
  path: data/ingredients/mapped/L-aspartate.yaml
  label: L-aspartate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-aspartate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-aspartate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-aspartate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-407c0dff68cff5a0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-407c0dff68cff5a0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-407c0dff68cff5a0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-407c0dff68cff5a0
evidence:
- evidence_id: ev-1577b199b9b32b75
  kind: record_content
  reference: data/ingredients/mapped/L-aspartate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[247],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29991","line":249,"mapping_status":"MAPPED","ontology_id":"CHEBI:29991","preferred_term":"L-aspartate"}],"identifier":"CHEBI:29991","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":21,"edge_count":21,"occurrences":21},"occurrence_statistics":{"media_count":21,"source_occurrences":[{"count":65,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":21},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:29991","ontology_label":"L-aspartate(1-)","ontology_source":"CHEBI"},"preferred_term":"L-aspartate","sssom_rows":[{"data_row":1603,"object_id":"CHEBI:29991","object_label":"L-aspartate(1-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-aspartate","synonym_count":1}'
  snapshot_sha256: cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766
- evidence_id: ev-5107271e159a7a1c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [247]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9da7a55c9bfdb54c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-aspartate; data-row positions=[1603]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1603,"object_id":"CHEBI:29991","object_label":"L-aspartate(1-)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:L-aspartate","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fe39d327a48cc035
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[249]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29991","line":249,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"21","ontology_id":"CHEBI:29991","preferred_term":"L-aspartate","total_occurrences":"21"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9a9aa0a7b05c5ed1
  kind: prior_review
  reference: reports/yaml_record_review/L-aspartate.md
  locator: '`data/ingredients/mapped/L-aspartate.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:27; Completeness:42; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 750f9303ec8373f00e85f70590bc4cf3d597c36e3de9720fe3f073e84c58a214
  quote: "Recommended Edits:\n- Minor: update the stale top-level `notes` in\n  `data/ingredients/mapped/L-aspartate.yaml`\
    \ and the aggregate copy the next\n  time the record is touched so the current\
    \ review text does not imply that the\n  CHEBI search is still unresolved."
- evidence_id: ev-363b3ef8361c7efe
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[807]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766","finding_id":"SEM:535045206f1690c6f83e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4526c887910dc056
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-407c0dff68cff5a0
  evidence_ids:
  - ev-1577b199b9b32b75
  - ev-5107271e159a7a1c
  - ev-9da7a55c9bfdb54c
  - ev-fe39d327a48cc035
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2e1025391c149831
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-407c0dff68cff5a0
  evidence_ids:
  - ev-9a9aa0a7b05c5ed1
  - ev-1577b199b9b32b75
  - ev-363b3ef8361c7efe
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:42:39Z;
    reviewed SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766;
    current SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766;
    hash_changed=False. Reports=["reports/yaml_record_review/L-aspartate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CHEBI synonym
    identity, monoanion structure, occurrence count, empty final other field, and
    SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9a9aa0a7b05c5ed1
    - ev-1577b199b9b32b75
  - name: legacy-native-ids
    value: '["SEM:535045206f1690c6f83e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1577b199b9b32b75
    - ev-9a9aa0a7b05c5ed1
    - ev-363b3ef8361c7efe
findings:
- finding_id: rec-f-ecbcc64e45227d47
  issue_key: mim-reconciliation-historical-review-coverage-and-r-407c0dff68cff5a0
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: L-aspartate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T22:42:39Z;
    reviewed SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766;
    current SHA-256=cc1876e2cec8da89a54b310d22139738c5484421e05759f5f99f5a3289fe1766;
    hash_changed=False. Reports=["reports/yaml_record_review/L-aspartate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CHEBI synonym
    identity, monoanion structure, occurrence count, empty final other field, and
    SSSOM row pass, but stale importer notes still say no CHEBI/NCIT match was found.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-407c0dff68cff5a0
  evidence_ids:
  - ev-9a9aa0a7b05c5ed1
  - ev-1577b199b9b32b75
  - ev-363b3ef8361c7efe
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-aspartate.yaml
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
