# Per-record structured review: Mgcl2_X_2_H2o (data/ingredients/mapped/Mgcl2_X_2_H2o.yaml)

- Review: 20261017T083000Z-mgcl2-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mgcl2_X_2_H2o (data/ingredients/mapped/Mgcl2_X_2_H2o.yaml, record-a56b16340bacaa11, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mgcl2_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mgcl2_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a56b16340bacaa11 | data/ingredients/mapped/Mgcl2_X_2_H2o.yaml | maintained | Mgcl2_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a56b16340bacaa11 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a56b16340bacaa11 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a56b16340bacaa11 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a56b16340bacaa11.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a56b16340bacaa11.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:09:28Z; reviewed SHA-256=2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73; current SHA-256=2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73; hash_changed=False. Reports=["reports/yaml_record_review/Mgcl2_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131394 dihydrate identity, CAS, hydrate grounding, and final SSSOM row pass, but MINERAL_SOURCE is still a provisional name-list role.

### Historical provisional-role concern

evidence: concern. Targets: record-a56b16340bacaa11.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e2c7b8419d59df0a: Reassess prediction-only role support: MgCl2 x 2 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-a56b16340bacaa11.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e2c7b8419d59df0a

Reassess prediction-only role support: MgCl2 x 2 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dd6db917987a432b | data/ingredients/mapped/Mgcl2_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1393],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131394","line":1395,"mapping_status":"MAPPED","ontology_id":"CHEBI:131394","preferred_term":"MgCl2 x 2 H2O"}],"identifier":"CHEBI:131394","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131394","ontology_label":"magnesium dichloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"MgCl2 x 2 H2O","sssom_rows":[{"data_row":1861,"object_id":"CHEBI:131394","object_label":"magnesium dichloride dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgcl2_X_2_H2o","synonym_count":3} |
| ev-8d19b7684251c4b2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1393] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-ec633169936901a3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mgcl2_X_2_H2o; data-row positions=[1861] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1861,"object_id":"CHEBI:131394","object_label":"magnesium dichloride dihydrate","other":"MgCl2.2H2O&#124;magnesium chloride dihydrate&#124;CAS:19098-17-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgcl2_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-6122c650396e4846 | docs/data/mapped_ingredients.csv; CSV lines=[1395] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131394","line":1395,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"29","ontology_id":"CHEBI:131394","preferred_term":"MgCl2 x 2 H2O","total_occurrences":"29"}] |
| ev-c5079874eef3b519 | reports/yaml_record_review/Mgcl2_X_2_H2o.md; &#96;data/ingredients/mapped/Mgcl2_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:13; Validation:27; Evidence:34; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-262022c32265ae4c | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[930,1687] | context_only | [{"current_record_sha256":"2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73","finding_id":"SEM:39002ae798e290e2a5e2","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73","finding_id":"SEM:c992263ed8b5859b566c","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-140cdc21324c8c13 | data/ingredients/mapped/Mgcl2_X_2_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1393],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131394","line":1395,"mapping_status":"MAPPED","ontology_id":"CHEBI:131394","preferred_term":"MgCl2 x 2 H2O"}],"identifier":"CHEBI:131394","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131394","ontology_label":"magnesium dichloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"MgCl2 x 2 H2O","sssom_rows":[{"data_row":1861,"object_id":"CHEBI:131394","object_label":"magnesium dichloride dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgcl2_X_2_H2o","synonym_count":3} |
| ev-774fc59d40d713cb | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-e2c7b8419d59df0a] | context_only | Predecessor structured review finding f-e2c7b8419d59df0a in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mgcl2-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mgcl2_X_2_H2o (data/ingredients/mapped/Mgcl2_X_2_H2o.yaml)'
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
summary: Per-record structured review for Mgcl2_X_2_H2o (data/ingredients/mapped/Mgcl2_X_2_H2o.yaml,
  record-a56b16340bacaa11, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
    sha256: 2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Mgcl2_X_2_H2o.md
    sha256: 52063b325f48b94d99f6a0d09f298ac02f733af5c30917d204a3b596aa38fc72
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a56b16340bacaa11
  path: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
  label: Mgcl2_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mgcl2_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a56b16340bacaa11
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-dd6db917987a432b
  - ev-8d19b7684251c4b2
  - ev-ec633169936901a3
  - ev-6122c650396e4846
  - ev-140cdc21324c8c13
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-dd6db917987a432b
  - ev-262022c32265ae4c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-c5079874eef3b519
  - ev-262022c32265ae4c
  - ev-774fc59d40d713cb
evidence:
- evidence_id: ev-dd6db917987a432b
  kind: record_content
  reference: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1393],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131394","line":1395,"mapping_status":"MAPPED","ontology_id":"CHEBI:131394","preferred_term":"MgCl2
    x 2 H2O"}],"identifier":"CHEBI:131394","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131394","ontology_label":"magnesium
    dichloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"MgCl2 x 2 H2O","sssom_rows":[{"data_row":1861,"object_id":"CHEBI:131394","object_label":"magnesium
    dichloride dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgcl2_X_2_H2o","synonym_count":3}'
  snapshot_sha256: 2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73
- evidence_id: ev-8d19b7684251c4b2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1393]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-ec633169936901a3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mgcl2_X_2_H2o; data-row positions=[1861]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1861,"object_id":"CHEBI:131394","object_label":"magnesium
    dichloride dihydrate","other":"MgCl2.2H2O|magnesium chloride dihydrate|CAS:19098-17-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Mgcl2_X_2_H2o","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6122c650396e4846
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1395]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131394","line":1395,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"29","ontology_id":"CHEBI:131394","preferred_term":"MgCl2
    x 2 H2O","total_occurrences":"29"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c5079874eef3b519
  kind: prior_review
  reference: reports/yaml_record_review/Mgcl2_X_2_H2o.md
  locator: '`data/ingredients/mapped/Mgcl2_X_2_H2o.yaml`:2; Verdict:4; Identity:13;
    Validation:27; Evidence:34; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 52063b325f48b94d99f6a0d09f298ac02f733af5c30917d204a3b596aa38fc72
  quote: "Recommended Edits:\n- Major: replace the provisional `MINERAL_SOURCE` role\
    \ with a CultureMech\n  `DATABASE_ENTRY` role assertion if this ingredient was\
    \ imported with a\n  mineral-source role, or remove the role facet from\n  `data/ingredients/mapped/Mgcl2_X_2_H2o.yaml`."
- evidence_id: ev-262022c32265ae4c
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[930,1687]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73","finding_id":"SEM:39002ae798e290e2a5e2","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73","finding_id":"SEM:c992263ed8b5859b566c","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-140cdc21324c8c13
  kind: record_content
  reference: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1393],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131394","line":1395,"mapping_status":"MAPPED","ontology_id":"CHEBI:131394","preferred_term":"MgCl2
    x 2 H2O"}],"identifier":"CHEBI:131394","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":29,"edge_count":29,"occurrences":29},"occurrence_statistics":{"media_count":29,"total_occurrences":29},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131394","ontology_label":"magnesium
    dichloride dihydrate","ontology_source":"CHEBI"},"preferred_term":"MgCl2 x 2 H2O","sssom_rows":[{"data_row":1861,"object_id":"CHEBI:131394","object_label":"magnesium
    dichloride dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mgcl2_X_2_H2o","synonym_count":3}'
  snapshot_sha256: 2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73
- evidence_id: ev-774fc59d40d713cb
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-e2c7b8419d59df0a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e2c7b8419d59df0a in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-f972ffce05cf289e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-dd6db917987a432b
  - ev-8d19b7684251c4b2
  - ev-ec633169936901a3
  - ev-6122c650396e4846
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1b3fdad1cc606b99
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-c5079874eef3b519
  - ev-dd6db917987a432b
  - ev-262022c32265ae4c
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:09:28Z;
    reviewed SHA-256=2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73;
    current SHA-256=2d0d4172d38d9ed333d812ef78b4c5846a0faeaa480494b183b09162d9434f73;
    hash_changed=False. Reports=["reports/yaml_record_review/Mgcl2_X_2_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:131394
    dihydrate identity, CAS, hydrate grounding, and final SSSOM row pass, but MINERAL_SOURCE
    is still a provisional name-list role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c5079874eef3b519
    - ev-dd6db917987a432b
  - name: legacy-native-ids
    value: '["SEM:39002ae798e290e2a5e2","SEM:c992263ed8b5859b566c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dd6db917987a432b
    - ev-c5079874eef3b519
    - ev-262022c32265ae4c
- assessment_id: a-140cdc21324c8c13
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-c5079874eef3b519
  - ev-140cdc21324c8c13
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c5079874eef3b519
    - ev-140cdc21324c8c13
findings:
- finding_id: rec-f-e2c7b8419d59df0a
  issue_key: mim-reconciliation-role-support-a56b16340bacaa11
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: MgCl2 x 2 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a56b16340bacaa11
  evidence_ids:
  - ev-c5079874eef3b519
  - ev-140cdc21324c8c13
  - ev-774fc59d40d713cb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-e2c7b8419d59df0a
actions:
- action_id: rec-action-e2c7b8419d59df0a
  description: 'Reassess prediction-only role support: MgCl2 x 2 H2O'
  finding_ids:
  - rec-f-e2c7b8419d59df0a
  target_ids:
  - record-a56b16340bacaa11
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mgcl2_X_2_H2o.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
