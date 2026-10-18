# Per-record structured review: G418_Disulfate_Salt_Solution (data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml)

- Review: 20261017T083000Z-g418-disulfate-salt-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for G418_Disulfate_Salt_Solution (data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml, record-d1dc2b95ca2b41f7, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d1dc2b95ca2b41f7 | data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml | maintained | G418_Disulfate_Salt_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d1dc2b95ca2b41f7 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d1dc2b95ca2b41f7 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d1dc2b95ca2b41f7 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d1dc2b95ca2b41f7.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d1dc2b95ca2b41f7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:19:20Z; reviewed SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce; current SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce; hash_changed=False. Reports=["reports/yaml_record_review/G418_Disulfate_Salt_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS identity resolves G418 disulfate, but the record still denotes a salt solution and exports bare G418.

## Findings

### rec-f-5aad539ae6489777: Historical review coverage and residual narrative: G418_Disulfate_Salt_Solution

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d1dc2b95ca2b41f7.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:19:20Z; reviewed SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce; current SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce; hash_changed=False. Reports=["reports/yaml_record_review/G418_Disulfate_Salt_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS identity resolves G418 disulfate, but the record still denotes a salt solution and exports bare G418.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-15dd6e8c0f968f85 | data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1033],"raw_equal":true},"docs_rows":[{"identifier":"cas:108321-42-2","line":1035,"mapping_status":"MAPPED","ontology_id":"cas:108321-42-2","preferred_term":"G418 disulfate salt solution"}],"identifier":"cas:108321-42-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:108321-42-2","ontology_label":"G418 disulfate salt solution","ontology_source":"CAS"},"preferred_term":"G418 disulfate salt solution","sssom_rows":[{"data_row":1265,"object_id":"cas:108321-42-2","object_label":"G418 disulfate salt solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:G418_Disulfate_Salt_Solution","synonym_count":1} |
| ev-dfd10c95bfd3043c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1033] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-20c7de81c4d17c34 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:G418_Disulfate_Salt_Solution; data-row positions=[1265] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1265,"object_id":"cas:108321-42-2","object_label":"G418 disulfate salt solution","other":"G418&#124;CAS:108321-42-2","predicate_id":"skos:exactMatch","subject_id":"MIM:G418_Disulfate_Salt_Solution","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-84e19a07049395a5 | docs/data/mapped_ingredients.csv; CSV lines=[1035] | supports | Published identity and count rows inspected: [{"identifier":"cas:108321-42-2","line":1035,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:108321-42-2","preferred_term":"G418 disulfate salt solution","total_occurrences":"0"}] |
| ev-98801bf7b83d2cf5 | reports/yaml_record_review/G418_Disulfate_Salt_Solution.md; &#96;data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:36; Completeness:56; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c7c5cdb7864df67e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[643] | context_only | [{"current_record_sha256":"c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce","finding_id":"SEM:6a2322bd046603ecb8da","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-g418-disulfate-salt-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: G418_Disulfate_Salt_Solution (data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml)'
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
summary: Per-record structured review for G418_Disulfate_Salt_Solution (data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml,
  record-d1dc2b95ca2b41f7, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
    sha256: c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce
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
  - path: reports/yaml_record_review/G418_Disulfate_Salt_Solution.md
    sha256: a59a7a2c0fa3e952a0d1cbc5f41af348e824019e3996ea30e9ae4a3a83afba37
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d1dc2b95ca2b41f7
  path: data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
  label: G418_Disulfate_Salt_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d1dc2b95ca2b41f7
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d1dc2b95ca2b41f7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d1dc2b95ca2b41f7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d1dc2b95ca2b41f7
evidence:
- evidence_id: ev-15dd6e8c0f968f85
  kind: record_content
  reference: data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1033],"raw_equal":true},"docs_rows":[{"identifier":"cas:108321-42-2","line":1035,"mapping_status":"MAPPED","ontology_id":"cas:108321-42-2","preferred_term":"G418
    disulfate salt solution"}],"identifier":"cas:108321-42-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:108321-42-2","ontology_label":"G418
    disulfate salt solution","ontology_source":"CAS"},"preferred_term":"G418 disulfate
    salt solution","sssom_rows":[{"data_row":1265,"object_id":"cas:108321-42-2","object_label":"G418
    disulfate salt solution","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:G418_Disulfate_Salt_Solution","synonym_count":1}'
  snapshot_sha256: c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce
- evidence_id: ev-dfd10c95bfd3043c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1033]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-20c7de81c4d17c34
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:G418_Disulfate_Salt_Solution; data-row positions=[1265]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1265,"object_id":"cas:108321-42-2","object_label":"G418
    disulfate salt solution","other":"G418|CAS:108321-42-2","predicate_id":"skos:exactMatch","subject_id":"MIM:G418_Disulfate_Salt_Solution","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-84e19a07049395a5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1035]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:108321-42-2","line":1035,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:108321-42-2","preferred_term":"G418
    disulfate salt solution","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-98801bf7b83d2cf5
  kind: prior_review
  reference: reports/yaml_record_review/G418_Disulfate_Salt_Solution.md
  locator: '`data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml`:2; Verdict:4;
    Identity:11; Validation:23; Evidence:36; Completeness:56; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a59a7a2c0fa3e952a0d1cbc5f41af348e824019e3996ea30e9ae4a3a83afba37
  quote: "Recommended Edits:\n- Major: choose the maintained identity for\n  `data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml`;\
    \ either make the\n  record a local stock-solution mint with G418 disulfate as\
    \ a component or\n  supplied form, or rename it to the disulfate salt and keep\n\
    \  `cas:108321-42-2` as the exact registry identity.\n- Major: remove or retag\
    \ bare `G418` unless the chosen subject is the free-base\n  antibiotic rather\
    \ than the disulfate salt or the stock solution; regenerate\n  final SSSOM and\
    \ rerun SSSOM invariants to prove `other` contains only true\n  same-subject aliases."
- evidence_id: ev-c7c5cdb7864df67e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[643]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce","finding_id":"SEM:6a2322bd046603ecb8da","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9f9f1bf2884f617f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d1dc2b95ca2b41f7
  evidence_ids:
  - ev-15dd6e8c0f968f85
  - ev-dfd10c95bfd3043c
  - ev-20c7de81c4d17c34
  - ev-84e19a07049395a5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-19b966f170198595
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1dc2b95ca2b41f7
  evidence_ids:
  - ev-98801bf7b83d2cf5
  - ev-15dd6e8c0f968f85
  - ev-c7c5cdb7864df67e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:19:20Z;
    reviewed SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce;
    current SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce;
    hash_changed=False. Reports=["reports/yaml_record_review/G418_Disulfate_Salt_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    identity resolves G418 disulfate, but the record still denotes a salt solution
    and exports bare G418.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-98801bf7b83d2cf5
    - ev-15dd6e8c0f968f85
  - name: legacy-native-ids
    value: '["SEM:6a2322bd046603ecb8da"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-15dd6e8c0f968f85
    - ev-98801bf7b83d2cf5
    - ev-c7c5cdb7864df67e
findings:
- finding_id: rec-f-5aad539ae6489777
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d1dc2b95ca2b41f7
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: G418_Disulfate_Salt_Solution'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:19:20Z;
    reviewed SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce;
    current SHA-256=c79dac32d955c66066e6ebfafdb9a8f600571857fb9eb582654c345a890a39ce;
    hash_changed=False. Reports=["reports/yaml_record_review/G418_Disulfate_Salt_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    identity resolves G418 disulfate, but the record still denotes a salt solution
    and exports bare G418.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d1dc2b95ca2b41f7
  evidence_ids:
  - ev-98801bf7b83d2cf5
  - ev-15dd6e8c0f968f85
  - ev-c7c5cdb7864df67e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/G418_Disulfate_Salt_Solution.yaml
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
