# Per-record structured review: D (data/ingredients/mapped/D.yaml)

- Review: 20261017T083000Z-d
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D (data/ingredients/mapped/D.yaml, record-68daef1f118ee60f, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-68daef1f118ee60f | data/ingredients/mapped/D.yaml | maintained | D |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-68daef1f118ee60f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-68daef1f118ee60f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-68daef1f118ee60f | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-68daef1f118ee60f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-68daef1f118ee60f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:56:15Z; reviewed SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4; current SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4; hash_changed=False. Reports=["reports/yaml_record_review/D.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected comma-split tombstone has no final SSSOM row, but stale aspartate synonyms and ingredient_type remain as minor cleanup.

## Findings

### rec-f-67050a3559408451: Historical review coverage and residual narrative: D

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-68daef1f118ee60f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:56:15Z; reviewed SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4; current SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4; hash_changed=False. Reports=["reports/yaml_record_review/D.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected comma-split tombstone has no final SSSOM row, but stale aspartate synonyms and ingredient_type remain as minor cleanup.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-04599c044fbc3039 | data/ingredients/mapped/D.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[845],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75228","line":847,"mapping_status":"REJECTED","ontology_id":"CHEBI:75228","preferred_term":"D"}],"identifier":"CHEBI:75228","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":283,"edge_count":283,"occurrences":283},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75228","ontology_label":"sodium lactate","ontology_source":"CHEBI"},"preferred_term":"D","sssom_rows":[],"sssom_subject":"MIM:D","synonym_count":5} |
| ev-4136ef9e1eb4981d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [845] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f3bf0dbf461207b7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-16004951d3bbd7b0 | docs/data/mapped_ingredients.csv; CSV lines=[847] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75228","line":847,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:75228","preferred_term":"D","total_occurrences":"0"}] |
| ev-2c49c94074d95d74 | reports/yaml_record_review/D.md; &#96;data/ingredients/mapped/D.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:43; Completeness:57; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-74fc0182ddda454b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[511] | context_only | [{"current_record_sha256":"3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4","finding_id":"SEM:3e584f639f76aaf3718d","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D (data/ingredients/mapped/D.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for D (data/ingredients/mapped/D.yaml, record-68daef1f118ee60f,
  mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D.yaml
    sha256: 3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D.md
    sha256: 1e4715221fc5f4bee224912789990399a24578dea4e8657098127605c881d7d9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-68daef1f118ee60f
  path: data/ingredients/mapped/D.yaml
  label: D
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/D.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-68daef1f118ee60f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-68daef1f118ee60f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-68daef1f118ee60f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-68daef1f118ee60f
evidence:
- evidence_id: ev-04599c044fbc3039
  kind: record_content
  reference: data/ingredients/mapped/D.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[845],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75228","line":847,"mapping_status":"REJECTED","ontology_id":"CHEBI:75228","preferred_term":"D"}],"identifier":"CHEBI:75228","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":283,"edge_count":283,"occurrences":283},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75228","ontology_label":"sodium
    lactate","ontology_source":"CHEBI"},"preferred_term":"D","sssom_rows":[],"sssom_subject":"MIM:D","synonym_count":5}'
  snapshot_sha256: 3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4
- evidence_id: ev-4136ef9e1eb4981d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [845]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f3bf0dbf461207b7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-16004951d3bbd7b0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[847]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75228","line":847,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:75228","preferred_term":"D","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2c49c94074d95d74
  kind: prior_review
  reference: reports/yaml_record_review/D.md
  locator: '`data/ingredients/mapped/D.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:43; Completeness:57; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1e4715221fc5f4bee224912789990399a24578dea4e8657098127605c881d7d9
  quote: "Recommended Edits:\n- Optionally remove the stale aspartate synonyms and\n\
    \  `ingredient_type: SINGLE_INGREDIENT` from\n  `data/ingredients/mapped/D.yaml`\
    \ so the tombstone contains only merge\n  provenance for the comma-split artifact.\n\
    - Rerun `uv run --frozen python scripts/validate_strict.py` and\n  `uv run --frozen\
    \ linkml-term-validator validate-data data/ingredients/mapped/D.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`\n  after that cleanup."
- evidence_id: ev-74fc0182ddda454b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[511]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4","finding_id":"SEM:3e584f639f76aaf3718d","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-4a4c7a334a72109b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-68daef1f118ee60f
  evidence_ids:
  - ev-04599c044fbc3039
  - ev-4136ef9e1eb4981d
  - ev-f3bf0dbf461207b7
  - ev-16004951d3bbd7b0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-efc650b8e72ecf97
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-68daef1f118ee60f
  evidence_ids:
  - ev-2c49c94074d95d74
  - ev-04599c044fbc3039
  - ev-74fc0182ddda454b
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:56:15Z;
    reviewed SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4;
    current SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4;
    hash_changed=False. Reports=["reports/yaml_record_review/D.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The rejected comma-split
    tombstone has no final SSSOM row, but stale aspartate synonyms and ingredient_type
    remain as minor cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2c49c94074d95d74
    - ev-04599c044fbc3039
  - name: legacy-native-ids
    value: '["SEM:3e584f639f76aaf3718d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-04599c044fbc3039
    - ev-2c49c94074d95d74
    - ev-74fc0182ddda454b
findings:
- finding_id: rec-f-67050a3559408451
  issue_key: mim-reconciliation-historical-review-coverage-and-r-68daef1f118ee60f
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: D'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:56:15Z;
    reviewed SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4;
    current SHA-256=3dd35a9da755f08b8a20e5e8ffe9a1b1aae5050aff54cc8b2d1034abcd8a39e4;
    hash_changed=False. Reports=["reports/yaml_record_review/D.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The rejected comma-split
    tombstone has no final SSSOM row, but stale aspartate synonyms and ingredient_type
    remain as minor cleanup.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-68daef1f118ee60f
  evidence_ids:
  - ev-2c49c94074d95d74
  - ev-04599c044fbc3039
  - ev-74fc0182ddda454b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
