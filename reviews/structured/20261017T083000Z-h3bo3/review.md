# Per-record structured review: H3bo3 (data/ingredients/mapped/H3bo3.yaml)

- Review: 20261017T083000Z-h3bo3
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for H3bo3 (data/ingredients/mapped/H3bo3.yaml, record-b5b196e022fb02fc, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/H3bo3.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/H3bo3.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b5b196e022fb02fc | data/ingredients/mapped/H3bo3.yaml | maintained | H3bo3 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b5b196e022fb02fc | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b5b196e022fb02fc | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b5b196e022fb02fc | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b5b196e022fb02fc.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b5b196e022fb02fc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:02:05Z; reviewed SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15; current SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15; hash_changed=False. Reports=["reports/yaml_record_review/H3bo3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact boric-acid identity passes, but malformed duplicate labels are exported as final SSSOM exact synonyms.

## Findings

### rec-f-5f3265cee3ec4362: Historical review coverage and residual narrative: H3bo3

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b5b196e022fb02fc.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:02:05Z; reviewed SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15; current SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15; hash_changed=False. Reports=["reports/yaml_record_review/H3bo3.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact boric-acid identity passes, but malformed duplicate labels are exported as final SSSOM exact synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1dce4bdc45cfc897 | data/ingredients/mapped/H3bo3.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1105],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:33118","line":1107,"mapping_status":"MAPPED","ontology_id":"CHEBI:33118","preferred_term":"H3BO3"}],"identifier":"CHEBI:33118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4212,"edge_count":4212,"occurrences":4216},"occurrence_statistics":{"media_count":4212,"total_occurrences":4216},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:33118","ontology_label":"boric acid","ontology_source":"CHEBI"},"preferred_term":"H3BO3","sssom_rows":[{"data_row":1398,"object_id":"CHEBI:33118","object_label":"boric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H3bo3","synonym_count":14} |
| ev-acaf553572f152f1 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1105] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fe883d29677ee889 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:H3bo3; data-row positions=[1398] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1398,"object_id":"CHEBI:33118","object_label":"boric acid","other":"B(OH)3&#124;[B(OH)3]&#124;boron trihydroxide&#124;orthoboric acid&#124;trihydroxidoboron&#124;H3BO&#124;H3BO3(Baker 0084)&#124;H BO&#124;CAS:10043-35-3","predicate_id":"skos:exactMatch","subject_id":"MIM:H3bo3","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ac8ff6f42d266971 | docs/data/mapped_ingredients.csv; CSV lines=[1107] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:33118","line":1107,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4212","ontology_id":"CHEBI:33118","preferred_term":"H3BO3","total_occurrences":"4216"}] |
| ev-5b262777e7f3d758 | reports/yaml_record_review/H3bo3.md; &#96;data/ingredients/mapped/H3bo3.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:32; Completeness:49; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4aca9482a09ba5a4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[720] | context_only | [{"current_record_sha256":"9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15","finding_id":"SEM:11a9a10d16ceebab99aa","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-h3bo3
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: H3bo3 (data/ingredients/mapped/H3bo3.yaml)'
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
summary: Per-record structured review for H3bo3 (data/ingredients/mapped/H3bo3.yaml,
  record-b5b196e022fb02fc, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/H3bo3.yaml
    sha256: 9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15
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
  - path: reports/yaml_record_review/H3bo3.md
    sha256: 5a1b327f8c1b74f0037223a2182ddf9e60d3a882e5b17c7c4d92dc828c5ff61e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b5b196e022fb02fc
  path: data/ingredients/mapped/H3bo3.yaml
  label: H3bo3
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H3bo3.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/H3bo3.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/H3bo3.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b5b196e022fb02fc
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b5b196e022fb02fc
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b5b196e022fb02fc
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b5b196e022fb02fc
evidence:
- evidence_id: ev-1dce4bdc45cfc897
  kind: record_content
  reference: data/ingredients/mapped/H3bo3.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1105],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:33118","line":1107,"mapping_status":"MAPPED","ontology_id":"CHEBI:33118","preferred_term":"H3BO3"}],"identifier":"CHEBI:33118","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4212,"edge_count":4212,"occurrences":4216},"occurrence_statistics":{"media_count":4212,"total_occurrences":4216},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:33118","ontology_label":"boric
    acid","ontology_source":"CHEBI"},"preferred_term":"H3BO3","sssom_rows":[{"data_row":1398,"object_id":"CHEBI:33118","object_label":"boric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:H3bo3","synonym_count":14}'
  snapshot_sha256: 9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15
- evidence_id: ev-acaf553572f152f1
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1105]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fe883d29677ee889
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:H3bo3; data-row positions=[1398]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1398,"object_id":"CHEBI:33118","object_label":"boric
    acid","other":"B(OH)3|[B(OH)3]|boron trihydroxide|orthoboric acid|trihydroxidoboron|H3BO|H3BO3(Baker
    0084)|H BO|CAS:10043-35-3","predicate_id":"skos:exactMatch","subject_id":"MIM:H3bo3","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ac8ff6f42d266971
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1107]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:33118","line":1107,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4212","ontology_id":"CHEBI:33118","preferred_term":"H3BO3","total_occurrences":"4216"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5b262777e7f3d758
  kind: prior_review
  reference: reports/yaml_record_review/H3bo3.md
  locator: '`data/ingredients/mapped/H3bo3.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:32; Completeness:49; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5a1b327f8c1b74f0037223a2182ddf9e60d3a882e5b17c7c4d92dc828c5ff61e
  quote: "Recommended Edits:\n- Major: suppress or delete `H3BO`, `H3BO3(Baker 0084)`,\
    \ and `H BO` so the\n  final SSSOM `other` column contains only genuine boric-acid\
    \ synonyms and the\n  CAS token."
- evidence_id: ev-4aca9482a09ba5a4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[720]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15","finding_id":"SEM:11a9a10d16ceebab99aa","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-412698de98ea3e09
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b5b196e022fb02fc
  evidence_ids:
  - ev-1dce4bdc45cfc897
  - ev-acaf553572f152f1
  - ev-fe883d29677ee889
  - ev-ac8ff6f42d266971
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6d4aae7c37521dfd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b5b196e022fb02fc
  evidence_ids:
  - ev-5b262777e7f3d758
  - ev-1dce4bdc45cfc897
  - ev-4aca9482a09ba5a4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:02:05Z;
    reviewed SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15;
    current SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15;
    hash_changed=False. Reports=["reports/yaml_record_review/H3bo3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact boric-acid identity
    passes, but malformed duplicate labels are exported as final SSSOM exact synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5b262777e7f3d758
    - ev-1dce4bdc45cfc897
  - name: legacy-native-ids
    value: '["SEM:11a9a10d16ceebab99aa"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1dce4bdc45cfc897
    - ev-5b262777e7f3d758
    - ev-4aca9482a09ba5a4
findings:
- finding_id: rec-f-5f3265cee3ec4362
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b5b196e022fb02fc
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: H3bo3'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:02:05Z;
    reviewed SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15;
    current SHA-256=9ba49752b7773e367ed46e4bcd6333e27ac444b797ba7d8ac0e32cf7baae1c15;
    hash_changed=False. Reports=["reports/yaml_record_review/H3bo3.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact boric-acid identity
    passes, but malformed duplicate labels are exported as final SSSOM exact synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b5b196e022fb02fc
  evidence_ids:
  - ev-5b262777e7f3d758
  - ev-1dce4bdc45cfc897
  - ev-4aca9482a09ba5a4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/H3bo3.yaml
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
