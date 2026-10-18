# Per-record structured review: Glucosamine (data/ingredients/mapped/Glucosamine.yaml)

- Review: 20261017T083000Z-glucosamine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucosamine (data/ingredients/mapped/Glucosamine.yaml, record-601c2a763e8995e5, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucosamine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucosamine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-601c2a763e8995e5 | data/ingredients/mapped/Glucosamine.yaml | maintained | Glucosamine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-601c2a763e8995e5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-601c2a763e8995e5 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-601c2a763e8995e5 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-601c2a763e8995e5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-601c2a763e8995e5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:44:41Z; reviewed SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8; current SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8; hash_changed=False. Reports=["reports/yaml_record_review/Glucosamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glucosamine identity passes, but final SSSOM exports a D-form surface string on the generic parent.

## Findings

### rec-f-3c8427573dbc9cda: Historical review coverage and residual narrative: Glucosamine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-601c2a763e8995e5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:44:41Z; reviewed SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8; current SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8; hash_changed=False. Reports=["reports/yaml_record_review/Glucosamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glucosamine identity passes, but final SSSOM exports a D-form surface string on the generic parent.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cd593ab8aaae6d67 | data/ingredients/mapped/Glucosamine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2288],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:5417","line":2290,"mapping_status":"MAPPED","ontology_id":"CHEBI:5417","preferred_term":"Glucosamine"}],"identifier":"CHEBI:5417","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":55,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:5417","ontology_label":"glucosamine","ontology_source":"CHEBI"},"preferred_term":"Glucosamine","sssom_rows":[{"data_row":1306,"object_id":"CHEBI:5417","object_label":"glucosamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucosamine","synonym_count":1} |
| ev-adce47cafbada54b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2288] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-efbc2fb009a79042 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucosamine; data-row positions=[1306] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1306,"object_id":"CHEBI:5417","object_label":"glucosamine","other":"(+)-d-glucosamine","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucosamine","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-56bcfa537e8242b3 | docs/data/mapped_ingredients.csv; CSV lines=[2290] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:5417","line":2290,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:5417","preferred_term":"Glucosamine","total_occurrences":"0"}] |
| ev-ff4873fe14683950 | reports/yaml_record_review/Glucosamine.md; &#96;data/ingredients/mapped/Glucosamine.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:33; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-638b5226d3584663 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[665] | context_only | [{"current_record_sha256":"dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8","finding_id":"SEM:a09dc185143b7f3973ac","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucosamine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucosamine (data/ingredients/mapped/Glucosamine.yaml)'
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
summary: Per-record structured review for Glucosamine (data/ingredients/mapped/Glucosamine.yaml,
  record-601c2a763e8995e5, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucosamine.yaml
    sha256: dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8
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
  - path: reports/yaml_record_review/Glucosamine.md
    sha256: b940d9d8801974befca8aadf87c09c11e23007a27056b8b68e7ccb5c52079f24
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-601c2a763e8995e5
  path: data/ingredients/mapped/Glucosamine.yaml
  label: Glucosamine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucosamine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucosamine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucosamine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-601c2a763e8995e5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-601c2a763e8995e5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-601c2a763e8995e5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-601c2a763e8995e5
evidence:
- evidence_id: ev-cd593ab8aaae6d67
  kind: record_content
  reference: data/ingredients/mapped/Glucosamine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2288],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:5417","line":2290,"mapping_status":"MAPPED","ontology_id":"CHEBI:5417","preferred_term":"Glucosamine"}],"identifier":"CHEBI:5417","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":55,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:5417","ontology_label":"glucosamine","ontology_source":"CHEBI"},"preferred_term":"Glucosamine","sssom_rows":[{"data_row":1306,"object_id":"CHEBI:5417","object_label":"glucosamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucosamine","synonym_count":1}'
  snapshot_sha256: dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8
- evidence_id: ev-adce47cafbada54b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2288]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-efbc2fb009a79042
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucosamine; data-row positions=[1306]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1306,"object_id":"CHEBI:5417","object_label":"glucosamine","other":"(+)-d-glucosamine","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucosamine","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-56bcfa537e8242b3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2290]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:5417","line":2290,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:5417","preferred_term":"Glucosamine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ff4873fe14683950
  kind: prior_review
  reference: reports/yaml_record_review/Glucosamine.md
  locator: '`data/ingredients/mapped/Glucosamine.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:33; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b940d9d8801974befca8aadf87c09c11e23007a27056b8b68e7ccb5c52079f24
  quote: "Recommended Edits:\n- Major: remove or retag `(+)-d-glucosamine` so final\
    \ SSSOM no longer exports a\n  D-specific surface string as a generic glucosamine\
    \ synonym, then regenerate\n  final SSSOM and rerun SSSOM invariants."
- evidence_id: ev-638b5226d3584663
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[665]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8","finding_id":"SEM:a09dc185143b7f3973ac","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a0e7ea8635088668
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-601c2a763e8995e5
  evidence_ids:
  - ev-cd593ab8aaae6d67
  - ev-adce47cafbada54b
  - ev-efbc2fb009a79042
  - ev-56bcfa537e8242b3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4c8d3555f305f41b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-601c2a763e8995e5
  evidence_ids:
  - ev-ff4873fe14683950
  - ev-cd593ab8aaae6d67
  - ev-638b5226d3584663
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:44:41Z;
    reviewed SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8;
    current SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucosamine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact glucosamine
    identity passes, but final SSSOM exports a D-form surface string on the generic
    parent.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ff4873fe14683950
    - ev-cd593ab8aaae6d67
  - name: legacy-native-ids
    value: '["SEM:a09dc185143b7f3973ac"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cd593ab8aaae6d67
    - ev-ff4873fe14683950
    - ev-638b5226d3584663
findings:
- finding_id: rec-f-3c8427573dbc9cda
  issue_key: mim-reconciliation-historical-review-coverage-and-r-601c2a763e8995e5
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glucosamine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:44:41Z;
    reviewed SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8;
    current SHA-256=dd7b0f542305b104f08b74c039ad2fda108796e7235c3eb3825616143ad92da8;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucosamine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact glucosamine
    identity passes, but final SSSOM exports a D-form surface string on the generic
    parent.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-601c2a763e8995e5
  evidence_ids:
  - ev-ff4873fe14683950
  - ev-cd593ab8aaae6d67
  - ev-638b5226d3584663
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucosamine.yaml
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
