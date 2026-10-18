# Per-record structured review: Actinotiocin (data/ingredients/mapped/Actinotiocin.yaml)

- Review: 20261017T083000Z-actinotiocin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Actinotiocin (data/ingredients/mapped/Actinotiocin.yaml, record-43b044d68f53b3d8, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Actinotiocin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Actinotiocin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-43b044d68f53b3d8 | data/ingredients/mapped/Actinotiocin.yaml | maintained | Actinotiocin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-43b044d68f53b3d8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-43b044d68f53b3d8 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-43b044d68f53b3d8 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-43b044d68f53b3d8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-43b044d68f53b3d8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:17:53Z; reviewed SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e; current SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e; hash_changed=False. Reports=["reports/yaml_record_review/Actinotiocin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH grounding, external-prefix OLS validation, SSSOM row, and aggregate pass; only stale placeholder evidence and old UNKNOWN_TERM review output predate the MeSH upgrade.

## Findings

### rec-f-a35745e292f8cf11: Historical review coverage and residual narrative: Actinotiocin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-43b044d68f53b3d8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:17:53Z; reviewed SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e; current SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e; hash_changed=False. Reports=["reports/yaml_record_review/Actinotiocin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH grounding, external-prefix OLS validation, SSSOM row, and aggregate pass; only stale placeholder evidence and old UNKNOWN_TERM review output predate the MeSH upgrade.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d8174525dd08443e | data/ingredients/mapped/Actinotiocin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[451],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C006403","line":453,"mapping_status":"MAPPED","ontology_id":"mesh:C006403","preferred_term":"Actinotiocin"}],"identifier":"mesh:C006403","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C006403","ontology_label":"actinotiocin","ontology_source":"MESH"},"preferred_term":"Actinotiocin","sssom_rows":[{"data_row":300,"object_id":"mesh:C006403","object_label":"actinotiocin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Actinotiocin","synonym_count":0} |
| ev-4affa6d7e6586264 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [451] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3f3c10c6c9166587 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Actinotiocin; data-row positions=[300] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":300,"object_id":"mesh:C006403","object_label":"actinotiocin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Actinotiocin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-1d4ae7d990d36fc8 | docs/data/mapped_ingredients.csv; CSV lines=[453] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C006403","line":453,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C006403","preferred_term":"Actinotiocin","total_occurrences":"0"}] |
| ev-aaff44f4b1b62209 | reports/yaml_record_review/Actinotiocin.md; &#96;data/ingredients/mapped/Actinotiocin.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:38; Completeness:55; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0c04af18e35c2062 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[209] | context_only | [{"current_record_sha256":"71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e","finding_id":"SEM:4ccb446fc577d576411b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-actinotiocin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Actinotiocin (data/ingredients/mapped/Actinotiocin.yaml)'
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
summary: Per-record structured review for Actinotiocin (data/ingredients/mapped/Actinotiocin.yaml,
  record-43b044d68f53b3d8, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Actinotiocin.yaml
    sha256: 71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Actinotiocin.md
    sha256: 2ab4f1932e71f6d81e99072d9c7dfeb3337d023bb01b98bbe1eb4a85540148b3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-43b044d68f53b3d8
  path: data/ingredients/mapped/Actinotiocin.yaml
  label: Actinotiocin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinotiocin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Actinotiocin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Actinotiocin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-43b044d68f53b3d8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-43b044d68f53b3d8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-43b044d68f53b3d8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-43b044d68f53b3d8
evidence:
- evidence_id: ev-d8174525dd08443e
  kind: record_content
  reference: data/ingredients/mapped/Actinotiocin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[451],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C006403","line":453,"mapping_status":"MAPPED","ontology_id":"mesh:C006403","preferred_term":"Actinotiocin"}],"identifier":"mesh:C006403","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C006403","ontology_label":"actinotiocin","ontology_source":"MESH"},"preferred_term":"Actinotiocin","sssom_rows":[{"data_row":300,"object_id":"mesh:C006403","object_label":"actinotiocin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Actinotiocin","synonym_count":0}'
  snapshot_sha256: 71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e
- evidence_id: ev-4affa6d7e6586264
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [451]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3f3c10c6c9166587
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Actinotiocin; data-row positions=[300]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":300,"object_id":"mesh:C006403","object_label":"actinotiocin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Actinotiocin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1d4ae7d990d36fc8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[453]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C006403","line":453,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C006403","preferred_term":"Actinotiocin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-aaff44f4b1b62209
  kind: prior_review
  reference: reports/yaml_record_review/Actinotiocin.md
  locator: '`data/ingredients/mapped/Actinotiocin.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:38; Completeness:55; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2ab4f1932e71f6d81e99072d9c7dfeb3337d023bb01b98bbe1eb4a85540148b3
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Actinotiocin.yaml`, either\
    \ move the stale\n  kg-microbe placeholder text out of `ontology_mapping.evidence`\
    \ or rewrite it\n  so the mapping evidence only describes the exact MeSH upgrade."
- evidence_id: ev-0c04af18e35c2062
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[209]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e","finding_id":"SEM:4ccb446fc577d576411b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8d1c6a4c34e808be
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-43b044d68f53b3d8
  evidence_ids:
  - ev-d8174525dd08443e
  - ev-4affa6d7e6586264
  - ev-3f3c10c6c9166587
  - ev-1d4ae7d990d36fc8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-131b832be656b166
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43b044d68f53b3d8
  evidence_ids:
  - ev-aaff44f4b1b62209
  - ev-d8174525dd08443e
  - ev-0c04af18e35c2062
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:17:53Z;
    reviewed SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e;
    current SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e;
    hash_changed=False. Reports=["reports/yaml_record_review/Actinotiocin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    grounding, external-prefix OLS validation, SSSOM row, and aggregate pass; only
    stale placeholder evidence and old UNKNOWN_TERM review output predate the MeSH
    upgrade.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-aaff44f4b1b62209
    - ev-d8174525dd08443e
  - name: legacy-native-ids
    value: '["SEM:4ccb446fc577d576411b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d8174525dd08443e
    - ev-aaff44f4b1b62209
    - ev-0c04af18e35c2062
findings:
- finding_id: rec-f-a35745e292f8cf11
  issue_key: mim-reconciliation-historical-review-coverage-and-r-43b044d68f53b3d8
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Actinotiocin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:17:53Z;
    reviewed SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e;
    current SHA-256=71c2d26e190386d2aff12045638357b3776e1323144da5370bbb0605f3f4257e;
    hash_changed=False. Reports=["reports/yaml_record_review/Actinotiocin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    grounding, external-prefix OLS validation, SSSOM row, and aggregate pass; only
    stale placeholder evidence and old UNKNOWN_TERM review output predate the MeSH
    upgrade.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43b044d68f53b3d8
  evidence_ids:
  - ev-aaff44f4b1b62209
  - ev-d8174525dd08443e
  - ev-0c04af18e35c2062
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinotiocin.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
