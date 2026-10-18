# Per-record structured review: Resazurin (data/ingredients/mapped/Resazurin.yaml)

- Review: 20261017T083000Z-resazurin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Resazurin (data/ingredients/mapped/Resazurin.yaml, record-43756d8d542b67b0, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Resazurin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Resazurin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-43756d8d542b67b0 | data/ingredients/mapped/Resazurin.yaml | maintained | Resazurin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-43756d8d542b67b0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-43756d8d542b67b0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-43756d8d542b67b0 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-43756d8d542b67b0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-43756d8d542b67b0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:53:10Z; reviewed SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a; current SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a; hash_changed=False. Reports=["reports/yaml_record_review/Resazurin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:8806 identity passes, but final SSSOM exports salt and concentration strings as other.

## Findings

### rec-f-9f72cde4c4eb9af6: Historical review coverage and residual narrative: Resazurin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-43756d8d542b67b0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:53:10Z; reviewed SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a; current SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a; hash_changed=False. Reports=["reports/yaml_record_review/Resazurin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:8806 identity passes, but final SSSOM exports salt and concentration strings as other.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9e595dc45352c194 | data/ingredients/mapped/Resazurin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1747],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:8806","line":1749,"mapping_status":"MAPPED","ontology_id":"CHEBI:8806","preferred_term":"Resazurin"}],"identifier":"CHEBI:8806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3671,"edge_count":3671,"occurrences":3671},"occurrence_statistics":{"media_count":3671,"total_occurrences":3671},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:8806","ontology_label":"Resazurin","ontology_source":"CHEBI"},"preferred_term":"Resazurin","sssom_rows":[{"data_row":2416,"object_id":"CHEBI:8806","object_label":"Resazurin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Resazurin","synonym_count":14} |
| ev-bc2b305c6137cca4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1747] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2577df62e3aa9706 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Resazurin; data-row positions=[2416] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2416,"object_id":"CHEBI:8806","object_label":"Resazurin","other":"Sodium resazurin&#124;resazurin sodium salt&#124;Sodium resazurin (0.1% w/v)&#124;Resazurin (0,1%)&#124;Resazurin (0.1%)&#124;Resazurin (0.02%)&#124;Resazurin (0.025%)&#124;Resazurin (0.1% w/v in water)&#124;Resazurin (1 mg/L)&#124;CAS:550-82-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Resazurin","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d45766286485aab9 | docs/data/mapped_ingredients.csv; CSV lines=[1749] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:8806","line":1749,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3671","ontology_id":"CHEBI:8806","preferred_term":"Resazurin","total_occurrences":"3671"}] |
| ev-b0a41c9189494159 | reports/yaml_record_review/Resazurin.md; &#96;data/ingredients/mapped/Resazurin.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6dc5a45081e289a1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1167] | context_only | [{"current_record_sha256":"b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a","finding_id":"SEM:0336734e1b72ab7b803d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-resazurin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Resazurin (data/ingredients/mapped/Resazurin.yaml)'
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
summary: Per-record structured review for Resazurin (data/ingredients/mapped/Resazurin.yaml,
  record-43756d8d542b67b0, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Resazurin.yaml
    sha256: b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a
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
  - path: reports/yaml_record_review/Resazurin.md
    sha256: 10846116c73b7aecc48ec1dd61932988185e9878fcbd6aa6233cb30e76d98998
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-43756d8d542b67b0
  path: data/ingredients/mapped/Resazurin.yaml
  label: Resazurin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Resazurin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Resazurin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Resazurin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-43756d8d542b67b0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-43756d8d542b67b0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-43756d8d542b67b0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-43756d8d542b67b0
evidence:
- evidence_id: ev-9e595dc45352c194
  kind: record_content
  reference: data/ingredients/mapped/Resazurin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1747],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:8806","line":1749,"mapping_status":"MAPPED","ontology_id":"CHEBI:8806","preferred_term":"Resazurin"}],"identifier":"CHEBI:8806","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3671,"edge_count":3671,"occurrences":3671},"occurrence_statistics":{"media_count":3671,"total_occurrences":3671},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:8806","ontology_label":"Resazurin","ontology_source":"CHEBI"},"preferred_term":"Resazurin","sssom_rows":[{"data_row":2416,"object_id":"CHEBI:8806","object_label":"Resazurin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Resazurin","synonym_count":14}'
  snapshot_sha256: b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a
- evidence_id: ev-bc2b305c6137cca4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1747]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2577df62e3aa9706
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Resazurin; data-row positions=[2416]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2416,"object_id":"CHEBI:8806","object_label":"Resazurin","other":"Sodium
    resazurin|resazurin sodium salt|Sodium resazurin (0.1% w/v)|Resazurin (0,1%)|Resazurin
    (0.1%)|Resazurin (0.02%)|Resazurin (0.025%)|Resazurin (0.1% w/v in water)|Resazurin
    (1 mg/L)|CAS:550-82-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Resazurin","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d45766286485aab9
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1749]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:8806","line":1749,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3671","ontology_id":"CHEBI:8806","preferred_term":"Resazurin","total_occurrences":"3671"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b0a41c9189494159
  kind: prior_review
  reference: reports/yaml_record_review/Resazurin.md
  locator: '`data/ingredients/mapped/Resazurin.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 10846116c73b7aecc48ec1dd61932988185e9878fcbd6aa6233cb30e76d98998
- evidence_id: ev-6dc5a45081e289a1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1167]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a","finding_id":"SEM:0336734e1b72ab7b803d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e9ac0ad943bd3044
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-43756d8d542b67b0
  evidence_ids:
  - ev-9e595dc45352c194
  - ev-bc2b305c6137cca4
  - ev-2577df62e3aa9706
  - ev-d45766286485aab9
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a4e6ed6fa854d822
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43756d8d542b67b0
  evidence_ids:
  - ev-b0a41c9189494159
  - ev-9e595dc45352c194
  - ev-6dc5a45081e289a1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:53:10Z;
    reviewed SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a;
    current SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a;
    hash_changed=False. Reports=["reports/yaml_record_review/Resazurin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:8806
    identity passes, but final SSSOM exports salt and concentration strings as other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b0a41c9189494159
    - ev-9e595dc45352c194
  - name: legacy-native-ids
    value: '["SEM:0336734e1b72ab7b803d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9e595dc45352c194
    - ev-b0a41c9189494159
    - ev-6dc5a45081e289a1
findings:
- finding_id: rec-f-9f72cde4c4eb9af6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-43756d8d542b67b0
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Resazurin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T11:53:10Z;
    reviewed SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a;
    current SHA-256=b7aee64c3b58a3c1c0f2bb01c7a75e035dbd9a7e036828872a5513b5b5bac59a;
    hash_changed=False. Reports=["reports/yaml_record_review/Resazurin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:8806
    identity passes, but final SSSOM exports salt and concentration strings as other.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43756d8d542b67b0
  evidence_ids:
  - ev-b0a41c9189494159
  - ev-9e595dc45352c194
  - ev-6dc5a45081e289a1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Resazurin.yaml
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
