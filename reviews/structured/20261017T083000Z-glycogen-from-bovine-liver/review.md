# Per-record structured review: Glycogen_From_Bovine_Liver (data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml)

- Review: 20261017T083000Z-glycogen-from-bovine-liver
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycogen_From_Bovine_Liver (data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml, record-08a5656509adb992, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-08a5656509adb992 | data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml | maintained | Glycogen_From_Bovine_Liver |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-08a5656509adb992 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-08a5656509adb992 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-08a5656509adb992 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-08a5656509adb992.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-08a5656509adb992.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:20:56Z; reviewed SHA-256=f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37; current SHA-256=f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37; hash_changed=False. Reports=["reports/yaml_record_review/Glycogen_From_Bovine_Liver.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The narrow glycogen parent and registry rows pass, but CARBON_SOURCE is computational and PubChem structure fields over-specify the polymer.

### Historical provisional-role concern

evidence: concern. Targets: record-08a5656509adb992.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-aaf7c8e19ffb99cd: Reassess prediction-only role support: Glycogen from bovine liver

major / open / confirmed; issue key: mim-reconciliation-role-support-08a5656509adb992.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-aaf7c8e19ffb99cd

Reassess prediction-only role support: Glycogen from bovine liver

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b9a701460f6c157b | data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1078],"raw_equal":true},"docs_rows":[{"identifier":"cas:9005-79-2","line":1080,"mapping_status":"MAPPED","ontology_id":"CHEBI:28087","preferred_term":"Glycogen from bovine liver"}],"identifier":"cas:9005-79-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:28087","ontology_label":"glycogen","ontology_source":"CHEBI"},"preferred_term":"Glycogen from bovine liver","sssom_rows":[{"data_row":1345,"object_id":"CHEBI:28087","object_label":"glycogen","predicate_id":"skos:broadMatch"},{"data_row":1346,"object_id":"cas:9005-79-2","object_label":"Glycogen from bovine liver","predicate_id":"skos:exactMatch"},{"data_row":1347,"object_id":"kgmicrobe.compound:glycogen_from_bovine_liver","object_label":"Glycogen from bovine liver","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycogen_From_Bovine_Liver","synonym_count":0} |
| ev-dca7321f6c439b9c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1078] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7b85d039d5d8daa6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycogen_From_Bovine_Liver; data-row positions=[1345, 1346, 1347] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1345,"object_id":"CHEBI:28087","object_label":"glycogen","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Glycogen_From_Bovine_Liver","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1346,"object_id":"cas:9005-79-2","object_label":"Glycogen from bovine liver","other":"CAS:9005-79-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycogen_From_Bovine_Liver","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1347,"object_id":"kgmicrobe.compound:glycogen_from_bovine_liver","object_label":"Glycogen from bovine liver","other":"CAS:9005-79-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycogen_From_Bovine_Liver","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-14d77579bea526e1 | docs/data/mapped_ingredients.csv; CSV lines=[1080] | supports | Published identity and count rows inspected: [{"identifier":"cas:9005-79-2","line":1080,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28087","preferred_term":"Glycogen from bovine liver","total_occurrences":"0"}] |
| ev-a7ef598b781b3f73 | reports/yaml_record_review/Glycogen_From_Bovine_Liver.md; &#96;data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:30; Completeness:61; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b6d883c87f2103a1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[696,1529] | context_only | [{"current_record_sha256":"f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37","finding_id":"SEM:b90730c5d701910ba350","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37","finding_id":"SEM:2830348ca2b53fb99300","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-6705c491b76291f9 | data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1078],"raw_equal":true},"docs_rows":[{"identifier":"cas:9005-79-2","line":1080,"mapping_status":"MAPPED","ontology_id":"CHEBI:28087","preferred_term":"Glycogen from bovine liver"}],"identifier":"cas:9005-79-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:28087","ontology_label":"glycogen","ontology_source":"CHEBI"},"preferred_term":"Glycogen from bovine liver","sssom_rows":[{"data_row":1345,"object_id":"CHEBI:28087","object_label":"glycogen","predicate_id":"skos:broadMatch"},{"data_row":1346,"object_id":"cas:9005-79-2","object_label":"Glycogen from bovine liver","predicate_id":"skos:exactMatch"},{"data_row":1347,"object_id":"kgmicrobe.compound:glycogen_from_bovine_liver","object_label":"Glycogen from bovine liver","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycogen_From_Bovine_Liver","synonym_count":0} |
| ev-951e9147f15ee3cc | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-aaf7c8e19ffb99cd] | context_only | Predecessor structured review finding f-aaf7c8e19ffb99cd in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycogen-from-bovine-liver
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycogen_From_Bovine_Liver (data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml)'
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
summary: Per-record structured review for Glycogen_From_Bovine_Liver (data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml,
  record-08a5656509adb992, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
    sha256: f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37
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
  - path: reports/yaml_record_review/Glycogen_From_Bovine_Liver.md
    sha256: 0825626b834708062405fc5ad207036ec3bac61050749d9869b0975715c41fb0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-08a5656509adb992
  path: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
  label: Glycogen_From_Bovine_Liver
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-08a5656509adb992
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-b9a701460f6c157b
  - ev-dca7321f6c439b9c
  - ev-7b85d039d5d8daa6
  - ev-14d77579bea526e1
  - ev-6705c491b76291f9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-b9a701460f6c157b
  - ev-b6d883c87f2103a1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-a7ef598b781b3f73
  - ev-b6d883c87f2103a1
  - ev-951e9147f15ee3cc
evidence:
- evidence_id: ev-b9a701460f6c157b
  kind: record_content
  reference: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1078],"raw_equal":true},"docs_rows":[{"identifier":"cas:9005-79-2","line":1080,"mapping_status":"MAPPED","ontology_id":"CHEBI:28087","preferred_term":"Glycogen
    from bovine liver"}],"identifier":"cas:9005-79-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:28087","ontology_label":"glycogen","ontology_source":"CHEBI"},"preferred_term":"Glycogen
    from bovine liver","sssom_rows":[{"data_row":1345,"object_id":"CHEBI:28087","object_label":"glycogen","predicate_id":"skos:broadMatch"},{"data_row":1346,"object_id":"cas:9005-79-2","object_label":"Glycogen
    from bovine liver","predicate_id":"skos:exactMatch"},{"data_row":1347,"object_id":"kgmicrobe.compound:glycogen_from_bovine_liver","object_label":"Glycogen
    from bovine liver","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycogen_From_Bovine_Liver","synonym_count":0}'
  snapshot_sha256: f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37
- evidence_id: ev-dca7321f6c439b9c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1078]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7b85d039d5d8daa6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycogen_From_Bovine_Liver; data-row positions=[1345, 1346,
    1347]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1345,"object_id":"CHEBI:28087","object_label":"glycogen","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Glycogen_From_Bovine_Liver","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1346,"object_id":"cas:9005-79-2","object_label":"Glycogen
    from bovine liver","other":"CAS:9005-79-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycogen_From_Bovine_Liver","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1347,"object_id":"kgmicrobe.compound:glycogen_from_bovine_liver","object_label":"Glycogen
    from bovine liver","other":"CAS:9005-79-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycogen_From_Bovine_Liver","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-14d77579bea526e1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1080]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:9005-79-2","line":1080,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28087","preferred_term":"Glycogen
    from bovine liver","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a7ef598b781b3f73
  kind: prior_review
  reference: reports/yaml_record_review/Glycogen_From_Bovine_Liver.md
  locator: '`data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml`:2; Verdict:4;
    Identity:12; Validation:23; Evidence:30; Completeness:61; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0825626b834708062405fc5ad207036ec3bac61050749d9869b0975715c41fb0
  quote: "Recommended Edits:\n- Major: remove or replace `chemical_properties.molecular_formula`,\n\
    \  `chemical_properties.inchi`, `chemical_properties.smiles`, and\n  `chemical_properties.pubchem_cid`\
    \ in\n  `data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml` unless inspected\n\
    \  evidence proves PubChem CID `439177` is a valid representative structure for\n\
    \  bovine-liver glycogen in this corpus.\n- Major: remove `nutritional_roles.CARBON_SOURCE`,\
    \ or replace its provisional\n  name-pattern evidence with inspected source evidence\
    \ that specifically\n  supports bovine-liver glycogen as a carbon source."
- evidence_id: ev-b6d883c87f2103a1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[696,1529]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37","finding_id":"SEM:b90730c5d701910ba350","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37","finding_id":"SEM:2830348ca2b53fb99300","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-6705c491b76291f9
  kind: record_content
  reference: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1078],"raw_equal":true},"docs_rows":[{"identifier":"cas:9005-79-2","line":1080,"mapping_status":"MAPPED","ontology_id":"CHEBI:28087","preferred_term":"Glycogen
    from bovine liver"}],"identifier":"cas:9005-79-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:28087","ontology_label":"glycogen","ontology_source":"CHEBI"},"preferred_term":"Glycogen
    from bovine liver","sssom_rows":[{"data_row":1345,"object_id":"CHEBI:28087","object_label":"glycogen","predicate_id":"skos:broadMatch"},{"data_row":1346,"object_id":"cas:9005-79-2","object_label":"Glycogen
    from bovine liver","predicate_id":"skos:exactMatch"},{"data_row":1347,"object_id":"kgmicrobe.compound:glycogen_from_bovine_liver","object_label":"Glycogen
    from bovine liver","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycogen_From_Bovine_Liver","synonym_count":0}'
  snapshot_sha256: f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37
- evidence_id: ev-951e9147f15ee3cc
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-aaf7c8e19ffb99cd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-aaf7c8e19ffb99cd in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-bd1cc96d5fe2718e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-b9a701460f6c157b
  - ev-dca7321f6c439b9c
  - ev-7b85d039d5d8daa6
  - ev-14d77579bea526e1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6392495f8e765bf3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-a7ef598b781b3f73
  - ev-b9a701460f6c157b
  - ev-b6d883c87f2103a1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:20:56Z;
    reviewed SHA-256=f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37;
    current SHA-256=f128118de1d8e776a928c8579b3689c24ca535aec9a41f00913550211c883d37;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycogen_From_Bovine_Liver.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The narrow
    glycogen parent and registry rows pass, but CARBON_SOURCE is computational and
    PubChem structure fields over-specify the polymer.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a7ef598b781b3f73
    - ev-b9a701460f6c157b
  - name: legacy-native-ids
    value: '["SEM:b90730c5d701910ba350","SEM:2830348ca2b53fb99300"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b9a701460f6c157b
    - ev-a7ef598b781b3f73
    - ev-b6d883c87f2103a1
- assessment_id: a-6705c491b76291f9
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-a7ef598b781b3f73
  - ev-6705c491b76291f9
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a7ef598b781b3f73
    - ev-6705c491b76291f9
findings:
- finding_id: rec-f-aaf7c8e19ffb99cd
  issue_key: mim-reconciliation-role-support-08a5656509adb992
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Glycogen from bovine liver'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-08a5656509adb992
  evidence_ids:
  - ev-a7ef598b781b3f73
  - ev-6705c491b76291f9
  - ev-951e9147f15ee3cc
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-aaf7c8e19ffb99cd
actions:
- action_id: rec-action-aaf7c8e19ffb99cd
  description: 'Reassess prediction-only role support: Glycogen from bovine liver'
  finding_ids:
  - rec-f-aaf7c8e19ffb99cd
  target_ids:
  - record-08a5656509adb992
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycogen_From_Bovine_Liver.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
