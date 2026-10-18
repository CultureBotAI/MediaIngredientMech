# Per-record structured review: Hunters_Trace_Stock_Solution (data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml)

- Review: 20261017T083000Z-hunters-trace-stock-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hunters_Trace_Stock_Solution (data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml, record-d5112125aff32fdc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d5112125aff32fdc | data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml | maintained | Hunters_Trace_Stock_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d5112125aff32fdc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d5112125aff32fdc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d5112125aff32fdc | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d5112125aff32fdc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d5112125aff32fdc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:44:09Z; reviewed SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222; current SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222; hash_changed=False. Reports=["reports/yaml_record_review/Hunters_Trace_Stock_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock-solution identity and final SSSOM row pass, but old generated unmapped-category summaries still list the pre-promotion label.

## Findings

### rec-f-b2d80cf9d8867167: Historical review coverage and residual narrative: Hunters_Trace_Stock_Solution

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d5112125aff32fdc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:44:09Z; reviewed SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222; current SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222; hash_changed=False. Reports=["reports/yaml_record_review/Hunters_Trace_Stock_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock-solution identity and final SSSOM row pass, but old generated unmapped-category summaries still list the pre-promotion label.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7d99d75082b61fde | data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[102],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:hunters_trace_stock_solution","line":104,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","preferred_term":"Hunter's Trace Stock Solution"}],"identifier":"kgmicrobe.ingredient:hunters_trace_stock_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","ontology_label":"Hunter's Trace Stock Solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Hunter's Trace Stock Solution","sssom_rows":[{"data_row":1440,"object_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","object_label":"Hunter's Trace Stock Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hunters_Trace_Stock_Solution","synonym_count":1} |
| ev-f95a98751cf8f424 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [102] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c1b2224916604440 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hunters_Trace_Stock_Solution; data-row positions=[1440] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1440,"object_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","object_label":"Hunter's Trace Stock Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Hunters_Trace_Stock_Solution","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-da5bc4ee40e77bcd | docs/data/mapped_ingredients.csv; CSV lines=[104] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:hunters_trace_stock_solution","line":104,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","preferred_term":"Hunter's Trace Stock Solution","total_occurrences":"1"}] |
| ev-8be681c6e7934fe4 | reports/yaml_record_review/Hunters_Trace_Stock_Solution.md; &#96;data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:36; Completeness:55; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4596bccc91c7828a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[734] | context_only | [{"current_record_sha256":"78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222","finding_id":"SEM:9549335db0b6b7e50990","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hunters-trace-stock-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hunters_Trace_Stock_Solution (data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml)'
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
summary: Per-record structured review for Hunters_Trace_Stock_Solution (data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml,
  record-d5112125aff32fdc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
    sha256: 78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222
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
  - path: reports/yaml_record_review/Hunters_Trace_Stock_Solution.md
    sha256: 13e0e493b58b55b8a18769f2932d706063e8f0b4113b8412120ddee00d9b9db0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d5112125aff32fdc
  path: data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
  label: Hunters_Trace_Stock_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d5112125aff32fdc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d5112125aff32fdc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d5112125aff32fdc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d5112125aff32fdc
evidence:
- evidence_id: ev-7d99d75082b61fde
  kind: record_content
  reference: data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[102],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:hunters_trace_stock_solution","line":104,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","preferred_term":"Hunter''s
    Trace Stock Solution"}],"identifier":"kgmicrobe.ingredient:hunters_trace_stock_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","ontology_label":"Hunter''s
    Trace Stock Solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Hunter''s
    Trace Stock Solution","sssom_rows":[{"data_row":1440,"object_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","object_label":"Hunter''s
    Trace Stock Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hunters_Trace_Stock_Solution","synonym_count":1}'
  snapshot_sha256: 78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222
- evidence_id: ev-f95a98751cf8f424
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [102]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c1b2224916604440
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hunters_Trace_Stock_Solution; data-row positions=[1440]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1440,"object_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","object_label":"Hunter''s
    Trace Stock Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Hunters_Trace_Stock_Solution","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-da5bc4ee40e77bcd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[104]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:hunters_trace_stock_solution","line":104,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:hunters_trace_stock_solution","preferred_term":"Hunter''s
    Trace Stock Solution","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8be681c6e7934fe4
  kind: prior_review
  reference: reports/yaml_record_review/Hunters_Trace_Stock_Solution.md
  locator: '`data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml`:2; Verdict:4;
    Identity:10; Validation:23; Evidence:36; Completeness:55; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 13e0e493b58b55b8a18769f2932d706063e8f0b4113b8412120ddee00d9b9db0
  quote: "Recommended Edits:\n- Minor: if the old unmapped category summaries are\
    \ still maintained products,\n  regenerate them from the current curated collections\
    \ so\n  `Hunter's Trace Stock Solution` no longer appears as an unmapped entry."
- evidence_id: ev-4596bccc91c7828a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[734]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222","finding_id":"SEM:9549335db0b6b7e50990","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-23409c069f93abc1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d5112125aff32fdc
  evidence_ids:
  - ev-7d99d75082b61fde
  - ev-f95a98751cf8f424
  - ev-c1b2224916604440
  - ev-da5bc4ee40e77bcd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-69ff8fdaa5e5b368
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d5112125aff32fdc
  evidence_ids:
  - ev-8be681c6e7934fe4
  - ev-7d99d75082b61fde
  - ev-4596bccc91c7828a
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:44:09Z;
    reviewed SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222;
    current SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222;
    hash_changed=False. Reports=["reports/yaml_record_review/Hunters_Trace_Stock_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock-solution identity and final SSSOM row pass, but old generated unmapped-category
    summaries still list the pre-promotion label.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8be681c6e7934fe4
    - ev-7d99d75082b61fde
  - name: legacy-native-ids
    value: '["SEM:9549335db0b6b7e50990"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7d99d75082b61fde
    - ev-8be681c6e7934fe4
    - ev-4596bccc91c7828a
findings:
- finding_id: rec-f-b2d80cf9d8867167
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d5112125aff32fdc
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Hunters_Trace_Stock_Solution'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:44:09Z;
    reviewed SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222;
    current SHA-256=78ffea5700354371cb549de4584b990820b493bceb0c75b3964c9c799357c222;
    hash_changed=False. Reports=["reports/yaml_record_review/Hunters_Trace_Stock_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock-solution identity and final SSSOM row pass, but old generated unmapped-category
    summaries still list the pre-promotion label.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d5112125aff32fdc
  evidence_ids:
  - ev-8be681c6e7934fe4
  - ev-7d99d75082b61fde
  - ev-4596bccc91c7828a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hunters_Trace_Stock_Solution.yaml
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
