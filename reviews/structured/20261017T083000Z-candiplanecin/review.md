# Per-record structured review: Candiplanecin (data/ingredients/mapped/Candiplanecin.yaml)

- Review: 20261017T083000Z-candiplanecin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Candiplanecin (data/ingredients/mapped/Candiplanecin.yaml, record-2e5e6858e9fa82d6, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Candiplanecin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Candiplanecin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2e5e6858e9fa82d6 | data/ingredients/mapped/Candiplanecin.yaml | maintained | Candiplanecin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2e5e6858e9fa82d6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2e5e6858e9fa82d6 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2e5e6858e9fa82d6 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2e5e6858e9fa82d6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2e5e6858e9fa82d6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:49:52Z; reviewed SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159; current SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159; hash_changed=False. Reports=["reports/yaml_record_review/Candiplanecin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH candiplanecin identity and SSSOM row pass, but one ontology evidence note still describes a pending placeholder.

## Findings

### rec-f-22890fbc5225fc6b: Historical review coverage and residual narrative: Candiplanecin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2e5e6858e9fa82d6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:49:52Z; reviewed SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159; current SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159; hash_changed=False. Reports=["reports/yaml_record_review/Candiplanecin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH candiplanecin identity and SSSOM row pass, but one ontology evidence note still describes a pending placeholder.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-fb033ed24c7baf87 | data/ingredients/mapped/Candiplanecin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[643],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C033379","line":645,"mapping_status":"MAPPED","ontology_id":"mesh:C033379","preferred_term":"Candiplanecin"}],"identifier":"mesh:C033379","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C033379","ontology_label":"candiplanecin","ontology_source":"MESH"},"preferred_term":"Candiplanecin","sssom_rows":[{"data_row":626,"object_id":"mesh:C033379","object_label":"candiplanecin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Candiplanecin","synonym_count":0} |
| ev-1a2aa7b5c9245a97 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [643] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-850b7c1390e5e025 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Candiplanecin; data-row positions=[626] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":626,"object_id":"mesh:C033379","object_label":"candiplanecin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Candiplanecin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-20f00af52ed76705 | docs/data/mapped_ingredients.csv; CSV lines=[645] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C033379","line":645,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C033379","preferred_term":"Candiplanecin","total_occurrences":"0"}] |
| ev-ccbe2777c4e2d3cf | reports/yaml_record_review/Candiplanecin.md; &#96;data/ingredients/mapped/Candiplanecin.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:37; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dfa3b998c1d08073 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[354] | context_only | [{"current_record_sha256":"1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159","finding_id":"SEM:8fc222acc8fd6587cdf4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-candiplanecin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Candiplanecin (data/ingredients/mapped/Candiplanecin.yaml)'
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
summary: Per-record structured review for Candiplanecin (data/ingredients/mapped/Candiplanecin.yaml,
  record-2e5e6858e9fa82d6, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Candiplanecin.yaml
    sha256: 1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159
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
  - path: reports/yaml_record_review/Candiplanecin.md
    sha256: c9e1b251e6b9b07f73807c5ba3792d331f1600fabc4e0c701bd9c3e0fef08113
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2e5e6858e9fa82d6
  path: data/ingredients/mapped/Candiplanecin.yaml
  label: Candiplanecin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Candiplanecin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Candiplanecin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Candiplanecin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2e5e6858e9fa82d6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2e5e6858e9fa82d6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2e5e6858e9fa82d6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2e5e6858e9fa82d6
evidence:
- evidence_id: ev-fb033ed24c7baf87
  kind: record_content
  reference: data/ingredients/mapped/Candiplanecin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[643],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C033379","line":645,"mapping_status":"MAPPED","ontology_id":"mesh:C033379","preferred_term":"Candiplanecin"}],"identifier":"mesh:C033379","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C033379","ontology_label":"candiplanecin","ontology_source":"MESH"},"preferred_term":"Candiplanecin","sssom_rows":[{"data_row":626,"object_id":"mesh:C033379","object_label":"candiplanecin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Candiplanecin","synonym_count":0}'
  snapshot_sha256: 1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159
- evidence_id: ev-1a2aa7b5c9245a97
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [643]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-850b7c1390e5e025
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Candiplanecin; data-row positions=[626]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":626,"object_id":"mesh:C033379","object_label":"candiplanecin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Candiplanecin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-20f00af52ed76705
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[645]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C033379","line":645,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C033379","preferred_term":"Candiplanecin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ccbe2777c4e2d3cf
  kind: prior_review
  reference: reports/yaml_record_review/Candiplanecin.md
  locator: '`data/ingredients/mapped/Candiplanecin.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:37; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c9e1b251e6b9b07f73807c5ba3792d331f1600fabc4e0c701bd9c3e0fef08113
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Candiplanecin.yaml`, remove\
    \ the stale\n  `kgmicrobe.compound` placeholder evidence note or rewrite it as\
    \ historical\n  source-label provenance that no longer claims promotion is pending.\n\
    - Regenerate aggregate/docs outputs and prove the cleanup with strict\n  validation\
    \ and round-trip verification."
- evidence_id: ev-dfa3b998c1d08073
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[354]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159","finding_id":"SEM:8fc222acc8fd6587cdf4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-11720b3863b24dc0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2e5e6858e9fa82d6
  evidence_ids:
  - ev-fb033ed24c7baf87
  - ev-1a2aa7b5c9245a97
  - ev-850b7c1390e5e025
  - ev-20f00af52ed76705
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2dbe78d432ec8718
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2e5e6858e9fa82d6
  evidence_ids:
  - ev-ccbe2777c4e2d3cf
  - ev-fb033ed24c7baf87
  - ev-dfa3b998c1d08073
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:49:52Z;
    reviewed SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159;
    current SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159;
    hash_changed=False. Reports=["reports/yaml_record_review/Candiplanecin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    candiplanecin identity and SSSOM row pass, but one ontology evidence note still
    describes a pending placeholder.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ccbe2777c4e2d3cf
    - ev-fb033ed24c7baf87
  - name: legacy-native-ids
    value: '["SEM:8fc222acc8fd6587cdf4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-fb033ed24c7baf87
    - ev-ccbe2777c4e2d3cf
    - ev-dfa3b998c1d08073
findings:
- finding_id: rec-f-22890fbc5225fc6b
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2e5e6858e9fa82d6
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Candiplanecin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T10:49:52Z;
    reviewed SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159;
    current SHA-256=1fe3f0e6adceb0602563f44bbbff8dfbf3f099acdfbd1a472ca33f64c271e159;
    hash_changed=False. Reports=["reports/yaml_record_review/Candiplanecin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    candiplanecin identity and SSSOM row pass, but one ontology evidence note still
    describes a pending placeholder.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2e5e6858e9fa82d6
  evidence_ids:
  - ev-ccbe2777c4e2d3cf
  - ev-fb033ed24c7baf87
  - ev-dfa3b998c1d08073
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Candiplanecin.yaml
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
