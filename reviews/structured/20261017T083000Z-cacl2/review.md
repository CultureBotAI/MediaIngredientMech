# Per-record structured review: Cacl2 (data/ingredients/mapped/Cacl2.yaml)

- Review: 20261017T083000Z-cacl2
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cacl2 (data/ingredients/mapped/Cacl2.yaml, record-2ea6a8cd58aa5204, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cacl2.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cacl2.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-2ea6a8cd58aa5204 | data/ingredients/mapped/Cacl2.yaml | maintained | Cacl2 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-2ea6a8cd58aa5204 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-2ea6a8cd58aa5204 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-2ea6a8cd58aa5204 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-2ea6a8cd58aa5204.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-2ea6a8cd58aa5204.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:32:41Z; reviewed SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031; current SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031; hash_changed=False. Reports=["reports/yaml_record_review/Cacl2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous calcium chloride identity passes, but CaCl .6H O remains a published exact synonym.

## Findings

### rec-f-dea16239412c4f61: Historical review coverage and residual narrative: Cacl2

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-2ea6a8cd58aa5204.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:32:41Z; reviewed SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031; current SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031; hash_changed=False. Reports=["reports/yaml_record_review/Cacl2.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous calcium chloride identity passes, but CaCl .6H O remains a published exact synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-840ecd1a4d9d17ae | data/ingredients/mapped/Cacl2.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[620],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3312","line":622,"mapping_status":"MAPPED","ontology_id":"CHEBI:3312","preferred_term":"CaCl2"}],"identifier":"CHEBI:3312","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1052,"edge_count":1052,"occurrences":1052},"occurrence_statistics":{"media_count":1052,"total_occurrences":1052},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3312","ontology_label":"calcium dichloride","ontology_source":"CHEBI"},"preferred_term":"CaCl2","sssom_rows":[{"data_row":601,"object_id":"CHEBI:3312","object_label":"calcium dichloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cacl2","synonym_count":21} |
| ev-090f174e7495176b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [620] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c1efded3ff56f494 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cacl2; data-row positions=[601] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":601,"object_id":"CHEBI:3312","object_label":"calcium dichloride","other":"Calcium chloride anhydrous&#124;Calcium chloride&#124;anhydrous calcium chloride&#124;CaCl .6H O&#124;[CaCl2]&#124;CaCl 2&#124;CAS:10043-52-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Cacl2","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-bd6d8e53eeedd78d | docs/data/mapped_ingredients.csv; CSV lines=[622] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3312","line":622,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1052","ontology_id":"CHEBI:3312","preferred_term":"CaCl2","total_occurrences":"1052"}] |
| ev-d891d93233ec9da9 | reports/yaml_record_review/Cacl2.md; &#96;data/ingredients/mapped/Cacl2.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:39; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a42ebcd75348a5d7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[343] | context_only | [{"current_record_sha256":"c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031","finding_id":"SEM:ca3f6b970f3879180a93","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cacl2
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cacl2 (data/ingredients/mapped/Cacl2.yaml)'
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
summary: Per-record structured review for Cacl2 (data/ingredients/mapped/Cacl2.yaml,
  record-2ea6a8cd58aa5204, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cacl2.yaml
    sha256: c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Cacl2.md
    sha256: f0083924c76df5e4d15b3d57664f763c469abcb7e54d857c3378fa7ac7d11d4e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-2ea6a8cd58aa5204
  path: data/ingredients/mapped/Cacl2.yaml
  label: Cacl2
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cacl2.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cacl2.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cacl2.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-2ea6a8cd58aa5204
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-2ea6a8cd58aa5204
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-2ea6a8cd58aa5204
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-2ea6a8cd58aa5204
evidence:
- evidence_id: ev-840ecd1a4d9d17ae
  kind: record_content
  reference: data/ingredients/mapped/Cacl2.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[620],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3312","line":622,"mapping_status":"MAPPED","ontology_id":"CHEBI:3312","preferred_term":"CaCl2"}],"identifier":"CHEBI:3312","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1052,"edge_count":1052,"occurrences":1052},"occurrence_statistics":{"media_count":1052,"total_occurrences":1052},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3312","ontology_label":"calcium
    dichloride","ontology_source":"CHEBI"},"preferred_term":"CaCl2","sssom_rows":[{"data_row":601,"object_id":"CHEBI:3312","object_label":"calcium
    dichloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cacl2","synonym_count":21}'
  snapshot_sha256: c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031
- evidence_id: ev-090f174e7495176b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [620]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c1efded3ff56f494
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cacl2; data-row positions=[601]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":601,"object_id":"CHEBI:3312","object_label":"calcium
    dichloride","other":"Calcium chloride anhydrous|Calcium chloride|anhydrous calcium
    chloride|CaCl .6H O|[CaCl2]|CaCl 2|CAS:10043-52-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Cacl2","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bd6d8e53eeedd78d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[622]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3312","line":622,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1052","ontology_id":"CHEBI:3312","preferred_term":"CaCl2","total_occurrences":"1052"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d891d93233ec9da9
  kind: prior_review
  reference: reports/yaml_record_review/Cacl2.md
  locator: '`data/ingredients/mapped/Cacl2.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:39; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f0083924c76df5e4d15b3d57664f763c469abcb7e54d857c3378fa7ac7d11d4e
  quote: "Recommended Edits:\n- Major: change `CaCl .6H O` from `EXACT_SYNONYM` to\
    \ `REJECTED_LABEL` in\n  `data/ingredients/mapped/Cacl2.yaml`, or move it to a\
    \ distinct local hydrate\n  identity if source inspection proves it denotes a\
    \ recoverable hydrate; then\n  run `just sync-curated` and regenerate SSSOM/docs\
    \ so\n  `mappings/ingredient_mappings.sssom.tsv` and `docs/data/label_index.csv`\
    \ stop\n  publishing it as an anhydrous calcium chloride alias."
- evidence_id: ev-a42ebcd75348a5d7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[343]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031","finding_id":"SEM:ca3f6b970f3879180a93","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-aa93069664871f77
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-2ea6a8cd58aa5204
  evidence_ids:
  - ev-840ecd1a4d9d17ae
  - ev-090f174e7495176b
  - ev-c1efded3ff56f494
  - ev-bd6d8e53eeedd78d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7d8758bfdeeedfbf
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2ea6a8cd58aa5204
  evidence_ids:
  - ev-d891d93233ec9da9
  - ev-840ecd1a4d9d17ae
  - ev-a42ebcd75348a5d7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:32:41Z;
    reviewed SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031;
    current SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031;
    hash_changed=False. Reports=["reports/yaml_record_review/Cacl2.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous calcium
    chloride identity passes, but CaCl .6H O remains a published exact synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d891d93233ec9da9
    - ev-840ecd1a4d9d17ae
  - name: legacy-native-ids
    value: '["SEM:ca3f6b970f3879180a93"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-840ecd1a4d9d17ae
    - ev-d891d93233ec9da9
    - ev-a42ebcd75348a5d7
findings:
- finding_id: rec-f-dea16239412c4f61
  issue_key: mim-reconciliation-historical-review-coverage-and-r-2ea6a8cd58aa5204
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Cacl2'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:32:41Z;
    reviewed SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031;
    current SHA-256=c4a8a17cb58d4aaa6949ca81143f684c04a4cea05da4113df6fd746a11bf0031;
    hash_changed=False. Reports=["reports/yaml_record_review/Cacl2.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous calcium
    chloride identity passes, but CaCl .6H O remains a published exact synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-2ea6a8cd58aa5204
  evidence_ids:
  - ev-d891d93233ec9da9
  - ev-840ecd1a4d9d17ae
  - ev-a42ebcd75348a5d7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cacl2.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
