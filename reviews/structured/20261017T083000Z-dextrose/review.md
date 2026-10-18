# Per-record structured review: Dextrose (data/ingredients/mapped/Dextrose.yaml)

- Review: 20261017T083000Z-dextrose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Dextrose (data/ingredients/mapped/Dextrose.yaml, record-a8be959897f2c1df, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Dextrose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Dextrose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a8be959897f2c1df | data/ingredients/mapped/Dextrose.yaml | maintained | Dextrose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a8be959897f2c1df | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a8be959897f2c1df | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a8be959897f2c1df | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a8be959897f2c1df.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a8be959897f2c1df.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T14:35:13Z; reviewed SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6; current SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6; hash_changed=False. Reports=["reports/yaml_record_review/Dextrose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The duplicate tombstone no longer exports SSSOM, but stale pre-merge fields remain.

## Findings

### rec-f-866f7b39e11da0a4: Historical review coverage and residual narrative: Dextrose

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a8be959897f2c1df.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T14:35:13Z; reviewed SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6; current SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6; hash_changed=False. Reports=["reports/yaml_record_review/Dextrose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The duplicate tombstone no longer exports SSSOM, but stale pre-merge fields remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-80c790f8f0b80d8d | data/ingredients/mapped/Dextrose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[880],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17634","line":882,"mapping_status":"REJECTED","ontology_id":"CHEBI:17634","preferred_term":"Dextrose"}],"identifier":"CHEBI:17634","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1211,"edge_count":1211,"occurrences":1250},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17634","ontology_label":"D-glucose","ontology_source":"CHEBI"},"preferred_term":"Dextrose","sssom_rows":[],"sssom_subject":"MIM:Dextrose","synonym_count":10} |
| ev-cd263aa8797b7ee1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [880] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d085c54d99b5237b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Dextrose; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-cfacaed19221dd02 | docs/data/mapped_ingredients.csv; CSV lines=[882] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17634","line":882,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17634","preferred_term":"Dextrose","total_occurrences":"0"}] |
| ev-31f447ccd5934bf8 | reports/yaml_record_review/Dextrose.md; &#96;data/ingredients/mapped/Dextrose.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:38; Completeness:54; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1f8183874fbe6ad3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[531] | context_only | [{"current_record_sha256":"528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6","finding_id":"SEM:2d8ee28781123379952f","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dextrose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Dextrose (data/ingredients/mapped/Dextrose.yaml)'
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
summary: Per-record structured review for Dextrose (data/ingredients/mapped/Dextrose.yaml,
  record-a8be959897f2c1df, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Dextrose.yaml
    sha256: 528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6
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
  - path: reports/yaml_record_review/Dextrose.md
    sha256: 5a70264915e4f9f7d15cf74751de0e55605cbc16563e7bd9be623855cca817c5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a8be959897f2c1df
  path: data/ingredients/mapped/Dextrose.yaml
  label: Dextrose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dextrose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Dextrose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Dextrose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a8be959897f2c1df
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a8be959897f2c1df
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a8be959897f2c1df
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a8be959897f2c1df
evidence:
- evidence_id: ev-80c790f8f0b80d8d
  kind: record_content
  reference: data/ingredients/mapped/Dextrose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[880],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17634","line":882,"mapping_status":"REJECTED","ontology_id":"CHEBI:17634","preferred_term":"Dextrose"}],"identifier":"CHEBI:17634","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1211,"edge_count":1211,"occurrences":1250},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17634","ontology_label":"D-glucose","ontology_source":"CHEBI"},"preferred_term":"Dextrose","sssom_rows":[],"sssom_subject":"MIM:Dextrose","synonym_count":10}'
  snapshot_sha256: 528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6
- evidence_id: ev-cd263aa8797b7ee1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [880]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d085c54d99b5237b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Dextrose; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cfacaed19221dd02
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[882]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17634","line":882,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:17634","preferred_term":"Dextrose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-31f447ccd5934bf8
  kind: prior_review
  reference: reports/yaml_record_review/Dextrose.md
  locator: '`data/ingredients/mapped/Dextrose.yaml`:2; Verdict:4; Identity:12; Validation:25;
    Evidence:38; Completeness:54; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5a70264915e4f9f7d15cf74751de0e55605cbc16563e7bd9be623855cca817c5
  quote: "Recommended Edits:\n- Minor: retire or mark reviewed the\n  `mappings/other_cross_record_baseline.tsv`\
    \ `UNREVIEWED` row for\n  `MIM:D-glucose`/`MIM:Dextrose`.\n- Minor: if rejected\
    \ tombstones are meant to retain only merge pointers and\n  raw labels, prune\
    \ stale role and structure fields from\n  `data/ingredients/mapped/Dextrose.yaml`\
    \ and synchronize\n  `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-1f8183874fbe6ad3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[531]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6","finding_id":"SEM:2d8ee28781123379952f","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-7576005931d7ae75
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a8be959897f2c1df
  evidence_ids:
  - ev-80c790f8f0b80d8d
  - ev-cd263aa8797b7ee1
  - ev-d085c54d99b5237b
  - ev-cfacaed19221dd02
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-678f49a210fff699
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a8be959897f2c1df
  evidence_ids:
  - ev-31f447ccd5934bf8
  - ev-80c790f8f0b80d8d
  - ev-1f8183874fbe6ad3
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T14:35:13Z;
    reviewed SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6;
    current SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6;
    hash_changed=False. Reports=["reports/yaml_record_review/Dextrose.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The duplicate tombstone
    no longer exports SSSOM, but stale pre-merge fields remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-31f447ccd5934bf8
    - ev-80c790f8f0b80d8d
  - name: legacy-native-ids
    value: '["SEM:2d8ee28781123379952f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-80c790f8f0b80d8d
    - ev-31f447ccd5934bf8
    - ev-1f8183874fbe6ad3
findings:
- finding_id: rec-f-866f7b39e11da0a4
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a8be959897f2c1df
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Dextrose'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T14:35:13Z;
    reviewed SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6;
    current SHA-256=528f7d44e2287090fc459ee1f96ab9ae8cdd7d73561686d1a1abbc369cb364c6;
    hash_changed=False. Reports=["reports/yaml_record_review/Dextrose.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The duplicate tombstone
    no longer exports SSSOM, but stale pre-merge fields remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a8be959897f2c1df
  evidence_ids:
  - ev-31f447ccd5934bf8
  - ev-80c790f8f0b80d8d
  - ev-1f8183874fbe6ad3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Dextrose.yaml
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
