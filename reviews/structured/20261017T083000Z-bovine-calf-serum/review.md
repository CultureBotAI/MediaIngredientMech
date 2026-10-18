# Per-record structured review: Bovine_Calf_Serum (data/ingredients/mapped/Bovine_Calf_Serum.yaml)

- Review: 20261017T083000Z-bovine-calf-serum
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Bovine_Calf_Serum (data/ingredients/mapped/Bovine_Calf_Serum.yaml, record-9f03f47106f2feee, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Bovine_Calf_Serum.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Bovine_Calf_Serum.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9f03f47106f2feee | data/ingredients/mapped/Bovine_Calf_Serum.yaml | maintained | Bovine_Calf_Serum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9f03f47106f2feee | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9f03f47106f2feee | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9f03f47106f2feee | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9f03f47106f2feee.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9f03f47106f2feee.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:10:47Z; reviewed SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857; current SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857; hash_changed=False. Reports=["reports/yaml_record_review/Bovine_Calf_Serum.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MICRO calf-serum mapping, catalog alias, occurrence count, SSSOM row, and aggregate copy pass, but top-level notes are stale.

## Findings

### rec-f-03ed42d336e5d223: Historical review coverage and residual narrative: Bovine_Calf_Serum

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9f03f47106f2feee.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:10:47Z; reviewed SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857; current SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857; hash_changed=False. Reports=["reports/yaml_record_review/Bovine_Calf_Serum.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MICRO calf-serum mapping, catalog alias, occurrence count, SSSOM row, and aggregate copy pass, but top-level notes are stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-167593d70e16cbaf | data/ingredients/mapped/Bovine_Calf_Serum.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[600],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001709","line":602,"mapping_status":"MAPPED","ontology_id":"MICRO:0001709","preferred_term":"Bovine calf serum"}],"identifier":"MICRO:0001709","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0001709","ontology_label":"calf serum","ontology_source":"MICRO"},"preferred_term":"Bovine calf serum","sssom_rows":[{"data_row":575,"object_id":"MICRO:0001709","object_label":"calf serum","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bovine_Calf_Serum","synonym_count":2} |
| ev-ae03b6a049a5a968 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [600] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1cdfef605f47154d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Bovine_Calf_Serum; data-row positions=[575] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":575,"object_id":"MICRO:0001709","object_label":"calf serum","other":"Calf serum (Gibco)","predicate_id":"skos:exactMatch","subject_id":"MIM:Bovine_Calf_Serum","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-8aa7bcceb1370d82 | docs/data/mapped_ingredients.csv; CSV lines=[602] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0001709","line":602,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"MICRO:0001709","preferred_term":"Bovine calf serum","total_occurrences":"8"}] |
| ev-c31ec5f83d5e4eae | reports/yaml_record_review/Bovine_Calf_Serum.md; &#96;data/ingredients/mapped/Bovine_Calf_Serum.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:34; Completeness:50; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-27e4ffbab1fc4344 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[329] | context_only | [{"current_record_sha256":"3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857","finding_id":"SEM:1da0fd18b3c531b690c7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-bovine-calf-serum
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Bovine_Calf_Serum (data/ingredients/mapped/Bovine_Calf_Serum.yaml)'
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
summary: Per-record structured review for Bovine_Calf_Serum (data/ingredients/mapped/Bovine_Calf_Serum.yaml,
  record-9f03f47106f2feee, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Bovine_Calf_Serum.yaml
    sha256: 3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Bovine_Calf_Serum.md
    sha256: 4e4f5bc7c5939f4851b5135461c84468de904966532a8693b07ac0a9862eeb94
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9f03f47106f2feee
  path: data/ingredients/mapped/Bovine_Calf_Serum.yaml
  label: Bovine_Calf_Serum
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bovine_Calf_Serum.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Bovine_Calf_Serum.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Bovine_Calf_Serum.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9f03f47106f2feee
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9f03f47106f2feee
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9f03f47106f2feee
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9f03f47106f2feee
evidence:
- evidence_id: ev-167593d70e16cbaf
  kind: record_content
  reference: data/ingredients/mapped/Bovine_Calf_Serum.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[600],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001709","line":602,"mapping_status":"MAPPED","ontology_id":"MICRO:0001709","preferred_term":"Bovine
    calf serum"}],"identifier":"MICRO:0001709","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"MICRO:0001709","ontology_label":"calf
    serum","ontology_source":"MICRO"},"preferred_term":"Bovine calf serum","sssom_rows":[{"data_row":575,"object_id":"MICRO:0001709","object_label":"calf
    serum","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Bovine_Calf_Serum","synonym_count":2}'
  snapshot_sha256: 3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857
- evidence_id: ev-ae03b6a049a5a968
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [600]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1cdfef605f47154d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Bovine_Calf_Serum; data-row positions=[575]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":575,"object_id":"MICRO:0001709","object_label":"calf
    serum","other":"Calf serum (Gibco)","predicate_id":"skos:exactMatch","subject_id":"MIM:Bovine_Calf_Serum","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8aa7bcceb1370d82
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[602]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0001709","line":602,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"MICRO:0001709","preferred_term":"Bovine
    calf serum","total_occurrences":"8"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c31ec5f83d5e4eae
  kind: prior_review
  reference: reports/yaml_record_review/Bovine_Calf_Serum.md
  locator: '`data/ingredients/mapped/Bovine_Calf_Serum.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:34; Completeness:50; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4e4f5bc7c5939f4851b5135461c84468de904966532a8693b07ac0a9862eeb94
  quote: "Recommended Edits:\n- Minor: replace the stale import note in\n  `data/ingredients/mapped/Bovine_Calf_Serum.yaml`\
    \ with a current note naming\n  the accepted MICRO calf-serum mapping, then run\
    \ `just sync-curated` and\n  focused strict validation."
- evidence_id: ev-27e4ffbab1fc4344
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[329]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857","finding_id":"SEM:1da0fd18b3c531b690c7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c6e42fe0fee4ba51
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9f03f47106f2feee
  evidence_ids:
  - ev-167593d70e16cbaf
  - ev-ae03b6a049a5a968
  - ev-1cdfef605f47154d
  - ev-8aa7bcceb1370d82
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e46d93be2bfe9ff2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9f03f47106f2feee
  evidence_ids:
  - ev-c31ec5f83d5e4eae
  - ev-167593d70e16cbaf
  - ev-27e4ffbab1fc4344
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:10:47Z;
    reviewed SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857;
    current SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857;
    hash_changed=False. Reports=["reports/yaml_record_review/Bovine_Calf_Serum.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The MICRO
    calf-serum mapping, catalog alias, occurrence count, SSSOM row, and aggregate
    copy pass, but top-level notes are stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c31ec5f83d5e4eae
    - ev-167593d70e16cbaf
  - name: legacy-native-ids
    value: '["SEM:1da0fd18b3c531b690c7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-167593d70e16cbaf
    - ev-c31ec5f83d5e4eae
    - ev-27e4ffbab1fc4344
findings:
- finding_id: rec-f-03ed42d336e5d223
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9f03f47106f2feee
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Bovine_Calf_Serum'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:10:47Z;
    reviewed SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857;
    current SHA-256=3303d83e01c861d0344266c6f5ecc3f34f8ab6f79c7e649c203ea01b0c651857;
    hash_changed=False. Reports=["reports/yaml_record_review/Bovine_Calf_Serum.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The MICRO
    calf-serum mapping, catalog alias, occurrence count, SSSOM row, and aggregate
    copy pass, but top-level notes are stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9f03f47106f2feee
  evidence_ids:
  - ev-c31ec5f83d5e4eae
  - ev-167593d70e16cbaf
  - ev-27e4ffbab1fc4344
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Bovine_Calf_Serum.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
