# Per-record structured review: 1-Kestose (data/ingredients/mapped/1-Kestose.yaml)

- Review: 20261017T083000Z-1-kestose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 1-Kestose (data/ingredients/mapped/1-Kestose.yaml, record-452ec4d4dc2579ca, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/1-Kestose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/1-Kestose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-452ec4d4dc2579ca | data/ingredients/mapped/1-Kestose.yaml | maintained | 1-Kestose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-452ec4d4dc2579ca | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-452ec4d4dc2579ca | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-452ec4d4dc2579ca | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-452ec4d4dc2579ca.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-452ec4d4dc2579ca.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:01:24Z; reviewed SHA-256=c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8; current SHA-256=c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8; hash_changed=False. Reports=["reports/yaml_record_review/1-Kestose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active ChEBI identity and exported products pass, but an open kgscan discussion is mostly irrelevant and unattached.

### Historical provisional-role concern

evidence: concern. Targets: record-452ec4d4dc2579ca.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9445b49fdf863d47: Reassess prediction-only role support: 1-Kestose

major / open / confirmed; issue key: mim-reconciliation-role-support-452ec4d4dc2579ca.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9445b49fdf863d47

Reassess prediction-only role support: 1-Kestose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-212bf32626671339 | data/ingredients/mapped/1-Kestose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[283],"raw_equal":false},"docs_rows":[{"identifier":"CHEBI:16885","line":285,"mapping_status":"MAPPED","ontology_id":"CHEBI:16885","preferred_term":"1-Kestose"}],"identifier":"CHEBI:16885","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16885","ontology_label":"1-kestose","ontology_source":"CHEBI"},"preferred_term":"1-Kestose","sssom_rows":[{"data_row":11,"object_id":"CHEBI:16885","object_label":"1-kestose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-Kestose","synonym_count":1} |
| ev-7fe430029259d4b0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [283] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=False. |
| ev-3318271f6f1a8f4a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:1-Kestose; data-row positions=[11] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":11,"object_id":"CHEBI:16885","object_label":"1-kestose","other":"beta-D-fructofuranosyl-(2-&gt;1)-beta-D-fructofuranosyl alpha-D-glucopyranoside&#124;CAS:470-69-9","predicate_id":"skos:exactMatch","subject_id":"MIM:1-Kestose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-700cdee52554a6f1 | docs/data/mapped_ingredients.csv; CSV lines=[285] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16885","line":285,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16885","preferred_term":"1-Kestose","total_occurrences":"0"}] |
| ev-90d64f718c3e330b | reports/yaml_record_review/1-Kestose.md; &#96;data/ingredients/mapped/1-Kestose.yaml&#96;:2; Verdict:4; Identity:12; Validation:32; Evidence:55; Completeness:85; Recommended Edits:97 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e3c0912d3962cebb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[12,1432] | context_only | [{"current_record_sha256":"c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8","finding_id":"SEM:1758aba761e0ac98d450","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8","finding_id":"SEM:ad313d4eabb6a03b4ba5","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e5fb7db00b278bda | data/ingredients/mapped/1-Kestose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-a549918f8ba6c443 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-9445b49fdf863d47] | context_only | Predecessor structured review finding f-9445b49fdf863d47 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-1-kestose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 1-Kestose (data/ingredients/mapped/1-Kestose.yaml)'
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
summary: Per-record structured review for 1-Kestose (data/ingredients/mapped/1-Kestose.yaml,
  record-452ec4d4dc2579ca, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/1-Kestose.yaml
    sha256: c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8
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
  - path: reports/yaml_record_review/1-Kestose.md
    sha256: beaae76c539cc03d45c6448c810c62442328ddf799d3c38e9615dfb84acf9070
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-452ec4d4dc2579ca
  path: data/ingredients/mapped/1-Kestose.yaml
  label: 1-Kestose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-Kestose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/1-Kestose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/1-Kestose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-452ec4d4dc2579ca
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-452ec4d4dc2579ca
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-452ec4d4dc2579ca
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-452ec4d4dc2579ca
evidence:
- evidence_id: ev-212bf32626671339
  kind: record_content
  reference: data/ingredients/mapped/1-Kestose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[283],"raw_equal":false},"docs_rows":[{"identifier":"CHEBI:16885","line":285,"mapping_status":"MAPPED","ontology_id":"CHEBI:16885","preferred_term":"1-Kestose"}],"identifier":"CHEBI:16885","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16885","ontology_label":"1-kestose","ontology_source":"CHEBI"},"preferred_term":"1-Kestose","sssom_rows":[{"data_row":11,"object_id":"CHEBI:16885","object_label":"1-kestose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:1-Kestose","synonym_count":1}'
  snapshot_sha256: c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8
- evidence_id: ev-7fe430029259d4b0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [283]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=False.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3318271f6f1a8f4a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:1-Kestose; data-row positions=[11]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":11,"object_id":"CHEBI:16885","object_label":"1-kestose","other":"beta-D-fructofuranosyl-(2->1)-beta-D-fructofuranosyl
    alpha-D-glucopyranoside|CAS:470-69-9","predicate_id":"skos:exactMatch","subject_id":"MIM:1-Kestose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-700cdee52554a6f1
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[285]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16885","line":285,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16885","preferred_term":"1-Kestose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-90d64f718c3e330b
  kind: prior_review
  reference: reports/yaml_record_review/1-Kestose.md
  locator: '`data/ingredients/mapped/1-Kestose.yaml`:2; Verdict:4; Identity:12; Validation:32;
    Evidence:55; Completeness:85; Recommended Edits:97'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: beaae76c539cc03d45c6448c810c62442328ddf799d3c38e9615dfb84acf9070
  quote: "Recommended Edits:\n1. Remove `PMID:41373036`, `DOI:10.21203/rs.3.rs-6822283/v1`,\
    \ and\n   `PMID:41367416` from `data/ingredients/mapped/1-Kestose.yaml`, or replace\n\
    \   the whole `kgscan-f77a72b7ddb7` discussion with a record-specific knowledge\n\
    \   gap attached to the role, mapping, or other exact claim it is meant to\n \
    \  qualify.\n2. If `mappings/record_research_validation.tsv` is meant to be a\
    \ live triage\n   queue, regenerate it from its maintained recipe or mark the\
    \ `1-Kestose`\n   exact-mapping row resolved so this already-verified ChEBI mapping\
    \ stops\n   reappearing as `P2` review work.\n3. No identity, synonym, chemical-property,\
    \ ingredient-type, component, or\n   SSSOM edit is needed for the active `CHEBI:16885`\
    \ mapping."
- evidence_id: ev-e3c0912d3962cebb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[12,1432]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8","finding_id":"SEM:1758aba761e0ac98d450","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8","finding_id":"SEM:ad313d4eabb6a03b4ba5","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e5fb7db00b278bda
  kind: record_content
  reference: data/ingredients/mapped/1-Kestose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8
- evidence_id: ev-a549918f8ba6c443
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-9445b49fdf863d47]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9445b49fdf863d47 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-71bbd7ed02f149d8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-452ec4d4dc2579ca
  evidence_ids:
  - ev-212bf32626671339
  - ev-7fe430029259d4b0
  - ev-3318271f6f1a8f4a
  - ev-700cdee52554a6f1
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3e3024f905ec89f7
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-452ec4d4dc2579ca
  evidence_ids:
  - ev-90d64f718c3e330b
  - ev-212bf32626671339
  - ev-e3c0912d3962cebb
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T05:01:24Z;
    reviewed SHA-256=c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8;
    current SHA-256=c3cd932ad6e3dd6b446c499cb8c69bca008dd05bf21dc30acc80368fe1b318e8;
    hash_changed=False. Reports=["reports/yaml_record_review/1-Kestose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: Active ChEBI identity
    and exported products pass, but an open kgscan discussion is mostly irrelevant
    and unattached.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-90d64f718c3e330b
    - ev-212bf32626671339
  - name: legacy-native-ids
    value: '["SEM:1758aba761e0ac98d450","SEM:ad313d4eabb6a03b4ba5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-212bf32626671339
    - ev-90d64f718c3e330b
    - ev-e3c0912d3962cebb
- assessment_id: a-e5fb7db00b278bda
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-452ec4d4dc2579ca
  evidence_ids:
  - ev-90d64f718c3e330b
  - ev-e5fb7db00b278bda
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-90d64f718c3e330b
    - ev-e5fb7db00b278bda
findings:
- finding_id: rec-f-9445b49fdf863d47
  issue_key: mim-reconciliation-role-support-452ec4d4dc2579ca
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 1-Kestose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-452ec4d4dc2579ca
  evidence_ids:
  - ev-90d64f718c3e330b
  - ev-e5fb7db00b278bda
  - ev-a549918f8ba6c443
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-Kestose.yaml
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
    finding_id: f-9445b49fdf863d47
actions:
- action_id: rec-action-9445b49fdf863d47
  description: 'Reassess prediction-only role support: 1-Kestose'
  finding_ids:
  - rec-f-9445b49fdf863d47
  target_ids:
  - record-452ec4d4dc2579ca
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/1-Kestose.yaml
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
