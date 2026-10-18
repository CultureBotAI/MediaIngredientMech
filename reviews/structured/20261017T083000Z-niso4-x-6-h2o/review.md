# Per-record structured review: Niso4_X_6_H2o (data/ingredients/mapped/Niso4_X_6_H2o.yaml)

- Review: 20261017T083000Z-niso4-x-6-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Niso4_X_6_H2o (data/ingredients/mapped/Niso4_X_6_H2o.yaml, record-5e4138c912ba3b4c, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Niso4_X_6_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Niso4_X_6_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5e4138c912ba3b4c | data/ingredients/mapped/Niso4_X_6_H2o.yaml | maintained | Niso4_X_6_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5e4138c912ba3b4c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5e4138c912ba3b4c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5e4138c912ba3b4c | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5e4138c912ba3b4c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5e4138c912ba3b4c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:03:03Z; reviewed SHA-256=98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289; current SHA-256=98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050303Z-Niso4_X_6_H2o.md","reports/yaml_record_review/Niso4_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Niso4_X_6_H2o.md&#96; after the record changed from f3c0ee65025450b953b2f3426700d87ef278a3edd67ff3e1f0b07e728d249a17 to 98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289; preserved the previous minor finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: unknown. Targets: record-5e4138c912ba3b4c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6d236617047c992a: Reassess prediction-only role support: NiSO4 x 6 H2O

minor / deferred / provisional; issue key: mim-reconciliation-role-support-5e4138c912ba3b4c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

Disposition: The current local observation is recorded, but the named source/context or policy decision is still required; no correction is inferred.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c06c3ca905a86233 | data/ingredients/mapped/Niso4_X_6_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1564],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53437","line":1566,"mapping_status":"REJECTED","ontology_id":"CHEBI:53437","preferred_term":"NiSO4 x 6 H2O"}],"identifier":"CHEBI:53437","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":54,"edge_count":54,"occurrences":54},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53437","ontology_label":"nickel sulfate hexahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 6 H2O","sssom_rows":[],"sssom_subject":"MIM:Niso4_X_6_H2o","synonym_count":6} |
| ev-b4a790b84fa08273 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1564] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6d4aaab3a0514334 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Niso4_X_6_H2o; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-636400473188a7e8 | docs/data/mapped_ingredients.csv; CSV lines=[1566] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:53437","line":1566,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:53437","preferred_term":"NiSO4 x 6 H2O","total_occurrences":"0"}] |
| ev-e611c3762b636a94 | reports/yaml_record_review/20261001T050303Z-Niso4_X_6_H2o.md; YAML Record Review: NiSO4 x 6 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-90cf1641ab90a223 | reports/yaml_record_review/Niso4_X_6_H2o.md; &#96;data/ingredients/mapped/Niso4_X_6_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:30; Completeness:46; Recommended Edits:53 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ce9ca54b919572bd | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1062] | context_only | [{"current_record_sha256":"98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289","finding_id":"SEM:40c78da59752cd7b40cd","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |
| ev-61cebb464e4f3c46 | data/ingredients/mapped/Niso4_X_6_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1564],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53437","line":1566,"mapping_status":"REJECTED","ontology_id":"CHEBI:53437","preferred_term":"NiSO4 x 6 H2O"}],"identifier":"CHEBI:53437","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":54,"edge_count":54,"occurrences":54},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53437","ontology_label":"nickel sulfate hexahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 6 H2O","sssom_rows":[],"sssom_subject":"MIM:Niso4_X_6_H2o","synonym_count":6} |
| ev-0320edda73e9ce1b | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-6d236617047c992a] | context_only | Predecessor structured review finding f-6d236617047c992a in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-niso4-x-6-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Niso4_X_6_H2o (data/ingredients/mapped/Niso4_X_6_H2o.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Niso4_X_6_H2o (data/ingredients/mapped/Niso4_X_6_H2o.yaml,
  record-5e4138c912ba3b4c, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Niso4_X_6_H2o.yaml
    sha256: 98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289
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
  - path: reports/yaml_record_review/20261001T050303Z-Niso4_X_6_H2o.md
    sha256: 7e1aa381bf9f5879699dbff23d7c7e4a70e84751f5bc9c1c6a9795877018d813
    role: context
  - path: reports/yaml_record_review/Niso4_X_6_H2o.md
    sha256: 2ec70920e207c45d46cc0f5816cef53690d3e60d6298db7dd5708cfff2d5fbaf
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5e4138c912ba3b4c
  path: data/ingredients/mapped/Niso4_X_6_H2o.yaml
  label: Niso4_X_6_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Niso4_X_6_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Niso4_X_6_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Niso4_X_6_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5e4138c912ba3b4c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-c06c3ca905a86233
  - ev-b4a790b84fa08273
  - ev-6d4aaab3a0514334
  - ev-636400473188a7e8
  - ev-61cebb464e4f3c46
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-c06c3ca905a86233
  - ev-ce9ca54b919572bd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-e611c3762b636a94
  - ev-90cf1641ab90a223
  - ev-ce9ca54b919572bd
  - ev-0320edda73e9ce1b
evidence:
- evidence_id: ev-c06c3ca905a86233
  kind: record_content
  reference: data/ingredients/mapped/Niso4_X_6_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1564],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53437","line":1566,"mapping_status":"REJECTED","ontology_id":"CHEBI:53437","preferred_term":"NiSO4
    x 6 H2O"}],"identifier":"CHEBI:53437","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":54,"edge_count":54,"occurrences":54},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53437","ontology_label":"nickel
    sulfate hexahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 6 H2O","sssom_rows":[],"sssom_subject":"MIM:Niso4_X_6_H2o","synonym_count":6}'
  snapshot_sha256: 98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289
- evidence_id: ev-b4a790b84fa08273
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1564]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6d4aaab3a0514334
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Niso4_X_6_H2o; data-row positions=[]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-636400473188a7e8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1566]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:53437","line":1566,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:53437","preferred_term":"NiSO4
    x 6 H2O","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e611c3762b636a94
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050303Z-Niso4_X_6_H2o.md
  locator: 'YAML Record Review: NiSO4 x 6 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7e1aa381bf9f5879699dbff23d7c7e4a70e84751f5bc9c1c6a9795877018d813
  quote: 'Findings:

    - **minor**: The previous finding set in `reports/yaml_record_review/Niso4_X_6_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The rejected
    duplicate no longer publishes final rows, but stale tombstone fields remain.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Niso4_X_6_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Niso4_X_6_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Niso4_X_6_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-90cf1641ab90a223
  kind: prior_review
  reference: reports/yaml_record_review/Niso4_X_6_H2o.md
  locator: '`data/ingredients/mapped/Niso4_X_6_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:30; Completeness:46; Recommended Edits:53'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2ec70920e207c45d46cc0f5816cef53690d3e60d6298db7dd5708cfff2d5fbaf
  quote: "Recommended Edits:\n- Minor: in `data/ingredients/mapped/Niso4_X_6_H2o.yaml`,\
    \ clear or refresh the\n  stale anhydrous structure, stale active hydrate synonyms,\
    \ and stale\n  `TRACE_ELEMENT` role so the rejected tombstone carries only merge-target\n\
    \  provenance."
- evidence_id: ev-ce9ca54b919572bd
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1062]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289","finding_id":"SEM:40c78da59752cd7b40cd","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-61cebb464e4f3c46
  kind: record_content
  reference: data/ingredients/mapped/Niso4_X_6_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1564],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:53437","line":1566,"mapping_status":"REJECTED","ontology_id":"CHEBI:53437","preferred_term":"NiSO4
    x 6 H2O"}],"identifier":"CHEBI:53437","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":54,"edge_count":54,"occurrences":54},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:53437","ontology_label":"nickel
    sulfate hexahydrate","ontology_source":"CHEBI"},"preferred_term":"NiSO4 x 6 H2O","sssom_rows":[],"sssom_subject":"MIM:Niso4_X_6_H2o","synonym_count":6}'
  snapshot_sha256: 98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289
- evidence_id: ev-0320edda73e9ce1b
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-6d236617047c992a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6d236617047c992a in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-a7c4d39f1f6b7356
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-c06c3ca905a86233
  - ev-b4a790b84fa08273
  - ev-6d4aaab3a0514334
  - ev-636400473188a7e8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ff9486a3b5e1cd61
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-e611c3762b636a94
  - ev-90cf1641ab90a223
  - ev-c06c3ca905a86233
  - ev-ce9ca54b919572bd
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:03:03Z;
    reviewed SHA-256=98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289;
    current SHA-256=98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050303Z-Niso4_X_6_H2o.md","reports/yaml_record_review/Niso4_X_6_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Niso4_X_6_H2o.md` after the record changed from f3c0ee65025450b953b2f3426700d87ef278a3edd67ff3e1f0b07e728d249a17
    to 98b56c307ba25d78a1cef9b0773c5b7aaece65b6d811e0130c706d90bcce2289; preserved
    the previous minor finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e611c3762b636a94
    - ev-90cf1641ab90a223
    - ev-c06c3ca905a86233
  - name: legacy-native-ids
    value: '["SEM:40c78da59752cd7b40cd"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c06c3ca905a86233
    - ev-e611c3762b636a94
    - ev-90cf1641ab90a223
    - ev-ce9ca54b919572bd
- assessment_id: a-61cebb464e4f3c46
  area: evidence
  topic: Historical provisional-role concern
  outcome: unknown
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-e611c3762b636a94
  - ev-90cf1641ab90a223
  - ev-61cebb464e4f3c46
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e611c3762b636a94
    - ev-90cf1641ab90a223
    - ev-61cebb464e4f3c46
findings:
- finding_id: rec-f-6d236617047c992a
  issue_key: mim-reconciliation-role-support-5e4138c912ba3b4c
  category: evidence
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Reassess prediction-only role support: NiSO4 x 6 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5e4138c912ba3b4c
  evidence_ids:
  - ev-e611c3762b636a94
  - ev-90cf1641ab90a223
  - ev-61cebb464e4f3c46
  - ev-0320edda73e9ce1b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Niso4_X_6_H2o.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  disposition_reason: The current local observation is recorded, but the named source/context
    or policy decision is still required; no correction is inferred.
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-6d236617047c992a
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
