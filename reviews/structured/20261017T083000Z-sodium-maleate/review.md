# Per-record structured review: Sodium_Maleate (data/ingredients/mapped/Sodium_Maleate.yaml)

- Review: 20261017T083000Z-sodium-maleate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Maleate (data/ingredients/mapped/Sodium_Maleate.yaml, record-22bb6338430c43cb, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Maleate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Maleate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-22bb6338430c43cb | data/ingredients/mapped/Sodium_Maleate.yaml | maintained | Sodium_Maleate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-22bb6338430c43cb | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-22bb6338430c43cb | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-22bb6338430c43cb | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-22bb6338430c43cb.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-22bb6338430c43cb.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:22:24Z; reviewed SHA-256=395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005; current SHA-256=395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Maleate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:91263 identity, CAS, structure, and final SSSOM row pass, but BUFFER is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-22bb6338430c43cb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c2b1952270153c20: Reassess prediction-only role support: Sodium maleate

major / open / confirmed; issue key: mim-reconciliation-role-support-22bb6338430c43cb.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c2b1952270153c20

Reassess prediction-only role support: Sodium maleate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9f18800ba2008ae4 | data/ingredients/mapped/Sodium_Maleate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1851],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91263","line":1853,"mapping_status":"MAPPED","ontology_id":"CHEBI:91263","preferred_term":"Sodium maleate"}],"identifier":"CHEBI:91263","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91263","ontology_label":"disodium maleate","ontology_source":"CHEBI"},"preferred_term":"Sodium maleate","sssom_rows":[{"data_row":2575,"object_id":"CHEBI:91263","object_label":"disodium maleate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Maleate","synonym_count":4} |
| ev-b70a8f746734c21a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1851] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0481b1e4e7f6aaba | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Maleate; data-row positions=[2575] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2575,"object_id":"CHEBI:91263","object_label":"disodium maleate","other":"Maleic acid, disodium salt&#124;disodium (2Z)-but-2-enedioate&#124;CAS:371-47-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Maleate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-f3b22bc53b1b8a69 | docs/data/mapped_ingredients.csv; CSV lines=[1853] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:91263","line":1853,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:91263","preferred_term":"Sodium maleate","total_occurrences":"3"}] |
| ev-f99cfb7095b6e433 | reports/yaml_record_review/Sodium_Maleate.md; &#96;data/ingredients/mapped/Sodium_Maleate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bf83d275cad00f4e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1222,1449] | context_only | [{"current_record_sha256":"395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005","finding_id":"SEM:64eefd8313d3800ab2f5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005","finding_id":"SEM:304749118802acee5e4d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7e7d6cd9632c2e93 | data/ingredients/mapped/Sodium_Maleate.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}] |
| ev-52d906d294c49c1c | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-c2b1952270153c20] | context_only | Predecessor structured review finding f-c2b1952270153c20 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-maleate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Maleate (data/ingredients/mapped/Sodium_Maleate.yaml)'
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
summary: Per-record structured review for Sodium_Maleate (data/ingredients/mapped/Sodium_Maleate.yaml,
  record-22bb6338430c43cb, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Maleate.yaml
    sha256: 395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005
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
  - path: reports/yaml_record_review/Sodium_Maleate.md
    sha256: 83c5b81113865f9be698b20c13f3ae80e7caa569173c9259754fa45e2a52b1da
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-22bb6338430c43cb
  path: data/ingredients/mapped/Sodium_Maleate.yaml
  label: Sodium_Maleate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Maleate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Maleate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Maleate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-22bb6338430c43cb
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-22bb6338430c43cb
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-22bb6338430c43cb
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-22bb6338430c43cb
evidence:
- evidence_id: ev-9f18800ba2008ae4
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Maleate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1851],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:91263","line":1853,"mapping_status":"MAPPED","ontology_id":"CHEBI:91263","preferred_term":"Sodium
    maleate"}],"identifier":"CHEBI:91263","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:91263","ontology_label":"disodium
    maleate","ontology_source":"CHEBI"},"preferred_term":"Sodium maleate","sssom_rows":[{"data_row":2575,"object_id":"CHEBI:91263","object_label":"disodium
    maleate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Maleate","synonym_count":4}'
  snapshot_sha256: 395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005
- evidence_id: ev-b70a8f746734c21a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1851]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0481b1e4e7f6aaba
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Maleate; data-row positions=[2575]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2575,"object_id":"CHEBI:91263","object_label":"disodium
    maleate","other":"Maleic acid, disodium salt|disodium (2Z)-but-2-enedioate|CAS:371-47-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Maleate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f3b22bc53b1b8a69
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1853]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:91263","line":1853,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:91263","preferred_term":"Sodium
    maleate","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f99cfb7095b6e433
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Maleate.md
  locator: '`data/ingredients/mapped/Sodium_Maleate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 83c5b81113865f9be698b20c13f3ae80e7caa569173c9259754fa45e2a52b1da
- evidence_id: ev-bf83d275cad00f4e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1222,1449]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005","finding_id":"SEM:64eefd8313d3800ab2f5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005","finding_id":"SEM:304749118802acee5e4d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7e7d6cd9632c2e93
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Maleate.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}]'
  snapshot_sha256: 395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005
- evidence_id: ev-52d906d294c49c1c
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-c2b1952270153c20]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c2b1952270153c20 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-6b63cbfa277178d2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-22bb6338430c43cb
  evidence_ids:
  - ev-9f18800ba2008ae4
  - ev-b70a8f746734c21a
  - ev-0481b1e4e7f6aaba
  - ev-f3b22bc53b1b8a69
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b2cecbdf4c3045f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-22bb6338430c43cb
  evidence_ids:
  - ev-f99cfb7095b6e433
  - ev-9f18800ba2008ae4
  - ev-bf83d275cad00f4e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:22:24Z;
    reviewed SHA-256=395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005;
    current SHA-256=395ed38b57a7bfb13ebc38c82ac7a88d45f75458cdc5b72c44c4216c49f7f005;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Maleate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:91263 identity, CAS, structure, and final SSSOM row pass, but BUFFER is
    provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f99cfb7095b6e433
    - ev-9f18800ba2008ae4
  - name: legacy-native-ids
    value: '["SEM:64eefd8313d3800ab2f5","SEM:304749118802acee5e4d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9f18800ba2008ae4
    - ev-f99cfb7095b6e433
    - ev-bf83d275cad00f4e
- assessment_id: a-7e7d6cd9632c2e93
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-22bb6338430c43cb
  evidence_ids:
  - ev-f99cfb7095b6e433
  - ev-7e7d6cd9632c2e93
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f99cfb7095b6e433
    - ev-7e7d6cd9632c2e93
findings:
- finding_id: rec-f-c2b1952270153c20
  issue_key: mim-reconciliation-role-support-22bb6338430c43cb
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sodium maleate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-22bb6338430c43cb
  evidence_ids:
  - ev-f99cfb7095b6e433
  - ev-7e7d6cd9632c2e93
  - ev-52d906d294c49c1c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Maleate.yaml
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
    finding_id: f-c2b1952270153c20
actions:
- action_id: rec-action-c2b1952270153c20
  description: 'Reassess prediction-only role support: Sodium maleate'
  finding_ids:
  - rec-f-c2b1952270153c20
  target_ids:
  - record-22bb6338430c43cb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Maleate.yaml
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
