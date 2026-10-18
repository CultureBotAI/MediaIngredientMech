# Per-record structured review: 2-fucosyllactose (data/ingredients/mapped/2-fucosyllactose.yaml)

- Review: 20261017T083000Z-2-fucosyllactose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 2-fucosyllactose (data/ingredients/mapped/2-fucosyllactose.yaml, record-addf66acec2d0722, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/2-fucosyllactose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/2-fucosyllactose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-addf66acec2d0722 | data/ingredients/mapped/2-fucosyllactose.yaml | maintained | 2-fucosyllactose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-addf66acec2d0722 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-addf66acec2d0722 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-addf66acec2d0722 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-addf66acec2d0722.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-addf66acec2d0722.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:42:43Z; reviewed SHA-256=bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a; current SHA-256=bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a; hash_changed=False. Reports=["reports/yaml_record_review/2-fucosyllactose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CHEBI identity, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE is only supported by provisional ChEBI-ancestry evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-addf66acec2d0722.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f65270519936776b: Reassess prediction-only role support: 2'-fucosyllactose

major / open / confirmed; issue key: mim-reconciliation-role-support-addf66acec2d0722.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f65270519936776b

Reassess prediction-only role support: 2'-fucosyllactose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4a92de13204ef2b7 | data/ingredients/mapped/2-fucosyllactose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[325],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:147155","line":327,"mapping_status":"MAPPED","ontology_id":"CHEBI:147155","preferred_term":"2'-fucosyllactose"}],"identifier":"CHEBI:147155","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:147155","ontology_label":"2'-fucosyllactose","ontology_source":"CHEBI"},"preferred_term":"2'-fucosyllactose","sssom_rows":[{"data_row":85,"object_id":"CHEBI:147155","object_label":"2'-fucosyllactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-fucosyllactose","synonym_count":1} |
| ev-982eae19e69fc438 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [325] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e32f8c2e73806055 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:2-fucosyllactose; data-row positions=[85] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":85,"object_id":"CHEBI:147155","object_label":"2'-fucosyllactose","other":"6-deoxy-alpha-L-galactopyranosyl-(1-&gt;2)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose&#124;CAS:41263-94-9","predicate_id":"skos:exactMatch","subject_id":"MIM:2-fucosyllactose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-24df2b9506ea2213 | docs/data/mapped_ingredients.csv; CSV lines=[327] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:147155","line":327,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:147155","preferred_term":"2'-fucosyllactose","total_occurrences":"0"}] |
| ev-2e0705894104cb5a | reports/yaml_record_review/2-fucosyllactose.md; &#96;data/ingredients/mapped/2-fucosyllactose.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:33; Completeness:49; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f8d0fcaae77b3e9d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[68,1704] | context_only | [{"current_record_sha256":"bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a","finding_id":"SEM:1c6d4de53209519ee45f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a","finding_id":"SEM:a2cc60a5d40561c393b1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2b2b884e9f843c6a | data/ingredients/mapped/2-fucosyllactose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-4e13b2c3ff172c51 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-f65270519936776b] | context_only | Predecessor structured review finding f-f65270519936776b in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-2-fucosyllactose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 2-fucosyllactose (data/ingredients/mapped/2-fucosyllactose.yaml)'
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
summary: Per-record structured review for 2-fucosyllactose (data/ingredients/mapped/2-fucosyllactose.yaml,
  record-addf66acec2d0722, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/2-fucosyllactose.yaml
    sha256: bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a
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
  - path: reports/yaml_record_review/2-fucosyllactose.md
    sha256: 4d575e731a06140a1404fc3d52e5f18f77945314e116bd36f28e3a3e97a58221
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-addf66acec2d0722
  path: data/ingredients/mapped/2-fucosyllactose.yaml
  label: 2-fucosyllactose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-fucosyllactose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/2-fucosyllactose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/2-fucosyllactose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-addf66acec2d0722
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-addf66acec2d0722
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-addf66acec2d0722
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-addf66acec2d0722
evidence:
- evidence_id: ev-4a92de13204ef2b7
  kind: record_content
  reference: data/ingredients/mapped/2-fucosyllactose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[325],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:147155","line":327,"mapping_status":"MAPPED","ontology_id":"CHEBI:147155","preferred_term":"2''-fucosyllactose"}],"identifier":"CHEBI:147155","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:147155","ontology_label":"2''-fucosyllactose","ontology_source":"CHEBI"},"preferred_term":"2''-fucosyllactose","sssom_rows":[{"data_row":85,"object_id":"CHEBI:147155","object_label":"2''-fucosyllactose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:2-fucosyllactose","synonym_count":1}'
  snapshot_sha256: bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a
- evidence_id: ev-982eae19e69fc438
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [325]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e32f8c2e73806055
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:2-fucosyllactose; data-row positions=[85]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":85,"object_id":"CHEBI:147155","object_label":"2''-fucosyllactose","other":"6-deoxy-alpha-L-galactopyranosyl-(1->2)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose|CAS:41263-94-9","predicate_id":"skos:exactMatch","subject_id":"MIM:2-fucosyllactose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-24df2b9506ea2213
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[327]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:147155","line":327,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:147155","preferred_term":"2''-fucosyllactose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2e0705894104cb5a
  kind: prior_review
  reference: reports/yaml_record_review/2-fucosyllactose.md
  locator: '`data/ingredients/mapped/2-fucosyllactose.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:33; Completeness:49; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4d575e731a06140a1404fc3d52e5f18f77945314e116bd36f28e3a3e97a58221
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/2-fucosyllactose.yaml`,\
    \ either remove the\n   provisional `CARBON_SOURCE` role or replace it with inspected\n\
    \   formulation-specific evidence that directly supports this exact ingredient\n\
    \   as a carbon source.\n2. Regenerate `data/curated/mapped_ingredients.yaml`,\n\
    \   `mappings/ingredient_mappings.sssom.tsv`, and docs from the maintained YAML.\n\
    3. Re-run the focused strict/LinkML validators and the full role/evidence\n  \
    \ checks after the role edit."
- evidence_id: ev-f8d0fcaae77b3e9d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[68,1704]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a","finding_id":"SEM:1c6d4de53209519ee45f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a","finding_id":"SEM:a2cc60a5d40561c393b1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2b2b884e9f843c6a
  kind: record_content
  reference: data/ingredients/mapped/2-fucosyllactose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a
- evidence_id: ev-4e13b2c3ff172c51
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-f65270519936776b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f65270519936776b in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-b241e76ec4234e27
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-addf66acec2d0722
  evidence_ids:
  - ev-4a92de13204ef2b7
  - ev-982eae19e69fc438
  - ev-e32f8c2e73806055
  - ev-24df2b9506ea2213
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3542b3c77e18aa1b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-addf66acec2d0722
  evidence_ids:
  - ev-2e0705894104cb5a
  - ev-4a92de13204ef2b7
  - ev-f8d0fcaae77b3e9d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T05:42:43Z;
    reviewed SHA-256=bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a;
    current SHA-256=bde00bf7772e8836de3a18247e7ba65b7a04c6242c5b59e16e35c97890ebb87a;
    hash_changed=False. Reports=["reports/yaml_record_review/2-fucosyllactose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CHEBI
    identity, chemistry, SSSOM, and aggregate pass, but CARBON_SOURCE is only supported
    by provisional ChEBI-ancestry evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2e0705894104cb5a
    - ev-4a92de13204ef2b7
  - name: legacy-native-ids
    value: '["SEM:1c6d4de53209519ee45f","SEM:a2cc60a5d40561c393b1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4a92de13204ef2b7
    - ev-2e0705894104cb5a
    - ev-f8d0fcaae77b3e9d
- assessment_id: a-2b2b884e9f843c6a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-addf66acec2d0722
  evidence_ids:
  - ev-2e0705894104cb5a
  - ev-2b2b884e9f843c6a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2e0705894104cb5a
    - ev-2b2b884e9f843c6a
findings:
- finding_id: rec-f-f65270519936776b
  issue_key: mim-reconciliation-role-support-addf66acec2d0722
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 2''-fucosyllactose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-addf66acec2d0722
  evidence_ids:
  - ev-2e0705894104cb5a
  - ev-2b2b884e9f843c6a
  - ev-4e13b2c3ff172c51
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-fucosyllactose.yaml
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
    finding_id: f-f65270519936776b
actions:
- action_id: rec-action-f65270519936776b
  description: 'Reassess prediction-only role support: 2''-fucosyllactose'
  finding_ids:
  - rec-f-f65270519936776b
  target_ids:
  - record-addf66acec2d0722
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/2-fucosyllactose.yaml
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
