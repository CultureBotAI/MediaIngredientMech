# Per-record structured review: Andirobin (data/ingredients/mapped/Andirobin.yaml)

- Review: 20261017T083000Z-andirobin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Andirobin (data/ingredients/mapped/Andirobin.yaml, record-ff34e7dfa5871b9f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Andirobin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Andirobin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ff34e7dfa5871b9f | data/ingredients/mapped/Andirobin.yaml | maintained | Andirobin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ff34e7dfa5871b9f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-ff34e7dfa5871b9f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ff34e7dfa5871b9f | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ff34e7dfa5871b9f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ff34e7dfa5871b9f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T08:14:22Z; reviewed SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254; current SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254; hash_changed=False. Reports=["reports/yaml_record_review/Andirobin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The direct CAS fallback, exact CAS SSSOM row, row-review disposition, aggregate copy, and zero CultureMech memberships pass, but PubChem now resolves the CAS and chemistry remains unpopulated.

## Findings

### rec-f-d09bf36869069c6e: Historical review coverage and residual narrative: Andirobin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-ff34e7dfa5871b9f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T08:14:22Z; reviewed SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254; current SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254; hash_changed=False. Reports=["reports/yaml_record_review/Andirobin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The direct CAS fallback, exact CAS SSSOM row, row-review disposition, aggregate copy, and zero CultureMech memberships pass, but PubChem now resolves the CAS and chemistry remains unpopulated.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e796ff4ea81c1d36 | data/ingredients/mapped/Andirobin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[493],"raw_equal":true},"docs_rows":[{"identifier":"cas:6488-63-7","line":495,"mapping_status":"MAPPED","ontology_id":"cas:6488-63-7","preferred_term":"Andirobin"}],"identifier":"cas:6488-63-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:6488-63-7","ontology_label":"Andirobin","ontology_source":"CAS"},"preferred_term":"Andirobin","sssom_rows":[{"data_row":380,"object_id":"cas:6488-63-7","object_label":"Andirobin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Andirobin","synonym_count":0} |
| ev-aa46fa175ad6a0f6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [493] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-aa0e497437419aa8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Andirobin; data-row positions=[380] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":380,"object_id":"cas:6488-63-7","object_label":"Andirobin","other":"CAS:6488-63-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Andirobin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-2cf33521963f607b | docs/data/mapped_ingredients.csv; CSV lines=[495] | supports | Published identity and count rows inspected: [{"identifier":"cas:6488-63-7","line":495,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:6488-63-7","preferred_term":"Andirobin","total_occurrences":"0"}] |
| ev-f6c2e99f90c4045d | reports/yaml_record_review/Andirobin.md; &#96;data/ingredients/mapped/Andirobin.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:37; Completeness:50; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0a28646ada707bc2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[258] | context_only | [{"current_record_sha256":"7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254","finding_id":"SEM:6be3a381c97adf446fe8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-andirobin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Andirobin (data/ingredients/mapped/Andirobin.yaml)'
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
summary: Per-record structured review for Andirobin (data/ingredients/mapped/Andirobin.yaml,
  record-ff34e7dfa5871b9f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Andirobin.yaml
    sha256: 7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254
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
  - path: reports/yaml_record_review/Andirobin.md
    sha256: 9d134d0016d3c7ddd7496db7ae57557ff505c74e973cb7eee89c4600847f01e6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ff34e7dfa5871b9f
  path: data/ingredients/mapped/Andirobin.yaml
  label: Andirobin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Andirobin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Andirobin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Andirobin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ff34e7dfa5871b9f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ff34e7dfa5871b9f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-ff34e7dfa5871b9f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ff34e7dfa5871b9f
evidence:
- evidence_id: ev-e796ff4ea81c1d36
  kind: record_content
  reference: data/ingredients/mapped/Andirobin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[493],"raw_equal":true},"docs_rows":[{"identifier":"cas:6488-63-7","line":495,"mapping_status":"MAPPED","ontology_id":"cas:6488-63-7","preferred_term":"Andirobin"}],"identifier":"cas:6488-63-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:6488-63-7","ontology_label":"Andirobin","ontology_source":"CAS"},"preferred_term":"Andirobin","sssom_rows":[{"data_row":380,"object_id":"cas:6488-63-7","object_label":"Andirobin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Andirobin","synonym_count":0}'
  snapshot_sha256: 7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254
- evidence_id: ev-aa46fa175ad6a0f6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [493]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-aa0e497437419aa8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Andirobin; data-row positions=[380]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":380,"object_id":"cas:6488-63-7","object_label":"Andirobin","other":"CAS:6488-63-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Andirobin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2cf33521963f607b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[495]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:6488-63-7","line":495,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:6488-63-7","preferred_term":"Andirobin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f6c2e99f90c4045d
  kind: prior_review
  reference: reports/yaml_record_review/Andirobin.md
  locator: '`data/ingredients/mapped/Andirobin.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:37; Completeness:50; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9d134d0016d3c7ddd7496db7ae57557ff505c74e973cb7eee89c4600847f01e6
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Andirobin.yaml`, add source-backed\
    \ PubChem\n  chemistry for CAS `6488-63-7` if the curation workflow wants CAS\
    \ fallbacks to\n  be structure-complete where PubChem has a CID."
- evidence_id: ev-0a28646ada707bc2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[258]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254","finding_id":"SEM:6be3a381c97adf446fe8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bbf8fbe56dddbe02
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ff34e7dfa5871b9f
  evidence_ids:
  - ev-e796ff4ea81c1d36
  - ev-aa46fa175ad6a0f6
  - ev-aa0e497437419aa8
  - ev-2cf33521963f607b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-57b2fb38747055b9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ff34e7dfa5871b9f
  evidence_ids:
  - ev-f6c2e99f90c4045d
  - ev-e796ff4ea81c1d36
  - ev-0a28646ada707bc2
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T08:14:22Z;
    reviewed SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254;
    current SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254;
    hash_changed=False. Reports=["reports/yaml_record_review/Andirobin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The direct CAS
    fallback, exact CAS SSSOM row, row-review disposition, aggregate copy, and zero
    CultureMech memberships pass, but PubChem now resolves the CAS and chemistry remains
    unpopulated.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f6c2e99f90c4045d
    - ev-e796ff4ea81c1d36
  - name: legacy-native-ids
    value: '["SEM:6be3a381c97adf446fe8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e796ff4ea81c1d36
    - ev-f6c2e99f90c4045d
    - ev-0a28646ada707bc2
findings:
- finding_id: rec-f-d09bf36869069c6e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-ff34e7dfa5871b9f
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Andirobin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T08:14:22Z;
    reviewed SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254;
    current SHA-256=7392dccf3f7c74483f317e5511dfe12096bcf83ccd2a97b35226a6e9c3946254;
    hash_changed=False. Reports=["reports/yaml_record_review/Andirobin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The direct CAS
    fallback, exact CAS SSSOM row, row-review disposition, aggregate copy, and zero
    CultureMech memberships pass, but PubChem now resolves the CAS and chemistry remains
    unpopulated.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ff34e7dfa5871b9f
  evidence_ids:
  - ev-f6c2e99f90c4045d
  - ev-e796ff4ea81c1d36
  - ev-0a28646ada707bc2
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Andirobin.yaml
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
