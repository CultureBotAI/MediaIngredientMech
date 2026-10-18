# Per-record structured review: Beef_Brain_Powder (data/ingredients/mapped/Beef_Brain_Powder.yaml)

- Review: 20261017T083000Z-beef-brain-powder
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Beef_Brain_Powder (data/ingredients/mapped/Beef_Brain_Powder.yaml, record-7cecbc2e3078cb72, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Beef_Brain_Powder.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Beef_Brain_Powder.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7cecbc2e3078cb72 | data/ingredients/mapped/Beef_Brain_Powder.yaml | maintained | Beef_Brain_Powder |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7cecbc2e3078cb72 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7cecbc2e3078cb72 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7cecbc2e3078cb72 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7cecbc2e3078cb72.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7cecbc2e3078cb72.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:24:42Z; reviewed SHA-256=9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d; current SHA-256=9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d; hash_changed=False. Reports=["reports/yaml_record_review/Beef_Brain_Powder.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient beef brain powder identity, FOODON parent, protein-source role, occurrence count, SSSOM rows, and aggregate copy pass, but top-level notes still describe the old unmapped state.

### Historical provisional-role concern

evidence: concern. Targets: record-7cecbc2e3078cb72.

Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-7cecbc2e3078cb72: Reassess prediction-only or empty role support: Beef_Brain_Powder

major / open / confirmed; issue key: mim-reconciliation-role-support-7cecbc2e3078cb72.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[0]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-7cecbc2e3078cb72

Reassess prediction-only or empty role support: Beef_Brain_Powder

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-09e08cb79e2da598 | data/ingredients/mapped/Beef_Brain_Powder.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[562],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:beef_brain_powder","line":564,"mapping_status":"MAPPED","ontology_id":"FOODON:02020911","preferred_term":"Beef brain powder"}],"identifier":"kgmicrobe.ingredient:beef_brain_powder","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"FOODON:02020911","ontology_label":"beef brain","ontology_source":"FOODON"},"preferred_term":"Beef brain powder","sssom_rows":[{"data_row":496,"object_id":"FOODON:02020911","object_label":"beef brain","predicate_id":"skos:broadMatch"},{"data_row":497,"object_id":"kgmicrobe.ingredient:beef_brain_powder","object_label":"Beef brain powder","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Brain_Powder","synonym_count":1} |
| ev-7b5c32e0cd18c343 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [562] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e6efefd76ee59fcd | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Beef_Brain_Powder; data-row positions=[496,497] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":496,"object_id":"FOODON:02020911","object_label":"beef brain","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Beef_Brain_Powder","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":497,"object_id":"kgmicrobe.ingredient:beef_brain_powder","object_label":"Beef brain powder","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Brain_Powder","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-0511d4bf09325151 | docs/data/mapped_ingredients.csv; CSV lines=[564] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:beef_brain_powder","line":564,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"FOODON:02020911","preferred_term":"Beef brain powder","total_occurrences":"3"}] |
| ev-7558e8cf1f38d267 | reports/yaml_record_review/Beef_Brain_Powder.md; &#96;data/ingredients/mapped/Beef_Brain_Powder.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:34; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-46ebaeda2f55e5f0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[298,1727] | context_only | [{"current_record_sha256":"9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d","finding_id":"SEM:80d73d6e44639d8012ac","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d","finding_id":"SEM:0821239c4fb303e088ca","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-256ed3f1c8a4c67e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Beef_Brain_Powder.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-beef-brain-powder
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Beef_Brain_Powder (data/ingredients/mapped/Beef_Brain_Powder.yaml)'
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
summary: Per-record structured review for Beef_Brain_Powder (data/ingredients/mapped/Beef_Brain_Powder.yaml,
  record-7cecbc2e3078cb72, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Beef_Brain_Powder.yaml
    sha256: 9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Beef_Brain_Powder.md
    sha256: 0854cd8b59e9e1ce5bebc57abe72796fa93db9399d98a181576093bf51da371e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7cecbc2e3078cb72
  path: data/ingredients/mapped/Beef_Brain_Powder.yaml
  label: Beef_Brain_Powder
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Brain_Powder.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Beef_Brain_Powder.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Beef_Brain_Powder.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7cecbc2e3078cb72
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7cecbc2e3078cb72
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7cecbc2e3078cb72
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7cecbc2e3078cb72
evidence:
- evidence_id: ev-09e08cb79e2da598
  kind: record_content
  reference: data/ingredients/mapped/Beef_Brain_Powder.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[562],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:beef_brain_powder","line":564,"mapping_status":"MAPPED","ontology_id":"FOODON:02020911","preferred_term":"Beef
    brain powder"}],"identifier":"kgmicrobe.ingredient:beef_brain_powder","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"FOODON:02020911","ontology_label":"beef
    brain","ontology_source":"FOODON"},"preferred_term":"Beef brain powder","sssom_rows":[{"data_row":496,"object_id":"FOODON:02020911","object_label":"beef
    brain","predicate_id":"skos:broadMatch"},{"data_row":497,"object_id":"kgmicrobe.ingredient:beef_brain_powder","object_label":"Beef
    brain powder","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Beef_Brain_Powder","synonym_count":1}'
  snapshot_sha256: 9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d
- evidence_id: ev-7b5c32e0cd18c343
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [562]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e6efefd76ee59fcd
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Beef_Brain_Powder; data-row positions=[496,497]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":496,"object_id":"FOODON:02020911","object_label":"beef
    brain","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Beef_Brain_Powder","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":497,"object_id":"kgmicrobe.ingredient:beef_brain_powder","object_label":"Beef
    brain powder","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Beef_Brain_Powder","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0511d4bf09325151
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[564]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:beef_brain_powder","line":564,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"FOODON:02020911","preferred_term":"Beef
    brain powder","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7558e8cf1f38d267
  kind: prior_review
  reference: reports/yaml_record_review/Beef_Brain_Powder.md
  locator: '`data/ingredients/mapped/Beef_Brain_Powder.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:34; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0854cd8b59e9e1ce5bebc57abe72796fa93db9399d98a181576093bf51da371e
  quote: "Recommended Edits:\n- Minor: update `notes` in `data/ingredients/mapped/Beef_Brain_Powder.yaml`\
    \ to\n  describe the current kg-microbe identity and FOODON parent mapping, then\
    \ run\n  `just sync-curated`."
- evidence_id: ev-46ebaeda2f55e5f0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[298,1727]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d","finding_id":"SEM:80d73d6e44639d8012ac","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d","finding_id":"SEM:0821239c4fb303e088ca","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-256ed3f1c8a4c67e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Beef_Brain_Powder.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8bbec2254ee6c0e2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7cecbc2e3078cb72
  evidence_ids:
  - ev-09e08cb79e2da598
  - ev-7b5c32e0cd18c343
  - ev-e6efefd76ee59fcd
  - ev-0511d4bf09325151
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9a3b2ce45f0dce51
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7cecbc2e3078cb72
  evidence_ids:
  - ev-7558e8cf1f38d267
  - ev-09e08cb79e2da598
  - ev-46ebaeda2f55e5f0
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:24:42Z;
    reviewed SHA-256=9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d;
    current SHA-256=9bdfb13d95e4140a9933254a20bdcab449311e70cfe334b001a5713d1526c51d;
    hash_changed=False. Reports=["reports/yaml_record_review/Beef_Brain_Powder.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The kgmicrobe.ingredient
    beef brain powder identity, FOODON parent, protein-source role, occurrence count,
    SSSOM rows, and aggregate copy pass, but top-level notes still describe the old
    unmapped state.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7558e8cf1f38d267
    - ev-09e08cb79e2da598
  - name: legacy-native-ids
    value: '["SEM:80d73d6e44639d8012ac","SEM:0821239c4fb303e088ca"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-09e08cb79e2da598
    - ev-7558e8cf1f38d267
    - ev-46ebaeda2f55e5f0
- assessment_id: a-role-7cecbc2e3078cb72
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-7cecbc2e3078cb72
  evidence_ids:
  - ev-09e08cb79e2da598
  - ev-256ed3f1c8a4c67e
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-09e08cb79e2da598
    - ev-256ed3f1c8a4c67e
findings:
- finding_id: rec-f-role-7cecbc2e3078cb72
  issue_key: mim-reconciliation-role-support-7cecbc2e3078cb72
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Beef_Brain_Powder'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[0]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-7cecbc2e3078cb72
  evidence_ids:
  - ev-09e08cb79e2da598
  - ev-256ed3f1c8a4c67e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Brain_Powder.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-7cecbc2e3078cb72
  description: 'Reassess prediction-only or empty role support: Beef_Brain_Powder'
  finding_ids:
  - rec-f-role-7cecbc2e3078cb72
  target_ids:
  - record-7cecbc2e3078cb72
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Beef_Brain_Powder.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
