# Per-record structured review: HOMOPIPES (data/ingredients/mapped/HOMOPIPES.yaml)

- Review: 20261017T083000Z-homopipes
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for HOMOPIPES (data/ingredients/mapped/HOMOPIPES.yaml, record-dd28c55a7efde5a3, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/HOMOPIPES.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/HOMOPIPES.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-dd28c55a7efde5a3 | data/ingredients/mapped/HOMOPIPES.yaml | maintained | HOMOPIPES |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-dd28c55a7efde5a3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-dd28c55a7efde5a3 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-dd28c55a7efde5a3 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-dd28c55a7efde5a3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-dd28c55a7efde5a3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:02:05Z; reviewed SHA-256=1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7; current SHA-256=1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7; hash_changed=False. Reports=["reports/yaml_record_review/HOMOPIPES.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS fallback identity passes, but final SSSOM exports non-exact HOMOPIPES labels and BUFFER is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-dd28c55a7efde5a3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b5acf211da9251bf: Reassess prediction-only role support: HOMOPIPES

major / open / confirmed; issue key: mim-reconciliation-role-support-dd28c55a7efde5a3.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b5acf211da9251bf

Reassess prediction-only role support: HOMOPIPES

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3bf08b10842622cb | data/ingredients/mapped/HOMOPIPES.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1106],"raw_equal":true},"docs_rows":[{"identifier":"cas:202185-84-0","line":1108,"mapping_status":"MAPPED","ontology_id":"cas:202185-84-0","preferred_term":"HOMOPIPES"}],"identifier":"cas:202185-84-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:202185-84-0","ontology_label":"HOMOPIPES","ontology_source":"CAS"},"preferred_term":"HOMOPIPES","sssom_rows":[{"data_row":1399,"object_id":"cas:202185-84-0","object_label":"HOMOPIPES","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:HOMOPIPES","synonym_count":3} |
| ev-ef6ac4bf92028214 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1106] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4778c4da0a226768 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:HOMOPIPES; data-row positions=[1399] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1399,"object_id":"cas:202185-84-0","object_label":"HOMOPIPES","other":"homopiperazine-1,4-bis(2-ethanesulfonic acid), HOMO-PIPES&#124;Homo-PIPES&#124;Homo-PIPES (SIGMA)&#124;CAS:202185-84-0","predicate_id":"skos:exactMatch","subject_id":"MIM:HOMOPIPES","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-3b622bdd686f40e0 | docs/data/mapped_ingredients.csv; CSV lines=[1108] | supports | Published identity and count rows inspected: [{"identifier":"cas:202185-84-0","line":1108,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"5","ontology_id":"cas:202185-84-0","preferred_term":"HOMOPIPES","total_occurrences":"5"}] |
| ev-df6374dc387333c6 | reports/yaml_record_review/HOMOPIPES.md; &#96;data/ingredients/mapped/HOMOPIPES.yaml&#96;:2; Verdict:4; Identity:11; Validation:26; Evidence:35; Completeness:52; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-358c857f9e4ed9fa | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[721,1835] | context_only | [{"current_record_sha256":"1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7","finding_id":"SEM:e278775d6d7d49491a53","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7","finding_id":"SEM:769762b8307d614aea15","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-8537c2d0aaf82815 | data/ingredients/mapped/HOMOPIPES.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}] |
| ev-b3b94854c2bbe8d9 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-b5acf211da9251bf] | context_only | Predecessor structured review finding f-b5acf211da9251bf in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-homopipes
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: HOMOPIPES (data/ingredients/mapped/HOMOPIPES.yaml)'
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
summary: Per-record structured review for HOMOPIPES (data/ingredients/mapped/HOMOPIPES.yaml,
  record-dd28c55a7efde5a3, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/HOMOPIPES.yaml
    sha256: 1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/HOMOPIPES.md
    sha256: fbb9dd54c94550bf43e5f057f52a9cce397ab196bdfe27060a854dbc3eff2606
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-dd28c55a7efde5a3
  path: data/ingredients/mapped/HOMOPIPES.yaml
  label: HOMOPIPES
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/HOMOPIPES.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/HOMOPIPES.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/HOMOPIPES.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-dd28c55a7efde5a3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-dd28c55a7efde5a3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-dd28c55a7efde5a3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-dd28c55a7efde5a3
evidence:
- evidence_id: ev-3bf08b10842622cb
  kind: record_content
  reference: data/ingredients/mapped/HOMOPIPES.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1106],"raw_equal":true},"docs_rows":[{"identifier":"cas:202185-84-0","line":1108,"mapping_status":"MAPPED","ontology_id":"cas:202185-84-0","preferred_term":"HOMOPIPES"}],"identifier":"cas:202185-84-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:202185-84-0","ontology_label":"HOMOPIPES","ontology_source":"CAS"},"preferred_term":"HOMOPIPES","sssom_rows":[{"data_row":1399,"object_id":"cas:202185-84-0","object_label":"HOMOPIPES","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:HOMOPIPES","synonym_count":3}'
  snapshot_sha256: 1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7
- evidence_id: ev-ef6ac4bf92028214
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1106]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4778c4da0a226768
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:HOMOPIPES; data-row positions=[1399]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1399,"object_id":"cas:202185-84-0","object_label":"HOMOPIPES","other":"homopiperazine-1,4-bis(2-ethanesulfonic
    acid), HOMO-PIPES|Homo-PIPES|Homo-PIPES (SIGMA)|CAS:202185-84-0","predicate_id":"skos:exactMatch","subject_id":"MIM:HOMOPIPES","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3b622bdd686f40e0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1108]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:202185-84-0","line":1108,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"5","ontology_id":"cas:202185-84-0","preferred_term":"HOMOPIPES","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-df6374dc387333c6
  kind: prior_review
  reference: reports/yaml_record_review/HOMOPIPES.md
  locator: '`data/ingredients/mapped/HOMOPIPES.yaml`:2; Verdict:4; Identity:11; Validation:26;
    Evidence:35; Completeness:52; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fbb9dd54c94550bf43e5f057f52a9cce397ab196bdfe27060a854dbc3eff2606
  quote: "Recommended Edits:\n- Major: split the comma-joined HOMOPIPES synonym into\
    \ separate exact labels and\n  suppress or retype `Homo-PIPES (SIGMA)` so it no\
    \ longer appears in final SSSOM\n  as an exact synonym.\n- Major: review the `BUFFER`\
    \ facet and either replace the provisional in-session\n  evidence with an external\
    \ source or remove the unsupported role."
- evidence_id: ev-358c857f9e4ed9fa
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[721,1835]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7","finding_id":"SEM:e278775d6d7d49491a53","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7","finding_id":"SEM:769762b8307d614aea15","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-8537c2d0aaf82815
  kind: record_content
  reference: data/ingredients/mapped/HOMOPIPES.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"BUFFER"}}]'
  snapshot_sha256: 1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7
- evidence_id: ev-b3b94854c2bbe8d9
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-b5acf211da9251bf]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b5acf211da9251bf in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-6fb8a957f108833e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-dd28c55a7efde5a3
  evidence_ids:
  - ev-3bf08b10842622cb
  - ev-ef6ac4bf92028214
  - ev-4778c4da0a226768
  - ev-3b622bdd686f40e0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0e466935ca25d77f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dd28c55a7efde5a3
  evidence_ids:
  - ev-df6374dc387333c6
  - ev-3bf08b10842622cb
  - ev-358c857f9e4ed9fa
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:02:05Z;
    reviewed SHA-256=1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7;
    current SHA-256=1873785d4e49c89c495ace5a36c8d2d965a3f2347947baffb0e928bb3227ace7;
    hash_changed=False. Reports=["reports/yaml_record_review/HOMOPIPES.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS fallback
    identity passes, but final SSSOM exports non-exact HOMOPIPES labels and BUFFER
    is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-df6374dc387333c6
    - ev-3bf08b10842622cb
  - name: legacy-native-ids
    value: '["SEM:e278775d6d7d49491a53","SEM:769762b8307d614aea15"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3bf08b10842622cb
    - ev-df6374dc387333c6
    - ev-358c857f9e4ed9fa
- assessment_id: a-8537c2d0aaf82815
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dd28c55a7efde5a3
  evidence_ids:
  - ev-df6374dc387333c6
  - ev-8537c2d0aaf82815
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-df6374dc387333c6
    - ev-8537c2d0aaf82815
findings:
- finding_id: rec-f-b5acf211da9251bf
  issue_key: mim-reconciliation-role-support-dd28c55a7efde5a3
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: HOMOPIPES'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dd28c55a7efde5a3
  evidence_ids:
  - ev-df6374dc387333c6
  - ev-8537c2d0aaf82815
  - ev-b3b94854c2bbe8d9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/HOMOPIPES.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-b5acf211da9251bf
actions:
- action_id: rec-action-b5acf211da9251bf
  description: 'Reassess prediction-only role support: HOMOPIPES'
  finding_ids:
  - rec-f-b5acf211da9251bf
  target_ids:
  - record-dd28c55a7efde5a3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/HOMOPIPES.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
