# Per-record structured review: Na2_Alpha-ketoglutarate (data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml)

- Review: 20261017T083000Z-na2-alpha-ketoglutarate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2_Alpha-ketoglutarate (data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml, record-159a15f9d3899077, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-159a15f9d3899077 | data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml | maintained | Na2_Alpha-ketoglutarate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-159a15f9d3899077 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-159a15f9d3899077 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-159a15f9d3899077 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-159a15f9d3899077.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-159a15f9d3899077.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:10:17Z; reviewed SHA-256=0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d; current SHA-256=0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d; hash_changed=False. Reports=["reports/yaml_record_review/Na2_Alpha-ketoglutarate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local kgmicrobe.compound identity and CHEBI acid parent rows pass, but both nutrient-role facets are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-159a15f9d3899077.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-de922796868d12b2: Reassess prediction-only role support: Na2 alpha-ketoglutarate

major / open / confirmed; issue key: mim-reconciliation-role-support-159a15f9d3899077.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-de922796868d12b2

Reassess prediction-only role support: Na2 alpha-ketoglutarate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c668a245953536ad | data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1481],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","line":1483,"mapping_status":"MAPPED","ontology_id":"CHEBI:30915","preferred_term":"Na2 alpha-ketoglutarate"}],"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:30915","ontology_label":"2-oxoglutaric acid","ontology_source":"CHEBI"},"preferred_term":"Na2 alpha-ketoglutarate","sssom_rows":[{"data_row":1988,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric acid","predicate_id":"skos:broadMatch"},{"data_row":1989,"object_id":"kgmicrobe.compound:na2_alpha-ketoglutarate","object_label":"Na2 alpha-ketoglutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2_Alpha-ketoglutarate","synonym_count":6} |
| ev-faa543fc9e0833b2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1481] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8a5ce66a08805a9d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2_Alpha-ketoglutarate; data-row positions=[1988, 1989] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1988,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric acid","other":"Na2 \u03b1-ketoglutarate","predicate_id":"skos:broadMatch","subject_id":"MIM:Na2_Alpha-ketoglutarate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1989,"object_id":"kgmicrobe.compound:na2_alpha-ketoglutarate","object_label":"Na2 alpha-ketoglutarate","other":"Na2 \u03b1-ketoglutarate","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2_Alpha-ketoglutarate","validation_method":""}] |
| ev-3a4b7b61f4d9091e | docs/data/mapped_ingredients.csv; CSV lines=[1483] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","line":1483,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:30915","preferred_term":"Na2 alpha-ketoglutarate","total_occurrences":"4"}] |
| ev-fecaf1b521582776 | reports/yaml_record_review/Na2_Alpha-ketoglutarate.md; &#96;data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a8da9d6f7e6f46ec | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[989,1733,1935] | context_only | [{"current_record_sha256":"0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d","finding_id":"SEM:f31a492dd63f2b8f8c90","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d","finding_id":"SEM:a0294f766cd44d283beb","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d","finding_id":"SEM:173a144d790a2a66da48","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-bbc88eaf27c8d251 | data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1481],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","line":1483,"mapping_status":"MAPPED","ontology_id":"CHEBI:30915","preferred_term":"Na2 alpha-ketoglutarate"}],"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:30915","ontology_label":"2-oxoglutaric acid","ontology_source":"CHEBI"},"preferred_term":"Na2 alpha-ketoglutarate","sssom_rows":[{"data_row":1988,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric acid","predicate_id":"skos:broadMatch"},{"data_row":1989,"object_id":"kgmicrobe.compound:na2_alpha-ketoglutarate","object_label":"Na2 alpha-ketoglutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2_Alpha-ketoglutarate","synonym_count":6} |
| ev-384913230440f234 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-de922796868d12b2] | context_only | Predecessor structured review finding f-de922796868d12b2 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2-alpha-ketoglutarate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2_Alpha-ketoglutarate (data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Na2_Alpha-ketoglutarate (data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml,
  record-159a15f9d3899077, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
    sha256: 0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Na2_Alpha-ketoglutarate.md
    sha256: 6d89e8164ba94c5cda3fecb06f2db9664014f963dceabae194fa1f89d7d04c1c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-159a15f9d3899077
  path: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
  label: Na2_Alpha-ketoglutarate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-159a15f9d3899077
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-c668a245953536ad
  - ev-faa543fc9e0833b2
  - ev-8a5ce66a08805a9d
  - ev-3a4b7b61f4d9091e
  - ev-bbc88eaf27c8d251
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-c668a245953536ad
  - ev-a8da9d6f7e6f46ec
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-fecaf1b521582776
  - ev-a8da9d6f7e6f46ec
  - ev-384913230440f234
evidence:
- evidence_id: ev-c668a245953536ad
  kind: record_content
  reference: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1481],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","line":1483,"mapping_status":"MAPPED","ontology_id":"CHEBI:30915","preferred_term":"Na2
    alpha-ketoglutarate"}],"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:30915","ontology_label":"2-oxoglutaric
    acid","ontology_source":"CHEBI"},"preferred_term":"Na2 alpha-ketoglutarate","sssom_rows":[{"data_row":1988,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric
    acid","predicate_id":"skos:broadMatch"},{"data_row":1989,"object_id":"kgmicrobe.compound:na2_alpha-ketoglutarate","object_label":"Na2
    alpha-ketoglutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2_Alpha-ketoglutarate","synonym_count":6}'
  snapshot_sha256: 0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d
- evidence_id: ev-faa543fc9e0833b2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1481]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8a5ce66a08805a9d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2_Alpha-ketoglutarate; data-row positions=[1988, 1989]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1988,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric
    acid","other":"Na2 \u03b1-ketoglutarate","predicate_id":"skos:broadMatch","subject_id":"MIM:Na2_Alpha-ketoglutarate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1989,"object_id":"kgmicrobe.compound:na2_alpha-ketoglutarate","object_label":"Na2
    alpha-ketoglutarate","other":"Na2 \u03b1-ketoglutarate","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2_Alpha-ketoglutarate","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3a4b7b61f4d9091e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1483]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","line":1483,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:30915","preferred_term":"Na2
    alpha-ketoglutarate","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-fecaf1b521582776
  kind: prior_review
  reference: reports/yaml_record_review/Na2_Alpha-ketoglutarate.md
  locator: '`data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6d89e8164ba94c5cda3fecb06f2db9664014f963dceabae194fa1f89d7d04c1c
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml`,\
    \ either\n  remove `CARBON_SOURCE` and `ENERGY_SOURCE` or replace their computational\n\
    \  placeholders with source-backed evidence from maintained occurrence,\n  role-text,\
    \ or literature inputs. Rerun strict validation and the role/output\n  SSSOM checks\
    \ after the role facet changes."
- evidence_id: ev-a8da9d6f7e6f46ec
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[989,1733,1935]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d","finding_id":"SEM:f31a492dd63f2b8f8c90","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d","finding_id":"SEM:a0294f766cd44d283beb","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d","finding_id":"SEM:173a144d790a2a66da48","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-bbc88eaf27c8d251
  kind: record_content
  reference: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1481],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","line":1483,"mapping_status":"MAPPED","ontology_id":"CHEBI:30915","preferred_term":"Na2
    alpha-ketoglutarate"}],"identifier":"kgmicrobe.compound:na2_alpha-ketoglutarate","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:30915","ontology_label":"2-oxoglutaric
    acid","ontology_source":"CHEBI"},"preferred_term":"Na2 alpha-ketoglutarate","sssom_rows":[{"data_row":1988,"object_id":"CHEBI:30915","object_label":"2-oxoglutaric
    acid","predicate_id":"skos:broadMatch"},{"data_row":1989,"object_id":"kgmicrobe.compound:na2_alpha-ketoglutarate","object_label":"Na2
    alpha-ketoglutarate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2_Alpha-ketoglutarate","synonym_count":6}'
  snapshot_sha256: 0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d
- evidence_id: ev-384913230440f234
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-de922796868d12b2]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-de922796868d12b2 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-51bef942c0457ad5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-c668a245953536ad
  - ev-faa543fc9e0833b2
  - ev-8a5ce66a08805a9d
  - ev-3a4b7b61f4d9091e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f1af0079846bc140
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-fecaf1b521582776
  - ev-c668a245953536ad
  - ev-a8da9d6f7e6f46ec
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:10:17Z;
    reviewed SHA-256=0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d;
    current SHA-256=0ee10fb6f9aacd8905e6ef3a4fef393e3d294b12f5c593339a78e5797fe8a58d;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2_Alpha-ketoglutarate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    kgmicrobe.compound identity and CHEBI acid parent rows pass, but both nutrient-role
    facets are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fecaf1b521582776
    - ev-c668a245953536ad
  - name: legacy-native-ids
    value: '["SEM:f31a492dd63f2b8f8c90","SEM:a0294f766cd44d283beb","SEM:173a144d790a2a66da48"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c668a245953536ad
    - ev-fecaf1b521582776
    - ev-a8da9d6f7e6f46ec
- assessment_id: a-bbc88eaf27c8d251
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-fecaf1b521582776
  - ev-bbc88eaf27c8d251
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-fecaf1b521582776
    - ev-bbc88eaf27c8d251
findings:
- finding_id: rec-f-de922796868d12b2
  issue_key: mim-reconciliation-role-support-159a15f9d3899077
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na2 alpha-ketoglutarate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-159a15f9d3899077
  evidence_ids:
  - ev-fecaf1b521582776
  - ev-bbc88eaf27c8d251
  - ev-384913230440f234
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-de922796868d12b2
actions:
- action_id: rec-action-de922796868d12b2
  description: 'Reassess prediction-only role support: Na2 alpha-ketoglutarate'
  finding_ids:
  - rec-f-de922796868d12b2
  target_ids:
  - record-159a15f9d3899077
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2_Alpha-ketoglutarate.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
