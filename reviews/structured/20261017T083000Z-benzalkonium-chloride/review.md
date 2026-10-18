# Per-record structured review: Benzalkonium_Chloride (data/ingredients/mapped/Benzalkonium_Chloride.yaml)

- Review: 20261017T083000Z-benzalkonium-chloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Benzalkonium_Chloride (data/ingredients/mapped/Benzalkonium_Chloride.yaml, record-a0cc64987723b82e, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Benzalkonium_Chloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Benzalkonium_Chloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a0cc64987723b82e | data/ingredients/mapped/Benzalkonium_Chloride.yaml | maintained | Benzalkonium_Chloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a0cc64987723b82e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a0cc64987723b82e | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a0cc64987723b82e | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a0cc64987723b82e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: not_applicable. Targets: record-a0cc64987723b82e.

The latest legacy review reports no outstanding finding. This run verifies local consistency only; it does not renew that earlier scientific pass.

Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:26:42Z; reviewed SHA-256=db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09; current SHA-256=db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09; hash_changed=False. Reports=["reports/yaml_record_review/Benzalkonium_Chloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI generic benzalkonium chloride identity, variable-alkyl formula, CAS, surfactant role, SSSOM row, and aggregate copy pass.

### Historical provisional-role concern

evidence: concern. Targets: record-a0cc64987723b82e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-37a95cc1ea0235e4: Reassess prediction-only role support: Benzalkonium Chloride

major / open / confirmed; issue key: mim-reconciliation-role-support-a0cc64987723b82e.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-37a95cc1ea0235e4

Reassess prediction-only role support: Benzalkonium Chloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-60d94bd979ece324 | data/ingredients/mapped/Benzalkonium_Chloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[566],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3020","line":568,"mapping_status":"MAPPED","ontology_id":"CHEBI:3020","preferred_term":"Benzalkonium Chloride"}],"identifier":"CHEBI:3020","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3020","ontology_label":"benzalkonium chloride","ontology_source":"CHEBI"},"preferred_term":"Benzalkonium Chloride","sssom_rows":[{"data_row":504,"object_id":"CHEBI:3020","object_label":"benzalkonium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Benzalkonium_Chloride","synonym_count":0} |
| ev-737362627e10cb9a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [566] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c201ea54325294eb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Benzalkonium_Chloride; data-row positions=[504] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":504,"object_id":"CHEBI:3020","object_label":"benzalkonium chloride","other":"CAS:63449-41-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Benzalkonium_Chloride","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-312cfd7fda1bb24f | docs/data/mapped_ingredients.csv; CSV lines=[568] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3020","line":568,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3020","preferred_term":"Benzalkonium Chloride","total_occurrences":"0"}] |
| ev-9bd5aaa9d2239c8c | reports/yaml_record_review/Benzalkonium_Chloride.md; &#96;data/ingredients/mapped/Benzalkonium_Chloride.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:33; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c585c9db7a8582e9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[2032] | context_only | [{"current_record_sha256":"db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09","finding_id":"SEM:30bb6a31b0ec11205fcf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-143115c8c8526b9e | data/ingredients/mapped/Benzalkonium_Chloride.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[566],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3020","line":568,"mapping_status":"MAPPED","ontology_id":"CHEBI:3020","preferred_term":"Benzalkonium Chloride"}],"identifier":"CHEBI:3020","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3020","ontology_label":"benzalkonium chloride","ontology_source":"CHEBI"},"preferred_term":"Benzalkonium Chloride","sssom_rows":[{"data_row":504,"object_id":"CHEBI:3020","object_label":"benzalkonium chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Benzalkonium_Chloride","synonym_count":0} |
| ev-a75d55a914fab23c | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-37a95cc1ea0235e4] | context_only | Predecessor structured review finding f-37a95cc1ea0235e4 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-benzalkonium-chloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Benzalkonium_Chloride (data/ingredients/mapped/Benzalkonium_Chloride.yaml)'
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
summary: Per-record structured review for Benzalkonium_Chloride (data/ingredients/mapped/Benzalkonium_Chloride.yaml,
  record-a0cc64987723b82e, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Benzalkonium_Chloride.yaml
    sha256: db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09
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
  - path: reports/yaml_record_review/Benzalkonium_Chloride.md
    sha256: 641f032b85a1e34d0dfd0d18f6a18b837aaf5a74f10ea1784004e341f7de705c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a0cc64987723b82e
  path: data/ingredients/mapped/Benzalkonium_Chloride.yaml
  label: Benzalkonium_Chloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Benzalkonium_Chloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Benzalkonium_Chloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Benzalkonium_Chloride.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a0cc64987723b82e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-60d94bd979ece324
  - ev-737362627e10cb9a
  - ev-c201ea54325294eb
  - ev-312cfd7fda1bb24f
  - ev-143115c8c8526b9e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-60d94bd979ece324
  - ev-c585c9db7a8582e9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-9bd5aaa9d2239c8c
  - ev-c585c9db7a8582e9
  - ev-a75d55a914fab23c
evidence:
- evidence_id: ev-60d94bd979ece324
  kind: record_content
  reference: data/ingredients/mapped/Benzalkonium_Chloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[566],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3020","line":568,"mapping_status":"MAPPED","ontology_id":"CHEBI:3020","preferred_term":"Benzalkonium
    Chloride"}],"identifier":"CHEBI:3020","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3020","ontology_label":"benzalkonium
    chloride","ontology_source":"CHEBI"},"preferred_term":"Benzalkonium Chloride","sssom_rows":[{"data_row":504,"object_id":"CHEBI:3020","object_label":"benzalkonium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Benzalkonium_Chloride","synonym_count":0}'
  snapshot_sha256: db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09
- evidence_id: ev-737362627e10cb9a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [566]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c201ea54325294eb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Benzalkonium_Chloride; data-row positions=[504]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":504,"object_id":"CHEBI:3020","object_label":"benzalkonium
    chloride","other":"CAS:63449-41-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Benzalkonium_Chloride","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-312cfd7fda1bb24f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[568]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3020","line":568,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3020","preferred_term":"Benzalkonium
    Chloride","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-9bd5aaa9d2239c8c
  kind: prior_review
  reference: reports/yaml_record_review/Benzalkonium_Chloride.md
  locator: '`data/ingredients/mapped/Benzalkonium_Chloride.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:33; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 641f032b85a1e34d0dfd0d18f6a18b837aaf5a74f10ea1784004e341f7de705c
  quote: 'Recommended Edits:

    - None.'
- evidence_id: ev-c585c9db7a8582e9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[2032]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09","finding_id":"SEM:30bb6a31b0ec11205fcf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-143115c8c8526b9e
  kind: record_content
  reference: data/ingredients/mapped/Benzalkonium_Chloride.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[566],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3020","line":568,"mapping_status":"MAPPED","ontology_id":"CHEBI:3020","preferred_term":"Benzalkonium
    Chloride"}],"identifier":"CHEBI:3020","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3020","ontology_label":"benzalkonium
    chloride","ontology_source":"CHEBI"},"preferred_term":"Benzalkonium Chloride","sssom_rows":[{"data_row":504,"object_id":"CHEBI:3020","object_label":"benzalkonium
    chloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Benzalkonium_Chloride","synonym_count":0}'
  snapshot_sha256: db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09
- evidence_id: ev-a75d55a914fab23c
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-37a95cc1ea0235e4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-37a95cc1ea0235e4 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-a29fd5aa49d3a664
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-60d94bd979ece324
  - ev-737362627e10cb9a
  - ev-c201ea54325294eb
  - ev-312cfd7fda1bb24f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cec4ce0b8d81f99c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: not_applicable
  summary: The latest legacy review reports no outstanding finding. This run verifies
    local consistency only; it does not renew that earlier scientific pass.
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-9bd5aaa9d2239c8c
  - ev-60d94bd979ece324
  - ev-c585c9db7a8582e9
  details: 'Latest manifest verdict=pass; severity=none; reviewed_at=2026-09-16T09:26:42Z;
    reviewed SHA-256=db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09;
    current SHA-256=db303175a982a9ccbd6db7aeb397289847f7dca690c94ebe8f281d8c45094c09;
    hash_changed=False. Reports=["reports/yaml_record_review/Benzalkonium_Chloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI generic benzalkonium chloride identity, variable-alkyl formula, CAS, surfactant
    role, SSSOM row, and aggregate copy pass.'
  dimensions:
  - name: legacy-native-ids
    value: '["SEM:30bb6a31b0ec11205fcf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-60d94bd979ece324
    - ev-9bd5aaa9d2239c8c
    - ev-c585c9db7a8582e9
- assessment_id: a-143115c8c8526b9e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-9bd5aaa9d2239c8c
  - ev-143115c8c8526b9e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-9bd5aaa9d2239c8c
    - ev-143115c8c8526b9e
findings:
- finding_id: rec-f-37a95cc1ea0235e4
  issue_key: mim-reconciliation-role-support-a0cc64987723b82e
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Benzalkonium Chloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a0cc64987723b82e
  evidence_ids:
  - ev-9bd5aaa9d2239c8c
  - ev-143115c8c8526b9e
  - ev-a75d55a914fab23c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Benzalkonium_Chloride.yaml
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
    finding_id: f-37a95cc1ea0235e4
actions:
- action_id: rec-action-37a95cc1ea0235e4
  description: 'Reassess prediction-only role support: Benzalkonium Chloride'
  finding_ids:
  - rec-f-37a95cc1ea0235e4
  target_ids:
  - record-a0cc64987723b82e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Benzalkonium_Chloride.yaml
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
