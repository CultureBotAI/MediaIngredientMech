# Per-record structured review: TYG_Salts_Solution (data/ingredients/mapped/TYG_Salts_Solution.yaml)

- Review: 20261017T083000Z-tyg-salts-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for TYG_Salts_Solution (data/ingredients/mapped/TYG_Salts_Solution.yaml, record-6ce64dd67481fcf9, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/TYG_Salts_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/TYG_Salts_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6ce64dd67481fcf9 | data/ingredients/mapped/TYG_Salts_Solution.yaml | maintained | TYG_Salts_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6ce64dd67481fcf9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-6ce64dd67481fcf9 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6ce64dd67481fcf9 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6ce64dd67481fcf9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6ce64dd67481fcf9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:42:11Z; reviewed SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb; current SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb; hash_changed=False. Reports=["reports/yaml_record_review/TYG_Salts_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock fallback is synchronized, but the stock solution has no component-level representation.

## Findings

### rec-f-7905ad309621af55: Historical review coverage and residual narrative: TYG_Salts_Solution

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-6ce64dd67481fcf9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:42:11Z; reviewed SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb; current SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb; hash_changed=False. Reports=["reports/yaml_record_review/TYG_Salts_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock fallback is synchronized, but the stock solution has no component-level representation.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ae5400770971548c | data/ingredients/mapped/TYG_Salts_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[116],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:tyg_salts_solution","line":118,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:tyg_salts_solution","preferred_term":"TYG salts solution"}],"identifier":"kgmicrobe.ingredient:tyg_salts_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:tyg_salts_solution","ontology_label":"TYG salts solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"TYG salts solution","sssom_rows":[{"data_row":2711,"object_id":"kgmicrobe.ingredient:tyg_salts_solution","object_label":"TYG salts solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:TYG_Salts_Solution","synonym_count":1} |
| ev-d6253bb5fcfd5f16 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [116] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c0b283b7bd1bf36a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:TYG_Salts_Solution; data-row positions=[2711] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2711,"object_id":"kgmicrobe.ingredient:tyg_salts_solution","object_label":"TYG salts solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:TYG_Salts_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-f0d11f9a0c170f48 | docs/data/mapped_ingredients.csv; CSV lines=[118] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:tyg_salts_solution","line":118,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:tyg_salts_solution","preferred_term":"TYG salts solution","total_occurrences":"2"}] |
| ev-32311bc102a18b09 | reports/yaml_record_review/TYG_Salts_Solution.md; &#96;data/ingredients/mapped/TYG_Salts_Solution.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:32; Completeness:44; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-00526485e8ae1e67 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1267] | context_only | [{"current_record_sha256":"fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb","finding_id":"SEM:d23435dac8f40ffdd486","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tyg-salts-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: TYG_Salts_Solution (data/ingredients/mapped/TYG_Salts_Solution.yaml)'
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
summary: Per-record structured review for TYG_Salts_Solution (data/ingredients/mapped/TYG_Salts_Solution.yaml,
  record-6ce64dd67481fcf9, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/TYG_Salts_Solution.yaml
    sha256: fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/TYG_Salts_Solution.md
    sha256: 56c5329a0ee8af6a39d74b51714283c5176ce544e92134272521320cd3a283cc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6ce64dd67481fcf9
  path: data/ingredients/mapped/TYG_Salts_Solution.yaml
  label: TYG_Salts_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/TYG_Salts_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/TYG_Salts_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/TYG_Salts_Solution.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6ce64dd67481fcf9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6ce64dd67481fcf9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-6ce64dd67481fcf9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6ce64dd67481fcf9
evidence:
- evidence_id: ev-ae5400770971548c
  kind: record_content
  reference: data/ingredients/mapped/TYG_Salts_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[116],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:tyg_salts_solution","line":118,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:tyg_salts_solution","preferred_term":"TYG
    salts solution"}],"identifier":"kgmicrobe.ingredient:tyg_salts_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:tyg_salts_solution","ontology_label":"TYG
    salts solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"TYG
    salts solution","sssom_rows":[{"data_row":2711,"object_id":"kgmicrobe.ingredient:tyg_salts_solution","object_label":"TYG
    salts solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:TYG_Salts_Solution","synonym_count":1}'
  snapshot_sha256: fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb
- evidence_id: ev-d6253bb5fcfd5f16
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [116]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c0b283b7bd1bf36a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:TYG_Salts_Solution; data-row positions=[2711]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2711,"object_id":"kgmicrobe.ingredient:tyg_salts_solution","object_label":"TYG
    salts solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:TYG_Salts_Solution","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f0d11f9a0c170f48
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[118]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:tyg_salts_solution","line":118,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"2","ontology_id":"kgmicrobe.ingredient:tyg_salts_solution","preferred_term":"TYG
    salts solution","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-32311bc102a18b09
  kind: prior_review
  reference: reports/yaml_record_review/TYG_Salts_Solution.md
  locator: '`data/ingredients/mapped/TYG_Salts_Solution.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:32; Completeness:44; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 56c5329a0ee8af6a39d74b51714283c5176ce544e92134272521320cd3a283cc
  quote: "Recommended Edits:\n- Major: curate the TYG salts solution formula in\n\
    \  `data/ingredients/mapped/TYG_Salts_Solution.yaml`, adding a supported\n  `components`\
    \ list and a `component_assertion` or recording an explicit\n  unresolved-composition\
    \ decision if the component amounts cannot be recovered.\n- Major: regenerate\
    \ generated component and product artifacts after the\n  per-record YAML gains\
    \ a component-level representation."
- evidence_id: ev-00526485e8ae1e67
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1267]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb","finding_id":"SEM:d23435dac8f40ffdd486","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b0db6cfa21ab2766
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6ce64dd67481fcf9
  evidence_ids:
  - ev-ae5400770971548c
  - ev-d6253bb5fcfd5f16
  - ev-c0b283b7bd1bf36a
  - ev-f0d11f9a0c170f48
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8104de2a1024b113
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6ce64dd67481fcf9
  evidence_ids:
  - ev-32311bc102a18b09
  - ev-ae5400770971548c
  - ev-00526485e8ae1e67
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:42:11Z;
    reviewed SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb;
    current SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb;
    hash_changed=False. Reports=["reports/yaml_record_review/TYG_Salts_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock fallback is synchronized, but the stock solution has no component-level
    representation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-32311bc102a18b09
    - ev-ae5400770971548c
  - name: legacy-native-ids
    value: '["SEM:d23435dac8f40ffdd486"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ae5400770971548c
    - ev-32311bc102a18b09
    - ev-00526485e8ae1e67
findings:
- finding_id: rec-f-7905ad309621af55
  issue_key: mim-reconciliation-historical-review-coverage-and-r-6ce64dd67481fcf9
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: TYG_Salts_Solution'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:42:11Z;
    reviewed SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb;
    current SHA-256=fbf220af63c83835e02a3cce65c8cb9c72140bdebb81c3fe73acc56a88d26abb;
    hash_changed=False. Reports=["reports/yaml_record_review/TYG_Salts_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock fallback is synchronized, but the stock solution has no component-level
    representation.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6ce64dd67481fcf9
  evidence_ids:
  - ev-32311bc102a18b09
  - ev-ae5400770971548c
  - ev-00526485e8ae1e67
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/TYG_Salts_Solution.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
