# Per-record structured review: Berberine (data/ingredients/mapped/Berberine.yaml)

- Review: 20261017T083000Z-berberine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Berberine (data/ingredients/mapped/Berberine.yaml, record-3c818d7e07f980e1, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Berberine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Berberine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3c818d7e07f980e1 | data/ingredients/mapped/Berberine.yaml | maintained | Berberine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3c818d7e07f980e1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3c818d7e07f980e1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3c818d7e07f980e1 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3c818d7e07f980e1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3c818d7e07f980e1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:34:57Z; reviewed SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3; current SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3; hash_changed=False. Reports=["reports/yaml_record_review/Berberine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI berberine chloride grounding and CAS pass, but chemical_properties still describe the pre-regrounding berberine cation and mapping_quality should preserve the CAS_RN_LOOKUP method.

## Findings

### rec-f-4e86099afb616daa: Historical review coverage and residual narrative: Berberine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3c818d7e07f980e1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:34:57Z; reviewed SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3; current SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3; hash_changed=False. Reports=["reports/yaml_record_review/Berberine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI berberine chloride grounding and CAS pass, but chemical_properties still describe the pre-regrounding berberine cation and mapping_quality should preserve the CAS_RN_LOOKUP method.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-04c2be2f3d3cdcb0 | data/ingredients/mapped/Berberine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[572],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31271","line":574,"mapping_status":"MAPPED","ontology_id":"CHEBI:31271","preferred_term":"Berberine"}],"identifier":"CHEBI:31271","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:31271","ontology_label":"Berberine chloride (TN)","ontology_source":"CHEBI"},"preferred_term":"Berberine","sssom_rows":[{"data_row":516,"object_id":"CHEBI:31271","object_label":"Berberine chloride (TN)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Berberine","synonym_count":6} |
| ev-a219388a03c6ad53 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [572] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-40e49c0e62ae2b91 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Berberine; data-row positions=[516] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":516,"object_id":"CHEBI:31271","object_label":"Berberine chloride (TN)","other":"9,10-dimethoxy-5,6-dihydro[1,3]dioxolo[4,5-g]isoquino[3,2-a]isoquinolin-7-ium&#124;5,6-dihydro-9,10-dimethoxy-1,3-benzodioxolo[5,6-a]benzo[g]quinolizinium&#124;7,8,13,13a-tetradehydro-9,10-dimethoxy-2,3-[methylenebis(oxy)]berbinium&#124;9,10-dimethoxy-2,3-(methylenedioxy)-7,8,13,13a-tetradehydroberbinium&#124;Berberin&#124;Umbellatine&#124;CAS:633-65-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Berberine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-807cbff4cc5e3e4f | docs/data/mapped_ingredients.csv; CSV lines=[574] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31271","line":574,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:31271","preferred_term":"Berberine","total_occurrences":"0"}] |
| ev-50119d81f522400f | reports/yaml_record_review/Berberine.md; &#96;data/ingredients/mapped/Berberine.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:34; Completeness:48; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4605cb7d63b512bc | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[305] | context_only | [{"current_record_sha256":"3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3","finding_id":"SEM:5514b3b3f8b83a2eb87c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-berberine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Berberine (data/ingredients/mapped/Berberine.yaml)'
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
summary: Per-record structured review for Berberine (data/ingredients/mapped/Berberine.yaml,
  record-3c818d7e07f980e1, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Berberine.yaml
    sha256: 3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3
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
  - path: reports/yaml_record_review/Berberine.md
    sha256: 83eb7dbcbe8a6ae11fdeaa100ecf10677cb5d3287bcf12b58ab50e93940c2200
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3c818d7e07f980e1
  path: data/ingredients/mapped/Berberine.yaml
  label: Berberine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Berberine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Berberine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Berberine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3c818d7e07f980e1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3c818d7e07f980e1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3c818d7e07f980e1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3c818d7e07f980e1
evidence:
- evidence_id: ev-04c2be2f3d3cdcb0
  kind: record_content
  reference: data/ingredients/mapped/Berberine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[572],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31271","line":574,"mapping_status":"MAPPED","ontology_id":"CHEBI:31271","preferred_term":"Berberine"}],"identifier":"CHEBI:31271","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:31271","ontology_label":"Berberine
    chloride (TN)","ontology_source":"CHEBI"},"preferred_term":"Berberine","sssom_rows":[{"data_row":516,"object_id":"CHEBI:31271","object_label":"Berberine
    chloride (TN)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Berberine","synonym_count":6}'
  snapshot_sha256: 3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3
- evidence_id: ev-a219388a03c6ad53
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [572]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-40e49c0e62ae2b91
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Berberine; data-row positions=[516]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":516,"object_id":"CHEBI:31271","object_label":"Berberine
    chloride (TN)","other":"9,10-dimethoxy-5,6-dihydro[1,3]dioxolo[4,5-g]isoquino[3,2-a]isoquinolin-7-ium|5,6-dihydro-9,10-dimethoxy-1,3-benzodioxolo[5,6-a]benzo[g]quinolizinium|7,8,13,13a-tetradehydro-9,10-dimethoxy-2,3-[methylenebis(oxy)]berbinium|9,10-dimethoxy-2,3-(methylenedioxy)-7,8,13,13a-tetradehydroberbinium|Berberin|Umbellatine|CAS:633-65-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Berberine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-807cbff4cc5e3e4f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[574]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31271","line":574,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:31271","preferred_term":"Berberine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-50119d81f522400f
  kind: prior_review
  reference: reports/yaml_record_review/Berberine.md
  locator: '`data/ingredients/mapped/Berberine.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:34; Completeness:48; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 83eb7dbcbe8a6ae11fdeaa100ecf10677cb5d3287bcf12b58ab50e93940c2200
  quote: "Recommended Edits:\n- Major: update `chemical_properties.molecular_formula`,\
    \ `inchi`, and `smiles`\n  in `data/ingredients/mapped/Berberine.yaml` to the\
    \ CAS `633-65-8` berberine\n  chloride structure, then run `just sync-curated`.\n\
    - Minor: change `ontology_mapping.mapping_quality` to `CAS_RN_LOOKUP` in the\n\
    \  same maintained record so the grade preserves the CAS method used in #320."
- evidence_id: ev-4605cb7d63b512bc
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[305]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3","finding_id":"SEM:5514b3b3f8b83a2eb87c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0c26e46df4c1c9ee
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3c818d7e07f980e1
  evidence_ids:
  - ev-04c2be2f3d3cdcb0
  - ev-a219388a03c6ad53
  - ev-40e49c0e62ae2b91
  - ev-807cbff4cc5e3e4f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-58b3c2e8ba3d92c7
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3c818d7e07f980e1
  evidence_ids:
  - ev-50119d81f522400f
  - ev-04c2be2f3d3cdcb0
  - ev-4605cb7d63b512bc
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:34:57Z;
    reviewed SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3;
    current SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3;
    hash_changed=False. Reports=["reports/yaml_record_review/Berberine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CHEBI berberine
    chloride grounding and CAS pass, but chemical_properties still describe the pre-regrounding
    berberine cation and mapping_quality should preserve the CAS_RN_LOOKUP method.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-50119d81f522400f
    - ev-04c2be2f3d3cdcb0
  - name: legacy-native-ids
    value: '["SEM:5514b3b3f8b83a2eb87c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-04c2be2f3d3cdcb0
    - ev-50119d81f522400f
    - ev-4605cb7d63b512bc
findings:
- finding_id: rec-f-4e86099afb616daa
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3c818d7e07f980e1
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Berberine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T09:34:57Z;
    reviewed SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3;
    current SHA-256=3428addbc9302d75c8b09f787463dddae92936347612066898ba8f7f7d9a6ed3;
    hash_changed=False. Reports=["reports/yaml_record_review/Berberine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CHEBI berberine
    chloride grounding and CAS pass, but chemical_properties still describe the pre-regrounding
    berberine cation and mapping_quality should preserve the CAS_RN_LOOKUP method.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3c818d7e07f980e1
  evidence_ids:
  - ev-50119d81f522400f
  - ev-04c2be2f3d3cdcb0
  - ev-4605cb7d63b512bc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Berberine.yaml
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
