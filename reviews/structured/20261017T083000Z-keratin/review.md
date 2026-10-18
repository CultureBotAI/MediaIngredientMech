# Per-record structured review: Keratin (data/ingredients/mapped/Keratin.yaml)

- Review: 20261017T083000Z-keratin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Keratin (data/ingredients/mapped/Keratin.yaml, record-af584a671cc1aa9e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Keratin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Keratin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-af584a671cc1aa9e | data/ingredients/mapped/Keratin.yaml | maintained | Keratin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-af584a671cc1aa9e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-af584a671cc1aa9e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-af584a671cc1aa9e | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-af584a671cc1aa9e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-af584a671cc1aa9e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:43:21Z; reviewed SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8; current SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8; hash_changed=False. Reports=["reports/yaml_record_review/Keratin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The close MeSH Keratins parent mapping and occurrence count pass, but final SSSOM publishes the curated CLOSE_MATCH as skos:exactMatch instead of skos:closeMatch.

## Findings

### rec-f-caded2a3c3578949: Historical review coverage and residual narrative: Keratin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-af584a671cc1aa9e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:43:21Z; reviewed SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8; current SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8; hash_changed=False. Reports=["reports/yaml_record_review/Keratin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The close MeSH Keratins parent mapping and occurrence count pass, but final SSSOM publishes the curated CLOSE_MATCH as skos:exactMatch instead of skos:closeMatch.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4bb3a5c339b628a9 | data/ingredients/mapped/Keratin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[167],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D007633","line":169,"mapping_status":"MAPPED","ontology_id":"mesh:D007633","preferred_term":"Keratin"}],"identifier":"mesh:D007633","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"mesh:D007633","ontology_label":"Keratins","ontology_source":"MESH"},"preferred_term":"Keratin","sssom_rows":[{"data_row":1545,"object_id":"mesh:D007633","object_label":"Keratins","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Keratin","synonym_count":1} |
| ev-4a2e1a0a4f6dfd64 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [167] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d4f78dc36511ebfa | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Keratin; data-row positions=[1545] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1545,"object_id":"mesh:D007633","object_label":"Keratins","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Keratin","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-6e86ee62d7312be5 | docs/data/mapped_ingredients.csv; CSV lines=[169] | supports | Published identity and count rows inspected: [{"identifier":"mesh:D007633","line":169,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"mesh:D007633","preferred_term":"Keratin","total_occurrences":"1"}] |
| ev-de5bce026c32581e | reports/yaml_record_review/Keratin.md; &#96;data/ingredients/mapped/Keratin.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Completeness:48; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4669f00f393552dc | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[772] | context_only | [{"current_record_sha256":"766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8","finding_id":"SEM:4850d6929b93483692ea","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-keratin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Keratin (data/ingredients/mapped/Keratin.yaml)'
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
summary: Per-record structured review for Keratin (data/ingredients/mapped/Keratin.yaml,
  record-af584a671cc1aa9e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Keratin.yaml
    sha256: 766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8
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
  - path: reports/yaml_record_review/Keratin.md
    sha256: 51ef0403608cd16f151b910e1c5b341881cf250530ce50b0e03f78f90d0f679f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-af584a671cc1aa9e
  path: data/ingredients/mapped/Keratin.yaml
  label: Keratin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Keratin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Keratin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Keratin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-af584a671cc1aa9e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-af584a671cc1aa9e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-af584a671cc1aa9e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-af584a671cc1aa9e
evidence:
- evidence_id: ev-4bb3a5c339b628a9
  kind: record_content
  reference: data/ingredients/mapped/Keratin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[167],"raw_equal":true},"docs_rows":[{"identifier":"mesh:D007633","line":169,"mapping_status":"MAPPED","ontology_id":"mesh:D007633","preferred_term":"Keratin"}],"identifier":"mesh:D007633","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"mesh:D007633","ontology_label":"Keratins","ontology_source":"MESH"},"preferred_term":"Keratin","sssom_rows":[{"data_row":1545,"object_id":"mesh:D007633","object_label":"Keratins","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Keratin","synonym_count":1}'
  snapshot_sha256: 766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8
- evidence_id: ev-4a2e1a0a4f6dfd64
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [167]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d4f78dc36511ebfa
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Keratin; data-row positions=[1545]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1545,"object_id":"mesh:D007633","object_label":"Keratins","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Keratin","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6e86ee62d7312be5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[169]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:D007633","line":169,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"mesh:D007633","preferred_term":"Keratin","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-de5bce026c32581e
  kind: prior_review
  reference: reports/yaml_record_review/Keratin.md
  locator: '`data/ingredients/mapped/Keratin.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:31; Completeness:48; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 51ef0403608cd16f151b910e1c5b341881cf250530ce50b0e03f78f90d0f679f
  quote: "Recommended Edits:\n- Major: regenerate or repair `mappings/ingredient_mappings.sssom.tsv`\
    \ so\n  `MIM:Keratin` maps to `mesh:D007633` with `skos:closeMatch`, then rerun\n\
    \  SSSOM invariants and id-label validation.\n- Minor: refresh `notes` in `data/ingredients/mapped/Keratin.yaml`\
    \ so it no\n  longer says curator review is pending after the MeSH repair."
- evidence_id: ev-4669f00f393552dc
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[772]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8","finding_id":"SEM:4850d6929b93483692ea","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-00aec9b711eef48a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-af584a671cc1aa9e
  evidence_ids:
  - ev-4bb3a5c339b628a9
  - ev-4a2e1a0a4f6dfd64
  - ev-d4f78dc36511ebfa
  - ev-6e86ee62d7312be5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cc67c0f261405f6b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-af584a671cc1aa9e
  evidence_ids:
  - ev-de5bce026c32581e
  - ev-4bb3a5c339b628a9
  - ev-4669f00f393552dc
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:43:21Z;
    reviewed SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8;
    current SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8;
    hash_changed=False. Reports=["reports/yaml_record_review/Keratin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The close MeSH Keratins
    parent mapping and occurrence count pass, but final SSSOM publishes the curated
    CLOSE_MATCH as skos:exactMatch instead of skos:closeMatch.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-de5bce026c32581e
    - ev-4bb3a5c339b628a9
  - name: legacy-native-ids
    value: '["SEM:4850d6929b93483692ea"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4bb3a5c339b628a9
    - ev-de5bce026c32581e
    - ev-4669f00f393552dc
findings:
- finding_id: rec-f-caded2a3c3578949
  issue_key: mim-reconciliation-historical-review-coverage-and-r-af584a671cc1aa9e
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Keratin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:43:21Z;
    reviewed SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8;
    current SHA-256=766f4c2300194f7dad8ceb303df1f29e4ae0a68968c0b05ff414bfdfb0d235d8;
    hash_changed=False. Reports=["reports/yaml_record_review/Keratin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The close MeSH Keratins
    parent mapping and occurrence count pass, but final SSSOM publishes the curated
    CLOSE_MATCH as skos:exactMatch instead of skos:closeMatch.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-af584a671cc1aa9e
  evidence_ids:
  - ev-de5bce026c32581e
  - ev-4bb3a5c339b628a9
  - ev-4669f00f393552dc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Keratin.yaml
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
