# Per-record structured review: K-acetate (data/ingredients/mapped/K-acetate.yaml)

- Review: 20261017T083000Z-k-acetate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for K-acetate (data/ingredients/mapped/K-acetate.yaml, record-086c2ee4af042d7f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/K-acetate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/K-acetate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-086c2ee4af042d7f | data/ingredients/mapped/K-acetate.yaml | maintained | K-acetate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-086c2ee4af042d7f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-086c2ee4af042d7f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-086c2ee4af042d7f | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-086c2ee4af042d7f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-086c2ee4af042d7f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:11:41Z; reviewed SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4; current SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4; hash_changed=False. Reports=["reports/yaml_record_review/K-acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact potassium acetate identity, CAS alias, kg-microbe synonyms, and structure fields pass, but broader acetate/acetyl ester labels export as synonyms and CARBON_SOURCE is not supported by the original Mineral role.

## Findings

### rec-f-433834258fd9a2d3: Historical review coverage and residual narrative: K-acetate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-086c2ee4af042d7f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:11:41Z; reviewed SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4; current SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4; hash_changed=False. Reports=["reports/yaml_record_review/K-acetate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact potassium acetate identity, CAS alias, kg-microbe synonyms, and structure fields pass, but broader acetate/acetyl ester labels export as synonyms and CARBON_SOURCE is not supported by the original Mineral role.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-51a71326dcdcd96d | data/ingredients/mapped/K-acetate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1185],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32029","line":1187,"mapping_status":"MAPPED","ontology_id":"CHEBI:32029","preferred_term":"K-acetate"}],"identifier":"CHEBI:32029","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":18,"edge_count":18,"occurrences":18},"occurrence_statistics":{"media_count":18,"total_occurrences":18},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32029","ontology_label":"potassium acetate","ontology_source":"CHEBI"},"preferred_term":"K-acetate","sssom_rows":[{"data_row":1521,"object_id":"CHEBI:32029","object_label":"potassium acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:K-acetate","synonym_count":16} |
| ev-268cd483aef5ab85 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1185] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f8340c95759af1ce | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:K-acetate; data-row positions=[1521] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1521,"object_id":"CHEBI:32029","object_label":"potassium acetate","other":"AcOK&#124;CH3CO2K&#124;E261&#124;KOAc&#124;Kaliumazetat&#124;MeCO2K&#124;Acetic ester&#124;Acetyl ester&#124;acetate ester&#124;acetate esters&#124;acetates&#124;acetyl esters&#124;an acetyl ester&#124;CAS:127-08-2","predicate_id":"skos:exactMatch","subject_id":"MIM:K-acetate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-7fab369574108bf2 | docs/data/mapped_ingredients.csv; CSV lines=[1187] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32029","line":1187,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"18","ontology_id":"CHEBI:32029","preferred_term":"K-acetate","total_occurrences":"18"}] |
| ev-2c1772d75898975f | reports/yaml_record_review/K-acetate.md; &#96;data/ingredients/mapped/K-acetate.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:34; Completeness:60; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b13dcac83e1c3e12 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[757] | context_only | [{"current_record_sha256":"7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4","finding_id":"SEM:1beec9d596075bf09331","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-k-acetate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: K-acetate (data/ingredients/mapped/K-acetate.yaml)'
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
summary: Per-record structured review for K-acetate (data/ingredients/mapped/K-acetate.yaml,
  record-086c2ee4af042d7f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/K-acetate.yaml
    sha256: 7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4
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
  - path: reports/yaml_record_review/K-acetate.md
    sha256: 3a5142e972fde164a284fdb13b2984ea6e9935f843f3b39b85be97ca5f8ff17e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-086c2ee4af042d7f
  path: data/ingredients/mapped/K-acetate.yaml
  label: K-acetate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/K-acetate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/K-acetate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/K-acetate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-086c2ee4af042d7f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-086c2ee4af042d7f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-086c2ee4af042d7f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-086c2ee4af042d7f
evidence:
- evidence_id: ev-51a71326dcdcd96d
  kind: record_content
  reference: data/ingredients/mapped/K-acetate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1185],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32029","line":1187,"mapping_status":"MAPPED","ontology_id":"CHEBI:32029","preferred_term":"K-acetate"}],"identifier":"CHEBI:32029","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":18,"edge_count":18,"occurrences":18},"occurrence_statistics":{"media_count":18,"total_occurrences":18},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32029","ontology_label":"potassium
    acetate","ontology_source":"CHEBI"},"preferred_term":"K-acetate","sssom_rows":[{"data_row":1521,"object_id":"CHEBI:32029","object_label":"potassium
    acetate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:K-acetate","synonym_count":16}'
  snapshot_sha256: 7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4
- evidence_id: ev-268cd483aef5ab85
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1185]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f8340c95759af1ce
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:K-acetate; data-row positions=[1521]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1521,"object_id":"CHEBI:32029","object_label":"potassium
    acetate","other":"AcOK|CH3CO2K|E261|KOAc|Kaliumazetat|MeCO2K|Acetic ester|Acetyl
    ester|acetate ester|acetate esters|acetates|acetyl esters|an acetyl ester|CAS:127-08-2","predicate_id":"skos:exactMatch","subject_id":"MIM:K-acetate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7fab369574108bf2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1187]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32029","line":1187,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"18","ontology_id":"CHEBI:32029","preferred_term":"K-acetate","total_occurrences":"18"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2c1772d75898975f
  kind: prior_review
  reference: reports/yaml_record_review/K-acetate.md
  locator: '`data/ingredients/mapped/K-acetate.yaml`:2; Verdict:4; Identity:12; Validation:23;
    Evidence:34; Completeness:60; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3a5142e972fde164a284fdb13b2984ea6e9935f843f3b39b85be97ca5f8ff17e
  quote: "Recommended Edits:\n- Major: remove the seven `sssom_other_backfill` class-label\
    \ synonyms from\n  `data/ingredients/mapped/K-acetate.yaml`, synchronize the curated\
    \ aggregate,\n  and rebuild the final SSSOM/docs surfaces so only true potassium\
    \ acetate\n  synonyms remain in `other`.\n- Major: fix `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/K-acetate.yaml`; either remove it or attach inspected\n\
    \  evidence that specifically supports potassium acetate as a carbon source,\n\
    \  then rerun strict, term, round-trip, id-label, component, and SSSOM\n  validation."
- evidence_id: ev-b13dcac83e1c3e12
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[757]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4","finding_id":"SEM:1beec9d596075bf09331","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-1e0e38ee01525af7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-086c2ee4af042d7f
  evidence_ids:
  - ev-51a71326dcdcd96d
  - ev-268cd483aef5ab85
  - ev-f8340c95759af1ce
  - ev-7fab369574108bf2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-10ece9476a2542b4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-086c2ee4af042d7f
  evidence_ids:
  - ev-2c1772d75898975f
  - ev-51a71326dcdcd96d
  - ev-b13dcac83e1c3e12
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:11:41Z;
    reviewed SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4;
    current SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4;
    hash_changed=False. Reports=["reports/yaml_record_review/K-acetate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact potassium
    acetate identity, CAS alias, kg-microbe synonyms, and structure fields pass, but
    broader acetate/acetyl ester labels export as synonyms and CARBON_SOURCE is not
    supported by the original Mineral role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2c1772d75898975f
    - ev-51a71326dcdcd96d
  - name: legacy-native-ids
    value: '["SEM:1beec9d596075bf09331"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-51a71326dcdcd96d
    - ev-2c1772d75898975f
    - ev-b13dcac83e1c3e12
findings:
- finding_id: rec-f-433834258fd9a2d3
  issue_key: mim-reconciliation-historical-review-coverage-and-r-086c2ee4af042d7f
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: K-acetate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:11:41Z;
    reviewed SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4;
    current SHA-256=7e76f61f55c0f3b3b1b018ada603db7dc8ea48a36af570ec26e7e72f253cc5a4;
    hash_changed=False. Reports=["reports/yaml_record_review/K-acetate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact potassium
    acetate identity, CAS alias, kg-microbe synonyms, and structure fields pass, but
    broader acetate/acetyl ester labels export as synonyms and CARBON_SOURCE is not
    supported by the original Mineral role.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-086c2ee4af042d7f
  evidence_ids:
  - ev-2c1772d75898975f
  - ev-51a71326dcdcd96d
  - ev-b13dcac83e1c3e12
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/K-acetate.yaml
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
