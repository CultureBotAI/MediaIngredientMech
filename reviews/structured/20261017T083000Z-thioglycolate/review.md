# Per-record structured review: Thioglycolate (data/ingredients/mapped/Thioglycolate.yaml)

- Review: 20261017T083000Z-thioglycolate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Thioglycolate (data/ingredients/mapped/Thioglycolate.yaml, record-ea8ce69d7ca31737, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Thioglycolate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Thioglycolate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ea8ce69d7ca31737 | data/ingredients/mapped/Thioglycolate.yaml | maintained | Thioglycolate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ea8ce69d7ca31737 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-ea8ce69d7ca31737 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ea8ce69d7ca31737 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ea8ce69d7ca31737.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ea8ce69d7ca31737.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:42:35Z; reviewed SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4; current SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4; hash_changed=False. Reports=["reports/yaml_record_review/Thioglycolate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synchronized CHEBI:47869 dianion row passes structurally, but CAS 513-66-6 resolves to monoanionic thioglycolate and conflicts with the curated target.

## Findings

### rec-f-32f013f1e87e63a7: Historical review coverage and residual narrative: Thioglycolate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-ea8ce69d7ca31737.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:42:35Z; reviewed SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4; current SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4; hash_changed=False. Reports=["reports/yaml_record_review/Thioglycolate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synchronized CHEBI:47869 dianion row passes structurally, but CAS 513-66-6 resolves to monoanionic thioglycolate and conflicts with the curated target.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-63d954d5d3537901 | data/ingredients/mapped/Thioglycolate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1960],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:47869","line":1962,"mapping_status":"MAPPED","ontology_id":"CHEBI:47869","preferred_term":"Thioglycolate"}],"identifier":"CHEBI:47869","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:47869","ontology_label":"thioglycolate(2-)","ontology_source":"CHEBI"},"preferred_term":"Thioglycolate","sssom_rows":[{"data_row":2767,"object_id":"CHEBI:47869","object_label":"thioglycolate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thioglycolate","synonym_count":2} |
| ev-6e0b2b96b9357f84 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1960] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-510ba060d2df95f3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Thioglycolate; data-row positions=[2767] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2767,"object_id":"CHEBI:47869","object_label":"thioglycolate(2-)","other":"sulfidoacetate&#124;CAS:513-66-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Thioglycolate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-5096e61ec71f3079 | docs/data/mapped_ingredients.csv; CSV lines=[1962] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:47869","line":1962,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:47869","preferred_term":"Thioglycolate","total_occurrences":"7"}] |
| ev-64000ead890405c1 | reports/yaml_record_review/Thioglycolate.md; &#96;data/ingredients/mapped/Thioglycolate.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:32; Completeness:45; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-17e2206d1d95d2cf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1287] | context_only | [{"current_record_sha256":"7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4","finding_id":"SEM:2e8bea54529ef3675202","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-thioglycolate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Thioglycolate (data/ingredients/mapped/Thioglycolate.yaml)'
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
summary: Per-record structured review for Thioglycolate (data/ingredients/mapped/Thioglycolate.yaml,
  record-ea8ce69d7ca31737, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Thioglycolate.yaml
    sha256: 7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4
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
  - path: reports/yaml_record_review/Thioglycolate.md
    sha256: d077dc37f79cd32af9990849f68ae970000e1a0e16c822717ad4ad9c263941d7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ea8ce69d7ca31737
  path: data/ingredients/mapped/Thioglycolate.yaml
  label: Thioglycolate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thioglycolate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Thioglycolate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Thioglycolate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ea8ce69d7ca31737
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ea8ce69d7ca31737
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-ea8ce69d7ca31737
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ea8ce69d7ca31737
evidence:
- evidence_id: ev-63d954d5d3537901
  kind: record_content
  reference: data/ingredients/mapped/Thioglycolate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1960],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:47869","line":1962,"mapping_status":"MAPPED","ontology_id":"CHEBI:47869","preferred_term":"Thioglycolate"}],"identifier":"CHEBI:47869","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":7,"edge_count":7,"occurrences":7},"occurrence_statistics":{"media_count":7,"total_occurrences":7},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:47869","ontology_label":"thioglycolate(2-)","ontology_source":"CHEBI"},"preferred_term":"Thioglycolate","sssom_rows":[{"data_row":2767,"object_id":"CHEBI:47869","object_label":"thioglycolate(2-)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Thioglycolate","synonym_count":2}'
  snapshot_sha256: 7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4
- evidence_id: ev-6e0b2b96b9357f84
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1960]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-510ba060d2df95f3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Thioglycolate; data-row positions=[2767]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2767,"object_id":"CHEBI:47869","object_label":"thioglycolate(2-)","other":"sulfidoacetate|CAS:513-66-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Thioglycolate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5096e61ec71f3079
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1962]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:47869","line":1962,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"7","ontology_id":"CHEBI:47869","preferred_term":"Thioglycolate","total_occurrences":"7"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-64000ead890405c1
  kind: prior_review
  reference: reports/yaml_record_review/Thioglycolate.md
  locator: '`data/ingredients/mapped/Thioglycolate.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:32; Completeness:45; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d077dc37f79cd32af9990849f68ae970000e1a0e16c822717ad4ad9c263941d7
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Thioglycolate.yaml`,\
    \ inspect the source\n  occurrences for whether the intended ingredient is thioglycolate\
    \ monoanion,\n  thioglycolate dianion, a salt, or the acid; then reground the\
    \ record or\n  remove the CAS RN so its ChEBI target, formula, and final SSSOM\
    \ `other`\n  payload agree. Rerun strict validation, term validation, SSSOM publication,\n\
    \  row review, and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-17e2206d1d95d2cf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1287]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4","finding_id":"SEM:2e8bea54529ef3675202","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-60435e49b0acecd6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ea8ce69d7ca31737
  evidence_ids:
  - ev-63d954d5d3537901
  - ev-6e0b2b96b9357f84
  - ev-510ba060d2df95f3
  - ev-5096e61ec71f3079
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-db80591d1387a8a9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ea8ce69d7ca31737
  evidence_ids:
  - ev-64000ead890405c1
  - ev-63d954d5d3537901
  - ev-17e2206d1d95d2cf
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:42:35Z;
    reviewed SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4;
    current SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4;
    hash_changed=False. Reports=["reports/yaml_record_review/Thioglycolate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The synchronized
    CHEBI:47869 dianion row passes structurally, but CAS 513-66-6 resolves to monoanionic
    thioglycolate and conflicts with the curated target.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-64000ead890405c1
    - ev-63d954d5d3537901
  - name: legacy-native-ids
    value: '["SEM:2e8bea54529ef3675202"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-63d954d5d3537901
    - ev-64000ead890405c1
    - ev-17e2206d1d95d2cf
findings:
- finding_id: rec-f-32f013f1e87e63a7
  issue_key: mim-reconciliation-historical-review-coverage-and-r-ea8ce69d7ca31737
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Thioglycolate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:42:35Z;
    reviewed SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4;
    current SHA-256=7bc62ba32447aaba996dbb9c6baf037c658c2d8ba7abf4d392e8c2c540b215a4;
    hash_changed=False. Reports=["reports/yaml_record_review/Thioglycolate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The synchronized
    CHEBI:47869 dianion row passes structurally, but CAS 513-66-6 resolves to monoanionic
    thioglycolate and conflicts with the curated target.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ea8ce69d7ca31737
  evidence_ids:
  - ev-64000ead890405c1
  - ev-63d954d5d3537901
  - ev-17e2206d1d95d2cf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Thioglycolate.yaml
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
