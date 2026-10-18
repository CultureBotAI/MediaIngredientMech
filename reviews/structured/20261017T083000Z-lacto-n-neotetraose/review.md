# Per-record structured review: Lacto-N-neotetraose (data/ingredients/mapped/Lacto-N-neotetraose.yaml)

- Review: 20261017T083000Z-lacto-n-neotetraose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lacto-N-neotetraose (data/ingredients/mapped/Lacto-N-neotetraose.yaml, record-40684f464baa618a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lacto-N-neotetraose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lacto-N-neotetraose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-40684f464baa618a | data/ingredients/mapped/Lacto-N-neotetraose.yaml | maintained | Lacto-N-neotetraose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-40684f464baa618a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-40684f464baa618a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-40684f464baa618a | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-40684f464baa618a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-40684f464baa618a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:49:27Z; reviewed SHA-256=96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302; current SHA-256=96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302; hash_changed=False. Reports=["reports/yaml_record_review/Lacto-N-neotetraose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI:60239 label, structure, synonym, and final SSSOM row pass, but the CAS-RN lookup conflicts with PubChem's current CAS/name target and CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-40684f464baa618a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-7dfb945c87a970e5: Reassess prediction-only role support: Lacto-N-neotetraose

major / open / confirmed; issue key: mim-reconciliation-role-support-40684f464baa618a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-7dfb945c87a970e5

Reassess prediction-only role support: Lacto-N-neotetraose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-be651cfb5ae5543a | data/ingredients/mapped/Lacto-N-neotetraose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1279],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:60239","line":1281,"mapping_status":"MAPPED","ontology_id":"CHEBI:60239","preferred_term":"Lacto-N-neotetraose"}],"identifier":"CHEBI:60239","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:60239","ontology_label":"beta-D-Gal-(1-&gt;4)-beta-D-GlcNAc-(1-&gt;3)-beta-D-Gal-(1-&gt;4)-D-Glc","ontology_source":"CHEBI"},"preferred_term":"Lacto-N-neotetraose","sssom_rows":[{"data_row":1662,"object_id":"CHEBI:60239","object_label":"beta-D-Gal-(1-&gt;4)-beta-D-GlcNAc-(1-&gt;3)-beta-D-Gal-(1-&gt;4)-D-Glc","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-neotetraose","synonym_count":1} |
| ev-8b1625a6d9f22285 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1279] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c22665cdfbb1edbe | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lacto-N-neotetraose; data-row positions=[1662] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1662,"object_id":"CHEBI:60239","object_label":"beta-D-Gal-(1-&gt;4)-beta-D-GlcNAc-(1-&gt;3)-beta-D-Gal-(1-&gt;4)-D-Glc","other":"beta-D-galactopyranosyl-(1-&gt;4)-2-acetamido-2-deoxy-beta-D-glucopyranosyl-(1-&gt;3)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose&#124;CAS:13007-32-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-neotetraose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-b94e2ba1e435ce11 | docs/data/mapped_ingredients.csv; CSV lines=[1281] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:60239","line":1281,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:60239","preferred_term":"Lacto-N-neotetraose","total_occurrences":"0"}] |
| ev-da25c18146e9d7ae | reports/yaml_record_review/Lacto-N-neotetraose.md; &#96;data/ingredients/mapped/Lacto-N-neotetraose.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:30; Completeness:52; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8fe3affc23d73482 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[848,1601] | context_only | [{"current_record_sha256":"96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302","finding_id":"SEM:914ef3da90ed03aa4ceb","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302","finding_id":"SEM:2eda2ccaa97354c6609f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-af08f16b1666e9d5 | data/ingredients/mapped/Lacto-N-neotetraose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-ead69adc51309c86 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-7dfb945c87a970e5] | context_only | Predecessor structured review finding f-7dfb945c87a970e5 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lacto-n-neotetraose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lacto-N-neotetraose (data/ingredients/mapped/Lacto-N-neotetraose.yaml)'
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
summary: Per-record structured review for Lacto-N-neotetraose (data/ingredients/mapped/Lacto-N-neotetraose.yaml,
  record-40684f464baa618a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lacto-N-neotetraose.yaml
    sha256: 96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Lacto-N-neotetraose.md
    sha256: b24bf0526f5c89781b42c84b0c6523347998a25669400c692c59a1b002f5079b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-40684f464baa618a
  path: data/ingredients/mapped/Lacto-N-neotetraose.yaml
  label: Lacto-N-neotetraose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-neotetraose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lacto-N-neotetraose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lacto-N-neotetraose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-40684f464baa618a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-40684f464baa618a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-40684f464baa618a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-40684f464baa618a
evidence:
- evidence_id: ev-be651cfb5ae5543a
  kind: record_content
  reference: data/ingredients/mapped/Lacto-N-neotetraose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1279],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:60239","line":1281,"mapping_status":"MAPPED","ontology_id":"CHEBI:60239","preferred_term":"Lacto-N-neotetraose"}],"identifier":"CHEBI:60239","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:60239","ontology_label":"beta-D-Gal-(1->4)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc","ontology_source":"CHEBI"},"preferred_term":"Lacto-N-neotetraose","sssom_rows":[{"data_row":1662,"object_id":"CHEBI:60239","object_label":"beta-D-Gal-(1->4)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-neotetraose","synonym_count":1}'
  snapshot_sha256: 96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302
- evidence_id: ev-8b1625a6d9f22285
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1279]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c22665cdfbb1edbe
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lacto-N-neotetraose; data-row positions=[1662]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1662,"object_id":"CHEBI:60239","object_label":"beta-D-Gal-(1->4)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc","other":"beta-D-galactopyranosyl-(1->4)-2-acetamido-2-deoxy-beta-D-glucopyranosyl-(1->3)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose|CAS:13007-32-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-neotetraose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b94e2ba1e435ce11
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1281]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:60239","line":1281,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:60239","preferred_term":"Lacto-N-neotetraose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-da25c18146e9d7ae
  kind: prior_review
  reference: reports/yaml_record_review/Lacto-N-neotetraose.md
  locator: '`data/ingredients/mapped/Lacto-N-neotetraose.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:30; Completeness:52; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b24bf0526f5c89781b42c84b0c6523347998a25669400c692c59a1b002f5079b
  quote: "Recommended Edits:\n- Major: resolve CAS RN `13007-32-4` against `CHEBI:60239`\
    \ and PubChem CIDs\n  `121853` and `9831622`; then either keep the current ChEBI\
    \ grounding with\n  reviewed CAS provenance, move the CAS value off this record,\
    \ or remap if the\n  CultureBotHT row denoted the PubChem CID instead.\n- Major:\
    \ either replace `nutritional_roles.CARBON_SOURCE` with inspected source\n  evidence\
    \ for exact Lacto-N-neotetraose use, or remove the provisional role.\n- Sync the\
    \ aggregate copy and regenerate final SSSOM after any YAML changes;\n  rerun strict,\
    \ term, product, component, and SSSOM validation."
- evidence_id: ev-8fe3affc23d73482
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[848,1601]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302","finding_id":"SEM:914ef3da90ed03aa4ceb","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302","finding_id":"SEM:2eda2ccaa97354c6609f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-af08f16b1666e9d5
  kind: record_content
  reference: data/ingredients/mapped/Lacto-N-neotetraose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302
- evidence_id: ev-ead69adc51309c86
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-7dfb945c87a970e5]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-7dfb945c87a970e5 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-49eadbb88476ff65
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-40684f464baa618a
  evidence_ids:
  - ev-be651cfb5ae5543a
  - ev-8b1625a6d9f22285
  - ev-c22665cdfbb1edbe
  - ev-b94e2ba1e435ce11
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3685b5eb9bf3f739
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-40684f464baa618a
  evidence_ids:
  - ev-da25c18146e9d7ae
  - ev-be651cfb5ae5543a
  - ev-8fe3affc23d73482
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:49:27Z;
    reviewed SHA-256=96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302;
    current SHA-256=96913ee317684409b9ac54446e0bd005fc66f989ffa0c06a8b48a85b96cbc302;
    hash_changed=False. Reports=["reports/yaml_record_review/Lacto-N-neotetraose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI:60239
    label, structure, synonym, and final SSSOM row pass, but the CAS-RN lookup conflicts
    with PubChem''s current CAS/name target and CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-da25c18146e9d7ae
    - ev-be651cfb5ae5543a
  - name: legacy-native-ids
    value: '["SEM:914ef3da90ed03aa4ceb","SEM:2eda2ccaa97354c6609f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-be651cfb5ae5543a
    - ev-da25c18146e9d7ae
    - ev-8fe3affc23d73482
- assessment_id: a-af08f16b1666e9d5
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-40684f464baa618a
  evidence_ids:
  - ev-da25c18146e9d7ae
  - ev-af08f16b1666e9d5
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-da25c18146e9d7ae
    - ev-af08f16b1666e9d5
findings:
- finding_id: rec-f-7dfb945c87a970e5
  issue_key: mim-reconciliation-role-support-40684f464baa618a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lacto-N-neotetraose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-40684f464baa618a
  evidence_ids:
  - ev-da25c18146e9d7ae
  - ev-af08f16b1666e9d5
  - ev-ead69adc51309c86
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-neotetraose.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-7dfb945c87a970e5
actions:
- action_id: rec-action-7dfb945c87a970e5
  description: 'Reassess prediction-only role support: Lacto-N-neotetraose'
  finding_ids:
  - rec-f-7dfb945c87a970e5
  target_ids:
  - record-40684f464baa618a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-neotetraose.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
