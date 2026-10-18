# Per-record structured review: Levodopa (data/ingredients/mapped/Levodopa.yaml)

- Review: 20261017T083000Z-levodopa
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Levodopa (data/ingredients/mapped/Levodopa.yaml, record-da818097f6edd08a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Levodopa.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Levodopa.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-da818097f6edd08a | data/ingredients/mapped/Levodopa.yaml | maintained | Levodopa |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-da818097f6edd08a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-da818097f6edd08a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-da818097f6edd08a | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-da818097f6edd08a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-da818097f6edd08a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z; reviewed SHA-256=aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289; current SHA-256=aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289; hash_changed=False. Reports=["reports/yaml_record_review/Levodopa.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI:15765 identity, CAS value, PubChem structure, exact synonym, and final SSSOM row pass, but AMINO_ACID_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-da818097f6edd08a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0eebfb7be9856ff1: Reassess prediction-only role support: Levodopa

major / open / confirmed; issue key: mim-reconciliation-role-support-da818097f6edd08a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0eebfb7be9856ff1

Reassess prediction-only role support: Levodopa

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bb08e4ccaa895e7e | data/ingredients/mapped/Levodopa.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1295],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15765","line":1297,"mapping_status":"MAPPED","ontology_id":"CHEBI:15765","preferred_term":"Levodopa"}],"identifier":"CHEBI:15765","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15765","ontology_label":"L-dopa","ontology_source":"CHEBI"},"preferred_term":"Levodopa","sssom_rows":[{"data_row":1685,"object_id":"CHEBI:15765","object_label":"L-dopa","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levodopa","synonym_count":1} |
| ev-514e1cf044e40612 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1295] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a1634be0e0903868 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Levodopa; data-row positions=[1685] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1685,"object_id":"CHEBI:15765","object_label":"L-dopa","other":"(2S)-2-amino-3-(3,4-dihydroxyphenyl)propanoic acid&#124;CAS:59-92-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Levodopa","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-6bc02379608ff67c | docs/data/mapped_ingredients.csv; CSV lines=[1297] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15765","line":1297,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15765","preferred_term":"Levodopa","total_occurrences":"0"}] |
| ev-930e378a624018cb | reports/yaml_record_review/Levodopa.md; &#96;data/ingredients/mapped/Levodopa.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:27; Completeness:45; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-54a001bf9638f3c5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[857,2004] | context_only | [{"current_record_sha256":"aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289","finding_id":"SEM:e48324db0dce15ab2125","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289","finding_id":"SEM:c67940f86288824c0462","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9e7b49f9663a4b50 | data/ingredients/mapped/Levodopa.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1295],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15765","line":1297,"mapping_status":"MAPPED","ontology_id":"CHEBI:15765","preferred_term":"Levodopa"}],"identifier":"CHEBI:15765","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15765","ontology_label":"L-dopa","ontology_source":"CHEBI"},"preferred_term":"Levodopa","sssom_rows":[{"data_row":1685,"object_id":"CHEBI:15765","object_label":"L-dopa","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levodopa","synonym_count":1} |
| ev-1ae92f0aeac6b227 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-0eebfb7be9856ff1] | context_only | Predecessor structured review finding f-0eebfb7be9856ff1 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-levodopa
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Levodopa (data/ingredients/mapped/Levodopa.yaml)'
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
summary: Per-record structured review for Levodopa (data/ingredients/mapped/Levodopa.yaml,
  record-da818097f6edd08a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Levodopa.yaml
    sha256: aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289
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
  - path: reports/yaml_record_review/Levodopa.md
    sha256: 73a04b9c075519fc67138b20e6ae8f4b318d9c3becc25a0bcf30eedd1c4532c0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-da818097f6edd08a
  path: data/ingredients/mapped/Levodopa.yaml
  label: Levodopa
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levodopa.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Levodopa.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Levodopa.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-da818097f6edd08a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-bb08e4ccaa895e7e
  - ev-514e1cf044e40612
  - ev-a1634be0e0903868
  - ev-6bc02379608ff67c
  - ev-9e7b49f9663a4b50
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-bb08e4ccaa895e7e
  - ev-54a001bf9638f3c5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-930e378a624018cb
  - ev-54a001bf9638f3c5
  - ev-1ae92f0aeac6b227
evidence:
- evidence_id: ev-bb08e4ccaa895e7e
  kind: record_content
  reference: data/ingredients/mapped/Levodopa.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1295],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15765","line":1297,"mapping_status":"MAPPED","ontology_id":"CHEBI:15765","preferred_term":"Levodopa"}],"identifier":"CHEBI:15765","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15765","ontology_label":"L-dopa","ontology_source":"CHEBI"},"preferred_term":"Levodopa","sssom_rows":[{"data_row":1685,"object_id":"CHEBI:15765","object_label":"L-dopa","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levodopa","synonym_count":1}'
  snapshot_sha256: aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289
- evidence_id: ev-514e1cf044e40612
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1295]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a1634be0e0903868
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Levodopa; data-row positions=[1685]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1685,"object_id":"CHEBI:15765","object_label":"L-dopa","other":"(2S)-2-amino-3-(3,4-dihydroxyphenyl)propanoic
    acid|CAS:59-92-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Levodopa","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6bc02379608ff67c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1297]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15765","line":1297,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:15765","preferred_term":"Levodopa","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-930e378a624018cb
  kind: prior_review
  reference: reports/yaml_record_review/Levodopa.md
  locator: '`data/ingredients/mapped/Levodopa.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:27; Completeness:45; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 73a04b9c075519fc67138b20e6ae8f4b318d9c3becc25a0bcf30eedd1c4532c0
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.AMINO_ACID_SOURCE`\
    \ in\n  `data/ingredients/mapped/Levodopa.yaml` with inspected source evidence\
    \ for\n  exact levodopa use, or remove the provisional role.\n- Sync the aggregate\
    \ copy and regenerate derived products after the YAML\n  change; rerun strict,\
    \ term, round-trip, component, and SSSOM validation."
- evidence_id: ev-54a001bf9638f3c5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[857,2004]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289","finding_id":"SEM:e48324db0dce15ab2125","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289","finding_id":"SEM:c67940f86288824c0462","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9e7b49f9663a4b50
  kind: record_content
  reference: data/ingredients/mapped/Levodopa.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1295],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15765","line":1297,"mapping_status":"MAPPED","ontology_id":"CHEBI:15765","preferred_term":"Levodopa"}],"identifier":"CHEBI:15765","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:15765","ontology_label":"L-dopa","ontology_source":"CHEBI"},"preferred_term":"Levodopa","sssom_rows":[{"data_row":1685,"object_id":"CHEBI:15765","object_label":"L-dopa","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Levodopa","synonym_count":1}'
  snapshot_sha256: aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289
- evidence_id: ev-1ae92f0aeac6b227
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-0eebfb7be9856ff1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0eebfb7be9856ff1 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-b59588543ba0af60
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-bb08e4ccaa895e7e
  - ev-514e1cf044e40612
  - ev-a1634be0e0903868
  - ev-6bc02379608ff67c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-96883e94d5a51202
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-930e378a624018cb
  - ev-bb08e4ccaa895e7e
  - ev-54a001bf9638f3c5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:13:53Z;
    reviewed SHA-256=aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289;
    current SHA-256=aee2a4121b935ca1e59b964a653d4ec540709a60735864c457525aeb4d4ba289;
    hash_changed=False. Reports=["reports/yaml_record_review/Levodopa.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI:15765
    identity, CAS value, PubChem structure, exact synonym, and final SSSOM row pass,
    but AMINO_ACID_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-930e378a624018cb
    - ev-bb08e4ccaa895e7e
  - name: legacy-native-ids
    value: '["SEM:e48324db0dce15ab2125","SEM:c67940f86288824c0462"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bb08e4ccaa895e7e
    - ev-930e378a624018cb
    - ev-54a001bf9638f3c5
- assessment_id: a-9e7b49f9663a4b50
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-930e378a624018cb
  - ev-9e7b49f9663a4b50
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-930e378a624018cb
    - ev-9e7b49f9663a4b50
findings:
- finding_id: rec-f-0eebfb7be9856ff1
  issue_key: mim-reconciliation-role-support-da818097f6edd08a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Levodopa'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-da818097f6edd08a
  evidence_ids:
  - ev-930e378a624018cb
  - ev-9e7b49f9663a4b50
  - ev-1ae92f0aeac6b227
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levodopa.yaml
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
    finding_id: f-0eebfb7be9856ff1
actions:
- action_id: rec-action-0eebfb7be9856ff1
  description: 'Reassess prediction-only role support: Levodopa'
  finding_ids:
  - rec-f-0eebfb7be9856ff1
  target_ids:
  - record-da818097f6edd08a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Levodopa.yaml
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
