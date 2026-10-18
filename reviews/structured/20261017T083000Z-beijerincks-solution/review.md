# Per-record structured review: Beijerincks_Solution (data/ingredients/mapped/Beijerincks_Solution.yaml)

- Review: 20261017T083000Z-beijerincks-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beijerincks_Solution (data/ingredients/mapped/Beijerincks_Solution.yaml, record-32adb3e00ddc5ddc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beijerincks_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beijerincks_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-32adb3e00ddc5ddc | data/ingredients/mapped/Beijerincks_Solution.yaml | maintained | Beijerincks_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-32adb3e00ddc5ddc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-32adb3e00ddc5ddc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-32adb3e00ddc5ddc | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-32adb3e00ddc5ddc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-32adb3e00ddc5ddc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:26:42Z; reviewed SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c; current SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c; hash_changed=False. Reports=["reports/yaml_record_review/Beijerincks_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient fallback mapping is correct for this stock solution, but component-level recipe curation is still pending.

## Findings

### rec-f-8f1b66650c9fdfb7: Historical review coverage and residual narrative: Beijerincks_Solution

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-32adb3e00ddc5ddc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:26:42Z; reviewed SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c; current SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c; hash_changed=False. Reports=["reports/yaml_record_review/Beijerincks_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient fallback mapping is correct for this stock solution, but component-level recipe curation is still pending.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0894fb1c130821f8 | data/ingredients/mapped/Beijerincks_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[111],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:beijerincks_solution","line":113,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:beijerincks_solution","preferred_term":"Beijerinck's Solution"}],"identifier":"kgmicrobe.ingredient:beijerincks_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:beijerincks_solution","ontology_label":"Beijerinck's Solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Beijerinck's Solution","sssom_rows":[{"data_row":502,"object_id":"kgmicrobe.ingredient:beijerincks_solution","object_label":"Beijerinck's Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beijerincks_Solution","synonym_count":1} |
| ev-a01b4f8bc69ae23c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [111] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d6d565f375073e72 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beijerincks_Solution; data-row positions=[502] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":502,"object_id":"kgmicrobe.ingredient:beijerincks_solution","object_label":"Beijerinck's Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beijerincks_Solution","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-3d12207c5360afa6 | docs/data/mapped_ingredients.csv; CSV lines=[113] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:beijerincks_solution","line":113,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:beijerincks_solution","preferred_term":"Beijerinck's Solution","total_occurrences":"1"}] |
| ev-e2615a47040b5840 | reports/yaml_record_review/Beijerincks_Solution.md; &#96;data/ingredients/mapped/Beijerincks_Solution.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:35; Completeness:48; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ee36f482d1cfed87 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[301] | context_only | [{"current_record_sha256":"d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c","finding_id":"SEM:1e7ed10d33b31c6a0955","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beijerincks-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beijerincks_Solution (data/ingredients/mapped/Beijerincks_Solution.yaml)'
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
summary: Per-record structured review for Beijerincks_Solution (data/ingredients/mapped/Beijerincks_Solution.yaml,
  record-32adb3e00ddc5ddc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beijerincks_Solution.yaml
    sha256: d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c
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
  - path: reports/yaml_record_review/Beijerincks_Solution.md
    sha256: 939cfcd40c543d8c411b625f7fc68206355259bf82d7035d6a908ed16f9575cf
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-32adb3e00ddc5ddc
  path: data/ingredients/mapped/Beijerincks_Solution.yaml
  label: Beijerincks_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beijerincks_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beijerincks_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beijerincks_Solution.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-32adb3e00ddc5ddc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-32adb3e00ddc5ddc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-32adb3e00ddc5ddc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-32adb3e00ddc5ddc
evidence:
- evidence_id: ev-0894fb1c130821f8
  kind: record_content
  reference: data/ingredients/mapped/Beijerincks_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[111],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:beijerincks_solution","line":113,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:beijerincks_solution","preferred_term":"Beijerinck''s
    Solution"}],"identifier":"kgmicrobe.ingredient:beijerincks_solution","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:beijerincks_solution","ontology_label":"Beijerinck''s
    Solution","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Beijerinck''s
    Solution","sssom_rows":[{"data_row":502,"object_id":"kgmicrobe.ingredient:beijerincks_solution","object_label":"Beijerinck''s
    Solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beijerincks_Solution","synonym_count":1}'
  snapshot_sha256: d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c
- evidence_id: ev-a01b4f8bc69ae23c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [111]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d6d565f375073e72
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beijerincks_Solution; data-row positions=[502]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":502,"object_id":"kgmicrobe.ingredient:beijerincks_solution","object_label":"Beijerinck''s
    Solution","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beijerincks_Solution","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3d12207c5360afa6
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[113]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:beijerincks_solution","line":113,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:beijerincks_solution","preferred_term":"Beijerinck''s
    Solution","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e2615a47040b5840
  kind: prior_review
  reference: reports/yaml_record_review/Beijerincks_Solution.md
  locator: '`data/ingredients/mapped/Beijerincks_Solution.yaml`:2; Verdict:4; Identity:10;
    Validation:24; Evidence:35; Completeness:48; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 939cfcd40c543d8c411b625f7fc68206355259bf82d7035d6a908ed16f9575cf
  quote: "Recommended Edits:\n- Major: curate the component recipe for\n  `data/ingredients/mapped/Beijerincks_Solution.yaml`\
    \ from the maintained\n  CultureMech source occurrence if it contains the formulation;\
    \ populate\n  `components` with a matching `component_assertion`, then run\n \
    \ `just sync-curated` and `just qc-component-partonomy`."
- evidence_id: ev-ee36f482d1cfed87
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[301]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c","finding_id":"SEM:1e7ed10d33b31c6a0955","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-cad882c007ee7c2d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-32adb3e00ddc5ddc
  evidence_ids:
  - ev-0894fb1c130821f8
  - ev-a01b4f8bc69ae23c
  - ev-d6d565f375073e72
  - ev-3d12207c5360afa6
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d15cea623ea8e2a1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-32adb3e00ddc5ddc
  evidence_ids:
  - ev-e2615a47040b5840
  - ev-0894fb1c130821f8
  - ev-ee36f482d1cfed87
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:26:42Z;
    reviewed SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c;
    current SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c;
    hash_changed=False. Reports=["reports/yaml_record_review/Beijerincks_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient
    fallback mapping is correct for this stock solution, but component-level recipe
    curation is still pending.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e2615a47040b5840
    - ev-0894fb1c130821f8
  - name: legacy-native-ids
    value: '["SEM:1e7ed10d33b31c6a0955"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0894fb1c130821f8
    - ev-e2615a47040b5840
    - ev-ee36f482d1cfed87
findings:
- finding_id: rec-f-8f1b66650c9fdfb7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-32adb3e00ddc5ddc
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Beijerincks_Solution'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:26:42Z;
    reviewed SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c;
    current SHA-256=d82b85ac20e4fe82d8d4b3319ba396fc4a70c049257d4cdfb4fa8bc74c86925c;
    hash_changed=False. Reports=["reports/yaml_record_review/Beijerincks_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient
    fallback mapping is correct for this stock solution, but component-level recipe
    curation is still pending.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-32adb3e00ddc5ddc
  evidence_ids:
  - ev-e2615a47040b5840
  - ev-0894fb1c130821f8
  - ev-ee36f482d1cfed87
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beijerincks_Solution.yaml
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
