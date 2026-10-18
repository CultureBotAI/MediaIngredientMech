# Per-record structured review: Caso4 (data/ingredients/mapped/Caso4.yaml)

- Review: 20261017T083000Z-caso4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Caso4 (data/ingredients/mapped/Caso4.yaml, record-800a127510e8ba13, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Caso4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Caso4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-800a127510e8ba13 | data/ingredients/mapped/Caso4.yaml | maintained | Caso4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-800a127510e8ba13 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-800a127510e8ba13 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-800a127510e8ba13 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-800a127510e8ba13.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-800a127510e8ba13.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:09:19Z; reviewed SHA-256=6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992; current SHA-256=6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992; hash_changed=False. Reports=["reports/yaml_record_review/Caso4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI anhydrous calcium sulfate identity and rejected hydrate alias pass, but MINERAL_SOURCE has an empty evidence list.

### Historical provisional-role concern

evidence: concern. Targets: record-800a127510e8ba13.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-800a127510e8ba13: Reassess prediction-only or empty role support: Caso4

major / open / confirmed; issue key: mim-reconciliation-role-support-800a127510e8ba13.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-800a127510e8ba13

Reassess prediction-only or empty role support: Caso4

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2f827fbdec425020 | data/ingredients/mapped/Caso4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[666],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31346","line":668,"mapping_status":"MAPPED","ontology_id":"CHEBI:31346","preferred_term":"CaSO4"}],"identifier":"CHEBI:31346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":15,"edge_count":15,"occurrences":15},"occurrence_statistics":{"media_count":15,"total_occurrences":15},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31346","ontology_label":"calcium sulfate","ontology_source":"CHEBI"},"preferred_term":"CaSO4","sssom_rows":[{"data_row":663,"object_id":"CHEBI:31346","object_label":"calcium sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caso4","synonym_count":5} |
| ev-a6ea2ae0b8f33e39 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [666] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a3d917338e20c808 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Caso4; data-row positions=[663] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":663,"object_id":"CHEBI:31346","object_label":"calcium sulfate","other":"Kalziumsulfat&#124;calcium sulphate&#124;CAS:7778-18-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Caso4","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-cef53b9f174a9d13 | docs/data/mapped_ingredients.csv; CSV lines=[668] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31346","line":668,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"15","ontology_id":"CHEBI:31346","preferred_term":"CaSO4","total_occurrences":"15"}] |
| ev-a45afaa9539b1d17 | reports/yaml_record_review/Caso4.md; &#96;data/ingredients/mapped/Caso4.yaml&#96;:2; Verdict:4; Identity:10; Validation:25; Evidence:46; Completeness:60; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8a5bec75f7b2bb23 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[370,2033] | context_only | [{"current_record_sha256":"6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992","finding_id":"SEM:cd33e3b22c3a62dca80f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992","finding_id":"SEM:df303b4d5f6b3e0e10ff","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-e334f003e4f667a0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Caso4.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-caso4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Caso4 (data/ingredients/mapped/Caso4.yaml)'
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
summary: Per-record structured review for Caso4 (data/ingredients/mapped/Caso4.yaml,
  record-800a127510e8ba13, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Caso4.yaml
    sha256: 6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992
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
  - path: reports/yaml_record_review/Caso4.md
    sha256: bbc2408bae928dea94caf278ab58b39d121e070dcd80a17f3be435d3ed132d66
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-800a127510e8ba13
  path: data/ingredients/mapped/Caso4.yaml
  label: Caso4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caso4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Caso4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Caso4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-800a127510e8ba13
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-800a127510e8ba13
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-800a127510e8ba13
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-800a127510e8ba13
evidence:
- evidence_id: ev-2f827fbdec425020
  kind: record_content
  reference: data/ingredients/mapped/Caso4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[666],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31346","line":668,"mapping_status":"MAPPED","ontology_id":"CHEBI:31346","preferred_term":"CaSO4"}],"identifier":"CHEBI:31346","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":15,"edge_count":15,"occurrences":15},"occurrence_statistics":{"media_count":15,"total_occurrences":15},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31346","ontology_label":"calcium
    sulfate","ontology_source":"CHEBI"},"preferred_term":"CaSO4","sssom_rows":[{"data_row":663,"object_id":"CHEBI:31346","object_label":"calcium
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caso4","synonym_count":5}'
  snapshot_sha256: 6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992
- evidence_id: ev-a6ea2ae0b8f33e39
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [666]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a3d917338e20c808
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Caso4; data-row positions=[663]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":663,"object_id":"CHEBI:31346","object_label":"calcium
    sulfate","other":"Kalziumsulfat|calcium sulphate|CAS:7778-18-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Caso4","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cef53b9f174a9d13
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[668]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31346","line":668,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"15","ontology_id":"CHEBI:31346","preferred_term":"CaSO4","total_occurrences":"15"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a45afaa9539b1d17
  kind: prior_review
  reference: reports/yaml_record_review/Caso4.md
  locator: '`data/ingredients/mapped/Caso4.yaml`:2; Verdict:4; Identity:10; Validation:25;
    Evidence:46; Completeness:60; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: bbc2408bae928dea94caf278ab58b39d121e070dcd80a17f3be435d3ed132d66
  quote: "Recommended Edits:\n- Major: add inspected evidence to\n  `nutritional_roles.MINERAL_SOURCE`\
    \ in\n  `data/ingredients/mapped/Caso4.yaml`, or remove the role if the bulk-cation\n\
    \  assertion is not supported for calcium sulfate, then rerun strict\n  validation,\
    \ SSSOM QC, aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-8a5bec75f7b2bb23
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[370,2033]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992","finding_id":"SEM:cd33e3b22c3a62dca80f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992","finding_id":"SEM:df303b4d5f6b3e0e10ff","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-e334f003e4f667a0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Caso4.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8cba292b9842a038
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-800a127510e8ba13
  evidence_ids:
  - ev-2f827fbdec425020
  - ev-a6ea2ae0b8f33e39
  - ev-a3d917338e20c808
  - ev-cef53b9f174a9d13
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f5d78180d897d39a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-800a127510e8ba13
  evidence_ids:
  - ev-a45afaa9539b1d17
  - ev-2f827fbdec425020
  - ev-8a5bec75f7b2bb23
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:09:19Z;
    reviewed SHA-256=6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992;
    current SHA-256=6da3aa885099c64ec01b21c9034309f9775620d7c21a6cc9c2c25c950eb29992;
    hash_changed=False. Reports=["reports/yaml_record_review/Caso4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI anhydrous
    calcium sulfate identity and rejected hydrate alias pass, but MINERAL_SOURCE has
    an empty evidence list.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a45afaa9539b1d17
    - ev-2f827fbdec425020
  - name: legacy-native-ids
    value: '["SEM:cd33e3b22c3a62dca80f","SEM:df303b4d5f6b3e0e10ff"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2f827fbdec425020
    - ev-a45afaa9539b1d17
    - ev-8a5bec75f7b2bb23
- assessment_id: a-role-800a127510e8ba13
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-800a127510e8ba13
  evidence_ids:
  - ev-2f827fbdec425020
  - ev-e334f003e4f667a0
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2f827fbdec425020
    - ev-e334f003e4f667a0
findings:
- finding_id: rec-f-role-800a127510e8ba13
  issue_key: mim-reconciliation-role-support-800a127510e8ba13
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Caso4'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-800a127510e8ba13
  evidence_ids:
  - ev-2f827fbdec425020
  - ev-e334f003e4f667a0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caso4.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-800a127510e8ba13
  description: 'Reassess prediction-only or empty role support: Caso4'
  finding_ids:
  - rec-f-role-800a127510e8ba13
  target_ids:
  - record-800a127510e8ba13
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caso4.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
