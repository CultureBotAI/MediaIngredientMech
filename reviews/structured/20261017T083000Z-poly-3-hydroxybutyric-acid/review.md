# Per-record structured review: Poly_3-hydroxybutyric_Acid (data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml)

- Review: 20261017T083000Z-poly-3-hydroxybutyric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Poly_3-hydroxybutyric_Acid (data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml, record-b39f2508e9b15e70, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b39f2508e9b15e70 | data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml | maintained | Poly_3-hydroxybutyric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b39f2508e9b15e70 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-b39f2508e9b15e70 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b39f2508e9b15e70 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b39f2508e9b15e70.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b39f2508e9b15e70.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:09Z; reviewed SHA-256=9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848; current SHA-256=9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050309Z-Poly_3-hydroxybutyric_Acid.md","reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md&#96; after the record changed from 7b40c7f28a9424e0cda7c685c3c53d839d54193ac278f265a461a29afaa53c34 to 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-b39f2508e9b15e70.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-91668becea8fd466: Reassess prediction-only role support: Poly(3-hydroxybutyric acid)

major / open / confirmed; issue key: mim-reconciliation-role-support-b39f2508e9b15e70.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-91668becea8fd466

Reassess prediction-only role support: Poly(3-hydroxybutyric acid)

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7a3af97044a0dea6 | data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1674],"raw_equal":true},"docs_rows":[{"identifier":"cas:29435-48-1","line":1676,"mapping_status":"MAPPED","ontology_id":"CHEBI:20067","preferred_term":"Poly(3-hydroxybutyric acid)"}],"identifier":"cas:29435-48-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:20067","ontology_label":"3-hydroxybutyric acid","ontology_source":"CHEBI"},"preferred_term":"Poly(3-hydroxybutyric acid)","sssom_rows":[{"data_row":2286,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric acid","predicate_id":"skos:broadMatch"},{"data_row":2287,"object_id":"cas:29435-48-1","object_label":"Poly(3-hydroxybutyric acid)","predicate_id":"skos:exactMatch"},{"data_row":2288,"object_id":"kgmicrobe.compound:poly_3-hydroxybutyric_acid","object_label":"Poly(3-hydroxybutyric acid)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Poly_3-hydroxybutyric_Acid","synonym_count":1} |
| ev-f6df2dbe19fc1622 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1674] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7173063e5fb0506f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Poly_3-hydroxybutyric_Acid; data-row positions=[2286, 2287, 2288] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2286,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Poly_3-hydroxybutyric_Acid","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2287,"object_id":"cas:29435-48-1","object_label":"Poly(3-hydroxybutyric acid)","other":"CAS:29435-48-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Poly_3-hydroxybutyric_Acid","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2288,"object_id":"kgmicrobe.compound:poly_3-hydroxybutyric_acid","object_label":"Poly(3-hydroxybutyric acid)","other":"CAS:29435-48-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Poly_3-hydroxybutyric_Acid","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-9fc5f7e9eb33c3de | docs/data/mapped_ingredients.csv; CSV lines=[1676] | supports | Published identity and count rows inspected: [{"identifier":"cas:29435-48-1","line":1676,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:20067","preferred_term":"Poly(3-hydroxybutyric acid)","total_occurrences":"0"}] |
| ev-590318d6fa15ef24 | reports/yaml_record_review/20261001T050309Z-Poly_3-hydroxybutyric_Acid.md; YAML Record Review: Poly(3-hydroxybutyric acid):2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5612a08ff776cea9 | reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md; &#96;data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f40df26c33af12b8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1125,1675] | context_only | [{"current_record_sha256":"9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848","finding_id":"SEM:2d7f1f6e968e4fcdab19","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848","finding_id":"SEM:fbc9a32871fc823f900c","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-33951119fa4ea50a | data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1674],"raw_equal":true},"docs_rows":[{"identifier":"cas:29435-48-1","line":1676,"mapping_status":"MAPPED","ontology_id":"CHEBI:20067","preferred_term":"Poly(3-hydroxybutyric acid)"}],"identifier":"cas:29435-48-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:20067","ontology_label":"3-hydroxybutyric acid","ontology_source":"CHEBI"},"preferred_term":"Poly(3-hydroxybutyric acid)","sssom_rows":[{"data_row":2286,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric acid","predicate_id":"skos:broadMatch"},{"data_row":2287,"object_id":"cas:29435-48-1","object_label":"Poly(3-hydroxybutyric acid)","predicate_id":"skos:exactMatch"},{"data_row":2288,"object_id":"kgmicrobe.compound:poly_3-hydroxybutyric_acid","object_label":"Poly(3-hydroxybutyric acid)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Poly_3-hydroxybutyric_Acid","synonym_count":1} |
| ev-2973e51b1f6a6923 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-91668becea8fd466] | context_only | Predecessor structured review finding f-91668becea8fd466 in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-poly-3-hydroxybutyric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Poly_3-hydroxybutyric_Acid (data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml)'
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
summary: Per-record structured review for Poly_3-hydroxybutyric_Acid (data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml,
  record-b39f2508e9b15e70, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
    sha256: 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/20261001T050309Z-Poly_3-hydroxybutyric_Acid.md
    sha256: 6a9687ec3c8b2ee0737d0b225ce1ecc58ca07dba0a9fa3bc02c4ce365aed04cf
    role: context
  - path: reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md
    sha256: 32a2a4ba8b98b12edd1fe909ae921e51edd81648154ab0eba069232efc36e149
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b39f2508e9b15e70
  path: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
  label: Poly_3-hydroxybutyric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b39f2508e9b15e70
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-7a3af97044a0dea6
  - ev-f6df2dbe19fc1622
  - ev-7173063e5fb0506f
  - ev-9fc5f7e9eb33c3de
  - ev-33951119fa4ea50a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-7a3af97044a0dea6
  - ev-f40df26c33af12b8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-590318d6fa15ef24
  - ev-5612a08ff776cea9
  - ev-f40df26c33af12b8
  - ev-2973e51b1f6a6923
evidence:
- evidence_id: ev-7a3af97044a0dea6
  kind: record_content
  reference: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1674],"raw_equal":true},"docs_rows":[{"identifier":"cas:29435-48-1","line":1676,"mapping_status":"MAPPED","ontology_id":"CHEBI:20067","preferred_term":"Poly(3-hydroxybutyric
    acid)"}],"identifier":"cas:29435-48-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:20067","ontology_label":"3-hydroxybutyric
    acid","ontology_source":"CHEBI"},"preferred_term":"Poly(3-hydroxybutyric acid)","sssom_rows":[{"data_row":2286,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric
    acid","predicate_id":"skos:broadMatch"},{"data_row":2287,"object_id":"cas:29435-48-1","object_label":"Poly(3-hydroxybutyric
    acid)","predicate_id":"skos:exactMatch"},{"data_row":2288,"object_id":"kgmicrobe.compound:poly_3-hydroxybutyric_acid","object_label":"Poly(3-hydroxybutyric
    acid)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Poly_3-hydroxybutyric_Acid","synonym_count":1}'
  snapshot_sha256: 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848
- evidence_id: ev-f6df2dbe19fc1622
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1674]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7173063e5fb0506f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Poly_3-hydroxybutyric_Acid; data-row positions=[2286, 2287,
    2288]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2286,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric
    acid","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Poly_3-hydroxybutyric_Acid","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2287,"object_id":"cas:29435-48-1","object_label":"Poly(3-hydroxybutyric
    acid)","other":"CAS:29435-48-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Poly_3-hydroxybutyric_Acid","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2288,"object_id":"kgmicrobe.compound:poly_3-hydroxybutyric_acid","object_label":"Poly(3-hydroxybutyric
    acid)","other":"CAS:29435-48-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Poly_3-hydroxybutyric_Acid","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9fc5f7e9eb33c3de
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1676]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:29435-48-1","line":1676,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:20067","preferred_term":"Poly(3-hydroxybutyric
    acid)","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-590318d6fa15ef24
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050309Z-Poly_3-hydroxybutyric_Acid.md
  locator: 'YAML Record Review: Poly(3-hydroxybutyric acid):2; Target:10; Validation:20;
    Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended
    Edits:56; Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6a9687ec3c8b2ee0737d0b225ce1ecc58ca07dba0a9fa3bc02c4ce365aed04cf
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The CAS identity
    is preserved, but the parent mapping and exported monomer synonym point at 3-hydroxybutyric
    acid.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`,
    `just validate-terms data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`
    where applicable, and `just qc-sssom`.'
- evidence_id: ev-5612a08ff776cea9
  kind: prior_review
  reference: reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md
  locator: '`data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 32a2a4ba8b98b12edd1fe909ae921e51edd81648154ab0eba069232efc36e149
- evidence_id: ev-f40df26c33af12b8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1125,1675]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848","finding_id":"SEM:2d7f1f6e968e4fcdab19","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848","finding_id":"SEM:fbc9a32871fc823f900c","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-33951119fa4ea50a
  kind: record_content
  reference: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1674],"raw_equal":true},"docs_rows":[{"identifier":"cas:29435-48-1","line":1676,"mapping_status":"MAPPED","ontology_id":"CHEBI:20067","preferred_term":"Poly(3-hydroxybutyric
    acid)"}],"identifier":"cas:29435-48-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:20067","ontology_label":"3-hydroxybutyric
    acid","ontology_source":"CHEBI"},"preferred_term":"Poly(3-hydroxybutyric acid)","sssom_rows":[{"data_row":2286,"object_id":"CHEBI:20067","object_label":"3-hydroxybutyric
    acid","predicate_id":"skos:broadMatch"},{"data_row":2287,"object_id":"cas:29435-48-1","object_label":"Poly(3-hydroxybutyric
    acid)","predicate_id":"skos:exactMatch"},{"data_row":2288,"object_id":"kgmicrobe.compound:poly_3-hydroxybutyric_acid","object_label":"Poly(3-hydroxybutyric
    acid)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Poly_3-hydroxybutyric_Acid","synonym_count":1}'
  snapshot_sha256: 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848
- evidence_id: ev-2973e51b1f6a6923
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-91668becea8fd466]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-91668becea8fd466 in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-811e7613aaca1f62
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-7a3af97044a0dea6
  - ev-f6df2dbe19fc1622
  - ev-7173063e5fb0506f
  - ev-9fc5f7e9eb33c3de
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c6b316e81f723b7a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-590318d6fa15ef24
  - ev-5612a08ff776cea9
  - ev-7a3af97044a0dea6
  - ev-f40df26c33af12b8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:03:09Z;
    reviewed SHA-256=9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848;
    current SHA-256=9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050309Z-Poly_3-hydroxybutyric_Acid.md","reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Poly_3-hydroxybutyric_Acid.md` after the record changed
    from 7b40c7f28a9424e0cda7c685c3c53d839d54193ac278f265a461a29afaa53c34 to 9e0e563c06141faa41510a655cc3e1821d7a225c09236b309e2a2c1d541b7848;
    preserved the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-590318d6fa15ef24
    - ev-5612a08ff776cea9
    - ev-7a3af97044a0dea6
  - name: legacy-native-ids
    value: '["SEM:2d7f1f6e968e4fcdab19","SEM:fbc9a32871fc823f900c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7a3af97044a0dea6
    - ev-590318d6fa15ef24
    - ev-5612a08ff776cea9
    - ev-f40df26c33af12b8
- assessment_id: a-33951119fa4ea50a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-590318d6fa15ef24
  - ev-5612a08ff776cea9
  - ev-33951119fa4ea50a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-590318d6fa15ef24
    - ev-5612a08ff776cea9
    - ev-33951119fa4ea50a
findings:
- finding_id: rec-f-91668becea8fd466
  issue_key: mim-reconciliation-role-support-b39f2508e9b15e70
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Poly(3-hydroxybutyric acid)'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-b39f2508e9b15e70
  evidence_ids:
  - ev-590318d6fa15ef24
  - ev-5612a08ff776cea9
  - ev-33951119fa4ea50a
  - ev-2973e51b1f6a6923
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-91668becea8fd466
actions:
- action_id: rec-action-91668becea8fd466
  description: 'Reassess prediction-only role support: Poly(3-hydroxybutyric acid)'
  finding_ids:
  - rec-f-91668becea8fd466
  target_ids:
  - record-b39f2508e9b15e70
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Poly_3-hydroxybutyric_Acid.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
