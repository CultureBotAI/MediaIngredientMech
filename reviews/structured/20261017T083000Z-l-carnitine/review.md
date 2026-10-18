# Per-record structured review: L-Carnitine (data/ingredients/mapped/L-Carnitine.yaml)

- Review: 20261017T083000Z-l-carnitine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Carnitine (data/ingredients/mapped/L-Carnitine.yaml, record-235fa915e6835391, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Carnitine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Carnitine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-235fa915e6835391 | data/ingredients/mapped/L-Carnitine.yaml | maintained | L-Carnitine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-235fa915e6835391 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-235fa915e6835391 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-235fa915e6835391 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-235fa915e6835391.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-235fa915e6835391.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:01:17Z; reviewed SHA-256=83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754; current SHA-256=83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754; hash_changed=False. Reports=["reports/yaml_record_review/L-Carnitine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The stereospecific CHEBI:16347 identity and final SSSOM row pass, but the InChI and SMILES still describe the old achiral parent and VITAMIN_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-235fa915e6835391.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b5530c70eab2b4a4: Reassess prediction-only role support: L-Carnitine

major / open / confirmed; issue key: mim-reconciliation-role-support-235fa915e6835391.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b5530c70eab2b4a4

Reassess prediction-only role support: L-Carnitine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2d48e5552efe353b | data/ingredients/mapped/L-Carnitine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1218],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16347","line":1220,"mapping_status":"MAPPED","ontology_id":"CHEBI:16347","preferred_term":"L-Carnitine"}],"identifier":"CHEBI:16347","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:16347","ontology_label":"(R)-carnitine","ontology_source":"CHEBI"},"preferred_term":"L-Carnitine","sssom_rows":[{"data_row":1565,"object_id":"CHEBI:16347","object_label":"(R)-carnitine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Carnitine","synonym_count":2} |
| ev-59eeef2cb04e0290 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1218] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-691a751a20180833 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Carnitine; data-row positions=[1565] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1565,"object_id":"CHEBI:16347","object_label":"(R)-carnitine","other":"(3R)-3-hydroxy-4-(trimethylammonio)butanoate","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Carnitine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-29a8239e0e244f18 | docs/data/mapped_ingredients.csv; CSV lines=[1220] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16347","line":1220,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:16347","preferred_term":"L-Carnitine","total_occurrences":"2"}] |
| ev-da3ace7836567544 | reports/yaml_record_review/L-Carnitine.md; &#96;data/ingredients/mapped/L-Carnitine.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:54; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b9bb4b044f1517d9 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[785,1638] | context_only | [{"current_record_sha256":"83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754","finding_id":"SEM:f5cb6848c17e8b169ecc","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754","finding_id":"SEM:ad17281b70a7304e78ac","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-86a3590e7bda0723 | data/ingredients/mapped/L-Carnitine.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33229 (vitamin (role))","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"VITAMIN_SOURCE"}}] |
| ev-07e3e0d309d5f5c1 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-b5530c70eab2b4a4] | context_only | Predecessor structured review finding f-b5530c70eab2b4a4 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-carnitine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Carnitine (data/ingredients/mapped/L-Carnitine.yaml)'
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
summary: Per-record structured review for L-Carnitine (data/ingredients/mapped/L-Carnitine.yaml,
  record-235fa915e6835391, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Carnitine.yaml
    sha256: 83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-Carnitine.md
    sha256: 1ef8c8549b2853f3956b8121eb53f1c66de0af013e3ffb48055c58e1aba00479
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-235fa915e6835391
  path: data/ingredients/mapped/L-Carnitine.yaml
  label: L-Carnitine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Carnitine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Carnitine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Carnitine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-235fa915e6835391
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-235fa915e6835391
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-235fa915e6835391
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-235fa915e6835391
evidence:
- evidence_id: ev-2d48e5552efe353b
  kind: record_content
  reference: data/ingredients/mapped/L-Carnitine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1218],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16347","line":1220,"mapping_status":"MAPPED","ontology_id":"CHEBI:16347","preferred_term":"L-Carnitine"}],"identifier":"CHEBI:16347","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:16347","ontology_label":"(R)-carnitine","ontology_source":"CHEBI"},"preferred_term":"L-Carnitine","sssom_rows":[{"data_row":1565,"object_id":"CHEBI:16347","object_label":"(R)-carnitine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Carnitine","synonym_count":2}'
  snapshot_sha256: 83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754
- evidence_id: ev-59eeef2cb04e0290
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1218]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-691a751a20180833
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Carnitine; data-row positions=[1565]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1565,"object_id":"CHEBI:16347","object_label":"(R)-carnitine","other":"(3R)-3-hydroxy-4-(trimethylammonio)butanoate","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Carnitine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-29a8239e0e244f18
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1220]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16347","line":1220,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:16347","preferred_term":"L-Carnitine","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-da3ace7836567544
  kind: prior_review
  reference: reports/yaml_record_review/L-Carnitine.md
  locator: '`data/ingredients/mapped/L-Carnitine.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:32; Completeness:54; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1ef8c8549b2853f3956b8121eb53f1c66de0af013e3ffb48055c58e1aba00479
  quote: "Recommended Edits:\n- Major: update `chemical_properties.inchi` and `chemical_properties.smiles`\
    \ in\n  `data/ingredients/mapped/L-Carnitine.yaml` from `CHEBI:16347`, not the\
    \ old\n  achiral parent.\n- Major: remove `nutritional_roles.VITAMIN_SOURCE` unless\
    \ an inspected\n  CultureMech, FEBA, Hans80, or literature source can support\
    \ L-carnitine as a\n  vitamin source.\n- Minor: refresh the stale `notes`.\n-\
    \ Rerun strict, term, round-trip, component, and SSSOM validation after those\n\
    \  changes."
- evidence_id: ev-b9bb4b044f1517d9
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[785,1638]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754","finding_id":"SEM:f5cb6848c17e8b169ecc","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754","finding_id":"SEM:ad17281b70a7304e78ac","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-86a3590e7bda0723
  kind: record_content
  reference: data/ingredients/mapped/L-Carnitine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33229 (vitamin (role))","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"VITAMIN_SOURCE"}}]'
  snapshot_sha256: 83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754
- evidence_id: ev-07e3e0d309d5f5c1
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-b5530c70eab2b4a4]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b5530c70eab2b4a4 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-4666f07fcc884222
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-235fa915e6835391
  evidence_ids:
  - ev-2d48e5552efe353b
  - ev-59eeef2cb04e0290
  - ev-691a751a20180833
  - ev-29a8239e0e244f18
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-2b26a2dadc283df5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-235fa915e6835391
  evidence_ids:
  - ev-da3ace7836567544
  - ev-2d48e5552efe353b
  - ev-b9bb4b044f1517d9
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:01:17Z;
    reviewed SHA-256=83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754;
    current SHA-256=83717e970a478ac8248672c11d82a8d91f5732ea5e520bd388f2060e3632e754;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Carnitine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The stereospecific
    CHEBI:16347 identity and final SSSOM row pass, but the InChI and SMILES still
    describe the old achiral parent and VITAMIN_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-da3ace7836567544
    - ev-2d48e5552efe353b
  - name: legacy-native-ids
    value: '["SEM:f5cb6848c17e8b169ecc","SEM:ad17281b70a7304e78ac"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2d48e5552efe353b
    - ev-da3ace7836567544
    - ev-b9bb4b044f1517d9
- assessment_id: a-86a3590e7bda0723
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-235fa915e6835391
  evidence_ids:
  - ev-da3ace7836567544
  - ev-86a3590e7bda0723
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-da3ace7836567544
    - ev-86a3590e7bda0723
findings:
- finding_id: rec-f-b5530c70eab2b4a4
  issue_key: mim-reconciliation-role-support-235fa915e6835391
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Carnitine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-235fa915e6835391
  evidence_ids:
  - ev-da3ace7836567544
  - ev-86a3590e7bda0723
  - ev-07e3e0d309d5f5c1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Carnitine.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-b5530c70eab2b4a4
actions:
- action_id: rec-action-b5530c70eab2b4a4
  description: 'Reassess prediction-only role support: L-Carnitine'
  finding_ids:
  - rec-f-b5530c70eab2b4a4
  target_ids:
  - record-235fa915e6835391
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Carnitine.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
