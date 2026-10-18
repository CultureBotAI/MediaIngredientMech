# Per-record structured review: Lomefloxacin_Hydrochloride (data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml)

- Review: 20261017T083000Z-lomefloxacin-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lomefloxacin_Hydrochloride (data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml, record-1d30e0a659b20fab, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1d30e0a659b20fab | data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml | maintained | Lomefloxacin_Hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1d30e0a659b20fab | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-1d30e0a659b20fab | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1d30e0a659b20fab | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1d30e0a659b20fab.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1d30e0a659b20fab.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:40:44Z; reviewed SHA-256=51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3; current SHA-256=51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3; hash_changed=False. Reports=["reports/yaml_record_review/Lomefloxacin_Hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:6518 identity, CAS value, PubChem structure, exact synonym, and final SSSOM row pass, but SELECTIVE_AGENT is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-1d30e0a659b20fab.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e2d19050a651b34c: Reassess prediction-only role support: Lomefloxacin hydrochloride

major / open / confirmed; issue key: mim-reconciliation-role-support-1d30e0a659b20fab.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e2d19050a651b34c

Reassess prediction-only role support: Lomefloxacin hydrochloride

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6e417977ee1253c4 | data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1315],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6518","line":1317,"mapping_status":"MAPPED","ontology_id":"CHEBI:6518","preferred_term":"Lomefloxacin hydrochloride"}],"identifier":"CHEBI:6518","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6518","ontology_label":"lomefloxacin hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Lomefloxacin hydrochloride","sssom_rows":[{"data_row":1712,"object_id":"CHEBI:6518","object_label":"lomefloxacin hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lomefloxacin_Hydrochloride","synonym_count":1} |
| ev-c26538a787baa9b4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1315] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-12aa17351508524b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lomefloxacin_Hydrochloride; data-row positions=[1712] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1712,"object_id":"CHEBI:6518","object_label":"lomefloxacin hydrochloride","other":"1-ethyl-6,8-difluoro-7-(3-methylpiperazin-1-yl)-4-oxo-1,4-dihydroquinoline-3-carboxylic acid hydrochloride&#124;CAS:98079-52-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lomefloxacin_Hydrochloride","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-20f2729fae0e671a | docs/data/mapped_ingredients.csv; CSV lines=[1317] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:6518","line":1317,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6518","preferred_term":"Lomefloxacin hydrochloride","total_occurrences":"0"}] |
| ev-c742bd8e524c4cde | reports/yaml_record_review/Lomefloxacin_Hydrochloride.md; &#96;data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e455ee64b4564f8f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[872,1416] | context_only | [{"current_record_sha256":"51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3","finding_id":"SEM:16c5077bc2475df43f53","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3","finding_id":"SEM:695a78f5c1a6c7996dd8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-bf879fa2024bf077 | data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-e875acd12f0a585c | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-e2d19050a651b34c] | context_only | Predecessor structured review finding f-e2d19050a651b34c in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lomefloxacin-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lomefloxacin_Hydrochloride (data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml)'
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
summary: Per-record structured review for Lomefloxacin_Hydrochloride (data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml,
  record-1d30e0a659b20fab, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
    sha256: 51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3
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
  - path: reports/yaml_record_review/Lomefloxacin_Hydrochloride.md
    sha256: ef295f79c8a63356a73a9db9ddcc94d676c8b7c2fe55630edec972a626f84748
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1d30e0a659b20fab
  path: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
  label: Lomefloxacin_Hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1d30e0a659b20fab
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1d30e0a659b20fab
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-1d30e0a659b20fab
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1d30e0a659b20fab
evidence:
- evidence_id: ev-6e417977ee1253c4
  kind: record_content
  reference: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1315],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:6518","line":1317,"mapping_status":"MAPPED","ontology_id":"CHEBI:6518","preferred_term":"Lomefloxacin
    hydrochloride"}],"identifier":"CHEBI:6518","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:6518","ontology_label":"lomefloxacin
    hydrochloride","ontology_source":"CHEBI"},"preferred_term":"Lomefloxacin hydrochloride","sssom_rows":[{"data_row":1712,"object_id":"CHEBI:6518","object_label":"lomefloxacin
    hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lomefloxacin_Hydrochloride","synonym_count":1}'
  snapshot_sha256: 51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3
- evidence_id: ev-c26538a787baa9b4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1315]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-12aa17351508524b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lomefloxacin_Hydrochloride; data-row positions=[1712]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1712,"object_id":"CHEBI:6518","object_label":"lomefloxacin
    hydrochloride","other":"1-ethyl-6,8-difluoro-7-(3-methylpiperazin-1-yl)-4-oxo-1,4-dihydroquinoline-3-carboxylic
    acid hydrochloride|CAS:98079-52-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lomefloxacin_Hydrochloride","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-20f2729fae0e671a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1317]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:6518","line":1317,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:6518","preferred_term":"Lomefloxacin
    hydrochloride","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c742bd8e524c4cde
  kind: prior_review
  reference: reports/yaml_record_review/Lomefloxacin_Hydrochloride.md
  locator: '`data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml`:2; Verdict:4;
    Identity:11; Validation:21; Evidence:28; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ef295f79c8a63356a73a9db9ddcc94d676c8b7c2fe55630edec972a626f84748
  quote: "Recommended Edits:\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ in\n  `data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml` with inspected\n\
    \  source evidence for exact lomefloxacin hydrochloride use as a selective agent,\n\
    \  or remove the provisional role.\n- Sync the aggregate copy and regenerate derived\
    \ products after the YAML\n  change; rerun strict, term, round-trip, component,\
    \ and SSSOM validation."
- evidence_id: ev-e455ee64b4564f8f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[872,1416]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3","finding_id":"SEM:16c5077bc2475df43f53","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3","finding_id":"SEM:695a78f5c1a6c7996dd8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-bf879fa2024bf077
  kind: record_content
  reference: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3
- evidence_id: ev-e875acd12f0a585c
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-e2d19050a651b34c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e2d19050a651b34c in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-17ef4f6830bcea32
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1d30e0a659b20fab
  evidence_ids:
  - ev-6e417977ee1253c4
  - ev-c26538a787baa9b4
  - ev-12aa17351508524b
  - ev-20f2729fae0e671a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d6d313fd17f05889
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1d30e0a659b20fab
  evidence_ids:
  - ev-c742bd8e524c4cde
  - ev-6e417977ee1253c4
  - ev-e455ee64b4564f8f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:40:44Z;
    reviewed SHA-256=51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3;
    current SHA-256=51c5de4f86137b8d87562e209b5d9005e2fb3cce298a88ce20b7edfd73366dc3;
    hash_changed=False. Reports=["reports/yaml_record_review/Lomefloxacin_Hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:6518 identity, CAS value, PubChem structure, exact synonym, and final SSSOM
    row pass, but SELECTIVE_AGENT is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c742bd8e524c4cde
    - ev-6e417977ee1253c4
  - name: legacy-native-ids
    value: '["SEM:16c5077bc2475df43f53","SEM:695a78f5c1a6c7996dd8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6e417977ee1253c4
    - ev-c742bd8e524c4cde
    - ev-e455ee64b4564f8f
- assessment_id: a-bf879fa2024bf077
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1d30e0a659b20fab
  evidence_ids:
  - ev-c742bd8e524c4cde
  - ev-bf879fa2024bf077
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c742bd8e524c4cde
    - ev-bf879fa2024bf077
findings:
- finding_id: rec-f-e2d19050a651b34c
  issue_key: mim-reconciliation-role-support-1d30e0a659b20fab
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lomefloxacin hydrochloride'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-1d30e0a659b20fab
  evidence_ids:
  - ev-c742bd8e524c4cde
  - ev-bf879fa2024bf077
  - ev-e875acd12f0a585c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-e2d19050a651b34c
actions:
- action_id: rec-action-e2d19050a651b34c
  description: 'Reassess prediction-only role support: Lomefloxacin hydrochloride'
  finding_ids:
  - rec-f-e2d19050a651b34c
  target_ids:
  - record-1d30e0a659b20fab
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lomefloxacin_Hydrochloride.yaml
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
