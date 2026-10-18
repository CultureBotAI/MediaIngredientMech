# Per-record structured review: 3-methyl-1-butanol (data/ingredients/mapped/3-methyl-1-butanol.yaml)

- Review: 20261017T083000Z-3-methyl-1-butanol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-methyl-1-butanol (data/ingredients/mapped/3-methyl-1-butanol.yaml, record-d94f211b34972c9b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-methyl-1-butanol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-methyl-1-butanol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d94f211b34972c9b | data/ingredients/mapped/3-methyl-1-butanol.yaml | maintained | 3-methyl-1-butanol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d94f211b34972c9b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d94f211b34972c9b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d94f211b34972c9b | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d94f211b34972c9b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d94f211b34972c9b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:06:04Z; reviewed SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16; current SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16; hash_changed=False. Reports=["reports/yaml_record_review/3-methyl-1-butanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-backed CHEBI identity, chemistry, SSSOM, and aggregate pass; only stale advisory rows remain.

## Findings

### rec-f-c48eb8fc0a636377: Historical review coverage and residual narrative: 3-methyl-1-butanol

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d94f211b34972c9b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:06:04Z; reviewed SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16; current SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16; hash_changed=False. Reports=["reports/yaml_record_review/3-methyl-1-butanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-backed CHEBI identity, chemistry, SSSOM, and aggregate pass; only stale advisory rows remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0b360889ddd829b7 | data/ingredients/mapped/3-methyl-1-butanol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[365],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15837","line":367,"mapping_status":"MAPPED","ontology_id":"CHEBI:15837","preferred_term":"3-methyl-1-butanol"}],"identifier":"CHEBI:15837","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15837","ontology_label":"isoamylol","ontology_source":"CHEBI"},"preferred_term":"3-methyl-1-butanol","sssom_rows":[{"data_row":148,"object_id":"CHEBI:15837","object_label":"isoamylol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-methyl-1-butanol","synonym_count":1} |
| ev-6c72171a8992d966 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [365] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f158ccb2820be6d6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-methyl-1-butanol; data-row positions=[148] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":148,"object_id":"CHEBI:15837","object_label":"isoamylol","other":"3-methylbutan-1-ol&#124;CAS:123-51-3","predicate_id":"skos:exactMatch","subject_id":"MIM:3-methyl-1-butanol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-6ae74246de0374cd | docs/data/mapped_ingredients.csv; CSV lines=[367] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15837","line":367,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15837","preferred_term":"3-methyl-1-butanol","total_occurrences":"0"}] |
| ev-80e605bee046abdb | reports/yaml_record_review/3-methyl-1-butanol.md; &#96;data/ingredients/mapped/3-methyl-1-butanol.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:35; Completeness:52; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c7eb811ca695d9a8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[124] | context_only | [{"current_record_sha256":"f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16","finding_id":"SEM:b4103461c163a1b9653d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-methyl-1-butanol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-methyl-1-butanol (data/ingredients/mapped/3-methyl-1-butanol.yaml)'
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
summary: Per-record structured review for 3-methyl-1-butanol (data/ingredients/mapped/3-methyl-1-butanol.yaml,
  record-d94f211b34972c9b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-methyl-1-butanol.yaml
    sha256: f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/3-methyl-1-butanol.md
    sha256: 10e2db76ad79edfb4bed76488ee0e931ca19ecd7ba04b46892c63fca05312aaf
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d94f211b34972c9b
  path: data/ingredients/mapped/3-methyl-1-butanol.yaml
  label: 3-methyl-1-butanol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-methyl-1-butanol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-methyl-1-butanol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-methyl-1-butanol.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d94f211b34972c9b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d94f211b34972c9b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d94f211b34972c9b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d94f211b34972c9b
evidence:
- evidence_id: ev-0b360889ddd829b7
  kind: record_content
  reference: data/ingredients/mapped/3-methyl-1-butanol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[365],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15837","line":367,"mapping_status":"MAPPED","ontology_id":"CHEBI:15837","preferred_term":"3-methyl-1-butanol"}],"identifier":"CHEBI:15837","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15837","ontology_label":"isoamylol","ontology_source":"CHEBI"},"preferred_term":"3-methyl-1-butanol","sssom_rows":[{"data_row":148,"object_id":"CHEBI:15837","object_label":"isoamylol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-methyl-1-butanol","synonym_count":1}'
  snapshot_sha256: f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16
- evidence_id: ev-6c72171a8992d966
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [365]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f158ccb2820be6d6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-methyl-1-butanol; data-row positions=[148]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":148,"object_id":"CHEBI:15837","object_label":"isoamylol","other":"3-methylbutan-1-ol|CAS:123-51-3","predicate_id":"skos:exactMatch","subject_id":"MIM:3-methyl-1-butanol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6ae74246de0374cd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[367]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15837","line":367,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15837","preferred_term":"3-methyl-1-butanol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-80e605bee046abdb
  kind: prior_review
  reference: reports/yaml_record_review/3-methyl-1-butanol.md
  locator: '`data/ingredients/mapped/3-methyl-1-butanol.yaml`:2; Verdict:4; Identity:10;
    Validation:24; Evidence:35; Completeness:52; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 10e2db76ad79edfb4bed76488ee0e931ca19ecd7ba04b46892c63fca05312aaf
  quote: 'Recommended Edits:

    No YAML edit is required for this record. The stale advisory rows can be ignored

    or refreshed when `mappings/record_research_validation.tsv` is rebuilt.'
- evidence_id: ev-c7eb811ca695d9a8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[124]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16","finding_id":"SEM:b4103461c163a1b9653d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-cf9ed222e92660c3
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d94f211b34972c9b
  evidence_ids:
  - ev-0b360889ddd829b7
  - ev-6c72171a8992d966
  - ev-f158ccb2820be6d6
  - ev-6ae74246de0374cd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ff85037218f9f67b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d94f211b34972c9b
  evidence_ids:
  - ev-80e605bee046abdb
  - ev-0b360889ddd829b7
  - ev-c7eb811ca695d9a8
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:06:04Z;
    reviewed SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16;
    current SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16;
    hash_changed=False. Reports=["reports/yaml_record_review/3-methyl-1-butanol.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CAS-backed
    CHEBI identity, chemistry, SSSOM, and aggregate pass; only stale advisory rows
    remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-80e605bee046abdb
    - ev-0b360889ddd829b7
  - name: legacy-native-ids
    value: '["SEM:b4103461c163a1b9653d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0b360889ddd829b7
    - ev-80e605bee046abdb
    - ev-c7eb811ca695d9a8
findings:
- finding_id: rec-f-c48eb8fc0a636377
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d94f211b34972c9b
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 3-methyl-1-butanol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T06:06:04Z;
    reviewed SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16;
    current SHA-256=f232c416faee481bf2769263f8f52e1bb7140078004765f081cf7102400a2f16;
    hash_changed=False. Reports=["reports/yaml_record_review/3-methyl-1-butanol.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CAS-backed
    CHEBI identity, chemistry, SSSOM, and aggregate pass; only stale advisory rows
    remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d94f211b34972c9b
  evidence_ids:
  - ev-80e605bee046abdb
  - ev-0b360889ddd829b7
  - ev-c7eb811ca695d9a8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-methyl-1-butanol.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
