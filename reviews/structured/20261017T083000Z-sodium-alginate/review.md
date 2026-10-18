# Per-record structured review: Sodium_Alginate (data/ingredients/mapped/Sodium_Alginate.yaml)

- Review: 20261017T083000Z-sodium-alginate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Alginate (data/ingredients/mapped/Sodium_Alginate.yaml, record-74c528c67d09dd9e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Alginate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Alginate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-74c528c67d09dd9e | data/ingredients/mapped/Sodium_Alginate.yaml | maintained | Sodium_Alginate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-74c528c67d09dd9e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-74c528c67d09dd9e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-74c528c67d09dd9e | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-74c528c67d09dd9e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-74c528c67d09dd9e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:43:36Z; reviewed SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a; current SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Alginate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:53311 identity, CAS, formula, and solidifying role pass, but kg-microbe related synonyms need review before final SSSOM export.

## Findings

### rec-f-e8396325124d1da9: Historical review coverage and residual narrative: Sodium_Alginate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-74c528c67d09dd9e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:43:36Z; reviewed SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a; current SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Alginate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:53311 identity, CAS, formula, and solidifying role pass, but kg-microbe related synonyms need review before final SSSOM export.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3b2051348b0d6a2b | data/ingredients/mapped/Sodium_Alginate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1817],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53311","line":1819,"mapping_status":"MAPPED","ontology_id":"CHEBI:53311","preferred_term":"Sodium alginate"}],"identifier":"CHEBI:53311","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53311","ontology_label":"sodium alginate","ontology_source":"CHEBI"},"preferred_term":"Sodium alginate","sssom_rows":[{"data_row":2536,"object_id":"CHEBI:53311","object_label":"sodium alginate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Alginate","synonym_count":7} |
| ev-6c76d0b63c0a15eb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1817] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e254c3a6515d6d84 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Alginate; data-row positions=[2536] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2536,"object_id":"CHEBI:53311","object_label":"sodium alginate","other":"Algiline&#124;Algin&#124;Arcrane&#124;Ascophyllum&#124;Sodium polymannuronate&#124;CAS:9005-38-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Alginate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-79086ab4e69e8866 | docs/data/mapped_ingredients.csv; CSV lines=[1819] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:53311","line":1819,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:53311","preferred_term":"Sodium alginate","total_occurrences":"4"}] |
| ev-78516629c5314a10 | reports/yaml_record_review/Sodium_Alginate.md; &#96;data/ingredients/mapped/Sodium_Alginate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b2707651e38daa57 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1206] | context_only | [{"current_record_sha256":"461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a","finding_id":"SEM:691cd808f765e0ea7954","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-alginate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Alginate (data/ingredients/mapped/Sodium_Alginate.yaml)'
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
summary: Per-record structured review for Sodium_Alginate (data/ingredients/mapped/Sodium_Alginate.yaml,
  record-74c528c67d09dd9e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Alginate.yaml
    sha256: 461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a
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
  - path: reports/yaml_record_review/Sodium_Alginate.md
    sha256: 9388cced08b8c757916e5fb7fcaf8b08a88bdd7b59d65c7965775f25150df38a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-74c528c67d09dd9e
  path: data/ingredients/mapped/Sodium_Alginate.yaml
  label: Sodium_Alginate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Alginate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Alginate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Alginate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-74c528c67d09dd9e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-74c528c67d09dd9e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-74c528c67d09dd9e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-74c528c67d09dd9e
evidence:
- evidence_id: ev-3b2051348b0d6a2b
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Alginate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1817],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53311","line":1819,"mapping_status":"MAPPED","ontology_id":"CHEBI:53311","preferred_term":"Sodium
    alginate"}],"identifier":"CHEBI:53311","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53311","ontology_label":"sodium
    alginate","ontology_source":"CHEBI"},"preferred_term":"Sodium alginate","sssom_rows":[{"data_row":2536,"object_id":"CHEBI:53311","object_label":"sodium
    alginate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Alginate","synonym_count":7}'
  snapshot_sha256: 461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a
- evidence_id: ev-6c76d0b63c0a15eb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1817]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e254c3a6515d6d84
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Alginate; data-row positions=[2536]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2536,"object_id":"CHEBI:53311","object_label":"sodium
    alginate","other":"Algiline|Algin|Arcrane|Ascophyllum|Sodium polymannuronate|CAS:9005-38-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Alginate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-79086ab4e69e8866
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1819]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:53311","line":1819,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:53311","preferred_term":"Sodium
    alginate","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-78516629c5314a10
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Alginate.md
  locator: '`data/ingredients/mapped/Sodium_Alginate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9388cced08b8c757916e5fb7fcaf8b08a88bdd7b59d65c7965775f25150df38a
- evidence_id: ev-b2707651e38daa57
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1206]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a","finding_id":"SEM:691cd808f765e0ea7954","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c5c339866d7ea3a5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-74c528c67d09dd9e
  evidence_ids:
  - ev-3b2051348b0d6a2b
  - ev-6c76d0b63c0a15eb
  - ev-e254c3a6515d6d84
  - ev-79086ab4e69e8866
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-66737f4f39851f3c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-74c528c67d09dd9e
  evidence_ids:
  - ev-78516629c5314a10
  - ev-3b2051348b0d6a2b
  - ev-b2707651e38daa57
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:43:36Z;
    reviewed SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a;
    current SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Alginate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:53311 identity, CAS, formula, and solidifying role pass, but kg-microbe
    related synonyms need review before final SSSOM export.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-78516629c5314a10
    - ev-3b2051348b0d6a2b
  - name: legacy-native-ids
    value: '["SEM:691cd808f765e0ea7954"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3b2051348b0d6a2b
    - ev-78516629c5314a10
    - ev-b2707651e38daa57
findings:
- finding_id: rec-f-e8396325124d1da9
  issue_key: mim-reconciliation-historical-review-coverage-and-r-74c528c67d09dd9e
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sodium_Alginate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:43:36Z;
    reviewed SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a;
    current SHA-256=461b8ed9f977ea61f8623face5efb0f388a1e6d8b629800b9a98bae63b5c7d9a;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Alginate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:53311 identity, CAS, formula, and solidifying role pass, but kg-microbe
    related synonyms need review before final SSSOM export.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-74c528c67d09dd9e
  evidence_ids:
  - ev-78516629c5314a10
  - ev-3b2051348b0d6a2b
  - ev-b2707651e38daa57
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Alginate.yaml
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
