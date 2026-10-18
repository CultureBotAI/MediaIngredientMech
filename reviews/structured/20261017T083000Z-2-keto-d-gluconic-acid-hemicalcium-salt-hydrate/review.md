# Per-record structured review: 2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate (data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml)

- Review: 20261017T083000Z-2-keto-d-gluconic-acid-hemicalcium-salt-hydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate (data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml, record-3ad52ef88b948716, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3ad52ef88b948716 | data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml | maintained | 2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3ad52ef88b948716 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3ad52ef88b948716 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3ad52ef88b948716 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3ad52ef88b948716.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3ad52ef88b948716.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:30:14Z; reviewed SHA-256=5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1; current SHA-256=5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1; hash_changed=False. Reports=["reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Exact hydrate CAS and closeMatch parent pass, but chemistry is missing, the monohydrate label leaks onto the generic hydrate, and provisional roles remain.

### Historical provisional-role concern

evidence: concern. Targets: record-3ad52ef88b948716.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ac0b127f0ccb4b70: Reassess prediction-only role support: 2-Keto-D-gluconic acid hemicalcium salt hydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-3ad52ef88b948716.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ac0b127f0ccb4b70

Reassess prediction-only role support: 2-Keto-D-gluconic acid hemicalcium salt hydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-23a71eb202d37d4f | data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[319],"raw_equal":true},"docs_rows":[{"identifier":"cas:1040352-40-6","line":321,"mapping_status":"MAPPED","ontology_id":"CHEBI:27469","preferred_term":"2-Keto-D-gluconic acid hemicalcium salt hydrate"}],"identifier":"cas:1040352-40-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:27469","ontology_label":"2-dehydro-D-gluconic acid","ontology_source":"CHEBI"},"preferred_term":"2-Keto-D-gluconic acid hemicalcium salt hydrate","sssom_rows":[{"data_row":65,"object_id":"CHEBI:27469","object_label":"2-dehydro-D-gluconic acid","predicate_id":"skos:closeMatch"},{"data_row":66,"object_id":"cas:1040352-40-6","object_label":"2-Keto-D-gluconic acid hemicalcium salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","synonym_count":0} |
| ev-24901b1d1a0aeda0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [319] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d3760072a1c49ad3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate; data-row positions=[65, 66] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":65,"object_id":"CHEBI:27469","object_label":"2-dehydro-D-gluconic acid","other":"2-Keto-D-gluconic acid hemicalcium salt monohydrate&#124;CAS:1040352-40-6","predicate_id":"skos:closeMatch","subject_id":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","validation_method":"OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-09-02"},{"data_row":66,"object_id":"cas:1040352-40-6","object_label":"2-Keto-D-gluconic acid hemicalcium salt hydrate","other":"CAS:1040352-40-6","predicate_id":"skos:exactMatch","subject_id":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-3e9402949db2186b | docs/data/mapped_ingredients.csv; CSV lines=[321] | supports | Published identity and count rows inspected: [{"identifier":"cas:1040352-40-6","line":321,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27469","preferred_term":"2-Keto-D-gluconic acid hemicalcium salt hydrate","total_occurrences":"0"}] |
| ev-ab33c133920a2084 | reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.md; &#96;data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:46; Completeness:64; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bd6a6289f8efe053 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[49,1455,1985] | context_only | [{"current_record_sha256":"5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1","finding_id":"SEM:3d200b71e49d5b93d308","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1","finding_id":"SEM:c853fe49e0fbf877a6f5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1","finding_id":"SEM:96719ef531fcbbca919d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-ff95babb8ebb29a0 | data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[319],"raw_equal":true},"docs_rows":[{"identifier":"cas:1040352-40-6","line":321,"mapping_status":"MAPPED","ontology_id":"CHEBI:27469","preferred_term":"2-Keto-D-gluconic acid hemicalcium salt hydrate"}],"identifier":"cas:1040352-40-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:27469","ontology_label":"2-dehydro-D-gluconic acid","ontology_source":"CHEBI"},"preferred_term":"2-Keto-D-gluconic acid hemicalcium salt hydrate","sssom_rows":[{"data_row":65,"object_id":"CHEBI:27469","object_label":"2-dehydro-D-gluconic acid","predicate_id":"skos:closeMatch"},{"data_row":66,"object_id":"cas:1040352-40-6","object_label":"2-Keto-D-gluconic acid hemicalcium salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","synonym_count":0} |
| ev-fe1acd0406e8f624 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-ac0b127f0ccb4b70] | context_only | Predecessor structured review finding f-ac0b127f0ccb4b70 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-keto-d-gluconic-acid-hemicalcium-salt-hydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate
  (data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml)'
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
summary: Per-record structured review for 2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate
  (data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml, record-3ad52ef88b948716,
  mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound
  to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
    sha256: 5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.md
    sha256: 79a4b90edf16fbbffddb173c29a0256ff3cff5cd13f8806b960288063b41663e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3ad52ef88b948716
  path: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
  label: 2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3ad52ef88b948716
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-23a71eb202d37d4f
  - ev-24901b1d1a0aeda0
  - ev-d3760072a1c49ad3
  - ev-3e9402949db2186b
  - ev-ff95babb8ebb29a0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-23a71eb202d37d4f
  - ev-bd6a6289f8efe053
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-ab33c133920a2084
  - ev-bd6a6289f8efe053
  - ev-fe1acd0406e8f624
evidence:
- evidence_id: ev-23a71eb202d37d4f
  kind: record_content
  reference: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[319],"raw_equal":true},"docs_rows":[{"identifier":"cas:1040352-40-6","line":321,"mapping_status":"MAPPED","ontology_id":"CHEBI:27469","preferred_term":"2-Keto-D-gluconic
    acid hemicalcium salt hydrate"}],"identifier":"cas:1040352-40-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:27469","ontology_label":"2-dehydro-D-gluconic
    acid","ontology_source":"CHEBI"},"preferred_term":"2-Keto-D-gluconic acid hemicalcium
    salt hydrate","sssom_rows":[{"data_row":65,"object_id":"CHEBI:27469","object_label":"2-dehydro-D-gluconic
    acid","predicate_id":"skos:closeMatch"},{"data_row":66,"object_id":"cas:1040352-40-6","object_label":"2-Keto-D-gluconic
    acid hemicalcium salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","synonym_count":0}'
  snapshot_sha256: 5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1
- evidence_id: ev-24901b1d1a0aeda0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [319]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d3760072a1c49ad3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate; data-row
    positions=[65, 66]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":65,"object_id":"CHEBI:27469","object_label":"2-dehydro-D-gluconic
    acid","other":"2-Keto-D-gluconic acid hemicalcium salt monohydrate|CAS:1040352-40-6","predicate_id":"skos:closeMatch","subject_id":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","validation_method":"OLS:chebi|SYNONYM_ENRICH|2026-09-02"},{"data_row":66,"object_id":"cas:1040352-40-6","object_label":"2-Keto-D-gluconic
    acid hemicalcium salt hydrate","other":"CAS:1040352-40-6","predicate_id":"skos:exactMatch","subject_id":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3e9402949db2186b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[321]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:1040352-40-6","line":321,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27469","preferred_term":"2-Keto-D-gluconic
    acid hemicalcium salt hydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ab33c133920a2084
  kind: prior_review
  reference: reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.md
  locator: '`data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml`:2;
    Verdict:4; Identity:12; Validation:28; Evidence:46; Completeness:64; Recommended
    Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 79a4b90edf16fbbffddb173c29a0256ff3cff5cd13f8806b960288063b41663e
  quote: "Recommended Edits:\n1. In\n   `data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml`,\n\
    \   backfill formula `C12H20CaO15`, exact SMILES/InChI, and PubChem CID\n   `17749212`\
    \ for CAS `1040352-40-6`.\n2. Remove `2-Keto-D-gluconic acid hemicalcium salt\
    \ monohydrate` from exact label\n   surfaces for the generic hydrate record.\n\
    3. Remove or directly substantiate the provisional `CARBON_SOURCE` and\n   `ENERGY_SOURCE`\
    \ roles.\n4. Regenerate `data/curated/mapped_ingredients.yaml`,\n   `mappings/ingredient_mappings.sssom.tsv`,\
    \ docs, and mapping review queues.\n5. Re-run strict/LinkML validation, `scripts/validate_sssom_invariants.py`,\
    \ and\n   docs/export checks after the chemistry, synonym, and role cleanup."
- evidence_id: ev-bd6a6289f8efe053
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[49,1455,1985]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1","finding_id":"SEM:3d200b71e49d5b93d308","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1","finding_id":"SEM:c853fe49e0fbf877a6f5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1","finding_id":"SEM:96719ef531fcbbca919d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ff95babb8ebb29a0
  kind: record_content
  reference: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[319],"raw_equal":true},"docs_rows":[{"identifier":"cas:1040352-40-6","line":321,"mapping_status":"MAPPED","ontology_id":"CHEBI:27469","preferred_term":"2-Keto-D-gluconic
    acid hemicalcium salt hydrate"}],"identifier":"cas:1040352-40-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:27469","ontology_label":"2-dehydro-D-gluconic
    acid","ontology_source":"CHEBI"},"preferred_term":"2-Keto-D-gluconic acid hemicalcium
    salt hydrate","sssom_rows":[{"data_row":65,"object_id":"CHEBI:27469","object_label":"2-dehydro-D-gluconic
    acid","predicate_id":"skos:closeMatch"},{"data_row":66,"object_id":"cas:1040352-40-6","object_label":"2-Keto-D-gluconic
    acid hemicalcium salt hydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate","synonym_count":0}'
  snapshot_sha256: 5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1
- evidence_id: ev-fe1acd0406e8f624
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-ac0b127f0ccb4b70]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ac0b127f0ccb4b70 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-22bff6dcd92c14cb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-23a71eb202d37d4f
  - ev-24901b1d1a0aeda0
  - ev-d3760072a1c49ad3
  - ev-3e9402949db2186b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-029540c67ff58b0b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-ab33c133920a2084
  - ev-23a71eb202d37d4f
  - ev-bd6a6289f8efe053
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:30:14Z;
    reviewed SHA-256=5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1;
    current SHA-256=5d30ccd4eb4f4148e5f06b6753c37739ebf7d5f678a679b9c5220b5c62bb40e1;
    hash_changed=False. Reports=["reports/yaml_record_review/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Exact hydrate
    CAS and closeMatch parent pass, but chemistry is missing, the monohydrate label
    leaks onto the generic hydrate, and provisional roles remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ab33c133920a2084
    - ev-23a71eb202d37d4f
  - name: legacy-native-ids
    value: '["SEM:3d200b71e49d5b93d308","SEM:c853fe49e0fbf877a6f5","SEM:96719ef531fcbbca919d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-23a71eb202d37d4f
    - ev-ab33c133920a2084
    - ev-bd6a6289f8efe053
- assessment_id: a-ff95babb8ebb29a0
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-ab33c133920a2084
  - ev-ff95babb8ebb29a0
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ab33c133920a2084
    - ev-ff95babb8ebb29a0
findings:
- finding_id: rec-f-ac0b127f0ccb4b70
  issue_key: mim-reconciliation-role-support-3ad52ef88b948716
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 2-Keto-D-gluconic acid hemicalcium
    salt hydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ad52ef88b948716
  evidence_ids:
  - ev-ab33c133920a2084
  - ev-ff95babb8ebb29a0
  - ev-fe1acd0406e8f624
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-ac0b127f0ccb4b70
actions:
- action_id: rec-action-ac0b127f0ccb4b70
  description: 'Reassess prediction-only role support: 2-Keto-D-gluconic acid hemicalcium
    salt hydrate'
  finding_ids:
  - rec-f-ac0b127f0ccb4b70
  target_ids:
  - record-3ad52ef88b948716
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-Keto-D-gluconic_Acid_Hemicalcium_Salt_Hydrate.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
