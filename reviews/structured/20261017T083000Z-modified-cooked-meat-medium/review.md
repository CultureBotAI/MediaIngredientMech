# Per-record structured review: Modified_Cooked_Meat_Medium (data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml)

- Review: 20261017T083000Z-modified-cooked-meat-medium
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Modified_Cooked_Meat_Medium (data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml, record-7d9bdb27da374251, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7d9bdb27da374251 | data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml | maintained | Modified_Cooked_Meat_Medium |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7d9bdb27da374251 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-7d9bdb27da374251 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7d9bdb27da374251 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7d9bdb27da374251.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-7d9bdb27da374251.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T03:47:06Z; reviewed SHA-256=85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97; current SHA-256=85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97; hash_changed=False. Reports=["reports/yaml_record_review/Modified_Cooked_Meat_Medium.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local Modified Cooked Meat Medium identity, curated partial component assertion, MicrobeDecoder provenance, and final registry row pass.

## Findings

### rec-f-1ffa75c14694dd8d: Reassess component source scope: Modified_Cooked_Meat_Medium

major / deferred / provisional; issue key: mim-semantic-component-source-scope-7d9bdb27da374251.

Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:a76f929f750eb6d00bd0d4cc00962dc25aef1815dc01dcba9c05c6b3d593c851.

Disposition: Expansion/interpretation is retained as an assertion, but the exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL completeness is not proof of membership. (Historical finding remains unresolved; no blanket approval.). Affected unit(s): MIM.assertion:a76f929f750eb6d00bd0d4cc00962dc25aef1815dc01dcba9c05c6b3d593c851.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c5ec34d85d88f6a6 | data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[46],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:modified_cooked_meat_medium","line":48,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","preferred_term":"Modified Cooked Meat Medium"}],"identifier":"kgmicrobe.ingredient:modified_cooked_meat_medium","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","ontology_label":"Modified Cooked Meat Medium","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Modified Cooked Meat Medium","sssom_rows":[{"data_row":1901,"object_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","object_label":"Modified Cooked Meat Medium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Modified_Cooked_Meat_Medium","synonym_count":1} |
| ev-e32481c800a1f611 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [46] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-53451362369292f4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Modified_Cooked_Meat_Medium; data-row positions=[1901] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1901,"object_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","object_label":"Modified Cooked Meat Medium","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Modified_Cooked_Meat_Medium","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-4c34b160ed5c5a41 | docs/data/mapped_ingredients.csv; CSV lines=[48] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:modified_cooked_meat_medium","line":48,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","preferred_term":"Modified Cooked Meat Medium","total_occurrences":"0"}] |
| ev-161e9c6eea067ec4 | reports/yaml_record_review/Modified_Cooked_Meat_Medium.md; &#96;data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml&#96;:2; Verdict:4; Identity:9; Validation:21; Evidence:30; Completeness:41; Recommended Edits:48 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3d85877c0bffac4e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1846] | context_only | [{"current_record_sha256":"85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97","finding_id":"SEM:c90dbfc1bb8a636cbbd1","kind":"component_source_scope","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-894446f6b3f6be3f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-modified-cooked-meat-medium
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Modified_Cooked_Meat_Medium (data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml)'
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
summary: Per-record structured review for Modified_Cooked_Meat_Medium (data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml,
  record-7d9bdb27da374251, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
    sha256: 85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Modified_Cooked_Meat_Medium.md
    sha256: d8d0300f62566ab02e8dcdf136c23d904480ece805be1847afdfc68df9b40ec9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7d9bdb27da374251
  path: data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
  label: Modified_Cooked_Meat_Medium
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7d9bdb27da374251
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7d9bdb27da374251
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-7d9bdb27da374251
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7d9bdb27da374251
evidence:
- evidence_id: ev-c5ec34d85d88f6a6
  kind: record_content
  reference: data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[46],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:modified_cooked_meat_medium","line":48,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","preferred_term":"Modified
    Cooked Meat Medium"}],"identifier":"kgmicrobe.ingredient:modified_cooked_meat_medium","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","ontology_label":"Modified
    Cooked Meat Medium","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Modified
    Cooked Meat Medium","sssom_rows":[{"data_row":1901,"object_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","object_label":"Modified
    Cooked Meat Medium","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Modified_Cooked_Meat_Medium","synonym_count":1}'
  snapshot_sha256: 85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97
- evidence_id: ev-e32481c800a1f611
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [46]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-53451362369292f4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Modified_Cooked_Meat_Medium; data-row positions=[1901]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1901,"object_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","object_label":"Modified
    Cooked Meat Medium","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Modified_Cooked_Meat_Medium","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4c34b160ed5c5a41
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[48]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:modified_cooked_meat_medium","line":48,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:modified_cooked_meat_medium","preferred_term":"Modified
    Cooked Meat Medium","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-161e9c6eea067ec4
  kind: prior_review
  reference: reports/yaml_record_review/Modified_Cooked_Meat_Medium.md
  locator: '`data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml`:2; Verdict:4;
    Identity:9; Validation:21; Evidence:30; Completeness:41; Recommended Edits:48'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d8d0300f62566ab02e8dcdf136c23d904480ece805be1847afdfc68df9b40ec9
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-3d85877c0bffac4e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1846]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97","finding_id":"SEM:c90dbfc1bb8a636cbbd1","kind":"component_source_scope","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-894446f6b3f6be3f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0a4796e088aa654a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7d9bdb27da374251
  evidence_ids:
  - ev-c5ec34d85d88f6a6
  - ev-e32481c800a1f611
  - ev-53451362369292f4
  - ev-4c34b160ed5c5a41
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-03037a9bca66e653
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-7d9bdb27da374251
  evidence_ids:
  - ev-161e9c6eea067ec4
  - ev-c5ec34d85d88f6a6
  - ev-3d85877c0bffac4e
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-17T03:47:06Z;
    reviewed SHA-256=85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97;
    current SHA-256=85ab9042f8e67c7ec43210a485b7a9f872d43fc769dc315887fd5d8c1cdacf97;
    hash_changed=False. Reports=["reports/yaml_record_review/Modified_Cooked_Meat_Medium.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    Modified Cooked Meat Medium identity, curated partial component assertion, MicrobeDecoder
    provenance, and final registry row pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:c90dbfc1bb8a636cbbd1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c5ec34d85d88f6a6
    - ev-161e9c6eea067ec4
    - ev-3d85877c0bffac4e
findings:
- finding_id: rec-f-1ffa75c14694dd8d
  issue_key: mim-semantic-component-source-scope-7d9bdb27da374251
  category: representation
  severity: major
  status: deferred
  certainty: provisional
  title: 'Reassess component source scope: Modified_Cooked_Meat_Medium'
  description: 'Expansion/interpretation is retained as an assertion, but the exact
    source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:a76f929f750eb6d00bd0d4cc00962dc25aef1815dc01dcba9c05c6b3d593c851.'
  disposition_reason: 'Expansion/interpretation is retained as an assertion, but the
    exact source preparation must be verified before semantic approval. UNKNOWN/PARTIAL
    completeness is not proof of membership. (Historical finding remains unresolved;
    no blanket approval.). Affected unit(s): MIM.assertion:a76f929f750eb6d00bd0d4cc00962dc25aef1815dc01dcba9c05c6b3d593c851.'
  target_ids:
  - record-7d9bdb27da374251
  evidence_ids:
  - ev-c5ec34d85d88f6a6
  - ev-894446f6b3f6be3f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Modified_Cooked_Meat_Medium.yaml
    role: maintained ingredient
  field_paths:
  - synonyms
  - occurrence_statistics
  tags:
  - reconciliation
  - bundle-by-owner
  - component-source-scope
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
