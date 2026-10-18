# Per-record structured review: Magnesium_Sulfate (data/ingredients/mapped/Magnesium_Sulfate.yaml)

- Review: 20261017T083000Z-magnesium-sulfate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Magnesium_Sulfate (data/ingredients/mapped/Magnesium_Sulfate.yaml, record-a78f799e7bf32886, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Magnesium_Sulfate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Magnesium_Sulfate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a78f799e7bf32886 | data/ingredients/mapped/Magnesium_Sulfate.yaml | maintained | Magnesium_Sulfate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a78f799e7bf32886 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a78f799e7bf32886 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a78f799e7bf32886 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a78f799e7bf32886.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a78f799e7bf32886.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:12:46Z; reviewed SHA-256=f6bcc2e50cfd37107da60e61659ec24e3f323164e569e8a91e283b6acac96f4a; current SHA-256=5fbbaa3e38928f2d5af3f2e9c24075c4472e19606b65c0f306bceb77150673c0; hash_changed=True. Reports=["reports/yaml_record_review/Magnesium_Sulfate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The anhydrous identity and hydrate filtering pass, but the CultureMech mineral evidence is attached to SULFUR_SOURCE while MINERAL_SOURCE has no evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-a78f799e7bf32886.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-a78f799e7bf32886: Reassess prediction-only or empty role support: Magnesium_Sulfate

major / open / confirmed; issue key: mim-reconciliation-role-support-a78f799e7bf32886.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-a78f799e7bf32886

Reassess prediction-only or empty role support: Magnesium_Sulfate

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-61106872e91ac49b | data/ingredients/mapped/Magnesium_Sulfate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1327],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32599","line":1329,"mapping_status":"MAPPED","ontology_id":"CHEBI:32599","preferred_term":"Magnesium sulfate"}],"identifier":"CHEBI:32599","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":677,"edge_count":677,"occurrences":679},"occurrence_statistics":{"media_count":677,"total_occurrences":679},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32599","ontology_label":"magnesium sulfate","ontology_source":"CHEBI"},"preferred_term":"Magnesium sulfate","sssom_rows":[{"data_row":1746,"object_id":"CHEBI:32599","object_label":"magnesium sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Magnesium_Sulfate","synonym_count":27} |
| ev-259073fdf8ec7c96 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1327] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-055f7277e21d0ade | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Magnesium_Sulfate; data-row positions=[1746] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1746,"object_id":"CHEBI:32599","object_label":"magnesium sulfate","other":"Magnesium sulfate (1:1)&#124;Magnesiumsulfat&#124;Mg2SO4&#124;MgSO .7H O&#124;MgSO4&#124;CAS:7487-88-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Magnesium_Sulfate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-5920b7a4769dc786 | docs/data/mapped_ingredients.csv; CSV lines=[1329] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32599","line":1329,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"677","ontology_id":"CHEBI:32599","preferred_term":"Magnesium sulfate","total_occurrences":"679"}] |
| ev-6f3a721d712d3751 | reports/yaml_record_review/Magnesium_Sulfate.md; &#96;data/ingredients/mapped/Magnesium_Sulfate.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:31; Completeness:42; Recommended Edits:52 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6811b1ec7324631d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[883,1707] | context_only | [{"current_record_sha256":"f6bcc2e50cfd37107da60e61659ec24e3f323164e569e8a91e283b6acac96f4a","finding_id":"SEM:2b3741abe841db696ce3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f6bcc2e50cfd37107da60e61659ec24e3f323164e569e8a91e283b6acac96f4a","finding_id":"SEM:b1afd7e4c3cf0f41d873","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-51eaddab1c38ead4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Magnesium_Sulfate.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-magnesium-sulfate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Magnesium_Sulfate (data/ingredients/mapped/Magnesium_Sulfate.yaml)'
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
summary: Per-record structured review for Magnesium_Sulfate (data/ingredients/mapped/Magnesium_Sulfate.yaml,
  record-a78f799e7bf32886, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Magnesium_Sulfate.yaml
    sha256: 5fbbaa3e38928f2d5af3f2e9c24075c4472e19606b65c0f306bceb77150673c0
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Magnesium_Sulfate.md
    sha256: 2c4a044745104f99853821ced36692e56513a28926ce41616535d50ec16e09c5
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a78f799e7bf32886
  path: data/ingredients/mapped/Magnesium_Sulfate.yaml
  label: Magnesium_Sulfate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Magnesium_Sulfate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Magnesium_Sulfate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Magnesium_Sulfate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a78f799e7bf32886
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a78f799e7bf32886
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a78f799e7bf32886
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a78f799e7bf32886
evidence:
- evidence_id: ev-61106872e91ac49b
  kind: record_content
  reference: data/ingredients/mapped/Magnesium_Sulfate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1327],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32599","line":1329,"mapping_status":"MAPPED","ontology_id":"CHEBI:32599","preferred_term":"Magnesium
    sulfate"}],"identifier":"CHEBI:32599","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":677,"edge_count":677,"occurrences":679},"occurrence_statistics":{"media_count":677,"total_occurrences":679},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32599","ontology_label":"magnesium
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Magnesium sulfate","sssom_rows":[{"data_row":1746,"object_id":"CHEBI:32599","object_label":"magnesium
    sulfate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Magnesium_Sulfate","synonym_count":27}'
  snapshot_sha256: 5fbbaa3e38928f2d5af3f2e9c24075c4472e19606b65c0f306bceb77150673c0
- evidence_id: ev-259073fdf8ec7c96
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1327]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-055f7277e21d0ade
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Magnesium_Sulfate; data-row positions=[1746]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1746,"object_id":"CHEBI:32599","object_label":"magnesium
    sulfate","other":"Magnesium sulfate (1:1)|Magnesiumsulfat|Mg2SO4|MgSO .7H O|MgSO4|CAS:7487-88-9","predicate_id":"skos:exactMatch","subject_id":"MIM:Magnesium_Sulfate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5920b7a4769dc786
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1329]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32599","line":1329,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"677","ontology_id":"CHEBI:32599","preferred_term":"Magnesium
    sulfate","total_occurrences":"679"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6f3a721d712d3751
  kind: prior_review
  reference: reports/yaml_record_review/Magnesium_Sulfate.md
  locator: '`data/ingredients/mapped/Magnesium_Sulfate.yaml`:2; Verdict:4; Identity:12;
    Validation:23; Evidence:31; Completeness:42; Recommended Edits:52'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2c4a044745104f99853821ced36692e56513a28926ce41616535d50ec16e09c5
  quote: "Recommended Edits:\n- Move the CultureMech mineral-source evidence to `MINERAL_SOURCE`,\
    \ and either\n  add independent source-backed evidence for `SULFUR_SOURCE` or\
    \ remove that\n  role."
- evidence_id: ev-6811b1ec7324631d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[883,1707]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f6bcc2e50cfd37107da60e61659ec24e3f323164e569e8a91e283b6acac96f4a","finding_id":"SEM:2b3741abe841db696ce3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"f6bcc2e50cfd37107da60e61659ec24e3f323164e569e8a91e283b6acac96f4a","finding_id":"SEM:b1afd7e4c3cf0f41d873","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-51eaddab1c38ead4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Magnesium_Sulfate.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-a5a95abdadd25644
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a78f799e7bf32886
  evidence_ids:
  - ev-61106872e91ac49b
  - ev-259073fdf8ec7c96
  - ev-055f7277e21d0ade
  - ev-5920b7a4769dc786
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-65829cbaad0602a5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a78f799e7bf32886
  evidence_ids:
  - ev-6f3a721d712d3751
  - ev-61106872e91ac49b
  - ev-6811b1ec7324631d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:12:46Z;
    reviewed SHA-256=f6bcc2e50cfd37107da60e61659ec24e3f323164e569e8a91e283b6acac96f4a;
    current SHA-256=5fbbaa3e38928f2d5af3f2e9c24075c4472e19606b65c0f306bceb77150673c0;
    hash_changed=True. Reports=["reports/yaml_record_review/Magnesium_Sulfate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The anhydrous
    identity and hydrate filtering pass, but the CultureMech mineral evidence is attached
    to SULFUR_SOURCE while MINERAL_SOURCE has no evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6f3a721d712d3751
    - ev-61106872e91ac49b
  - name: legacy-native-ids
    value: '["SEM:2b3741abe841db696ce3","SEM:b1afd7e4c3cf0f41d873"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-61106872e91ac49b
    - ev-6f3a721d712d3751
    - ev-6811b1ec7324631d
- assessment_id: a-role-a78f799e7bf32886
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-a78f799e7bf32886
  evidence_ids:
  - ev-61106872e91ac49b
  - ev-51eaddab1c38ead4
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-61106872e91ac49b
    - ev-51eaddab1c38ead4
findings:
- finding_id: rec-f-role-a78f799e7bf32886
  issue_key: mim-reconciliation-role-support-a78f799e7bf32886
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Magnesium_Sulfate'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-a78f799e7bf32886
  evidence_ids:
  - ev-61106872e91ac49b
  - ev-51eaddab1c38ead4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Magnesium_Sulfate.yaml
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
- action_id: rec-act-role-a78f799e7bf32886
  description: 'Reassess prediction-only or empty role support: Magnesium_Sulfate'
  finding_ids:
  - rec-f-role-a78f799e7bf32886
  target_ids:
  - record-a78f799e7bf32886
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Magnesium_Sulfate.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
