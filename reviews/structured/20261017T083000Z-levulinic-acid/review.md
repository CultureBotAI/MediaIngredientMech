# Per-record structured review: Levulinic_Acid (data/ingredients/mapped/Levulinic_Acid.yaml)

- Review: 20261017T083000Z-levulinic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Levulinic_Acid (data/ingredients/mapped/Levulinic_Acid.yaml, record-ef691379a1f967a6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Levulinic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Levulinic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ef691379a1f967a6 | data/ingredients/mapped/Levulinic_Acid.yaml | maintained | Levulinic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ef691379a1f967a6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ef691379a1f967a6 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ef691379a1f967a6 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ef691379a1f967a6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ef691379a1f967a6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:20:11Z; reviewed SHA-256=60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d; current SHA-256=60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d; hash_changed=False. Reports=["reports/yaml_record_review/Levulinic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI:45630 identity, CAS value, PubChem structure, occurrence count, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-ef691379a1f967a6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-674cc612729bdbbb: Reassess prediction-only role support: Levulinic Acid

major / open / confirmed; issue key: mim-reconciliation-role-support-ef691379a1f967a6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-674cc612729bdbbb

Reassess prediction-only role support: Levulinic Acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6b576ec71e438677 | data/ingredients/mapped/Levulinic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1299],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45630","line":1301,"mapping_status":"MAPPED","ontology_id":"CHEBI:45630","preferred_term":"Levulinic Acid"}],"identifier":"CHEBI:45630","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:45630","ontology_label":"4-oxopentanoic acid","ontology_source":"CHEBI"},"preferred_term":"Levulinic Acid","sssom_rows":[{"data_row":1689,"object_id":"CHEBI:45630","object_label":"4-oxopentanoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levulinic_Acid","synonym_count":0} |
| ev-f6d4eedec2e96092 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1299] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f134b8482708f32c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Levulinic_Acid; data-row positions=[1689] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1689,"object_id":"CHEBI:45630","object_label":"4-oxopentanoic acid","other":"CAS:123-76-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Levulinic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-5db3b8d9c70484cf | docs/data/mapped_ingredients.csv; CSV lines=[1301] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:45630","line":1301,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:45630","preferred_term":"Levulinic Acid","total_occurrences":"1"}] |
| ev-8e6839cde8cedd16 | reports/yaml_record_review/Levulinic_Acid.md; &#96;data/ingredients/mapped/Levulinic_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:28; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-164d3935419b5830 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[860,1702] | context_only | [{"current_record_sha256":"60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d","finding_id":"SEM:0861fe3b558ecfd19017","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d","finding_id":"SEM:abd2c83b4aac9fdea794","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-73ac72a30e8a0c8a | data/ingredients/mapped/Levulinic_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-458e3483c62accd6 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-674cc612729bdbbb] | context_only | Predecessor structured review finding f-674cc612729bdbbb in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-levulinic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Levulinic_Acid (data/ingredients/mapped/Levulinic_Acid.yaml)'
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
summary: Per-record structured review for Levulinic_Acid (data/ingredients/mapped/Levulinic_Acid.yaml,
  record-ef691379a1f967a6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Levulinic_Acid.yaml
    sha256: 60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d
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
  - path: reports/yaml_record_review/Levulinic_Acid.md
    sha256: af55e7567c1d76be97f727f239a336edeb02af9c782dcd2fcadc8c6742b3aa99
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ef691379a1f967a6
  path: data/ingredients/mapped/Levulinic_Acid.yaml
  label: Levulinic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levulinic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Levulinic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Levulinic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ef691379a1f967a6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ef691379a1f967a6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ef691379a1f967a6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ef691379a1f967a6
evidence:
- evidence_id: ev-6b576ec71e438677
  kind: record_content
  reference: data/ingredients/mapped/Levulinic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1299],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:45630","line":1301,"mapping_status":"MAPPED","ontology_id":"CHEBI:45630","preferred_term":"Levulinic
    Acid"}],"identifier":"CHEBI:45630","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:45630","ontology_label":"4-oxopentanoic
    acid","ontology_source":"CHEBI"},"preferred_term":"Levulinic Acid","sssom_rows":[{"data_row":1689,"object_id":"CHEBI:45630","object_label":"4-oxopentanoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levulinic_Acid","synonym_count":0}'
  snapshot_sha256: 60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d
- evidence_id: ev-f6d4eedec2e96092
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1299]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f134b8482708f32c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Levulinic_Acid; data-row positions=[1689]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1689,"object_id":"CHEBI:45630","object_label":"4-oxopentanoic
    acid","other":"CAS:123-76-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Levulinic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5db3b8d9c70484cf
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1301]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:45630","line":1301,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:45630","preferred_term":"Levulinic
    Acid","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8e6839cde8cedd16
  kind: prior_review
  reference: reports/yaml_record_review/Levulinic_Acid.md
  locator: '`data/ingredients/mapped/Levulinic_Acid.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:28; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: af55e7567c1d76be97f727f239a336edeb02af9c782dcd2fcadc8c6742b3aa99
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Levulinic_Acid.yaml` with inspected source evidence\n\
    \  for exact levulinic acid use, or remove the provisional role.\n- Sync the aggregate\
    \ copy and regenerate derived products after the YAML\n  change; rerun strict,\
    \ term, round-trip, component, and SSSOM validation."
- evidence_id: ev-164d3935419b5830
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[860,1702]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d","finding_id":"SEM:0861fe3b558ecfd19017","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d","finding_id":"SEM:abd2c83b4aac9fdea794","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-73ac72a30e8a0c8a
  kind: record_content
  reference: data/ingredients/mapped/Levulinic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d
- evidence_id: ev-458e3483c62accd6
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-674cc612729bdbbb]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-674cc612729bdbbb in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-377021fef3fbcab1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ef691379a1f967a6
  evidence_ids:
  - ev-6b576ec71e438677
  - ev-f6d4eedec2e96092
  - ev-f134b8482708f32c
  - ev-5db3b8d9c70484cf
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2c71976c45cef541
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ef691379a1f967a6
  evidence_ids:
  - ev-8e6839cde8cedd16
  - ev-6b576ec71e438677
  - ev-164d3935419b5830
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:20:11Z;
    reviewed SHA-256=60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d;
    current SHA-256=60348b221a8383646fbebd9deff7b07a6c6f701830401e59343742e9c72c1a5d;
    hash_changed=False. Reports=["reports/yaml_record_review/Levulinic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-backed
    CHEBI:45630 identity, CAS value, PubChem structure, occurrence count, and final
    SSSOM row pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8e6839cde8cedd16
    - ev-6b576ec71e438677
  - name: legacy-native-ids
    value: '["SEM:0861fe3b558ecfd19017","SEM:abd2c83b4aac9fdea794"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6b576ec71e438677
    - ev-8e6839cde8cedd16
    - ev-164d3935419b5830
- assessment_id: a-73ac72a30e8a0c8a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ef691379a1f967a6
  evidence_ids:
  - ev-8e6839cde8cedd16
  - ev-73ac72a30e8a0c8a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8e6839cde8cedd16
    - ev-73ac72a30e8a0c8a
findings:
- finding_id: rec-f-674cc612729bdbbb
  issue_key: mim-reconciliation-role-support-ef691379a1f967a6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Levulinic Acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ef691379a1f967a6
  evidence_ids:
  - ev-8e6839cde8cedd16
  - ev-73ac72a30e8a0c8a
  - ev-458e3483c62accd6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levulinic_Acid.yaml
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
    finding_id: f-674cc612729bdbbb
actions:
- action_id: rec-action-674cc612729bdbbb
  description: 'Reassess prediction-only role support: Levulinic Acid'
  finding_ids:
  - rec-f-674cc612729bdbbb
  target_ids:
  - record-ef691379a1f967a6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levulinic_Acid.yaml
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
