# Per-record structured review: D-Proline (data/ingredients/mapped/D-Proline.yaml)

- Review: 20261017T083000Z-d-proline
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Proline (data/ingredients/mapped/D-Proline.yaml, record-f651c3c92559068f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Proline.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Proline.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f651c3c92559068f | data/ingredients/mapped/D-Proline.yaml | maintained | D-Proline |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f651c3c92559068f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-f651c3c92559068f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f651c3c92559068f | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f651c3c92559068f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f651c3c92559068f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:19:42Z; reviewed SHA-256=cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279; current SHA-256=cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279; hash_changed=False. Reports=["reports/yaml_record_review/D-Proline.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, structure fields, 0/0 count, and final SSSOM row pass, but the amino-acid role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-f651c3c92559068f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9ade4a5f22ff6230: Reassess prediction-only role support: D-Proline

major / open / confirmed; issue key: mim-reconciliation-role-support-f651c3c92559068f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9ade4a5f22ff6230

Reassess prediction-only role support: D-Proline

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-414cc7fbab1bc953 | data/ingredients/mapped/D-Proline.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[823],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16313","line":825,"mapping_status":"MAPPED","ontology_id":"CHEBI:16313","preferred_term":"D-Proline"}],"identifier":"CHEBI:16313","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16313","ontology_label":"D-proline","ontology_source":"CHEBI"},"preferred_term":"D-Proline","sssom_rows":[{"data_row":905,"object_id":"CHEBI:16313","object_label":"D-proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Proline","synonym_count":0} |
| ev-e718305288114cdb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [823] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a109f8ba06a52076 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Proline; data-row positions=[905] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":905,"object_id":"CHEBI:16313","object_label":"D-proline","other":"CAS:344-25-2","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Proline","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-fc5584be4b728c1c | docs/data/mapped_ingredients.csv; CSV lines=[825] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16313","line":825,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16313","preferred_term":"D-Proline","total_occurrences":"0"}] |
| ev-ae7188e078dc3f4e | reports/yaml_record_review/D-Proline.md; &#96;data/ingredients/mapped/D-Proline.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:43; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-754548779060ea63 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[475,1624] | context_only | [{"current_record_sha256":"cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279","finding_id":"SEM:67c923618030fea83bde","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279","finding_id":"SEM:4e6778d3304ac93a23d3","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-5e4355125c683f84 | data/ingredients/mapped/D-Proline.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-fa256eee39f733a1 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-9ade4a5f22ff6230] | context_only | Predecessor structured review finding f-9ade4a5f22ff6230 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-proline
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Proline (data/ingredients/mapped/D-Proline.yaml)'
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
summary: Per-record structured review for D-Proline (data/ingredients/mapped/D-Proline.yaml,
  record-f651c3c92559068f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Proline.yaml
    sha256: cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-Proline.md
    sha256: ccf52112f8a1cce1780176ae03191be5729817c26f23bc267f756d0c23c4c378
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f651c3c92559068f
  path: data/ingredients/mapped/D-Proline.yaml
  label: D-Proline
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Proline.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Proline.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Proline.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f651c3c92559068f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f651c3c92559068f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-f651c3c92559068f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f651c3c92559068f
evidence:
- evidence_id: ev-414cc7fbab1bc953
  kind: record_content
  reference: data/ingredients/mapped/D-Proline.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[823],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16313","line":825,"mapping_status":"MAPPED","ontology_id":"CHEBI:16313","preferred_term":"D-Proline"}],"identifier":"CHEBI:16313","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16313","ontology_label":"D-proline","ontology_source":"CHEBI"},"preferred_term":"D-Proline","sssom_rows":[{"data_row":905,"object_id":"CHEBI:16313","object_label":"D-proline","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Proline","synonym_count":0}'
  snapshot_sha256: cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279
- evidence_id: ev-e718305288114cdb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [823]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a109f8ba06a52076
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Proline; data-row positions=[905]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":905,"object_id":"CHEBI:16313","object_label":"D-proline","other":"CAS:344-25-2","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Proline","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fc5584be4b728c1c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[825]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16313","line":825,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16313","preferred_term":"D-Proline","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ae7188e078dc3f4e
  kind: prior_review
  reference: reports/yaml_record_review/D-Proline.md
  locator: '`data/ingredients/mapped/D-Proline.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:43; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ccf52112f8a1cce1780176ae03191be5729817c26f23bc267f756d0c23c4c378
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Proline.yaml`, either\
    \ replace the computational\n  `AMINO_ACID_SOURCE` evidence with direct CultureBotHT\
    \ or source-backed\n  media-role evidence for this ingredient, or remove the role\
    \ facet; then rerun\n  strict validation and the final SSSOM build."
- evidence_id: ev-754548779060ea63
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[475,1624]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279","finding_id":"SEM:67c923618030fea83bde","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279","finding_id":"SEM:4e6778d3304ac93a23d3","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5e4355125c683f84
  kind: record_content
  reference: data/ingredients/mapped/D-Proline.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279
- evidence_id: ev-fa256eee39f733a1
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-9ade4a5f22ff6230]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9ade4a5f22ff6230 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-3bca854bbe850796
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f651c3c92559068f
  evidence_ids:
  - ev-414cc7fbab1bc953
  - ev-e718305288114cdb
  - ev-a109f8ba06a52076
  - ev-fc5584be4b728c1c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f099620e8a7c85f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f651c3c92559068f
  evidence_ids:
  - ev-ae7188e078dc3f4e
  - ev-414cc7fbab1bc953
  - ev-754548779060ea63
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:19:42Z;
    reviewed SHA-256=cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279;
    current SHA-256=cd4c31bf43a22d6cce53ad49dc8cc30b3ce3f844a05a9a5f682d3484f1d17279;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Proline.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, structure fields, 0/0 count, and final SSSOM row pass, but the amino-acid
    role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ae7188e078dc3f4e
    - ev-414cc7fbab1bc953
  - name: legacy-native-ids
    value: '["SEM:67c923618030fea83bde","SEM:4e6778d3304ac93a23d3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-414cc7fbab1bc953
    - ev-ae7188e078dc3f4e
    - ev-754548779060ea63
- assessment_id: a-5e4355125c683f84
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f651c3c92559068f
  evidence_ids:
  - ev-ae7188e078dc3f4e
  - ev-5e4355125c683f84
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ae7188e078dc3f4e
    - ev-5e4355125c683f84
findings:
- finding_id: rec-f-9ade4a5f22ff6230
  issue_key: mim-reconciliation-role-support-f651c3c92559068f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Proline'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-f651c3c92559068f
  evidence_ids:
  - ev-ae7188e078dc3f4e
  - ev-5e4355125c683f84
  - ev-fa256eee39f733a1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Proline.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-9ade4a5f22ff6230
actions:
- action_id: rec-action-9ade4a5f22ff6230
  description: 'Reassess prediction-only role support: D-Proline'
  finding_ids:
  - rec-f-9ade4a5f22ff6230
  target_ids:
  - record-f651c3c92559068f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Proline.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
