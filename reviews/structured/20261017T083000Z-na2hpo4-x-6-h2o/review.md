# Per-record structured review: Na2hpo4_X_6_H2o (data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml)

- Review: 20261017T083000Z-na2hpo4-x-6-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2hpo4_X_6_H2o (data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml, record-06f0e0a068672ab8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-06f0e0a068672ab8 | data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml | maintained | Na2hpo4_X_6_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-06f0e0a068672ab8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-06f0e0a068672ab8 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-06f0e0a068672ab8 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-06f0e0a068672ab8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-06f0e0a068672ab8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:19:32Z; reviewed SHA-256=e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf; current SHA-256=e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf; hash_changed=False. Reports=["reports/yaml_record_review/Na2hpo4_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local hexahydrate identity and final rows pass, but BUFFER is an in-session LLM prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-06f0e0a068672ab8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c8f6ea3f47b388a9: Reassess prediction-only role support: Na2HPO4 x 6 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-06f0e0a068672ab8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c8f6ea3f47b388a9

Reassess prediction-only role support: Na2HPO4 x 6 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8068f49932aa61b2 | data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1491],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","line":1493,"mapping_status":"MAPPED","ontology_id":"CHEBI:34683","preferred_term":"Na2HPO4 x 6 H2O"}],"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Na2HPO4 x 6 H2O","sssom_rows":[{"data_row":2003,"object_id":"CHEBI:34683","object_label":"disodium hydrogenphosphate","predicate_id":"skos:closeMatch"},{"data_row":2004,"object_id":"kgmicrobe.compound:na2hpo4_x_6_h2o","object_label":"Na2HPO4 x 6 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2hpo4_X_6_H2o","synonym_count":12} |
| ev-56a29381a9676c6a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1491] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-47c13bad8b33801b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2hpo4_X_6_H2o; data-row positions=[2003, 2004] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2003,"object_id":"CHEBI:34683","object_label":"disodium hydrogenphosphate","other":"Na2HPO4\u00b76H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Na2hpo4_X_6_H2o","validation_method":""},{"data_row":2004,"object_id":"kgmicrobe.compound:na2hpo4_x_6_h2o","object_label":"Na2HPO4 x 6 H2O","other":"Na2HPO4\u00b76H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2hpo4_X_6_H2o","validation_method":""}] |
| ev-e18ac390f320255c | docs/data/mapped_ingredients.csv; CSV lines=[1493] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","line":1493,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:34683","preferred_term":"Na2HPO4 x 6 H2O","total_occurrences":"5"}] |
| ev-c82b352b5f70dc9e | reports/yaml_record_review/Na2hpo4_X_6_H2o.md; &#96;data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:29; Completeness:46; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7332577afde08ce0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[998,1726] | context_only | [{"current_record_sha256":"e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf","finding_id":"SEM:0fad339b0784bcf5a86d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf","finding_id":"SEM:92546d43becfa2df2cdf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2f8898b3d04c9be8 | data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1491],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","line":1493,"mapping_status":"MAPPED","ontology_id":"CHEBI:34683","preferred_term":"Na2HPO4 x 6 H2O"}],"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Na2HPO4 x 6 H2O","sssom_rows":[{"data_row":2003,"object_id":"CHEBI:34683","object_label":"disodium hydrogenphosphate","predicate_id":"skos:closeMatch"},{"data_row":2004,"object_id":"kgmicrobe.compound:na2hpo4_x_6_h2o","object_label":"Na2HPO4 x 6 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2hpo4_X_6_H2o","synonym_count":12} |
| ev-b541cd93c6193c80 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-c8f6ea3f47b388a9] | context_only | Predecessor structured review finding f-c8f6ea3f47b388a9 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2hpo4-x-6-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2hpo4_X_6_H2o (data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml)'
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
summary: Per-record structured review for Na2hpo4_X_6_H2o (data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml,
  record-06f0e0a068672ab8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
    sha256: e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf
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
  - path: reports/yaml_record_review/Na2hpo4_X_6_H2o.md
    sha256: 2c393d4ab15a442704f4773f98eb85b85eb9d04738b213b5644cd05054f969bf
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-06f0e0a068672ab8
  path: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
  label: Na2hpo4_X_6_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-06f0e0a068672ab8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-8068f49932aa61b2
  - ev-56a29381a9676c6a
  - ev-47c13bad8b33801b
  - ev-e18ac390f320255c
  - ev-2f8898b3d04c9be8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-8068f49932aa61b2
  - ev-7332577afde08ce0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-c82b352b5f70dc9e
  - ev-7332577afde08ce0
  - ev-b541cd93c6193c80
evidence:
- evidence_id: ev-8068f49932aa61b2
  kind: record_content
  reference: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1491],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","line":1493,"mapping_status":"MAPPED","ontology_id":"CHEBI:34683","preferred_term":"Na2HPO4
    x 6 H2O"}],"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium
    hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Na2HPO4 x 6 H2O","sssom_rows":[{"data_row":2003,"object_id":"CHEBI:34683","object_label":"disodium
    hydrogenphosphate","predicate_id":"skos:closeMatch"},{"data_row":2004,"object_id":"kgmicrobe.compound:na2hpo4_x_6_h2o","object_label":"Na2HPO4
    x 6 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2hpo4_X_6_H2o","synonym_count":12}'
  snapshot_sha256: e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf
- evidence_id: ev-56a29381a9676c6a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1491]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-47c13bad8b33801b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2hpo4_X_6_H2o; data-row positions=[2003, 2004]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2003,"object_id":"CHEBI:34683","object_label":"disodium
    hydrogenphosphate","other":"Na2HPO4\u00b76H2O","predicate_id":"skos:closeMatch","subject_id":"MIM:Na2hpo4_X_6_H2o","validation_method":""},{"data_row":2004,"object_id":"kgmicrobe.compound:na2hpo4_x_6_h2o","object_label":"Na2HPO4
    x 6 H2O","other":"Na2HPO4\u00b76H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Na2hpo4_X_6_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e18ac390f320255c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1493]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","line":1493,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:34683","preferred_term":"Na2HPO4
    x 6 H2O","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c82b352b5f70dc9e
  kind: prior_review
  reference: reports/yaml_record_review/Na2hpo4_X_6_H2o.md
  locator: '`data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:29; Completeness:46; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2c393d4ab15a442704f4773f98eb85b85eb9d04738b213b5644cd05054f969bf
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml`,\
    \ either remove\n  `physicochemical_roles.BUFFER` or replace its LLM placeholder\
    \ with\n  source-backed evidence from maintained role-text or literature inputs.\
    \ Rerun\n  strict validation and the role/output SSSOM checks after the role facet\n\
    \  change."
- evidence_id: ev-7332577afde08ce0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[998,1726]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf","finding_id":"SEM:0fad339b0784bcf5a86d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf","finding_id":"SEM:92546d43becfa2df2cdf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2f8898b3d04c9be8
  kind: record_content
  reference: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1491],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","line":1493,"mapping_status":"MAPPED","ontology_id":"CHEBI:34683","preferred_term":"Na2HPO4
    x 6 H2O"}],"identifier":"kgmicrobe.compound:na2hpo4_x_6_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:34683","ontology_label":"disodium
    hydrogenphosphate","ontology_source":"CHEBI"},"preferred_term":"Na2HPO4 x 6 H2O","sssom_rows":[{"data_row":2003,"object_id":"CHEBI:34683","object_label":"disodium
    hydrogenphosphate","predicate_id":"skos:closeMatch"},{"data_row":2004,"object_id":"kgmicrobe.compound:na2hpo4_x_6_h2o","object_label":"Na2HPO4
    x 6 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na2hpo4_X_6_H2o","synonym_count":12}'
  snapshot_sha256: e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf
- evidence_id: ev-b541cd93c6193c80
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-c8f6ea3f47b388a9]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c8f6ea3f47b388a9 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-2076c0a74528c0af
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-8068f49932aa61b2
  - ev-56a29381a9676c6a
  - ev-47c13bad8b33801b
  - ev-e18ac390f320255c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7d03664fb372ae0a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-c82b352b5f70dc9e
  - ev-8068f49932aa61b2
  - ev-7332577afde08ce0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T05:19:32Z;
    reviewed SHA-256=e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf;
    current SHA-256=e4a2756db9e7876f8766f868af533266acc86bd21db5c1d79559048c717acebf;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2hpo4_X_6_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    hexahydrate identity and final rows pass, but BUFFER is an in-session LLM prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c82b352b5f70dc9e
    - ev-8068f49932aa61b2
  - name: legacy-native-ids
    value: '["SEM:0fad339b0784bcf5a86d","SEM:92546d43becfa2df2cdf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8068f49932aa61b2
    - ev-c82b352b5f70dc9e
    - ev-7332577afde08ce0
- assessment_id: a-2f8898b3d04c9be8
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-c82b352b5f70dc9e
  - ev-2f8898b3d04c9be8
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c82b352b5f70dc9e
    - ev-2f8898b3d04c9be8
findings:
- finding_id: rec-f-c8f6ea3f47b388a9
  issue_key: mim-reconciliation-role-support-06f0e0a068672ab8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na2HPO4 x 6 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-06f0e0a068672ab8
  evidence_ids:
  - ev-c82b352b5f70dc9e
  - ev-2f8898b3d04c9be8
  - ev-b541cd93c6193c80
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-c8f6ea3f47b388a9
actions:
- action_id: rec-action-c8f6ea3f47b388a9
  description: 'Reassess prediction-only role support: Na2HPO4 x 6 H2O'
  finding_ids:
  - rec-f-c8f6ea3f47b388a9
  target_ids:
  - record-06f0e0a068672ab8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2hpo4_X_6_H2o.yaml
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
