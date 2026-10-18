# Per-record structured review: Candimycin (data/ingredients/mapped/Candimycin.yaml)

- Review: 20261017T083000Z-candimycin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Candimycin (data/ingredients/mapped/Candimycin.yaml, record-396235b1696a4bc4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Candimycin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Candimycin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-396235b1696a4bc4 | data/ingredients/mapped/Candimycin.yaml | maintained | Candimycin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-396235b1696a4bc4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-396235b1696a4bc4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-396235b1696a4bc4 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-396235b1696a4bc4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-396235b1696a4bc4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:48:06Z; reviewed SHA-256=69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb; current SHA-256=69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb; hash_changed=False. Reports=["reports/yaml_record_review/Candimycin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe placeholder is intentionally retained after no-hit OLS review, but SELECTIVE_AGENT is only a provisional name-pattern prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-396235b1696a4bc4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c4954fd07d936d1d: Reassess prediction-only role support: Candimycin

major / open / confirmed; issue key: mim-reconciliation-role-support-396235b1696a4bc4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c4954fd07d936d1d

Reassess prediction-only role support: Candimycin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a9af28a8c20fc827 | data/ingredients/mapped/Candimycin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[642],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:candimycin","line":644,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:candimycin","preferred_term":"Candimycin"}],"identifier":"kgmicrobe.compound:candimycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:candimycin","ontology_label":"Candimycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Candimycin","sssom_rows":[{"data_row":625,"object_id":"kgmicrobe.compound:candimycin","object_label":"Candimycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Candimycin","synonym_count":0} |
| ev-be7353d5b393d566 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [642] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fcde47a1b74c5026 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Candimycin; data-row positions=[625] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":625,"object_id":"kgmicrobe.compound:candimycin","object_label":"Candimycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Candimycin","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-11b88a8334b8e520 | docs/data/mapped_ingredients.csv; CSV lines=[644] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:candimycin","line":644,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:candimycin","preferred_term":"Candimycin","total_occurrences":"0"}] |
| ev-c4a3c345725e6385 | reports/yaml_record_review/Candimycin.md; &#96;data/ingredients/mapped/Candimycin.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:37; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-fde2e9e3d0ee10f2 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[353,1632] | context_only | [{"current_record_sha256":"69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb","finding_id":"SEM:dcbc078a62401b98b91d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb","finding_id":"SEM:c145da0f329daf813604","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9dd1408238fc6581 | data/ingredients/mapped/Candimycin.yaml; physicochemical_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}] |
| ev-f879edf8c58be192 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-c4954fd07d936d1d] | context_only | Predecessor structured review finding f-c4954fd07d936d1d in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-candimycin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Candimycin (data/ingredients/mapped/Candimycin.yaml)'
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
summary: Per-record structured review for Candimycin (data/ingredients/mapped/Candimycin.yaml,
  record-396235b1696a4bc4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Candimycin.yaml
    sha256: 69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Candimycin.md
    sha256: 2570c8ee958ea91da94f82e94d91ee83222e31fa6367c1832ea010276d509ac2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-396235b1696a4bc4
  path: data/ingredients/mapped/Candimycin.yaml
  label: Candimycin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Candimycin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Candimycin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Candimycin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-396235b1696a4bc4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-396235b1696a4bc4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-396235b1696a4bc4
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-396235b1696a4bc4
evidence:
- evidence_id: ev-a9af28a8c20fc827
  kind: record_content
  reference: data/ingredients/mapped/Candimycin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[642],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:candimycin","line":644,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.compound:candimycin","preferred_term":"Candimycin"}],"identifier":"kgmicrobe.compound:candimycin","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"PLACEHOLDER","ontology_id":"kgmicrobe.compound:candimycin","ontology_label":"Candimycin","ontology_source":"kgmicrobe.compound"},"preferred_term":"Candimycin","sssom_rows":[{"data_row":625,"object_id":"kgmicrobe.compound:candimycin","object_label":"Candimycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Candimycin","synonym_count":0}'
  snapshot_sha256: 69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb
- evidence_id: ev-be7353d5b393d566
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [642]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fcde47a1b74c5026
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Candimycin; data-row positions=[625]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":625,"object_id":"kgmicrobe.compound:candimycin","object_label":"Candimycin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Candimycin","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-11b88a8334b8e520
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[644]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:candimycin","line":644,"mapping_quality":"PLACEHOLDER","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.compound:candimycin","preferred_term":"Candimycin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c4a3c345725e6385
  kind: prior_review
  reference: reports/yaml_record_review/Candimycin.md
  locator: '`data/ingredients/mapped/Candimycin.yaml`:2; Verdict:4; Identity:10; Validation:22;
    Evidence:37; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2570c8ee958ea91da94f82e94d91ee83222e31fa6367c1832ea010276d509ac2
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Candimycin.yaml`, remove\n\
    \  `physicochemical_roles.SELECTIVE_AGENT` unless a future curator can attach\n\
    \  compound-specific evidence for candimycin as a selective agent in microbial\n\
    \  media.\n- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and\
    \ any role\n  exports that consume the aggregate; prove the cleanup with strict\
    \ validation\n  and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-fde2e9e3d0ee10f2
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[353,1632]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb","finding_id":"SEM:dcbc078a62401b98b91d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb","finding_id":"SEM:c145da0f329daf813604","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9dd1408238fc6581
  kind: record_content
  reference: data/ingredients/mapped/Candimycin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"physicochemical_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"SELECTIVE_AGENT"}}]'
  snapshot_sha256: 69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb
- evidence_id: ev-f879edf8c58be192
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-c4954fd07d936d1d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c4954fd07d936d1d in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-b370e246d4382a03
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-396235b1696a4bc4
  evidence_ids:
  - ev-a9af28a8c20fc827
  - ev-be7353d5b393d566
  - ev-fcde47a1b74c5026
  - ev-11b88a8334b8e520
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f1c37a48a63b38b5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-396235b1696a4bc4
  evidence_ids:
  - ev-c4a3c345725e6385
  - ev-a9af28a8c20fc827
  - ev-fde2e9e3d0ee10f2
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:48:06Z;
    reviewed SHA-256=69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb;
    current SHA-256=69aa2fbd292fd485d514c1e3fb6cc74a81b19f485ee82cd0fb1fc09fbc91fcbb;
    hash_changed=False. Reports=["reports/yaml_record_review/Candimycin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The kgmicrobe placeholder
    is intentionally retained after no-hit OLS review, but SELECTIVE_AGENT is only
    a provisional name-pattern prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c4a3c345725e6385
    - ev-a9af28a8c20fc827
  - name: legacy-native-ids
    value: '["SEM:dcbc078a62401b98b91d","SEM:c145da0f329daf813604"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a9af28a8c20fc827
    - ev-c4a3c345725e6385
    - ev-fde2e9e3d0ee10f2
- assessment_id: a-9dd1408238fc6581
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-396235b1696a4bc4
  evidence_ids:
  - ev-c4a3c345725e6385
  - ev-9dd1408238fc6581
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c4a3c345725e6385
    - ev-9dd1408238fc6581
findings:
- finding_id: rec-f-c4954fd07d936d1d
  issue_key: mim-reconciliation-role-support-396235b1696a4bc4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Candimycin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-396235b1696a4bc4
  evidence_ids:
  - ev-c4a3c345725e6385
  - ev-9dd1408238fc6581
  - ev-f879edf8c58be192
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Candimycin.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-c4954fd07d936d1d
actions:
- action_id: rec-action-c4954fd07d936d1d
  description: 'Reassess prediction-only role support: Candimycin'
  finding_ids:
  - rec-f-c4954fd07d936d1d
  target_ids:
  - record-396235b1696a4bc4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Candimycin.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
