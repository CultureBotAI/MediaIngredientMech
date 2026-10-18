# Per-record structured review: Deuterated_Glucose (data/ingredients/mapped/Deuterated_Glucose.yaml)

- Review: 20261017T083000Z-deuterated-glucose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Deuterated_Glucose (data/ingredients/mapped/Deuterated_Glucose.yaml, record-6afee93083898c0f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Deuterated_Glucose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Deuterated_Glucose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6afee93083898c0f | data/ingredients/mapped/Deuterated_Glucose.yaml | maintained | Deuterated_Glucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6afee93083898c0f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6afee93083898c0f | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6afee93083898c0f | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6afee93083898c0f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6afee93083898c0f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:30:48Z; reviewed SHA-256=2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59; current SHA-256=2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59; hash_changed=False. Reports=["reports/yaml_record_review/Deuterated_Glucose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS/NCIT parent mapping shape passes, but stored SMILES drops isotope labels and both roles are computational.

### Historical provisional-role concern

evidence: concern. Targets: record-6afee93083898c0f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-a883232ab1a1062d: Reassess prediction-only role support: deuterated glucose

major / open / confirmed; issue key: mim-reconciliation-role-support-6afee93083898c0f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-a883232ab1a1062d

Reassess prediction-only role support: deuterated glucose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-738d75e554ce0b33 | data/ingredients/mapped/Deuterated_Glucose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[877],"raw_equal":true},"docs_rows":[{"identifier":"cas:201417-01-8","line":879,"mapping_status":"MAPPED","ontology_id":"NCIT:C200498","preferred_term":"deuterated glucose"}],"identifier":"cas:201417-01-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C200498","ontology_label":"Deuterated Glucose","ontology_source":"NCIT"},"preferred_term":"deuterated glucose","sssom_rows":[{"data_row":1022,"object_id":"NCIT:C200498","object_label":"Deuterated Glucose","predicate_id":"skos:broadMatch"},{"data_row":1023,"object_id":"cas:201417-01-8","object_label":"deuterated glucose","predicate_id":"skos:exactMatch"},{"data_row":1024,"object_id":"kgmicrobe.compound:deuterated_glucose","object_label":"deuterated glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Deuterated_Glucose","synonym_count":0} |
| ev-544245c352bedd36 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [877] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a2377c2b46db5a12 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Deuterated_Glucose; data-row positions=[1022, 1023, 1024] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1022,"object_id":"NCIT:C200498","object_label":"Deuterated Glucose","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Deuterated_Glucose","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1023,"object_id":"cas:201417-01-8","object_label":"deuterated glucose","other":"CAS:201417-01-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Deuterated_Glucose","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1024,"object_id":"kgmicrobe.compound:deuterated_glucose","object_label":"deuterated glucose","other":"CAS:201417-01-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Deuterated_Glucose","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-3d1e804f9495369f | docs/data/mapped_ingredients.csv; CSV lines=[879] | supports | Published identity and count rows inspected: [{"identifier":"cas:201417-01-8","line":879,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C200498","preferred_term":"deuterated glucose","total_occurrences":"0"}] |
| ev-5e934b084ec3d5e3 | reports/yaml_record_review/Deuterated_Glucose.md; &#96;data/ingredients/mapped/Deuterated_Glucose.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:42; Completeness:65; Recommended Edits:72 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c1752d1f918eedaf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[529,1884,1979] | context_only | [{"current_record_sha256":"2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59","finding_id":"SEM:3702375c50724a106873","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59","finding_id":"SEM:e922e8623c4c658d1a06","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59","finding_id":"SEM:d4d73b34d85ded394c0b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2b758950a2c9aa3c | data/ingredients/mapped/Deuterated_Glucose.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[877],"raw_equal":true},"docs_rows":[{"identifier":"cas:201417-01-8","line":879,"mapping_status":"MAPPED","ontology_id":"NCIT:C200498","preferred_term":"deuterated glucose"}],"identifier":"cas:201417-01-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C200498","ontology_label":"Deuterated Glucose","ontology_source":"NCIT"},"preferred_term":"deuterated glucose","sssom_rows":[{"data_row":1022,"object_id":"NCIT:C200498","object_label":"Deuterated Glucose","predicate_id":"skos:broadMatch"},{"data_row":1023,"object_id":"cas:201417-01-8","object_label":"deuterated glucose","predicate_id":"skos:exactMatch"},{"data_row":1024,"object_id":"kgmicrobe.compound:deuterated_glucose","object_label":"deuterated glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Deuterated_Glucose","synonym_count":0} |
| ev-cae1bf10513add68 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-a883232ab1a1062d] | context_only | Predecessor structured review finding f-a883232ab1a1062d in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-deuterated-glucose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Deuterated_Glucose (data/ingredients/mapped/Deuterated_Glucose.yaml)'
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
summary: Per-record structured review for Deuterated_Glucose (data/ingredients/mapped/Deuterated_Glucose.yaml,
  record-6afee93083898c0f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Deuterated_Glucose.yaml
    sha256: 2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59
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
  - path: reports/yaml_record_review/Deuterated_Glucose.md
    sha256: 49df7f8d7e300486a21eb1e633f0421318f79871999986cf9d30ce7e082fe962
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6afee93083898c0f
  path: data/ingredients/mapped/Deuterated_Glucose.yaml
  label: Deuterated_Glucose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Deuterated_Glucose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Deuterated_Glucose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Deuterated_Glucose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6afee93083898c0f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-738d75e554ce0b33
  - ev-544245c352bedd36
  - ev-a2377c2b46db5a12
  - ev-3d1e804f9495369f
  - ev-2b758950a2c9aa3c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-738d75e554ce0b33
  - ev-c1752d1f918eedaf
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-5e934b084ec3d5e3
  - ev-c1752d1f918eedaf
  - ev-cae1bf10513add68
evidence:
- evidence_id: ev-738d75e554ce0b33
  kind: record_content
  reference: data/ingredients/mapped/Deuterated_Glucose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[877],"raw_equal":true},"docs_rows":[{"identifier":"cas:201417-01-8","line":879,"mapping_status":"MAPPED","ontology_id":"NCIT:C200498","preferred_term":"deuterated
    glucose"}],"identifier":"cas:201417-01-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C200498","ontology_label":"Deuterated
    Glucose","ontology_source":"NCIT"},"preferred_term":"deuterated glucose","sssom_rows":[{"data_row":1022,"object_id":"NCIT:C200498","object_label":"Deuterated
    Glucose","predicate_id":"skos:broadMatch"},{"data_row":1023,"object_id":"cas:201417-01-8","object_label":"deuterated
    glucose","predicate_id":"skos:exactMatch"},{"data_row":1024,"object_id":"kgmicrobe.compound:deuterated_glucose","object_label":"deuterated
    glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Deuterated_Glucose","synonym_count":0}'
  snapshot_sha256: 2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59
- evidence_id: ev-544245c352bedd36
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [877]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a2377c2b46db5a12
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Deuterated_Glucose; data-row positions=[1022, 1023, 1024]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1022,"object_id":"NCIT:C200498","object_label":"Deuterated
    Glucose","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Deuterated_Glucose","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1023,"object_id":"cas:201417-01-8","object_label":"deuterated
    glucose","other":"CAS:201417-01-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Deuterated_Glucose","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1024,"object_id":"kgmicrobe.compound:deuterated_glucose","object_label":"deuterated
    glucose","other":"CAS:201417-01-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Deuterated_Glucose","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3d1e804f9495369f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[879]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:201417-01-8","line":879,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"NCIT:C200498","preferred_term":"deuterated
    glucose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5e934b084ec3d5e3
  kind: prior_review
  reference: reports/yaml_record_review/Deuterated_Glucose.md
  locator: '`data/ingredients/mapped/Deuterated_Glucose.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:42; Completeness:65; Recommended Edits:72'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 49df7f8d7e300486a21eb1e633f0421318f79871999986cf9d30ce7e082fe962
  quote: "Recommended Edits:\n- Major: update the `chemical_properties.smiles` in\n\
    \  `data/ingredients/mapped/Deuterated_Glucose.yaml` to the isotope-specific\n\
    \  PubChem isomeric SMILES for CID `71777455`, then synchronize\n  `data/curated/mapped_ingredients.yaml`.\n\
    - Major: source or remove `nutritional_roles.CARBON_SOURCE` and\n  `nutritional_roles.ENERGY_SOURCE`;\
    \ neither role should rest only on generic\n  name-based inference for a labeled\
    \ isotope reagent."
- evidence_id: ev-c1752d1f918eedaf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[529,1884,1979]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59","finding_id":"SEM:3702375c50724a106873","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59","finding_id":"SEM:e922e8623c4c658d1a06","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59","finding_id":"SEM:d4d73b34d85ded394c0b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2b758950a2c9aa3c
  kind: record_content
  reference: data/ingredients/mapped/Deuterated_Glucose.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[877],"raw_equal":true},"docs_rows":[{"identifier":"cas:201417-01-8","line":879,"mapping_status":"MAPPED","ontology_id":"NCIT:C200498","preferred_term":"deuterated
    glucose"}],"identifier":"cas:201417-01-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"NCIT:C200498","ontology_label":"Deuterated
    Glucose","ontology_source":"NCIT"},"preferred_term":"deuterated glucose","sssom_rows":[{"data_row":1022,"object_id":"NCIT:C200498","object_label":"Deuterated
    Glucose","predicate_id":"skos:broadMatch"},{"data_row":1023,"object_id":"cas:201417-01-8","object_label":"deuterated
    glucose","predicate_id":"skos:exactMatch"},{"data_row":1024,"object_id":"kgmicrobe.compound:deuterated_glucose","object_label":"deuterated
    glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Deuterated_Glucose","synonym_count":0}'
  snapshot_sha256: 2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59
- evidence_id: ev-cae1bf10513add68
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-a883232ab1a1062d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-a883232ab1a1062d in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-f374c3eab4e3c9b1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-738d75e554ce0b33
  - ev-544245c352bedd36
  - ev-a2377c2b46db5a12
  - ev-3d1e804f9495369f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-911ef921c04d84ba
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-5e934b084ec3d5e3
  - ev-738d75e554ce0b33
  - ev-c1752d1f918eedaf
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:30:48Z;
    reviewed SHA-256=2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59;
    current SHA-256=2482918b98a21024cd45f4b2db753342d8f4eb83997d99556171af5931d99c59;
    hash_changed=False. Reports=["reports/yaml_record_review/Deuterated_Glucose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS/NCIT
    parent mapping shape passes, but stored SMILES drops isotope labels and both roles
    are computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5e934b084ec3d5e3
    - ev-738d75e554ce0b33
  - name: legacy-native-ids
    value: '["SEM:3702375c50724a106873","SEM:e922e8623c4c658d1a06","SEM:d4d73b34d85ded394c0b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-738d75e554ce0b33
    - ev-5e934b084ec3d5e3
    - ev-c1752d1f918eedaf
- assessment_id: a-2b758950a2c9aa3c
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-5e934b084ec3d5e3
  - ev-2b758950a2c9aa3c
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5e934b084ec3d5e3
    - ev-2b758950a2c9aa3c
findings:
- finding_id: rec-f-a883232ab1a1062d
  issue_key: mim-reconciliation-role-support-6afee93083898c0f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: deuterated glucose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6afee93083898c0f
  evidence_ids:
  - ev-5e934b084ec3d5e3
  - ev-2b758950a2c9aa3c
  - ev-cae1bf10513add68
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Deuterated_Glucose.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-a883232ab1a1062d
actions:
- action_id: rec-action-a883232ab1a1062d
  description: 'Reassess prediction-only role support: deuterated glucose'
  finding_ids:
  - rec-f-a883232ab1a1062d
  target_ids:
  - record-6afee93083898c0f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Deuterated_Glucose.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
