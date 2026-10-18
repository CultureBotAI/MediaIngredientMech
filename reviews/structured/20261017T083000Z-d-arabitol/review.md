# Per-record structured review: D-arabitol (data/ingredients/mapped/D-arabitol.yaml)

- Review: 20261017T083000Z-d-arabitol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-arabitol (data/ingredients/mapped/D-arabitol.yaml, record-8424077872965184, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-arabitol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-arabitol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8424077872965184 | data/ingredients/mapped/D-arabitol.yaml | maintained | D-arabitol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8424077872965184 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-8424077872965184 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8424077872965184 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8424077872965184.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8424077872965184.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:33:32Z; reviewed SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db; current SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db; hash_changed=False. Reports=["reports/yaml_record_review/D-arabitol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI identity, BacDive source-occurrence count, and final SSSOM payload pass, but the top-level import note is stale.

## Findings

### rec-f-0612f32e5e482115: Historical review coverage and residual narrative: D-arabitol

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-8424077872965184.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:33:32Z; reviewed SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db; current SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db; hash_changed=False. Reports=["reports/yaml_record_review/D-arabitol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The synonym-matched CHEBI identity, BacDive source-occurrence count, and final SSSOM payload pass, but the top-level import note is stale.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bc15696c73e165f5 | data/ingredients/mapped/D-arabitol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[238],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18333","line":240,"mapping_status":"MAPPED","ontology_id":"CHEBI:18333","preferred_term":"D-arabitol"}],"identifier":"CHEBI:18333","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":331,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18333","ontology_label":"D-arabinitol","ontology_source":"CHEBI"},"preferred_term":"D-arabitol","sssom_rows":[{"data_row":925,"object_id":"CHEBI:18333","object_label":"D-arabinitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-arabitol","synonym_count":1} |
| ev-34934896740f44cb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [238] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1da5e61cb179f80c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-arabitol; data-row positions=[925] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":925,"object_id":"CHEBI:18333","object_label":"D-arabinitol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:D-arabitol","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-05"}] |
| ev-5c07ac7efc6ca192 | docs/data/mapped_ingredients.csv; CSV lines=[240] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18333","line":240,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:18333","preferred_term":"D-arabitol","total_occurrences":"0"}] |
| ev-a072c84544ccb21f | reports/yaml_record_review/D-arabitol.md; &#96;data/ingredients/mapped/D-arabitol.yaml&#96;:2; Verdict:4; Identity:13; Validation:28; Evidence:48; Completeness:61; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1666eb6ae951578a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[489] | context_only | [{"current_record_sha256":"a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db","finding_id":"SEM:55f8d6e859478ce20c0b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-arabitol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-arabitol (data/ingredients/mapped/D-arabitol.yaml)'
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
summary: Per-record structured review for D-arabitol (data/ingredients/mapped/D-arabitol.yaml,
  record-8424077872965184, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-arabitol.yaml
    sha256: a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-arabitol.md
    sha256: 1cc13dc1fcc804d6a258e9ab34b63e2473486764c145dbb64fdf27507842e1c4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8424077872965184
  path: data/ingredients/mapped/D-arabitol.yaml
  label: D-arabitol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-arabitol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-arabitol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-arabitol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8424077872965184
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8424077872965184
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8424077872965184
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8424077872965184
evidence:
- evidence_id: ev-bc15696c73e165f5
  kind: record_content
  reference: data/ingredients/mapped/D-arabitol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[238],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18333","line":240,"mapping_status":"MAPPED","ontology_id":"CHEBI:18333","preferred_term":"D-arabitol"}],"identifier":"CHEBI:18333","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":331,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:18333","ontology_label":"D-arabinitol","ontology_source":"CHEBI"},"preferred_term":"D-arabitol","sssom_rows":[{"data_row":925,"object_id":"CHEBI:18333","object_label":"D-arabinitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-arabitol","synonym_count":1}'
  snapshot_sha256: a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db
- evidence_id: ev-34934896740f44cb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [238]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1da5e61cb179f80c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-arabitol; data-row positions=[925]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":925,"object_id":"CHEBI:18333","object_label":"D-arabinitol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:D-arabitol","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-05"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5c07ac7efc6ca192
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[240]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18333","line":240,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:18333","preferred_term":"D-arabitol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a072c84544ccb21f
  kind: prior_review
  reference: reports/yaml_record_review/D-arabitol.md
  locator: '`data/ingredients/mapped/D-arabitol.yaml`:2; Verdict:4; Identity:13; Validation:28;
    Evidence:48; Completeness:61; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1cc13dc1fcc804d6a258e9ab34b63e2473486764c145dbb64fdf27507842e1c4
  quote: "Recommended Edits:\n- Minor: in `data/ingredients/mapped/D-arabitol.yaml`,\
    \ replace the stale\n  import-time top-level `notes` with a short note that this\
    \ was a MicrobeDecoder\n  BacDive utilization import later promoted through the\
    \ ChEBI `D-arabitol`\n  synonym; rerun strict validation afterward."
- evidence_id: ev-1666eb6ae951578a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[489]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db","finding_id":"SEM:55f8d6e859478ce20c0b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9e80854b43c97cc8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8424077872965184
  evidence_ids:
  - ev-bc15696c73e165f5
  - ev-34934896740f44cb
  - ev-1da5e61cb179f80c
  - ev-5c07ac7efc6ca192
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bef85b819427ec14
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8424077872965184
  evidence_ids:
  - ev-a072c84544ccb21f
  - ev-bc15696c73e165f5
  - ev-1666eb6ae951578a
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:33:32Z;
    reviewed SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db;
    current SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db;
    hash_changed=False. Reports=["reports/yaml_record_review/D-arabitol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The synonym-matched
    CHEBI identity, BacDive source-occurrence count, and final SSSOM payload pass,
    but the top-level import note is stale.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a072c84544ccb21f
    - ev-bc15696c73e165f5
  - name: legacy-native-ids
    value: '["SEM:55f8d6e859478ce20c0b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bc15696c73e165f5
    - ev-a072c84544ccb21f
    - ev-1666eb6ae951578a
findings:
- finding_id: rec-f-0612f32e5e482115
  issue_key: mim-reconciliation-historical-review-coverage-and-r-8424077872965184
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: D-arabitol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T13:33:32Z;
    reviewed SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db;
    current SHA-256=a039abf322fba3aa48025d809e603af94f7bd648f18741a37efc16646610d5db;
    hash_changed=False. Reports=["reports/yaml_record_review/D-arabitol.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The synonym-matched
    CHEBI identity, BacDive source-occurrence count, and final SSSOM payload pass,
    but the top-level import note is stale.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8424077872965184
  evidence_ids:
  - ev-a072c84544ccb21f
  - ev-bc15696c73e165f5
  - ev-1666eb6ae951578a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-arabitol.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
