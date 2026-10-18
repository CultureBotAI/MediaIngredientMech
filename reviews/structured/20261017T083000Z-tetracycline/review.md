# Per-record structured review: Tetracycline (data/ingredients/mapped/Tetracycline.yaml)

- Review: 20261017T083000Z-tetracycline
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Tetracycline (data/ingredients/mapped/Tetracycline.yaml, record-e7e0774740634242, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Tetracycline.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Tetracycline.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e7e0774740634242 | data/ingredients/mapped/Tetracycline.yaml | maintained | Tetracycline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e7e0774740634242 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e7e0774740634242 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e7e0774740634242 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e7e0774740634242.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e7e0774740634242.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:11:59Z; reviewed SHA-256=48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429; current SHA-256=48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429; hash_changed=False. Reports=["reports/yaml_record_review/Tetracycline.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:27902 identity passes, but SELECTIVE_AGENT is still only a provisional computational name-pattern role.

### Historical provisional-role concern

evidence: concern. Targets: record-e7e0774740634242.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e01b7881f898cd0f: Reassess prediction-only role support: Tetracycline

major / open / confirmed; issue key: mim-reconciliation-role-support-e7e0774740634242.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e01b7881f898cd0f

Reassess prediction-only role support: Tetracycline

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e01e3a41483886ef | data/ingredients/mapped/Tetracycline.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27902","line":1943,"mapping_status":"MAPPED","ontology_id":"CHEBI:27902","preferred_term":"Tetracycline"}],"identifier":"CHEBI:27902","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27902","ontology_label":"tetracycline","ontology_source":"CHEBI"},"preferred_term":"Tetracycline","sssom_rows":[{"data_row":2736,"object_id":"CHEBI:27902","object_label":"tetracycline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tetracycline","synonym_count":2} |
| ev-d93edc8900ec4f7a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1941] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6b6964818d6313db | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Tetracycline; data-row positions=[2736] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2736,"object_id":"CHEBI:27902","object_label":"tetracycline","other":"(4S,4aS,5aS,6S,12aS)-4-(dimethylamino)-3,6,10,12,12a-pentahydroxy-6-methyl-1,11-dioxo-1,4,4a,5,5a,6,11,12a-octahydrotetracene-2-carboxamide&#124;Achromycin","predicate_id":"skos:exactMatch","subject_id":"MIM:Tetracycline","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-378c6804e4f04ade | docs/data/mapped_ingredients.csv; CSV lines=[1943] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27902","line":1943,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:27902","preferred_term":"Tetracycline","total_occurrences":"3"}] |
| ev-c7f6f88448e202a7 | reports/yaml_record_review/Tetracycline.md; &#96;data/ingredients/mapped/Tetracycline.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:30; Completeness:44; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5c04c1e24be67436 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1276,1538] | context_only | [{"current_record_sha256":"48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429","finding_id":"SEM:8f9aecc24505f643a6b5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429","finding_id":"SEM:cd1dc3a1414e2ced4bba","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f72b44c3a5e117ea | data/ingredients/mapped/Tetracycline.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-81b322a23b74b344 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-e01b7881f898cd0f] | context_only | Predecessor structured review finding f-e01b7881f898cd0f in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-tetracycline
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Tetracycline (data/ingredients/mapped/Tetracycline.yaml)'
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
summary: Per-record structured review for Tetracycline (data/ingredients/mapped/Tetracycline.yaml,
  record-e7e0774740634242, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Tetracycline.yaml
    sha256: 48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Tetracycline.md
    sha256: e63be3bac14c431f4e24679cbb55f9f0c48a7593375b2bc83d2f19219e745e9f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e7e0774740634242
  path: data/ingredients/mapped/Tetracycline.yaml
  label: Tetracycline
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tetracycline.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Tetracycline.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Tetracycline.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e7e0774740634242
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e7e0774740634242
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e7e0774740634242
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e7e0774740634242
evidence:
- evidence_id: ev-e01e3a41483886ef
  kind: record_content
  reference: data/ingredients/mapped/Tetracycline.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1941],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27902","line":1943,"mapping_status":"MAPPED","ontology_id":"CHEBI:27902","preferred_term":"Tetracycline"}],"identifier":"CHEBI:27902","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27902","ontology_label":"tetracycline","ontology_source":"CHEBI"},"preferred_term":"Tetracycline","sssom_rows":[{"data_row":2736,"object_id":"CHEBI:27902","object_label":"tetracycline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Tetracycline","synonym_count":2}'
  snapshot_sha256: 48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429
- evidence_id: ev-d93edc8900ec4f7a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1941]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6b6964818d6313db
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Tetracycline; data-row positions=[2736]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2736,"object_id":"CHEBI:27902","object_label":"tetracycline","other":"(4S,4aS,5aS,6S,12aS)-4-(dimethylamino)-3,6,10,12,12a-pentahydroxy-6-methyl-1,11-dioxo-1,4,4a,5,5a,6,11,12a-octahydrotetracene-2-carboxamide|Achromycin","predicate_id":"skos:exactMatch","subject_id":"MIM:Tetracycline","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-378c6804e4f04ade
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1943]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27902","line":1943,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:27902","preferred_term":"Tetracycline","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c7f6f88448e202a7
  kind: prior_review
  reference: reports/yaml_record_review/Tetracycline.md
  locator: '`data/ingredients/mapped/Tetracycline.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:30; Completeness:44; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e63be3bac14c431f4e24679cbb55f9f0c48a7593375b2bc83d2f19219e745e9f
  quote: "Recommended Edits:\n- Major: replace the provisional name-pattern `SELECTIVE_AGENT`\
    \ role in\n  `data/ingredients/mapped/Tetracycline.yaml` with source-backed evidence\
    \ for\n  tetracycline as a selective agent, or remove the role if no maintained\
    \ source\n  supports it.\n- Major: after any role edit, synchronize `data/curated/mapped_ingredients.yaml`\n\
    \  and regenerate generated products so the role facets match the per-record\n\
    \  YAML."
- evidence_id: ev-5c04c1e24be67436
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1276,1538]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429","finding_id":"SEM:8f9aecc24505f643a6b5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429","finding_id":"SEM:cd1dc3a1414e2ced4bba","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f72b44c3a5e117ea
  kind: record_content
  reference: data/ingredients/mapped/Tetracycline.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429
- evidence_id: ev-81b322a23b74b344
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-e01b7881f898cd0f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e01b7881f898cd0f in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-c5de14f6b9778deb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e7e0774740634242
  evidence_ids:
  - ev-e01e3a41483886ef
  - ev-d93edc8900ec4f7a
  - ev-6b6964818d6313db
  - ev-378c6804e4f04ade
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a37ac63bb65de976
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e7e0774740634242
  evidence_ids:
  - ev-c7f6f88448e202a7
  - ev-e01e3a41483886ef
  - ev-5c04c1e24be67436
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:11:59Z;
    reviewed SHA-256=48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429;
    current SHA-256=48a0f106a49f0b33faa49697b5c79377b2e7f92ce63327594f903ee0ab316429;
    hash_changed=False. Reports=["reports/yaml_record_review/Tetracycline.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:27902
    identity passes, but SELECTIVE_AGENT is still only a provisional computational
    name-pattern role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c7f6f88448e202a7
    - ev-e01e3a41483886ef
  - name: legacy-native-ids
    value: '["SEM:8f9aecc24505f643a6b5","SEM:cd1dc3a1414e2ced4bba"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e01e3a41483886ef
    - ev-c7f6f88448e202a7
    - ev-5c04c1e24be67436
- assessment_id: a-f72b44c3a5e117ea
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e7e0774740634242
  evidence_ids:
  - ev-c7f6f88448e202a7
  - ev-f72b44c3a5e117ea
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c7f6f88448e202a7
    - ev-f72b44c3a5e117ea
findings:
- finding_id: rec-f-e01b7881f898cd0f
  issue_key: mim-reconciliation-role-support-e7e0774740634242
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Tetracycline'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e7e0774740634242
  evidence_ids:
  - ev-c7f6f88448e202a7
  - ev-f72b44c3a5e117ea
  - ev-81b322a23b74b344
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tetracycline.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-e01b7881f898cd0f
actions:
- action_id: rec-action-e01b7881f898cd0f
  description: 'Reassess prediction-only role support: Tetracycline'
  finding_ids:
  - rec-f-e01b7881f898cd0f
  target_ids:
  - record-e7e0774740634242
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Tetracycline.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
