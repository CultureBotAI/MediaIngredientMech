# Per-record structured review: Zinc_Acetate (data/ingredients/mapped/Zinc_Acetate.yaml)

- Review: 20261017T083000Z-zinc-acetate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Zinc_Acetate (data/ingredients/mapped/Zinc_Acetate.yaml, record-490f1f0d743f83c2, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Zinc_Acetate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Zinc_Acetate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-490f1f0d743f83c2 | data/ingredients/mapped/Zinc_Acetate.yaml | maintained | Zinc_Acetate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-490f1f0d743f83c2 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-490f1f0d743f83c2 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-490f1f0d743f83c2 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-490f1f0d743f83c2.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-490f1f0d743f83c2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-17T21:41:53Z; reviewed SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614; current SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614; hash_changed=False. Reports=["reports/yaml_record_review/Zinc_Acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI zinc acetate identity and CultureMech provenance pass, but ingredient_type and chemical_properties are still absent.

## Findings

### rec-f-1270daf22c8b9687: Historical review coverage and residual narrative: Zinc_Acetate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-490f1f0d743f83c2.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-17T21:41:53Z; reviewed SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614; current SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614; hash_changed=False. Reports=["reports/yaml_record_review/Zinc_Acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI zinc acetate identity and CultureMech provenance pass, but ingredient_type and chemical_properties are still absent.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-08d37edba94f75a1 | data/ingredients/mapped/Zinc_Acetate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2622],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62984","line":2624,"mapping_status":"MAPPED","ontology_id":"CHEBI:62984","preferred_term":"Zinc Acetate"}],"identifier":"CHEBI:62984","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:62984","ontology_label":"zinc acetate","ontology_source":"CHEBI"},"preferred_term":"Zinc Acetate","sssom_rows":[{"data_row":2959,"object_id":"CHEBI:62984","object_label":"zinc acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Zinc_Acetate","synonym_count":0} |
| ev-9c17746e323c3d8f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2622] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6f49e8797c7aa95d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Zinc_Acetate; data-row positions=[2959] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2959,"object_id":"CHEBI:62984","object_label":"zinc acetate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Zinc_Acetate","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-7b9bb4eb4a176d1a | docs/data/mapped_ingredients.csv; CSV lines=[2624] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:62984","line":2624,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:62984","preferred_term":"Zinc Acetate","total_occurrences":"7"}] |
| ev-71dc1780d3aacc86 | reports/yaml_record_review/Zinc_Acetate.md; &#96;data/ingredients/mapped/Zinc_Acetate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:33; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a5607e49f706b009 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1361] | context_only | [{"current_record_sha256":"0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614","finding_id":"SEM:bb1795628e59ed91a1db","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-zinc-acetate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Zinc_Acetate (data/ingredients/mapped/Zinc_Acetate.yaml)'
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
summary: Per-record structured review for Zinc_Acetate (data/ingredients/mapped/Zinc_Acetate.yaml,
  record-490f1f0d743f83c2, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Zinc_Acetate.yaml
    sha256: 0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614
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
  - path: reports/yaml_record_review/Zinc_Acetate.md
    sha256: 2a41f4713db50f7e9b91aa7740911e8e5d3799bac9ff34f6040c05e2d683d6e4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-490f1f0d743f83c2
  path: data/ingredients/mapped/Zinc_Acetate.yaml
  label: Zinc_Acetate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Zinc_Acetate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Zinc_Acetate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Zinc_Acetate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-490f1f0d743f83c2
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-490f1f0d743f83c2
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-490f1f0d743f83c2
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-490f1f0d743f83c2
evidence:
- evidence_id: ev-08d37edba94f75a1
  kind: record_content
  reference: data/ingredients/mapped/Zinc_Acetate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2622],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62984","line":2624,"mapping_status":"MAPPED","ontology_id":"CHEBI:62984","preferred_term":"Zinc
    Acetate"}],"identifier":"CHEBI:62984","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:62984","ontology_label":"zinc
    acetate","ontology_source":"CHEBI"},"preferred_term":"Zinc Acetate","sssom_rows":[{"data_row":2959,"object_id":"CHEBI:62984","object_label":"zinc
    acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Zinc_Acetate","synonym_count":0}'
  snapshot_sha256: 0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614
- evidence_id: ev-9c17746e323c3d8f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2622]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6f49e8797c7aa95d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Zinc_Acetate; data-row positions=[2959]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2959,"object_id":"CHEBI:62984","object_label":"zinc
    acetate","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Zinc_Acetate","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7b9bb4eb4a176d1a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2624]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:62984","line":2624,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:62984","preferred_term":"Zinc
    Acetate","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-71dc1780d3aacc86
  kind: prior_review
  reference: reports/yaml_record_review/Zinc_Acetate.md
  locator: '`data/ingredients/mapped/Zinc_Acetate.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:33; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2a41f4713db50f7e9b91aa7740911e8e5d3799bac9ff34f6040c05e2d683d6e4
  quote: "Recommended Edits:\n- Add `ingredient_type: SINGLE_INGREDIENT`.\n- Backfill\
    \ `chemical_properties` from `CHEBI:62984`.\n- Sync `data/curated/mapped_ingredients.yaml`,\
    \ rebuild SSSOM, and rerun strict\n  validation plus SSSOM invariant validation."
- evidence_id: ev-a5607e49f706b009
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1361]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614","finding_id":"SEM:bb1795628e59ed91a1db","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-51483770aa39b6a8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-490f1f0d743f83c2
  evidence_ids:
  - ev-08d37edba94f75a1
  - ev-9c17746e323c3d8f
  - ev-6f49e8797c7aa95d
  - ev-7b9bb4eb4a176d1a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-89d43a80e2ec423b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-490f1f0d743f83c2
  evidence_ids:
  - ev-71dc1780d3aacc86
  - ev-08d37edba94f75a1
  - ev-a5607e49f706b009
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-17T21:41:53Z;
    reviewed SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614;
    current SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614;
    hash_changed=False. Reports=["reports/yaml_record_review/Zinc_Acetate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    zinc acetate identity and CultureMech provenance pass, but ingredient_type and
    chemical_properties are still absent.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-71dc1780d3aacc86
    - ev-08d37edba94f75a1
  - name: legacy-native-ids
    value: '["SEM:bb1795628e59ed91a1db"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-08d37edba94f75a1
    - ev-71dc1780d3aacc86
    - ev-a5607e49f706b009
findings:
- finding_id: rec-f-1270daf22c8b9687
  issue_key: mim-reconciliation-historical-review-coverage-and-r-490f1f0d743f83c2
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Zinc_Acetate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-17T21:41:53Z;
    reviewed SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614;
    current SHA-256=0b85ce9a3101931b9f1deaec6cc66454b22c0f9a2a8a6f5c630a435c4c018614;
    hash_changed=False. Reports=["reports/yaml_record_review/Zinc_Acetate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    zinc acetate identity and CultureMech provenance pass, but ingredient_type and
    chemical_properties are still absent.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-490f1f0d743f83c2
  evidence_ids:
  - ev-71dc1780d3aacc86
  - ev-08d37edba94f75a1
  - ev-a5607e49f706b009
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Zinc_Acetate.yaml
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
