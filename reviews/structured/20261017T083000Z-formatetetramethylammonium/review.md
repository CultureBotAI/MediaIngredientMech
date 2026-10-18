# Per-record structured review: Formatetetramethylammonium (data/ingredients/mapped/Formatetetramethylammonium.yaml)

- Review: 20261017T083000Z-formatetetramethylammonium
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Formatetetramethylammonium (data/ingredients/mapped/Formatetetramethylammonium.yaml, record-b0cbacff8fb44778, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Formatetetramethylammonium.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Formatetetramethylammonium.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b0cbacff8fb44778 | data/ingredients/mapped/Formatetetramethylammonium.yaml | maintained | Formatetetramethylammonium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b0cbacff8fb44778 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b0cbacff8fb44778 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b0cbacff8fb44778 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b0cbacff8fb44778.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b0cbacff8fb44778.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T16:58:08Z; reviewed SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867; current SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867; hash_changed=False. Reports=["reports/yaml_record_review/Formatetetramethylammonium.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local two-component fallback identity, component partonomy, and SSSOM row pass, but notes are stale.

## Findings

### rec-f-2eff5ae9df80bca0: Historical review coverage and residual narrative: Formatetetramethylammonium

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b0cbacff8fb44778.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T16:58:08Z; reviewed SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867; current SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867; hash_changed=False. Reports=["reports/yaml_record_review/Formatetetramethylammonium.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local two-component fallback identity, component partonomy, and SSSOM row pass, but notes are stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4945accfcfdbfada | data/ingredients/mapped/Formatetetramethylammonium.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[28],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:formate_tetramethylammonium","line":30,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:formate_tetramethylammonium","preferred_term":"Formate+tetramethylammonium"}],"identifier":"kgmicrobe.ingredient:formate_tetramethylammonium","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:formate_tetramethylammonium","ontology_label":"Formate+tetramethylammonium","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Formate+tetramethylammonium","sssom_rows":[{"data_row":1234,"object_id":"kgmicrobe.ingredient:formate_tetramethylammonium","object_label":"Formate+tetramethylammonium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Formatetetramethylammonium","synonym_count":1} |
| ev-aca3e70b029cfd5b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [28] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-dc08e9de688eab0d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Formatetetramethylammonium; data-row positions=[1234] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1234,"object_id":"kgmicrobe.ingredient:formate_tetramethylammonium","object_label":"Formate+tetramethylammonium","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Formatetetramethylammonium","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-11a974454278792b | docs/data/mapped_ingredients.csv; CSV lines=[30] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:formate_tetramethylammonium","line":30,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:formate_tetramethylammonium","preferred_term":"Formate+tetramethylammonium","total_occurrences":"0"}] |
| ev-8228960de850c1e2 | reports/yaml_record_review/Formatetetramethylammonium.md; &#96;data/ingredients/mapped/Formatetetramethylammonium.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:40; Completeness:68; Recommended Edits:75 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f4d0bb0956bffcff | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[629] | context_only | [{"current_record_sha256":"541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867","finding_id":"SEM:27950122f33763143e54","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-formatetetramethylammonium
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Formatetetramethylammonium (data/ingredients/mapped/Formatetetramethylammonium.yaml)'
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
summary: Per-record structured review for Formatetetramethylammonium (data/ingredients/mapped/Formatetetramethylammonium.yaml,
  record-b0cbacff8fb44778, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Formatetetramethylammonium.yaml
    sha256: 541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867
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
  - path: reports/yaml_record_review/Formatetetramethylammonium.md
    sha256: 1805a83ebb805b000609970ffcdf4099f53b07fcf4006e942fd1d069d9b52fc8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b0cbacff8fb44778
  path: data/ingredients/mapped/Formatetetramethylammonium.yaml
  label: Formatetetramethylammonium
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Formatetetramethylammonium.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Formatetetramethylammonium.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Formatetetramethylammonium.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b0cbacff8fb44778
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b0cbacff8fb44778
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b0cbacff8fb44778
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b0cbacff8fb44778
evidence:
- evidence_id: ev-4945accfcfdbfada
  kind: record_content
  reference: data/ingredients/mapped/Formatetetramethylammonium.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[28],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:formate_tetramethylammonium","line":30,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:formate_tetramethylammonium","preferred_term":"Formate+tetramethylammonium"}],"identifier":"kgmicrobe.ingredient:formate_tetramethylammonium","ingredient_type":"NAMED_MEDIUM","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:formate_tetramethylammonium","ontology_label":"Formate+tetramethylammonium","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Formate+tetramethylammonium","sssom_rows":[{"data_row":1234,"object_id":"kgmicrobe.ingredient:formate_tetramethylammonium","object_label":"Formate+tetramethylammonium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Formatetetramethylammonium","synonym_count":1}'
  snapshot_sha256: 541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867
- evidence_id: ev-aca3e70b029cfd5b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [28]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-dc08e9de688eab0d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Formatetetramethylammonium; data-row positions=[1234]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1234,"object_id":"kgmicrobe.ingredient:formate_tetramethylammonium","object_label":"Formate+tetramethylammonium","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Formatetetramethylammonium","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-11a974454278792b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[30]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:formate_tetramethylammonium","line":30,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:formate_tetramethylammonium","preferred_term":"Formate+tetramethylammonium","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8228960de850c1e2
  kind: prior_review
  reference: reports/yaml_record_review/Formatetetramethylammonium.md
  locator: '`data/ingredients/mapped/Formatetetramethylammonium.yaml`:2; Verdict:4;
    Identity:11; Validation:26; Evidence:40; Completeness:68; Recommended Edits:75'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1805a83ebb805b000609970ffcdf4099f53b07fcf4006e942fd1d069d9b52fc8
  quote: "Recommended Edits:\n- Minor: refresh `notes` in\n  `data/ingredients/mapped/Formatetetramethylammonium.yaml`\
    \ so it describes the\n  current reviewed local fallback decomposition.\n- Minor:\
    \ replace `ontology_mapping.evidence[0].notes` with the post-curated\n  state:\
    \ both source-label parts are resolved, both carry component IDs, and\n  the current\
    \ type is `NAMED_MEDIUM`."
- evidence_id: ev-f4d0bb0956bffcff
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[629]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867","finding_id":"SEM:27950122f33763143e54","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d8f58453ec0c5c2c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b0cbacff8fb44778
  evidence_ids:
  - ev-4945accfcfdbfada
  - ev-aca3e70b029cfd5b
  - ev-dc08e9de688eab0d
  - ev-11a974454278792b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6fcce31af57c7295
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b0cbacff8fb44778
  evidence_ids:
  - ev-8228960de850c1e2
  - ev-4945accfcfdbfada
  - ev-f4d0bb0956bffcff
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T16:58:08Z;
    reviewed SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867;
    current SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867;
    hash_changed=False. Reports=["reports/yaml_record_review/Formatetetramethylammonium.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    two-component fallback identity, component partonomy, and SSSOM row pass, but
    notes are stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8228960de850c1e2
    - ev-4945accfcfdbfada
  - name: legacy-native-ids
    value: '["SEM:27950122f33763143e54"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4945accfcfdbfada
    - ev-8228960de850c1e2
    - ev-f4d0bb0956bffcff
findings:
- finding_id: rec-f-2eff5ae9df80bca0
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b0cbacff8fb44778
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Formatetetramethylammonium'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T16:58:08Z;
    reviewed SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867;
    current SHA-256=541472c373a94d1840aed93b6234f25e9f560d3a82caa7c88970d5a89faea867;
    hash_changed=False. Reports=["reports/yaml_record_review/Formatetetramethylammonium.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    two-component fallback identity, component partonomy, and SSSOM row pass, but
    notes are stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b0cbacff8fb44778
  evidence_ids:
  - ev-8228960de850c1e2
  - ev-4945accfcfdbfada
  - ev-f4d0bb0956bffcff
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Formatetetramethylammonium.yaml
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
