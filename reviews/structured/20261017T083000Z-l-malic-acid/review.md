# Per-record structured review: L-Malic_Acid (data/ingredients/mapped/L-Malic_Acid.yaml)

- Review: 20261017T083000Z-l-malic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-Malic_Acid (data/ingredients/mapped/L-Malic_Acid.yaml, record-5f893bb18a917432, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-Malic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-Malic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5f893bb18a917432 | data/ingredients/mapped/L-Malic_Acid.yaml | maintained | L-Malic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5f893bb18a917432 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5f893bb18a917432 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5f893bb18a917432 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5f893bb18a917432.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5f893bb18a917432.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:17:50Z; reviewed SHA-256=e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4; current SHA-256=e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4; hash_changed=False. Reports=["reports/yaml_record_review/L-Malic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI lookup identity, active CHEBI:30797 grounding, ChEBI synonym, PubChem structure, and final SSSOM row pass, but CARBON_SOURCE and ENERGY_SOURCE are provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-5f893bb18a917432.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-57fa98147568cb98: Reassess prediction-only role support: L-Malic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-5f893bb18a917432.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-57fa98147568cb98

Reassess prediction-only role support: L-Malic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-583d7a6fb05792dc | data/ingredients/mapped/L-Malic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1227],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30797","line":1229,"mapping_status":"MAPPED","ontology_id":"CHEBI:30797","preferred_term":"L-Malic acid"}],"identifier":"CHEBI:30797","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:30797","ontology_label":"(S)-malic acid","ontology_source":"CHEBI"},"preferred_term":"L-Malic acid","sssom_rows":[{"data_row":1579,"object_id":"CHEBI:30797","object_label":"(S)-malic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Malic_Acid","synonym_count":1} |
| ev-23c54e176be298ec | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1227] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-06e78b0e1a3b3741 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-Malic_Acid; data-row positions=[1579] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1579,"object_id":"CHEBI:30797","object_label":"(S)-malic acid","other":"(2S)-2-hydroxybutanedioic acid&#124;CAS:97-67-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Malic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-a10c3676cee51040 | docs/data/mapped_ingredients.csv; CSV lines=[1229] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30797","line":1229,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30797","preferred_term":"L-Malic acid","total_occurrences":"0"}] |
| ev-d9eaeaa661612935 | reports/yaml_record_review/L-Malic_Acid.md; &#96;data/ingredients/mapped/L-Malic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:32; Completeness:51; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bc7d92054fda5917 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[794,1915,1925] | context_only | [{"current_record_sha256":"e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4","finding_id":"SEM:125e58096aa485f19d93","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4","finding_id":"SEM:2608131fae071e1bff85","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4","finding_id":"SEM:aca9caf6bad7c0ee8301","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-406534c61b3f2673 | data/ingredients/mapped/L-Malic_Acid.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-e3a76e3f854db174 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-57fa98147568cb98] | context_only | Predecessor structured review finding f-57fa98147568cb98 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-malic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-Malic_Acid (data/ingredients/mapped/L-Malic_Acid.yaml)'
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
summary: Per-record structured review for L-Malic_Acid (data/ingredients/mapped/L-Malic_Acid.yaml,
  record-5f893bb18a917432, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-Malic_Acid.yaml
    sha256: e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4
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
  - path: reports/yaml_record_review/L-Malic_Acid.md
    sha256: d7118bab9a360413a9b35ba507b464527d891ef59e6b6da04cc4f140030d76e3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5f893bb18a917432
  path: data/ingredients/mapped/L-Malic_Acid.yaml
  label: L-Malic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Malic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-Malic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-Malic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5f893bb18a917432
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5f893bb18a917432
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-5f893bb18a917432
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5f893bb18a917432
evidence:
- evidence_id: ev-583d7a6fb05792dc
  kind: record_content
  reference: data/ingredients/mapped/L-Malic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1227],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30797","line":1229,"mapping_status":"MAPPED","ontology_id":"CHEBI:30797","preferred_term":"L-Malic
    acid"}],"identifier":"CHEBI:30797","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:30797","ontology_label":"(S)-malic
    acid","ontology_source":"CHEBI"},"preferred_term":"L-Malic acid","sssom_rows":[{"data_row":1579,"object_id":"CHEBI:30797","object_label":"(S)-malic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-Malic_Acid","synonym_count":1}'
  snapshot_sha256: e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4
- evidence_id: ev-23c54e176be298ec
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1227]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-06e78b0e1a3b3741
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-Malic_Acid; data-row positions=[1579]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1579,"object_id":"CHEBI:30797","object_label":"(S)-malic
    acid","other":"(2S)-2-hydroxybutanedioic acid|CAS:97-67-6","predicate_id":"skos:exactMatch","subject_id":"MIM:L-Malic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-a10c3676cee51040
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1229]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30797","line":1229,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30797","preferred_term":"L-Malic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d9eaeaa661612935
  kind: prior_review
  reference: reports/yaml_record_review/L-Malic_Acid.md
  locator: '`data/ingredients/mapped/L-Malic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:32; Completeness:51; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d7118bab9a360413a9b35ba507b464527d891ef59e6b6da04cc4f140030d76e3
  quote: "Recommended Edits:\n- Major: remove `nutritional_roles.CARBON_SOURCE` and\n\
    \  `nutritional_roles.ENERGY_SOURCE` unless inspected CultureMech, FEBA, Hans80,\n\
    \  or literature sources can support L-malic acid as a carbon and energy source.\n\
    - Rerun strict, term, round-trip, role, component, and SSSOM validation after\n\
    \  the role changes."
- evidence_id: ev-bc7d92054fda5917
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[794,1915,1925]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4","finding_id":"SEM:125e58096aa485f19d93","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4","finding_id":"SEM:2608131fae071e1bff85","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4","finding_id":"SEM:aca9caf6bad7c0ee8301","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-406534c61b3f2673
  kind: record_content
  reference: data/ingredients/mapped/L-Malic_Acid.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4
- evidence_id: ev-e3a76e3f854db174
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-57fa98147568cb98]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-57fa98147568cb98 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-6f2e5105c2147a7d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5f893bb18a917432
  evidence_ids:
  - ev-583d7a6fb05792dc
  - ev-23c54e176be298ec
  - ev-06e78b0e1a3b3741
  - ev-a10c3676cee51040
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b39fde006eced230
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5f893bb18a917432
  evidence_ids:
  - ev-d9eaeaa661612935
  - ev-583d7a6fb05792dc
  - ev-bc7d92054fda5917
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T22:17:50Z;
    reviewed SHA-256=e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4;
    current SHA-256=e7b8206eb0d5eb266272a7b60dc9468ec69264e86f427d8aacb0d32730cb1af4;
    hash_changed=False. Reports=["reports/yaml_record_review/L-Malic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-to-ChEBI
    lookup identity, active CHEBI:30797 grounding, ChEBI synonym, PubChem structure,
    and final SSSOM row pass, but CARBON_SOURCE and ENERGY_SOURCE are provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d9eaeaa661612935
    - ev-583d7a6fb05792dc
  - name: legacy-native-ids
    value: '["SEM:125e58096aa485f19d93","SEM:2608131fae071e1bff85","SEM:aca9caf6bad7c0ee8301"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-583d7a6fb05792dc
    - ev-d9eaeaa661612935
    - ev-bc7d92054fda5917
- assessment_id: a-406534c61b3f2673
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5f893bb18a917432
  evidence_ids:
  - ev-d9eaeaa661612935
  - ev-406534c61b3f2673
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d9eaeaa661612935
    - ev-406534c61b3f2673
findings:
- finding_id: rec-f-57fa98147568cb98
  issue_key: mim-reconciliation-role-support-5f893bb18a917432
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Malic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5f893bb18a917432
  evidence_ids:
  - ev-d9eaeaa661612935
  - ev-406534c61b3f2673
  - ev-e3a76e3f854db174
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Malic_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-57fa98147568cb98
actions:
- action_id: rec-action-57fa98147568cb98
  description: 'Reassess prediction-only role support: L-Malic acid'
  finding_ids:
  - rec-f-57fa98147568cb98
  target_ids:
  - record-5f893bb18a917432
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-Malic_Acid.yaml
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
