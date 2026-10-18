# Per-record structured review: Oat_Flour_B-glucan (data/ingredients/mapped/Oat_Flour_B-glucan.yaml)

- Review: 20261017T083000Z-oat-flour-b-glucan
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Oat_Flour_B-glucan (data/ingredients/mapped/Oat_Flour_B-glucan.yaml, record-da9b8eb5a6624f60, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Oat_Flour_B-glucan.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Oat_Flour_B-glucan.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-da9b8eb5a6624f60 | data/ingredients/mapped/Oat_Flour_B-glucan.yaml | maintained | Oat_Flour_B-glucan |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-da9b8eb5a6624f60 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-da9b8eb5a6624f60 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-da9b8eb5a6624f60 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-da9b8eb5a6624f60.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-da9b8eb5a6624f60.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:26:28Z; reviewed SHA-256=5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d; current SHA-256=5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d; hash_changed=False. Reports=["reports/yaml_record_review/Oat_Flour_B-glucan.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The current exact FOODON:03301312 oat-flour mapping drops the beta-glucan qualifier, and CARBON_SOURCE is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-da9b8eb5a6624f60.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4bfbffde5d0c2c74: Reassess prediction-only role support: Oat flour B-glucan

major / open / confirmed; issue key: mim-reconciliation-role-support-da9b8eb5a6624f60.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4bfbffde5d0c2c74

Reassess prediction-only role support: Oat flour B-glucan

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-de2fc5e6560a98be | data/ingredients/mapped/Oat_Flour_B-glucan.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1585],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03301312","line":1587,"mapping_status":"MAPPED","ontology_id":"FOODON:03301312","preferred_term":"Oat flour B-glucan"}],"identifier":"FOODON:03301312","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"FOODON:03301312","ontology_label":"oat flour","ontology_source":"FOODON"},"preferred_term":"Oat flour B-glucan","sssom_rows":[{"data_row":2135,"object_id":"FOODON:03301312","object_label":"oat flour","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oat_Flour_B-glucan","synonym_count":1} |
| ev-268b63fab0033200 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1585] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5585b3489ac8547a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Oat_Flour_B-glucan; data-row positions=[2135] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2135,"object_id":"FOODON:03301312","object_label":"oat flour","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Oat_Flour_B-glucan","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-fbce49df90097e82 | docs/data/mapped_ingredients.csv; CSV lines=[1587] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03301312","line":1587,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"FOODON:03301312","preferred_term":"Oat flour B-glucan","total_occurrences":"0"}] |
| ev-8db51eac1cfa4371 | reports/yaml_record_review/Oat_Flour_B-glucan.md; &#96;data/ingredients/mapped/Oat_Flour_B-glucan.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:27; Completeness:41; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-282a8fcda7295c37 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1075,1766] | context_only | [{"current_record_sha256":"5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d","finding_id":"SEM:74a0c3fcf2fe4cacfc76","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d","finding_id":"SEM:a508d97fe9d8bdf67ec3","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7b06efb406daf837 | data/ingredients/mapped/Oat_Flour_B-glucan.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1585],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03301312","line":1587,"mapping_status":"MAPPED","ontology_id":"FOODON:03301312","preferred_term":"Oat flour B-glucan"}],"identifier":"FOODON:03301312","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"FOODON:03301312","ontology_label":"oat flour","ontology_source":"FOODON"},"preferred_term":"Oat flour B-glucan","sssom_rows":[{"data_row":2135,"object_id":"FOODON:03301312","object_label":"oat flour","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oat_Flour_B-glucan","synonym_count":1} |
| ev-d656a7131bf88461 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-4bfbffde5d0c2c74] | context_only | Predecessor structured review finding f-4bfbffde5d0c2c74 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-oat-flour-b-glucan
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Oat_Flour_B-glucan (data/ingredients/mapped/Oat_Flour_B-glucan.yaml)'
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
summary: Per-record structured review for Oat_Flour_B-glucan (data/ingredients/mapped/Oat_Flour_B-glucan.yaml,
  record-da9b8eb5a6624f60, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
    sha256: 5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d
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
  - path: reports/yaml_record_review/Oat_Flour_B-glucan.md
    sha256: d38075f9beb9f127addceff7f54aeb8d3d5b220c00e40260f191841c13454996
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-da9b8eb5a6624f60
  path: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
  label: Oat_Flour_B-glucan
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Oat_Flour_B-glucan.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Oat_Flour_B-glucan.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-da9b8eb5a6624f60
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-de2fc5e6560a98be
  - ev-268b63fab0033200
  - ev-5585b3489ac8547a
  - ev-fbce49df90097e82
  - ev-7b06efb406daf837
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-de2fc5e6560a98be
  - ev-282a8fcda7295c37
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-8db51eac1cfa4371
  - ev-282a8fcda7295c37
  - ev-d656a7131bf88461
evidence:
- evidence_id: ev-de2fc5e6560a98be
  kind: record_content
  reference: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1585],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03301312","line":1587,"mapping_status":"MAPPED","ontology_id":"FOODON:03301312","preferred_term":"Oat
    flour B-glucan"}],"identifier":"FOODON:03301312","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"FOODON:03301312","ontology_label":"oat
    flour","ontology_source":"FOODON"},"preferred_term":"Oat flour B-glucan","sssom_rows":[{"data_row":2135,"object_id":"FOODON:03301312","object_label":"oat
    flour","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oat_Flour_B-glucan","synonym_count":1}'
  snapshot_sha256: 5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d
- evidence_id: ev-268b63fab0033200
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1585]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5585b3489ac8547a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Oat_Flour_B-glucan; data-row positions=[2135]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2135,"object_id":"FOODON:03301312","object_label":"oat
    flour","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Oat_Flour_B-glucan","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fbce49df90097e82
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1587]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03301312","line":1587,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"FOODON:03301312","preferred_term":"Oat
    flour B-glucan","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8db51eac1cfa4371
  kind: prior_review
  reference: reports/yaml_record_review/Oat_Flour_B-glucan.md
  locator: '`data/ingredients/mapped/Oat_Flour_B-glucan.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:27; Completeness:41; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d38075f9beb9f127addceff7f54aeb8d3d5b220c00e40260f191841c13454996
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Oat_Flour_B-glucan.yaml`,\
    \ re-curate the source\n  label against the original CultureBotHT row and ontology\
    \ candidates. Use a\n  beta-glucan-specific term if one resolves exactly; otherwise\
    \ mint a\n  `kgmicrobe` fallback for the distinct ingredient and keep `oat flour`\
    \ out of\n  `skos:exactMatch`.\n- Remove or replace `nutritional_roles.CARBON_SOURCE`\
    \ unless source evidence\n  supports the role for this exact ingredient.\n- After\
    \ curation, sync the aggregate record, regenerate\n  `mappings/ingredient_mappings.sssom.tsv`,\
    \ and rerun strict validation,\n  `validate_sssom_invariants.py`, `validate_id_label_correspondence.py`,\
    \ and\n  `check_flat_export_coverage.py`."
- evidence_id: ev-282a8fcda7295c37
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1075,1766]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d","finding_id":"SEM:74a0c3fcf2fe4cacfc76","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d","finding_id":"SEM:a508d97fe9d8bdf67ec3","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7b06efb406daf837
  kind: record_content
  reference: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1585],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03301312","line":1587,"mapping_status":"MAPPED","ontology_id":"FOODON:03301312","preferred_term":"Oat
    flour B-glucan"}],"identifier":"FOODON:03301312","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"FOODON:03301312","ontology_label":"oat
    flour","ontology_source":"FOODON"},"preferred_term":"Oat flour B-glucan","sssom_rows":[{"data_row":2135,"object_id":"FOODON:03301312","object_label":"oat
    flour","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Oat_Flour_B-glucan","synonym_count":1}'
  snapshot_sha256: 5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d
- evidence_id: ev-d656a7131bf88461
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-4bfbffde5d0c2c74]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4bfbffde5d0c2c74 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-e07de05447ede3f0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-de2fc5e6560a98be
  - ev-268b63fab0033200
  - ev-5585b3489ac8547a
  - ev-fbce49df90097e82
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7645825774eb2f64
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-8db51eac1cfa4371
  - ev-de2fc5e6560a98be
  - ev-282a8fcda7295c37
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T07:26:28Z;
    reviewed SHA-256=5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d;
    current SHA-256=5ac0b28a58c475303b3a7c8169241317e60053324189d598d1836c5141240e9d;
    hash_changed=False. Reports=["reports/yaml_record_review/Oat_Flour_B-glucan.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The current
    exact FOODON:03301312 oat-flour mapping drops the beta-glucan qualifier, and CARBON_SOURCE
    is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8db51eac1cfa4371
    - ev-de2fc5e6560a98be
  - name: legacy-native-ids
    value: '["SEM:74a0c3fcf2fe4cacfc76","SEM:a508d97fe9d8bdf67ec3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-de2fc5e6560a98be
    - ev-8db51eac1cfa4371
    - ev-282a8fcda7295c37
- assessment_id: a-7b06efb406daf837
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-8db51eac1cfa4371
  - ev-7b06efb406daf837
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8db51eac1cfa4371
    - ev-7b06efb406daf837
findings:
- finding_id: rec-f-4bfbffde5d0c2c74
  issue_key: mim-reconciliation-role-support-da9b8eb5a6624f60
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Oat flour B-glucan'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-da9b8eb5a6624f60
  evidence_ids:
  - ev-8db51eac1cfa4371
  - ev-7b06efb406daf837
  - ev-d656a7131bf88461
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-4bfbffde5d0c2c74
actions:
- action_id: rec-action-4bfbffde5d0c2c74
  description: 'Reassess prediction-only role support: Oat flour B-glucan'
  finding_ids:
  - rec-f-4bfbffde5d0c2c74
  target_ids:
  - record-da9b8eb5a6624f60
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Oat_Flour_B-glucan.yaml
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
