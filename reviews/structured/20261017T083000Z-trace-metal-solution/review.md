# Per-record structured review: Trace_Metal_Solution (data/ingredients/mapped/Trace_Metal_Solution.yaml)

- Review: 20261017T083000Z-trace-metal-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trace_Metal_Solution (data/ingredients/mapped/Trace_Metal_Solution.yaml, record-89541aac4daefe1b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trace_Metal_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trace_Metal_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-89541aac4daefe1b | data/ingredients/mapped/Trace_Metal_Solution.yaml | maintained | Trace_Metal_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-89541aac4daefe1b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-89541aac4daefe1b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-89541aac4daefe1b | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-89541aac4daefe1b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-89541aac4daefe1b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:13:37Z; reviewed SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f; current SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f; hash_changed=False. Reports=["reports/yaml_record_review/Trace_Metal_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity passes, but a starred CultureMech alias leaks into final SSSOM other.

## Findings

### rec-f-0819b3fc81e07f15: Historical review coverage and residual narrative: Trace_Metal_Solution

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-89541aac4daefe1b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:13:37Z; reviewed SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f; current SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f; hash_changed=False. Reports=["reports/yaml_record_review/Trace_Metal_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity passes, but a starred CultureMech alias leaks into final SSSOM other.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0d7b307f7a91c729 | data/ingredients/mapped/Trace_Metal_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2510],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_metal_solution","line":2512,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_metal_solution","preferred_term":"Trace metal solution"}],"identifier":"kgmicrobe.ingredient:trace_metal_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_metal_solution","ontology_label":"Trace metal solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace metal solution","sssom_rows":[{"data_row":2805,"object_id":"kgmicrobe.ingredient:trace_metal_solution","object_label":"Trace metal solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Metal_Solution","synonym_count":2} |
| ev-70de50dfb62648c5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2510] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a8165a4594592227 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trace_Metal_Solution; data-row positions=[2805] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2805,"object_id":"kgmicrobe.ingredient:trace_metal_solution","object_label":"Trace metal solution","other":"Trace metal solution*","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Metal_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-c04eea78eb57c6b3 | docs/data/mapped_ingredients.csv; CSV lines=[2512] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:trace_metal_solution","line":2512,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:trace_metal_solution","preferred_term":"Trace metal solution","total_occurrences":"2"}] |
| ev-2eeca26642943ff3 | reports/yaml_record_review/Trace_Metal_Solution.md; &#96;data/ingredients/mapped/Trace_Metal_Solution.yaml&#96;:2; Verdict:4; Identity:9; Validation:21; Evidence:31; Issues:42; Major: the starred source form reaches final SSSOM:44; Completeness:50; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4c918509009d08ed | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1299] | context_only | [{"current_record_sha256":"b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f","finding_id":"SEM:2d655daa757da0d4880d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trace-metal-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trace_Metal_Solution (data/ingredients/mapped/Trace_Metal_Solution.yaml)'
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
summary: Per-record structured review for Trace_Metal_Solution (data/ingredients/mapped/Trace_Metal_Solution.yaml,
  record-89541aac4daefe1b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trace_Metal_Solution.yaml
    sha256: b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Trace_Metal_Solution.md
    sha256: dde61ea6f77a0f1bf46e2efbe5e00aca7180e43e502254590b1e436c0660e821
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-89541aac4daefe1b
  path: data/ingredients/mapped/Trace_Metal_Solution.yaml
  label: Trace_Metal_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trace_Metal_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trace_Metal_Solution.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-89541aac4daefe1b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-89541aac4daefe1b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-89541aac4daefe1b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-89541aac4daefe1b
evidence:
- evidence_id: ev-0d7b307f7a91c729
  kind: record_content
  reference: data/ingredients/mapped/Trace_Metal_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2510],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:trace_metal_solution","line":2512,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:trace_metal_solution","preferred_term":"Trace
    metal solution"}],"identifier":"kgmicrobe.ingredient:trace_metal_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:trace_metal_solution","ontology_label":"Trace
    metal solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Trace
    metal solution","sssom_rows":[{"data_row":2805,"object_id":"kgmicrobe.ingredient:trace_metal_solution","object_label":"Trace
    metal solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trace_Metal_Solution","synonym_count":2}'
  snapshot_sha256: b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f
- evidence_id: ev-70de50dfb62648c5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2510]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a8165a4594592227
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trace_Metal_Solution; data-row positions=[2805]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2805,"object_id":"kgmicrobe.ingredient:trace_metal_solution","object_label":"Trace
    metal solution","other":"Trace metal solution*","predicate_id":"skos:exactMatch","subject_id":"MIM:Trace_Metal_Solution","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c04eea78eb57c6b3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2512]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:trace_metal_solution","line":2512,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:trace_metal_solution","preferred_term":"Trace
    metal solution","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2eeca26642943ff3
  kind: prior_review
  reference: reports/yaml_record_review/Trace_Metal_Solution.md
  locator: '`data/ingredients/mapped/Trace_Metal_Solution.yaml`:2; Verdict:4; Identity:9;
    Validation:21; Evidence:31; Issues:42; Major: the starred source form reaches
    final SSSOM:44; Completeness:50; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dde61ea6f77a0f1bf46e2efbe5e00aca7180e43e502254590b1e436c0660e821
  quote: "Issues:\n\n\nMajor: the starred source form reaches final SSSOM:\n`Trace\
    \ metal solution*` is a CultureMech occurrence label with a footnote\nmarker,\
    \ not a true synonym of the local stock identity. The marker should be\nretained\
    \ only as source provenance and filtered from final `other`.\n\nRecommended Edits:\n\
    - Mark `Trace metal solution*` as non-exportable raw source text so the final\n\
    \  SSSOM `other` column is empty for this row."
- evidence_id: ev-4c918509009d08ed
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1299]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f","finding_id":"SEM:2d655daa757da0d4880d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e9abcb7bf3a85b1f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-89541aac4daefe1b
  evidence_ids:
  - ev-0d7b307f7a91c729
  - ev-70de50dfb62648c5
  - ev-a8165a4594592227
  - ev-c04eea78eb57c6b3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cc13fd2be463ef5b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-89541aac4daefe1b
  evidence_ids:
  - ev-2eeca26642943ff3
  - ev-0d7b307f7a91c729
  - ev-4c918509009d08ed
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:13:37Z;
    reviewed SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f;
    current SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f;
    hash_changed=False. Reports=["reports/yaml_record_review/Trace_Metal_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity passes, but a starred CultureMech alias leaks into final SSSOM
    other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2eeca26642943ff3
    - ev-0d7b307f7a91c729
  - name: legacy-native-ids
    value: '["SEM:2d655daa757da0d4880d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0d7b307f7a91c729
    - ev-2eeca26642943ff3
    - ev-4c918509009d08ed
findings:
- finding_id: rec-f-0819b3fc81e07f15
  issue_key: mim-reconciliation-historical-review-coverage-and-r-89541aac4daefe1b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Trace_Metal_Solution'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:13:37Z;
    reviewed SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f;
    current SHA-256=b7ab5c76c74a3803abae8e6f13cd04596c382ac4e360ef9b9935932691649d6f;
    hash_changed=False. Reports=["reports/yaml_record_review/Trace_Metal_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity passes, but a starred CultureMech alias leaks into final SSSOM
    other.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-89541aac4daefe1b
  evidence_ids:
  - ev-2eeca26642943ff3
  - ev-0d7b307f7a91c729
  - ev-4c918509009d08ed
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trace_Metal_Solution.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
