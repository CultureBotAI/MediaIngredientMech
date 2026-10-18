# Per-record structured review: Malate (data/ingredients/mapped/Malate.yaml)

- Review: 20261017T083000Z-malate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Malate (data/ingredients/mapped/Malate.yaml, record-e23320615cf965b8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Malate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Malate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e23320615cf965b8 | data/ingredients/mapped/Malate.yaml | maintained | Malate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e23320615cf965b8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e23320615cf965b8 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e23320615cf965b8 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e23320615cf965b8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e23320615cf965b8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:19:00Z; reviewed SHA-256=62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719; current SHA-256=62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719; hash_changed=False. Reports=["reports/yaml_record_review/Malate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:25115 identity and exact synonyms pass, but final SSSOM exports a neutral malic-acid CAS token and the carbon/energy roles are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-e23320615cf965b8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1376b826c07c855b: Reassess prediction-only role support: Malate

major / open / confirmed; issue key: mim-reconciliation-role-support-e23320615cf965b8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1376b826c07c855b

Reassess prediction-only role support: Malate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bb358622baca62ce | data/ingredients/mapped/Malate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1329],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25115","line":1331,"mapping_status":"MAPPED","ontology_id":"CHEBI:25115","preferred_term":"Malate"}],"identifier":"CHEBI:25115","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:25115","ontology_label":"malate","ontology_source":"CHEBI"},"preferred_term":"Malate","sssom_rows":[{"data_row":1748,"object_id":"CHEBI:25115","object_label":"malate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Malate","synonym_count":2} |
| ev-e02fdf831a00f715 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1329] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6ae0c79bb5c78d18 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Malate; data-row positions=[1748] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1748,"object_id":"CHEBI:25115","object_label":"malate","other":"malates&#124;malic acid anion&#124;CAS:6915-15-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Malate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-bf8420df2882ff58 | docs/data/mapped_ingredients.csv; CSV lines=[1331] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:25115","line":1331,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:25115","preferred_term":"Malate","total_occurrences":"2"}] |
| ev-6b550d59ccf0516b | reports/yaml_record_review/Malate.md; &#96;data/ingredients/mapped/Malate.yaml&#96;:2; Verdict:4; Identity:13; Validation:22; Evidence:30; Completeness:41; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c5dbd2ddb24d9ea8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[884,1589,1811] | context_only | [{"current_record_sha256":"62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719","finding_id":"SEM:e1ad8f62b672883bbe18","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719","finding_id":"SEM:710043382c2059b1d399","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719","finding_id":"SEM:7098abffd0cfc278cb3e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-72448ac34d84012d | data/ingredients/mapped/Malate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1329],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25115","line":1331,"mapping_status":"MAPPED","ontology_id":"CHEBI:25115","preferred_term":"Malate"}],"identifier":"CHEBI:25115","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:25115","ontology_label":"malate","ontology_source":"CHEBI"},"preferred_term":"Malate","sssom_rows":[{"data_row":1748,"object_id":"CHEBI:25115","object_label":"malate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Malate","synonym_count":2} |
| ev-5d1bea0e6d83251e | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-1376b826c07c855b] | context_only | Predecessor structured review finding f-1376b826c07c855b in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-malate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Malate (data/ingredients/mapped/Malate.yaml)'
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
summary: Per-record structured review for Malate (data/ingredients/mapped/Malate.yaml,
  record-e23320615cf965b8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Malate.yaml
    sha256: 62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719
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
  - path: reports/yaml_record_review/Malate.md
    sha256: 4494ed6ef4f64c656929e28d6e6aa66ac76ed2d3aac3c5ee821a945a75e90a67
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e23320615cf965b8
  path: data/ingredients/mapped/Malate.yaml
  label: Malate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Malate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Malate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Malate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e23320615cf965b8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-bb358622baca62ce
  - ev-e02fdf831a00f715
  - ev-6ae0c79bb5c78d18
  - ev-bf8420df2882ff58
  - ev-72448ac34d84012d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-bb358622baca62ce
  - ev-c5dbd2ddb24d9ea8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-6b550d59ccf0516b
  - ev-c5dbd2ddb24d9ea8
  - ev-5d1bea0e6d83251e
evidence:
- evidence_id: ev-bb358622baca62ce
  kind: record_content
  reference: data/ingredients/mapped/Malate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1329],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25115","line":1331,"mapping_status":"MAPPED","ontology_id":"CHEBI:25115","preferred_term":"Malate"}],"identifier":"CHEBI:25115","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:25115","ontology_label":"malate","ontology_source":"CHEBI"},"preferred_term":"Malate","sssom_rows":[{"data_row":1748,"object_id":"CHEBI:25115","object_label":"malate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Malate","synonym_count":2}'
  snapshot_sha256: 62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719
- evidence_id: ev-e02fdf831a00f715
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1329]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6ae0c79bb5c78d18
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Malate; data-row positions=[1748]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1748,"object_id":"CHEBI:25115","object_label":"malate","other":"malates|malic
    acid anion|CAS:6915-15-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Malate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bf8420df2882ff58
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1331]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:25115","line":1331,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:25115","preferred_term":"Malate","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6b550d59ccf0516b
  kind: prior_review
  reference: reports/yaml_record_review/Malate.md
  locator: '`data/ingredients/mapped/Malate.yaml`:2; Verdict:4; Identity:13; Validation:22;
    Evidence:30; Completeness:41; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4494ed6ef4f64c656929e28d6e6aa66ac76ed2d3aac3c5ee821a945a75e90a67
  quote: "Recommended Edits:\n- Remove `chemical_properties.cas_rn: 6915-15-7` from\
    \ `Malate` or replace it\n  only with an exact registry identifier for `CHEBI:25115`.\n\
    - Remove the provisional `CARBON_SOURCE` and `ENERGY_SOURCE` facets unless\n \
    \ source-backed evidence can be attached."
- evidence_id: ev-c5dbd2ddb24d9ea8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[884,1589,1811]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719","finding_id":"SEM:e1ad8f62b672883bbe18","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719","finding_id":"SEM:710043382c2059b1d399","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719","finding_id":"SEM:7098abffd0cfc278cb3e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-72448ac34d84012d
  kind: record_content
  reference: data/ingredients/mapped/Malate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1329],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:25115","line":1331,"mapping_status":"MAPPED","ontology_id":"CHEBI:25115","preferred_term":"Malate"}],"identifier":"CHEBI:25115","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:25115","ontology_label":"malate","ontology_source":"CHEBI"},"preferred_term":"Malate","sssom_rows":[{"data_row":1748,"object_id":"CHEBI:25115","object_label":"malate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Malate","synonym_count":2}'
  snapshot_sha256: 62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719
- evidence_id: ev-5d1bea0e6d83251e
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-1376b826c07c855b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1376b826c07c855b in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-7a0c88fce9a7af2e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-bb358622baca62ce
  - ev-e02fdf831a00f715
  - ev-6ae0c79bb5c78d18
  - ev-bf8420df2882ff58
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-dff54fe07b278bf8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-6b550d59ccf0516b
  - ev-bb358622baca62ce
  - ev-c5dbd2ddb24d9ea8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:19:00Z;
    reviewed SHA-256=62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719;
    current SHA-256=62a8259a7530c278262cde1b866c602f96c494a805488eb0e5d27ba49c6f5719;
    hash_changed=False. Reports=["reports/yaml_record_review/Malate.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:25115 identity
    and exact synonyms pass, but final SSSOM exports a neutral malic-acid CAS token
    and the carbon/energy roles are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6b550d59ccf0516b
    - ev-bb358622baca62ce
  - name: legacy-native-ids
    value: '["SEM:e1ad8f62b672883bbe18","SEM:710043382c2059b1d399","SEM:7098abffd0cfc278cb3e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bb358622baca62ce
    - ev-6b550d59ccf0516b
    - ev-c5dbd2ddb24d9ea8
- assessment_id: a-72448ac34d84012d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-6b550d59ccf0516b
  - ev-72448ac34d84012d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6b550d59ccf0516b
    - ev-72448ac34d84012d
findings:
- finding_id: rec-f-1376b826c07c855b
  issue_key: mim-reconciliation-role-support-e23320615cf965b8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Malate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e23320615cf965b8
  evidence_ids:
  - ev-6b550d59ccf0516b
  - ev-72448ac34d84012d
  - ev-5d1bea0e6d83251e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Malate.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-1376b826c07c855b
actions:
- action_id: rec-action-1376b826c07c855b
  description: 'Reassess prediction-only role support: Malate'
  finding_ids:
  - rec-f-1376b826c07c855b
  target_ids:
  - record-e23320615cf965b8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Malate.yaml
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
