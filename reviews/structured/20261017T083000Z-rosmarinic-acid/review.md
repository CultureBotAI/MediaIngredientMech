# Per-record structured review: Rosmarinic_Acid (data/ingredients/mapped/Rosmarinic_Acid.yaml)

- Review: 20261017T083000Z-rosmarinic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Rosmarinic_Acid (data/ingredients/mapped/Rosmarinic_Acid.yaml, record-1a786724babaa675, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Rosmarinic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Rosmarinic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1a786724babaa675 | data/ingredients/mapped/Rosmarinic_Acid.yaml | maintained | Rosmarinic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1a786724babaa675 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1a786724babaa675 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1a786724babaa675 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1a786724babaa675.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1a786724babaa675.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:39:18Z; reviewed SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855; current SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855; hash_changed=False. Reports=["reports/yaml_record_review/Rosmarinic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:17226 identity passes, but the CAS alias is too narrow for the mapped subject.

## Findings

### rec-f-3b63d477d2bcf383: Historical review coverage and residual narrative: Rosmarinic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1a786724babaa675.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:39:18Z; reviewed SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855; current SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855; hash_changed=False. Reports=["reports/yaml_record_review/Rosmarinic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:17226 identity passes, but the CAS alias is too narrow for the mapped subject.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6bf37028585152e4 | data/ingredients/mapped/Rosmarinic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1764],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17226","line":1766,"mapping_status":"MAPPED","ontology_id":"CHEBI:17226","preferred_term":"Rosmarinic acid"}],"identifier":"CHEBI:17226","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17226","ontology_label":"rosmarinic acid","ontology_source":"CHEBI"},"preferred_term":"Rosmarinic acid","sssom_rows":[{"data_row":2452,"object_id":"CHEBI:17226","object_label":"rosmarinic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Rosmarinic_Acid","synonym_count":1} |
| ev-e832157dfe9803a7 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1764] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a24a4778e4e5f4bf | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Rosmarinic_Acid; data-row positions=[2452] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2452,"object_id":"CHEBI:17226","object_label":"rosmarinic acid","other":"3-(3,4-dihydroxyphenyl)-2-[(2E)-3-(3,4-dihydroxyphenyl)prop-2-enoyloxy]propanoic acid&#124;CAS:20283-92-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Rosmarinic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-e3f3f3dc56b52a4c | docs/data/mapped_ingredients.csv; CSV lines=[1766] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17226","line":1766,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17226","preferred_term":"Rosmarinic acid","total_occurrences":"0"}] |
| ev-ab8ff1e04ca854f8 | reports/yaml_record_review/Rosmarinic_Acid.md; &#96;data/ingredients/mapped/Rosmarinic_Acid.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8ce3404ed503128c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1178] | context_only | [{"current_record_sha256":"63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855","finding_id":"SEM:62d4ae74e54d4dc5943b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-rosmarinic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Rosmarinic_Acid (data/ingredients/mapped/Rosmarinic_Acid.yaml)'
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
summary: Per-record structured review for Rosmarinic_Acid (data/ingredients/mapped/Rosmarinic_Acid.yaml,
  record-1a786724babaa675, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Rosmarinic_Acid.yaml
    sha256: 63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Rosmarinic_Acid.md
    sha256: 41cb6bbaf5a9de5b6cc6df8d4dfdbe9b644523d719bf7233a4dfdb3a307131d6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1a786724babaa675
  path: data/ingredients/mapped/Rosmarinic_Acid.yaml
  label: Rosmarinic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rosmarinic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Rosmarinic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Rosmarinic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1a786724babaa675
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1a786724babaa675
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1a786724babaa675
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1a786724babaa675
evidence:
- evidence_id: ev-6bf37028585152e4
  kind: record_content
  reference: data/ingredients/mapped/Rosmarinic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1764],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17226","line":1766,"mapping_status":"MAPPED","ontology_id":"CHEBI:17226","preferred_term":"Rosmarinic
    acid"}],"identifier":"CHEBI:17226","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17226","ontology_label":"rosmarinic
    acid","ontology_source":"CHEBI"},"preferred_term":"Rosmarinic acid","sssom_rows":[{"data_row":2452,"object_id":"CHEBI:17226","object_label":"rosmarinic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Rosmarinic_Acid","synonym_count":1}'
  snapshot_sha256: 63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855
- evidence_id: ev-e832157dfe9803a7
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1764]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a24a4778e4e5f4bf
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Rosmarinic_Acid; data-row positions=[2452]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2452,"object_id":"CHEBI:17226","object_label":"rosmarinic
    acid","other":"3-(3,4-dihydroxyphenyl)-2-[(2E)-3-(3,4-dihydroxyphenyl)prop-2-enoyloxy]propanoic
    acid|CAS:20283-92-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Rosmarinic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e3f3f3dc56b52a4c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1766]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17226","line":1766,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17226","preferred_term":"Rosmarinic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ab8ff1e04ca854f8
  kind: prior_review
  reference: reports/yaml_record_review/Rosmarinic_Acid.md
  locator: '`data/ingredients/mapped/Rosmarinic_Acid.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 41cb6bbaf5a9de5b6cc6df8d4dfdbe9b644523d719bf7233a4dfdb3a307131d6
- evidence_id: ev-8ce3404ed503128c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1178]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855","finding_id":"SEM:62d4ae74e54d4dc5943b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-2dc4a8b41c77fdd9
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1a786724babaa675
  evidence_ids:
  - ev-6bf37028585152e4
  - ev-e832157dfe9803a7
  - ev-a24a4778e4e5f4bf
  - ev-e3f3f3dc56b52a4c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2246a44dd7f27111
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1a786724babaa675
  evidence_ids:
  - ev-ab8ff1e04ca854f8
  - ev-6bf37028585152e4
  - ev-8ce3404ed503128c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:39:18Z;
    reviewed SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855;
    current SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855;
    hash_changed=False. Reports=["reports/yaml_record_review/Rosmarinic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:17226 identity passes, but the CAS alias is too narrow for the mapped subject.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ab8ff1e04ca854f8
    - ev-6bf37028585152e4
  - name: legacy-native-ids
    value: '["SEM:62d4ae74e54d4dc5943b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6bf37028585152e4
    - ev-ab8ff1e04ca854f8
    - ev-8ce3404ed503128c
findings:
- finding_id: rec-f-3b63d477d2bcf383
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1a786724babaa675
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Rosmarinic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T12:39:18Z;
    reviewed SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855;
    current SHA-256=63e2f62b614ceefac935b8e3e7e0554b6508341bf0a6884c61f151082c743855;
    hash_changed=False. Reports=["reports/yaml_record_review/Rosmarinic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:17226 identity passes, but the CAS alias is too narrow for the mapped subject.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1a786724babaa675
  evidence_ids:
  - ev-ab8ff1e04ca854f8
  - ev-6bf37028585152e4
  - ev-8ce3404ed503128c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Rosmarinic_Acid.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
