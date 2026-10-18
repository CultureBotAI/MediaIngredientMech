# Per-record structured review: DL-glyceraldehyde (data/ingredients/mapped/DL-glyceraldehyde.yaml)

- Review: 20261017T083000Z-dl-glyceraldehyde
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for DL-glyceraldehyde (data/ingredients/mapped/DL-glyceraldehyde.yaml, record-29b97c22d4678505, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/DL-glyceraldehyde.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/DL-glyceraldehyde.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-29b97c22d4678505 | data/ingredients/mapped/DL-glyceraldehyde.yaml | maintained | DL-glyceraldehyde |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-29b97c22d4678505 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-29b97c22d4678505 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-29b97c22d4678505 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-29b97c22d4678505.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-29b97c22d4678505.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:07:05Z; reviewed SHA-256=928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538; current SHA-256=928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538; hash_changed=False. Reports=["reports/yaml_record_review/DL-glyceraldehyde.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The September stereochemical repair holds, but the carbon-source role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-29b97c22d4678505.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-073ba66f7b3c0851: Reassess prediction-only role support: DL-glyceraldehyde

major / open / confirmed; issue key: mim-reconciliation-role-support-29b97c22d4678505.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-073ba66f7b3c0851

Reassess prediction-only role support: DL-glyceraldehyde

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a461b24a43c41fc6 | data/ingredients/mapped/DL-glyceraldehyde.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[857],"raw_equal":true},"docs_rows":[{"identifier":"cas:56-82-6","line":859,"mapping_status":"MAPPED","ontology_id":"CHEBI:5445","preferred_term":"DL-glyceraldehyde"}],"identifier":"cas:56-82-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:5445","ontology_label":"glyceraldehyde","ontology_source":"CHEBI"},"preferred_term":"DL-glyceraldehyde","sssom_rows":[{"data_row":990,"object_id":"CHEBI:5445","object_label":"glyceraldehyde","predicate_id":"skos:broadMatch"},{"data_row":991,"object_id":"cas:56-82-6","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"},{"data_row":992,"object_id":"kgmicrobe.compound:dl-glyceraldehyde","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-glyceraldehyde","synonym_count":1} |
| ev-5a6a99c166f78a12 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [857] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a6c297cd4648a569 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:DL-glyceraldehyde; data-row positions=[990, 991, 992] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":990,"object_id":"CHEBI:5445","object_label":"glyceraldehyde","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:DL-glyceraldehyde","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":991,"object_id":"cas:56-82-6","object_label":"DL-glyceraldehyde","other":"CAS:56-82-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-glyceraldehyde","validation_method":""},{"data_row":992,"object_id":"kgmicrobe.compound:dl-glyceraldehyde","object_label":"DL-glyceraldehyde","other":"CAS:56-82-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-glyceraldehyde","validation_method":""}] |
| ev-283981eca42629a2 | docs/data/mapped_ingredients.csv; CSV lines=[859] | supports | Published identity and count rows inspected: [{"identifier":"cas:56-82-6","line":859,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:5445","preferred_term":"DL-glyceraldehyde","total_occurrences":"0"}] |
| ev-cfabe4bf46ad4c4c | reports/yaml_record_review/DL-glyceraldehyde.md; &#96;data/ingredients/mapped/DL-glyceraldehyde.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:45; Completeness:61; Recommended Edits:72 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fc1416fd3a1bdbf7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[519,1736] | context_only | [{"current_record_sha256":"928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538","finding_id":"SEM:953417d9ebb629e9af28","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538","finding_id":"SEM:5c07277f5a9f92ab287a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-70956365cc5a79a7 | data/ingredients/mapped/DL-glyceraldehyde.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[857],"raw_equal":true},"docs_rows":[{"identifier":"cas:56-82-6","line":859,"mapping_status":"MAPPED","ontology_id":"CHEBI:5445","preferred_term":"DL-glyceraldehyde"}],"identifier":"cas:56-82-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:5445","ontology_label":"glyceraldehyde","ontology_source":"CHEBI"},"preferred_term":"DL-glyceraldehyde","sssom_rows":[{"data_row":990,"object_id":"CHEBI:5445","object_label":"glyceraldehyde","predicate_id":"skos:broadMatch"},{"data_row":991,"object_id":"cas:56-82-6","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"},{"data_row":992,"object_id":"kgmicrobe.compound:dl-glyceraldehyde","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-glyceraldehyde","synonym_count":1} |
| ev-ff8ca481b26aff4a | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-073ba66f7b3c0851] | context_only | Predecessor structured review finding f-073ba66f7b3c0851 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-dl-glyceraldehyde
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: DL-glyceraldehyde (data/ingredients/mapped/DL-glyceraldehyde.yaml)'
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
summary: Per-record structured review for DL-glyceraldehyde (data/ingredients/mapped/DL-glyceraldehyde.yaml,
  record-29b97c22d4678505, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/DL-glyceraldehyde.yaml
    sha256: 928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538
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
  - path: reports/yaml_record_review/DL-glyceraldehyde.md
    sha256: ca2163af576c0642b82a27f4eba559380b192696ebb68166265d3d325f5d11d3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-29b97c22d4678505
  path: data/ingredients/mapped/DL-glyceraldehyde.yaml
  label: DL-glyceraldehyde
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-glyceraldehyde.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/DL-glyceraldehyde.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/DL-glyceraldehyde.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-29b97c22d4678505
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-a461b24a43c41fc6
  - ev-5a6a99c166f78a12
  - ev-a6c297cd4648a569
  - ev-283981eca42629a2
  - ev-70956365cc5a79a7
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-a461b24a43c41fc6
  - ev-fc1416fd3a1bdbf7
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-cfabe4bf46ad4c4c
  - ev-fc1416fd3a1bdbf7
  - ev-ff8ca481b26aff4a
evidence:
- evidence_id: ev-a461b24a43c41fc6
  kind: record_content
  reference: data/ingredients/mapped/DL-glyceraldehyde.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[857],"raw_equal":true},"docs_rows":[{"identifier":"cas:56-82-6","line":859,"mapping_status":"MAPPED","ontology_id":"CHEBI:5445","preferred_term":"DL-glyceraldehyde"}],"identifier":"cas:56-82-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:5445","ontology_label":"glyceraldehyde","ontology_source":"CHEBI"},"preferred_term":"DL-glyceraldehyde","sssom_rows":[{"data_row":990,"object_id":"CHEBI:5445","object_label":"glyceraldehyde","predicate_id":"skos:broadMatch"},{"data_row":991,"object_id":"cas:56-82-6","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"},{"data_row":992,"object_id":"kgmicrobe.compound:dl-glyceraldehyde","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-glyceraldehyde","synonym_count":1}'
  snapshot_sha256: 928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538
- evidence_id: ev-5a6a99c166f78a12
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [857]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a6c297cd4648a569
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:DL-glyceraldehyde; data-row positions=[990, 991, 992]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":990,"object_id":"CHEBI:5445","object_label":"glyceraldehyde","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:DL-glyceraldehyde","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":991,"object_id":"cas:56-82-6","object_label":"DL-glyceraldehyde","other":"CAS:56-82-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-glyceraldehyde","validation_method":""},{"data_row":992,"object_id":"kgmicrobe.compound:dl-glyceraldehyde","object_label":"DL-glyceraldehyde","other":"CAS:56-82-6","predicate_id":"skos:exactMatch","subject_id":"MIM:DL-glyceraldehyde","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-283981eca42629a2
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[859]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:56-82-6","line":859,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:5445","preferred_term":"DL-glyceraldehyde","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-cfabe4bf46ad4c4c
  kind: prior_review
  reference: reports/yaml_record_review/DL-glyceraldehyde.md
  locator: '`data/ingredients/mapped/DL-glyceraldehyde.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:45; Completeness:61; Recommended Edits:72'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ca2163af576c0642b82a27f4eba559380b192696ebb68166265d3d325f5d11d3
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/DL-glyceraldehyde.yaml`,\
    \ remove the provisional\n  `CARBON_SOURCE` role or replace its `COMPUTATIONAL_PREDICTION`\
    \ evidence with\n  inspected claim-level evidence for this supplied form.\n- Regenerate\
    \ synchronized curated and SSSOM products, then rerun\n  `uv run --frozen python\
    \ scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator validate-data\
    \ data/ingredients/mapped/DL-glyceraldehyde.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-fc1416fd3a1bdbf7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[519,1736]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538","finding_id":"SEM:953417d9ebb629e9af28","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538","finding_id":"SEM:5c07277f5a9f92ab287a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-70956365cc5a79a7
  kind: record_content
  reference: data/ingredients/mapped/DL-glyceraldehyde.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[857],"raw_equal":true},"docs_rows":[{"identifier":"cas:56-82-6","line":859,"mapping_status":"MAPPED","ontology_id":"CHEBI:5445","preferred_term":"DL-glyceraldehyde"}],"identifier":"cas:56-82-6","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:5445","ontology_label":"glyceraldehyde","ontology_source":"CHEBI"},"preferred_term":"DL-glyceraldehyde","sssom_rows":[{"data_row":990,"object_id":"CHEBI:5445","object_label":"glyceraldehyde","predicate_id":"skos:broadMatch"},{"data_row":991,"object_id":"cas:56-82-6","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"},{"data_row":992,"object_id":"kgmicrobe.compound:dl-glyceraldehyde","object_label":"DL-glyceraldehyde","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:DL-glyceraldehyde","synonym_count":1}'
  snapshot_sha256: 928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538
- evidence_id: ev-ff8ca481b26aff4a
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-073ba66f7b3c0851]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-073ba66f7b3c0851 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-2feda7498d1b6287
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-a461b24a43c41fc6
  - ev-5a6a99c166f78a12
  - ev-a6c297cd4648a569
  - ev-283981eca42629a2
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ec2cb3d8fa126e53
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-cfabe4bf46ad4c4c
  - ev-a461b24a43c41fc6
  - ev-fc1416fd3a1bdbf7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:07:05Z;
    reviewed SHA-256=928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538;
    current SHA-256=928ab995a38d52e6db4ce0ed1badd586a4fa1535446f02bb073f0ff921cb7538;
    hash_changed=False. Reports=["reports/yaml_record_review/DL-glyceraldehyde.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The September
    stereochemical repair holds, but the carbon-source role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cfabe4bf46ad4c4c
    - ev-a461b24a43c41fc6
  - name: legacy-native-ids
    value: '["SEM:953417d9ebb629e9af28","SEM:5c07277f5a9f92ab287a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a461b24a43c41fc6
    - ev-cfabe4bf46ad4c4c
    - ev-fc1416fd3a1bdbf7
- assessment_id: a-70956365cc5a79a7
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-cfabe4bf46ad4c4c
  - ev-70956365cc5a79a7
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cfabe4bf46ad4c4c
    - ev-70956365cc5a79a7
findings:
- finding_id: rec-f-073ba66f7b3c0851
  issue_key: mim-reconciliation-role-support-29b97c22d4678505
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: DL-glyceraldehyde'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-29b97c22d4678505
  evidence_ids:
  - ev-cfabe4bf46ad4c4c
  - ev-70956365cc5a79a7
  - ev-ff8ca481b26aff4a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-glyceraldehyde.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-073ba66f7b3c0851
actions:
- action_id: rec-action-073ba66f7b3c0851
  description: 'Reassess prediction-only role support: DL-glyceraldehyde'
  finding_ids:
  - rec-f-073ba66f7b3c0851
  target_ids:
  - record-29b97c22d4678505
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/DL-glyceraldehyde.yaml
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
