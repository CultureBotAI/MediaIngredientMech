# Per-record structured review: 2-Acetylpyrrole (data/ingredients/mapped/2-Acetylpyrrole.yaml)

- Review: 20261017T083000Z-2-acetylpyrrole
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-Acetylpyrrole (data/ingredients/mapped/2-Acetylpyrrole.yaml, record-95eb8a603eb6b61a, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-Acetylpyrrole.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-Acetylpyrrole.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-95eb8a603eb6b61a | data/ingredients/mapped/2-Acetylpyrrole.yaml | maintained | 2-Acetylpyrrole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-95eb8a603eb6b61a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-95eb8a603eb6b61a | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-95eb8a603eb6b61a | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-95eb8a603eb6b61a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-95eb8a603eb6b61a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:25:08Z; reviewed SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438; current SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438; hash_changed=False. Reports=["reports/yaml_record_review/2-Acetylpyrrole.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, SSSOM, aggregate, and docs pass; only stale advisory rows remain.

## Findings

### rec-f-f57f84e8185fc738: Historical review coverage and residual narrative: 2-Acetylpyrrole

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-95eb8a603eb6b61a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:25:08Z; reviewed SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438; current SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438; hash_changed=False. Reports=["reports/yaml_record_review/2-Acetylpyrrole.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, SSSOM, aggregate, and docs pass; only stale advisory rows remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-674cd35ad1d56a17 | data/ingredients/mapped/2-Acetylpyrrole.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[305],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:59981","line":307,"mapping_status":"MAPPED","ontology_id":"CHEBI:59981","preferred_term":"2-Acetylpyrrole"}],"identifier":"CHEBI:59981","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:59981","ontology_label":"2-acetylpyrrole","ontology_source":"CHEBI"},"preferred_term":"2-Acetylpyrrole","sssom_rows":[{"data_row":44,"object_id":"CHEBI:59981","object_label":"2-acetylpyrrole","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Acetylpyrrole","synonym_count":0} |
| ev-bc3fab09e4cae4d9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [305] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fadefec248a75e96 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-Acetylpyrrole; data-row positions=[44] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":44,"object_id":"CHEBI:59981","object_label":"2-acetylpyrrole","other":"CAS:1072-83-9","predicate_id":"skos:exactMatch","subject_id":"MIM:2-Acetylpyrrole","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-464f18fd8261f5fa | docs/data/mapped_ingredients.csv; CSV lines=[307] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:59981","line":307,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:59981","preferred_term":"2-Acetylpyrrole","total_occurrences":"0"}] |
| ev-5e438bce285d6dbb | reports/yaml_record_review/2-Acetylpyrrole.md; &#96;data/ingredients/mapped/2-Acetylpyrrole.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:35; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bb8a2ea8fbd5b3ff | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[39] | context_only | [{"current_record_sha256":"68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438","finding_id":"SEM:559c44c65802f2805248","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-acetylpyrrole
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-Acetylpyrrole (data/ingredients/mapped/2-Acetylpyrrole.yaml)'
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
summary: Per-record structured review for 2-Acetylpyrrole (data/ingredients/mapped/2-Acetylpyrrole.yaml,
  record-95eb8a603eb6b61a, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-Acetylpyrrole.yaml
    sha256: 68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438
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
  - path: reports/yaml_record_review/2-Acetylpyrrole.md
    sha256: cffdab726f2fb016d66a0f35d8873cdb3b055699690d6d0cd3cb35c631c999ff
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-95eb8a603eb6b61a
  path: data/ingredients/mapped/2-Acetylpyrrole.yaml
  label: 2-Acetylpyrrole
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Acetylpyrrole.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-Acetylpyrrole.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-Acetylpyrrole.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-95eb8a603eb6b61a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-95eb8a603eb6b61a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-95eb8a603eb6b61a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-95eb8a603eb6b61a
evidence:
- evidence_id: ev-674cd35ad1d56a17
  kind: record_content
  reference: data/ingredients/mapped/2-Acetylpyrrole.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[305],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:59981","line":307,"mapping_status":"MAPPED","ontology_id":"CHEBI:59981","preferred_term":"2-Acetylpyrrole"}],"identifier":"CHEBI:59981","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:59981","ontology_label":"2-acetylpyrrole","ontology_source":"CHEBI"},"preferred_term":"2-Acetylpyrrole","sssom_rows":[{"data_row":44,"object_id":"CHEBI:59981","object_label":"2-acetylpyrrole","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Acetylpyrrole","synonym_count":0}'
  snapshot_sha256: 68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438
- evidence_id: ev-bc3fab09e4cae4d9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [305]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fadefec248a75e96
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-Acetylpyrrole; data-row positions=[44]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":44,"object_id":"CHEBI:59981","object_label":"2-acetylpyrrole","other":"CAS:1072-83-9","predicate_id":"skos:exactMatch","subject_id":"MIM:2-Acetylpyrrole","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-464f18fd8261f5fa
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[307]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:59981","line":307,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:59981","preferred_term":"2-Acetylpyrrole","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5e438bce285d6dbb
  kind: prior_review
  reference: reports/yaml_record_review/2-Acetylpyrrole.md
  locator: '`data/ingredients/mapped/2-Acetylpyrrole.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:35; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cffdab726f2fb016d66a0f35d8873cdb3b055699690d6d0cd3cb35c631c999ff
  quote: "Recommended Edits:\n1. If `mappings/record_research_validation.tsv` is intended\
    \ to be a live queue,\n   regenerate it so stale `CHEBI:59981` uncertainty no\
    \ longer implies pending\n   work.\n2. No YAML, aggregate, SSSOM, or docs identity\
    \ edit is needed for the active\n   `2-Acetylpyrrole` record."
- evidence_id: ev-bb8a2ea8fbd5b3ff
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[39]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438","finding_id":"SEM:559c44c65802f2805248","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-22551ba98e10d459
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-95eb8a603eb6b61a
  evidence_ids:
  - ev-674cd35ad1d56a17
  - ev-bc3fab09e4cae4d9
  - ev-fadefec248a75e96
  - ev-464f18fd8261f5fa
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-71d7a41902a2fd18
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-95eb8a603eb6b61a
  evidence_ids:
  - ev-5e438bce285d6dbb
  - ev-674cd35ad1d56a17
  - ev-bb8a2ea8fbd5b3ff
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:25:08Z;
    reviewed SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438;
    current SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438;
    hash_changed=False. Reports=["reports/yaml_record_review/2-Acetylpyrrole.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, SSSOM, aggregate, and docs pass; only stale advisory rows
    remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5e438bce285d6dbb
    - ev-674cd35ad1d56a17
  - name: legacy-native-ids
    value: '["SEM:559c44c65802f2805248"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-674cd35ad1d56a17
    - ev-5e438bce285d6dbb
    - ev-bb8a2ea8fbd5b3ff
findings:
- finding_id: rec-f-f57f84e8185fc738
  issue_key: mim-reconciliation-historical-review-coverage-and-r-95eb8a603eb6b61a
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 2-Acetylpyrrole'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T05:25:08Z;
    reviewed SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438;
    current SHA-256=68c999e6bca5da4ae9d2296e44cfe958547534debfd03e8bebf9bc21b1c86438;
    hash_changed=False. Reports=["reports/yaml_record_review/2-Acetylpyrrole.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, SSSOM, aggregate, and docs pass; only stale advisory rows
    remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-95eb8a603eb6b61a
  evidence_ids:
  - ev-5e438bce285d6dbb
  - ev-674cd35ad1d56a17
  - ev-bb8a2ea8fbd5b3ff
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Acetylpyrrole.yaml
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
