# Per-record structured review: 3-fucosyllactose (data/ingredients/mapped/3-fucosyllactose.yaml)

- Review: 20261017T083000Z-3-fucosyllactose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-fucosyllactose (data/ingredients/mapped/3-fucosyllactose.yaml, record-10a47d07d73281e9, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-fucosyllactose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-fucosyllactose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-10a47d07d73281e9 | data/ingredients/mapped/3-fucosyllactose.yaml | maintained | 3-fucosyllactose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-10a47d07d73281e9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-10a47d07d73281e9 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-10a47d07d73281e9 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-10a47d07d73281e9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-10a47d07d73281e9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:03:57Z; reviewed SHA-256=42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87; current SHA-256=42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87; hash_changed=False. Reports=["reports/yaml_record_review/3-fucosyllactose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, CAS companion row, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE is only supported by provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-10a47d07d73281e9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-29dd3a02d84d0708: Reassess prediction-only role support: 3'-fucosyllactose

major / open / confirmed; issue key: mim-reconciliation-role-support-10a47d07d73281e9.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-29dd3a02d84d0708

Reassess prediction-only role support: 3'-fucosyllactose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-626b28bb51b4e593 | data/ingredients/mapped/3-fucosyllactose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[361],"raw_equal":true},"docs_rows":[{"identifier":"cas:41312-47-4","line":363,"mapping_status":"MAPPED","ontology_id":"CHEBI:90065","preferred_term":"3'-fucosyllactose"}],"identifier":"cas:41312-47-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:90065","ontology_label":"3-fucosyllactose","ontology_source":"CHEBI"},"preferred_term":"3'-fucosyllactose","sssom_rows":[{"data_row":141,"object_id":"CHEBI:90065","object_label":"3-fucosyllactose","predicate_id":"skos:exactMatch"},{"data_row":142,"object_id":"cas:41312-47-4","object_label":"3'-fucosyllactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-fucosyllactose","synonym_count":2} |
| ev-3a40f33e5eea069b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [361] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-47db87efc48d3bc4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-fucosyllactose; data-row positions=[141,142] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":141,"object_id":"CHEBI:90065","object_label":"3-fucosyllactose","other":"6-deoxy-alpha-L-galactopyranosyl-(1-&gt;3)-[beta-D-galactopyranosyl-(1-&gt;4)]-D-glucopyranose&#124;Fuc(a1-3)[Gal(b1-4)]Glc&#124;CAS:41312-47-4","predicate_id":"skos:exactMatch","subject_id":"MIM:3-fucosyllactose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":142,"object_id":"cas:41312-47-4","object_label":"3'-fucosyllactose","other":"CAS:41312-47-4","predicate_id":"skos:exactMatch","subject_id":"MIM:3-fucosyllactose","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-ea3250acfca50464 | docs/data/mapped_ingredients.csv; CSV lines=[363] | supports | Published identity and count rows inspected: [{"identifier":"cas:41312-47-4","line":363,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:90065","preferred_term":"3'-fucosyllactose","total_occurrences":"0"}] |
| ev-f76a8a41a8388762 | reports/yaml_record_review/3-fucosyllactose.md; &#96;data/ingredients/mapped/3-fucosyllactose.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:39; Completeness:58; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6ac62dfc0854e7b5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[118,1451] | context_only | [{"current_record_sha256":"42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87","finding_id":"SEM:2c78f1c1d2fcb478e748","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87","finding_id":"SEM:464de34546a9ecef9283","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2308d9da0376af6a | data/ingredients/mapped/3-fucosyllactose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-a66252e651a2dbe6 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-29dd3a02d84d0708] | context_only | Predecessor structured review finding f-29dd3a02d84d0708 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-fucosyllactose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-fucosyllactose (data/ingredients/mapped/3-fucosyllactose.yaml)'
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
summary: Per-record structured review for 3-fucosyllactose (data/ingredients/mapped/3-fucosyllactose.yaml,
  record-10a47d07d73281e9, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-fucosyllactose.yaml
    sha256: 42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87
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
  - path: reports/yaml_record_review/3-fucosyllactose.md
    sha256: fdceef9790155a48ec6e3698de9160d9c2f67ec07aadbc51b58c407763bba569
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-10a47d07d73281e9
  path: data/ingredients/mapped/3-fucosyllactose.yaml
  label: 3-fucosyllactose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-fucosyllactose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-fucosyllactose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-fucosyllactose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-10a47d07d73281e9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-10a47d07d73281e9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-10a47d07d73281e9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-10a47d07d73281e9
evidence:
- evidence_id: ev-626b28bb51b4e593
  kind: record_content
  reference: data/ingredients/mapped/3-fucosyllactose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[361],"raw_equal":true},"docs_rows":[{"identifier":"cas:41312-47-4","line":363,"mapping_status":"MAPPED","ontology_id":"CHEBI:90065","preferred_term":"3''-fucosyllactose"}],"identifier":"cas:41312-47-4","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:90065","ontology_label":"3-fucosyllactose","ontology_source":"CHEBI"},"preferred_term":"3''-fucosyllactose","sssom_rows":[{"data_row":141,"object_id":"CHEBI:90065","object_label":"3-fucosyllactose","predicate_id":"skos:exactMatch"},{"data_row":142,"object_id":"cas:41312-47-4","object_label":"3''-fucosyllactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-fucosyllactose","synonym_count":2}'
  snapshot_sha256: 42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87
- evidence_id: ev-3a40f33e5eea069b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [361]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-47db87efc48d3bc4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-fucosyllactose; data-row positions=[141,142]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":141,"object_id":"CHEBI:90065","object_label":"3-fucosyllactose","other":"6-deoxy-alpha-L-galactopyranosyl-(1->3)-[beta-D-galactopyranosyl-(1->4)]-D-glucopyranose|Fuc(a1-3)[Gal(b1-4)]Glc|CAS:41312-47-4","predicate_id":"skos:exactMatch","subject_id":"MIM:3-fucosyllactose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":142,"object_id":"cas:41312-47-4","object_label":"3''-fucosyllactose","other":"CAS:41312-47-4","predicate_id":"skos:exactMatch","subject_id":"MIM:3-fucosyllactose","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ea3250acfca50464
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[363]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:41312-47-4","line":363,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:90065","preferred_term":"3''-fucosyllactose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f76a8a41a8388762
  kind: prior_review
  reference: reports/yaml_record_review/3-fucosyllactose.md
  locator: '`data/ingredients/mapped/3-fucosyllactose.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:39; Completeness:58; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fdceef9790155a48ec6e3698de9160d9c2f67ec07aadbc51b58c407763bba569
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/3-fucosyllactose.yaml`,\
    \ remove\n   `nutritional_roles.CARBON_SOURCE` or replace it with direct medium-use\n\
    \   evidence for this exact fucosyllactose form.\n2. Run the per-record strict\
    \ validator, compare the record against\n   `data/curated/mapped_ingredients.yaml`,\
    \ rebuild the SSSOM/docs with the\n   maintained generators, and then rerun the\
    \ whole-corpus SSSOM and flat-export\n   checks."
- evidence_id: ev-6ac62dfc0854e7b5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[118,1451]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87","finding_id":"SEM:2c78f1c1d2fcb478e748","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87","finding_id":"SEM:464de34546a9ecef9283","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2308d9da0376af6a
  kind: record_content
  reference: data/ingredients/mapped/3-fucosyllactose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87
- evidence_id: ev-a66252e651a2dbe6
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-29dd3a02d84d0708]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-29dd3a02d84d0708 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-9a6ee219a84e27b2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-10a47d07d73281e9
  evidence_ids:
  - ev-626b28bb51b4e593
  - ev-3a40f33e5eea069b
  - ev-47db87efc48d3bc4
  - ev-ea3250acfca50464
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1d34a50343741880
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-10a47d07d73281e9
  evidence_ids:
  - ev-f76a8a41a8388762
  - ev-626b28bb51b4e593
  - ev-6ac62dfc0854e7b5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:03:57Z;
    reviewed SHA-256=42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87;
    current SHA-256=42b31a88125f2631aa30c20666307b40a494373b1a747d36627a6278dd383f87;
    hash_changed=False. Reports=["reports/yaml_record_review/3-fucosyllactose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, CAS companion row, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE
    is only supported by provisional name-pattern evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f76a8a41a8388762
    - ev-626b28bb51b4e593
  - name: legacy-native-ids
    value: '["SEM:2c78f1c1d2fcb478e748","SEM:464de34546a9ecef9283"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-626b28bb51b4e593
    - ev-f76a8a41a8388762
    - ev-6ac62dfc0854e7b5
- assessment_id: a-2308d9da0376af6a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-10a47d07d73281e9
  evidence_ids:
  - ev-f76a8a41a8388762
  - ev-2308d9da0376af6a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f76a8a41a8388762
    - ev-2308d9da0376af6a
findings:
- finding_id: rec-f-29dd3a02d84d0708
  issue_key: mim-reconciliation-role-support-10a47d07d73281e9
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 3''-fucosyllactose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-10a47d07d73281e9
  evidence_ids:
  - ev-f76a8a41a8388762
  - ev-2308d9da0376af6a
  - ev-a66252e651a2dbe6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-fucosyllactose.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-29dd3a02d84d0708
actions:
- action_id: rec-action-29dd3a02d84d0708
  description: 'Reassess prediction-only role support: 3''-fucosyllactose'
  finding_ids:
  - rec-f-29dd3a02d84d0708
  target_ids:
  - record-10a47d07d73281e9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-fucosyllactose.yaml
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
