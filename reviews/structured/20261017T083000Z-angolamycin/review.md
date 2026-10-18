# Per-record structured review: Angolamycin (data/ingredients/mapped/Angolamycin.yaml)

- Review: 20261017T083000Z-angolamycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Angolamycin (data/ingredients/mapped/Angolamycin.yaml, record-4ca81146caf15a17, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Angolamycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Angolamycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4ca81146caf15a17 | data/ingredients/mapped/Angolamycin.yaml | maintained | Angolamycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4ca81146caf15a17 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4ca81146caf15a17 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4ca81146caf15a17 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4ca81146caf15a17.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4ca81146caf15a17.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:17:18Z; reviewed SHA-256=f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46; current SHA-256=f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46; hash_changed=False. Reports=["reports/yaml_record_review/Angolamycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MeSH identity, SSSOM row, and row-review disposition pass, but the selective-agent role is only a computational name-pattern inference.

### Historical provisional-role concern

evidence: concern. Targets: record-4ca81146caf15a17.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6a2af12b1fce30b3: Reassess prediction-only role support: Angolamycin

major / open / confirmed; issue key: mim-reconciliation-role-support-4ca81146caf15a17.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6a2af12b1fce30b3

Reassess prediction-only role support: Angolamycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-80d5af41ca949ffb | data/ingredients/mapped/Angolamycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[496],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C002547","line":498,"mapping_status":"MAPPED","ontology_id":"mesh:C002547","preferred_term":"Angolamycin"}],"identifier":"mesh:C002547","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C002547","ontology_label":"angolamycin","ontology_source":"MESH"},"preferred_term":"Angolamycin","sssom_rows":[{"data_row":383,"object_id":"mesh:C002547","object_label":"angolamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Angolamycin","synonym_count":0} |
| ev-80a93dbfa382b7b4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [496] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c0e77d4602e9584e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Angolamycin; data-row positions=[383] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":383,"object_id":"mesh:C002547","object_label":"angolamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Angolamycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-2f1bc62a857c19bd | docs/data/mapped_ingredients.csv; CSV lines=[498] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C002547","line":498,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C002547","preferred_term":"Angolamycin","total_occurrences":"0"}] |
| ev-1754df56911ad503 | reports/yaml_record_review/Angolamycin.md; &#96;data/ingredients/mapped/Angolamycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:34; Completeness:51; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5a7d98ded542c5f9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[260,1406] | context_only | [{"current_record_sha256":"f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46","finding_id":"SEM:5de5adf89b6d073e0b16","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46","finding_id":"SEM:38cfe88b3aef57329599","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-574c5997a1e38f61 | data/ingredients/mapped/Angolamycin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[496],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C002547","line":498,"mapping_status":"MAPPED","ontology_id":"mesh:C002547","preferred_term":"Angolamycin"}],"identifier":"mesh:C002547","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C002547","ontology_label":"angolamycin","ontology_source":"MESH"},"preferred_term":"Angolamycin","sssom_rows":[{"data_row":383,"object_id":"mesh:C002547","object_label":"angolamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Angolamycin","synonym_count":0} |
| ev-9887ccddef6807f0 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-6a2af12b1fce30b3] | context_only | Predecessor structured review finding f-6a2af12b1fce30b3 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-angolamycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Angolamycin (data/ingredients/mapped/Angolamycin.yaml)'
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
summary: Per-record structured review for Angolamycin (data/ingredients/mapped/Angolamycin.yaml,
  record-4ca81146caf15a17, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Angolamycin.yaml
    sha256: f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Angolamycin.md
    sha256: 730b72e1dbe843bbdb53374347e106b138f38a713f4fe928bf8e16fd9728cb4b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4ca81146caf15a17
  path: data/ingredients/mapped/Angolamycin.yaml
  label: Angolamycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Angolamycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Angolamycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Angolamycin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4ca81146caf15a17
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-80d5af41ca949ffb
  - ev-80a93dbfa382b7b4
  - ev-c0e77d4602e9584e
  - ev-2f1bc62a857c19bd
  - ev-574c5997a1e38f61
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-80d5af41ca949ffb
  - ev-5a7d98ded542c5f9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-1754df56911ad503
  - ev-5a7d98ded542c5f9
  - ev-9887ccddef6807f0
evidence:
- evidence_id: ev-80d5af41ca949ffb
  kind: record_content
  reference: data/ingredients/mapped/Angolamycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[496],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C002547","line":498,"mapping_status":"MAPPED","ontology_id":"mesh:C002547","preferred_term":"Angolamycin"}],"identifier":"mesh:C002547","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C002547","ontology_label":"angolamycin","ontology_source":"MESH"},"preferred_term":"Angolamycin","sssom_rows":[{"data_row":383,"object_id":"mesh:C002547","object_label":"angolamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Angolamycin","synonym_count":0}'
  snapshot_sha256: f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46
- evidence_id: ev-80a93dbfa382b7b4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [496]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c0e77d4602e9584e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Angolamycin; data-row positions=[383]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":383,"object_id":"mesh:C002547","object_label":"angolamycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Angolamycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2f1bc62a857c19bd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[498]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C002547","line":498,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C002547","preferred_term":"Angolamycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1754df56911ad503
  kind: prior_review
  reference: reports/yaml_record_review/Angolamycin.md
  locator: '`data/ingredients/mapped/Angolamycin.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:34; Completeness:51; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 730b72e1dbe843bbdb53374347e106b138f38a713f4fe928bf8e16fd9728cb4b
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Angolamycin.yaml`, replace\
    \ the\n  `SELECTIVE_AGENT` computational prediction with source-backed evidence,\
    \ or\n  remove it.\n- Regenerate synchronized products, then rerun\n  `uv run\
    \ --frozen python scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/Angolamycin.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-5a7d98ded542c5f9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[260,1406]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46","finding_id":"SEM:5de5adf89b6d073e0b16","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46","finding_id":"SEM:38cfe88b3aef57329599","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-574c5997a1e38f61
  kind: record_content
  reference: data/ingredients/mapped/Angolamycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[496],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C002547","line":498,"mapping_status":"MAPPED","ontology_id":"mesh:C002547","preferred_term":"Angolamycin"}],"identifier":"mesh:C002547","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C002547","ontology_label":"angolamycin","ontology_source":"MESH"},"preferred_term":"Angolamycin","sssom_rows":[{"data_row":383,"object_id":"mesh:C002547","object_label":"angolamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Angolamycin","synonym_count":0}'
  snapshot_sha256: f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46
- evidence_id: ev-9887ccddef6807f0
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-6a2af12b1fce30b3]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6a2af12b1fce30b3 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-d392de6517b0e824
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-80d5af41ca949ffb
  - ev-80a93dbfa382b7b4
  - ev-c0e77d4602e9584e
  - ev-2f1bc62a857c19bd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-62acf27085ff220b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-1754df56911ad503
  - ev-80d5af41ca949ffb
  - ev-5a7d98ded542c5f9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:17:18Z;
    reviewed SHA-256=f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46;
    current SHA-256=f6e9c5f989543b3e94db17124b1c4d30f742346e5258b6a5bbe1dd46ab7cca46;
    hash_changed=False. Reports=["reports/yaml_record_review/Angolamycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact MeSH
    identity, SSSOM row, and row-review disposition pass, but the selective-agent
    role is only a computational name-pattern inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1754df56911ad503
    - ev-80d5af41ca949ffb
  - name: legacy-native-ids
    value: '["SEM:5de5adf89b6d073e0b16","SEM:38cfe88b3aef57329599"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-80d5af41ca949ffb
    - ev-1754df56911ad503
    - ev-5a7d98ded542c5f9
- assessment_id: a-574c5997a1e38f61
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-1754df56911ad503
  - ev-574c5997a1e38f61
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1754df56911ad503
    - ev-574c5997a1e38f61
findings:
- finding_id: rec-f-6a2af12b1fce30b3
  issue_key: mim-reconciliation-role-support-4ca81146caf15a17
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Angolamycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4ca81146caf15a17
  evidence_ids:
  - ev-1754df56911ad503
  - ev-574c5997a1e38f61
  - ev-9887ccddef6807f0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Angolamycin.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-6a2af12b1fce30b3
actions:
- action_id: rec-action-6a2af12b1fce30b3
  description: 'Reassess prediction-only role support: Angolamycin'
  finding_ids:
  - rec-f-6a2af12b1fce30b3
  target_ids:
  - record-4ca81146caf15a17
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Angolamycin.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
