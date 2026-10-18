# Per-record structured review: H2so4 (data/ingredients/mapped/H2so4.yaml)

- Review: 20261017T083000Z-h2so4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for H2so4 (data/ingredients/mapped/H2so4.yaml, record-bee6c3a6ba5235a7, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/H2so4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/H2so4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bee6c3a6ba5235a7 | data/ingredients/mapped/H2so4.yaml | maintained | H2so4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bee6c3a6ba5235a7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-bee6c3a6ba5235a7 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bee6c3a6ba5235a7 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bee6c3a6ba5235a7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bee6c3a6ba5235a7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:55:35Z; reviewed SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346; current SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346; hash_changed=False. Reports=["reports/yaml_record_review/H2so4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact sulfuric-acid identity passes, but H2SO4 (0.1 N) is exported as a final SSSOM exact synonym.

## Findings

### rec-f-999d528637fec73a: Historical review coverage and residual narrative: H2so4

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-bee6c3a6ba5235a7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:55:35Z; reviewed SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346; current SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346; hash_changed=False. Reports=["reports/yaml_record_review/H2so4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact sulfuric-acid identity passes, but H2SO4 (0.1 N) is exported as a final SSSOM exact synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-05ad35db7b1fea2b | data/ingredients/mapped/H2so4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1102],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26836","line":1104,"mapping_status":"MAPPED","ontology_id":"CHEBI:26836","preferred_term":"H2SO4"}],"identifier":"CHEBI:26836","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":337,"edge_count":337,"occurrences":337},"occurrence_statistics":{"media_count":337,"total_occurrences":337},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26836","ontology_label":"sulfuric acid","ontology_source":"CHEBI"},"preferred_term":"H2SO4","sssom_rows":[{"data_row":1392,"object_id":"CHEBI:26836","object_label":"sulfuric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H2so4","synonym_count":19} |
| ev-80e49661c00cbe0c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1102] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8076cd6c1562425b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:H2so4; data-row positions=[1392] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1392,"object_id":"CHEBI:26836","object_label":"sulfuric acid","other":"Acide sulfurique&#124;Acido sulfurico&#124;Acidum sulfuricum&#124;Schwefelsaeureloesungen&#124;[S(OH)2O2]&#124;[SO2(OH)2]&#124;dihydrogen tetraoxosulfate&#124;dihydroxidodioxidosulfur&#124;hydrogen tetraoxosulfate(VI)&#124;sulphuric acid&#124;tetraoxosulfuric acid&#124;hydrogen tetraoxosulfate(2-)&#124;H2SO4 (0.1 N)&#124;CAS:7664-93-9","predicate_id":"skos:exactMatch","subject_id":"MIM:H2so4","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-5b4e9022452baa57 | docs/data/mapped_ingredients.csv; CSV lines=[1104] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26836","line":1104,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"337","ontology_id":"CHEBI:26836","preferred_term":"H2SO4","total_occurrences":"337"}] |
| ev-817a849e785bed8b | reports/yaml_record_review/H2so4.md; &#96;data/ingredients/mapped/H2so4.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:31; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-92b3a27fe5b51457 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[715] | context_only | [{"current_record_sha256":"6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346","finding_id":"SEM:9ba80c4d9e91efc3f5ac","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-h2so4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: H2so4 (data/ingredients/mapped/H2so4.yaml)'
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
summary: Per-record structured review for H2so4 (data/ingredients/mapped/H2so4.yaml,
  record-bee6c3a6ba5235a7, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/H2so4.yaml
    sha256: 6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/H2so4.md
    sha256: 4126fdcaa4bd3505ca8b8dfc61e050db2dbfd2af2ac844784a35fb6464db3ee1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bee6c3a6ba5235a7
  path: data/ingredients/mapped/H2so4.yaml
  label: H2so4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H2so4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/H2so4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/H2so4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bee6c3a6ba5235a7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bee6c3a6ba5235a7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-bee6c3a6ba5235a7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bee6c3a6ba5235a7
evidence:
- evidence_id: ev-05ad35db7b1fea2b
  kind: record_content
  reference: data/ingredients/mapped/H2so4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1102],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26836","line":1104,"mapping_status":"MAPPED","ontology_id":"CHEBI:26836","preferred_term":"H2SO4"}],"identifier":"CHEBI:26836","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":337,"edge_count":337,"occurrences":337},"occurrence_statistics":{"media_count":337,"total_occurrences":337},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26836","ontology_label":"sulfuric
    acid","ontology_source":"CHEBI"},"preferred_term":"H2SO4","sssom_rows":[{"data_row":1392,"object_id":"CHEBI:26836","object_label":"sulfuric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H2so4","synonym_count":19}'
  snapshot_sha256: 6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346
- evidence_id: ev-80e49661c00cbe0c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1102]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8076cd6c1562425b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:H2so4; data-row positions=[1392]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1392,"object_id":"CHEBI:26836","object_label":"sulfuric
    acid","other":"Acide sulfurique|Acido sulfurico|Acidum sulfuricum|Schwefelsaeureloesungen|[S(OH)2O2]|[SO2(OH)2]|dihydrogen
    tetraoxosulfate|dihydroxidodioxidosulfur|hydrogen tetraoxosulfate(VI)|sulphuric
    acid|tetraoxosulfuric acid|hydrogen tetraoxosulfate(2-)|H2SO4 (0.1 N)|CAS:7664-93-9","predicate_id":"skos:exactMatch","subject_id":"MIM:H2so4","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5b4e9022452baa57
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1104]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26836","line":1104,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"337","ontology_id":"CHEBI:26836","preferred_term":"H2SO4","total_occurrences":"337"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-817a849e785bed8b
  kind: prior_review
  reference: reports/yaml_record_review/H2so4.md
  locator: '`data/ingredients/mapped/H2so4.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:31; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4126fdcaa4bd3505ca8b8dfc61e050db2dbfd2af2ac844784a35fb6464db3ee1
  quote: "Recommended Edits:\n- Major: remove `H2SO4 (0.1 N)` as an exported exact\
    \ synonym, either by\n  deleting it from this record or by extending the final-SSSOM\
    \ synonym policy to\n  reject concentration-qualified surface forms."
- evidence_id: ev-92b3a27fe5b51457
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[715]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346","finding_id":"SEM:9ba80c4d9e91efc3f5ac","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c67209df9392505b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bee6c3a6ba5235a7
  evidence_ids:
  - ev-05ad35db7b1fea2b
  - ev-80e49661c00cbe0c
  - ev-8076cd6c1562425b
  - ev-5b4e9022452baa57
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a90c6ae6f8bf1a82
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bee6c3a6ba5235a7
  evidence_ids:
  - ev-817a849e785bed8b
  - ev-05ad35db7b1fea2b
  - ev-92b3a27fe5b51457
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:55:35Z;
    reviewed SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346;
    current SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346;
    hash_changed=False. Reports=["reports/yaml_record_review/H2so4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact sulfuric-acid
    identity passes, but H2SO4 (0.1 N) is exported as a final SSSOM exact synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-817a849e785bed8b
    - ev-05ad35db7b1fea2b
  - name: legacy-native-ids
    value: '["SEM:9ba80c4d9e91efc3f5ac"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-05ad35db7b1fea2b
    - ev-817a849e785bed8b
    - ev-92b3a27fe5b51457
findings:
- finding_id: rec-f-999d528637fec73a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-bee6c3a6ba5235a7
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: H2so4'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:55:35Z;
    reviewed SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346;
    current SHA-256=6e6f1329c07905f5fae75ee9b3b3d0df521fe63b85c20262dff0c43c17c1f346;
    hash_changed=False. Reports=["reports/yaml_record_review/H2so4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact sulfuric-acid
    identity passes, but H2SO4 (0.1 N) is exported as a final SSSOM exact synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bee6c3a6ba5235a7
  evidence_ids:
  - ev-817a849e785bed8b
  - ev-05ad35db7b1fea2b
  - ev-92b3a27fe5b51457
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H2so4.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
