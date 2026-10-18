# Per-record structured review: Caproic_Acid (data/ingredients/mapped/Caproic_Acid.yaml)

- Review: 20261017T083000Z-caproic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Caproic_Acid (data/ingredients/mapped/Caproic_Acid.yaml, record-604f4ded295836c8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Caproic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Caproic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-604f4ded295836c8 | data/ingredients/mapped/Caproic_Acid.yaml | maintained | Caproic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-604f4ded295836c8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-604f4ded295836c8 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-604f4ded295836c8 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-604f4ded295836c8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-604f4ded295836c8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:43Z; reviewed SHA-256=49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5; current SHA-256=49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050143Z-Caproic_Acid.md","reports/yaml_record_review/Caproic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Caproic_Acid.md&#96; after the record changed from 3a0e9bb0f34f0527ccc71b0e740d3582ac047b50bf32c45d600bd69b04a33373 to 49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-604f4ded295836c8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f1059d9657bfbc03: Reassess prediction-only role support: Caproic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-604f4ded295836c8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f1059d9657bfbc03

Reassess prediction-only role support: Caproic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4aa1d97b46ff4b29 | data/ingredients/mapped/Caproic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[646],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30776","line":648,"mapping_status":"MAPPED","ontology_id":"CHEBI:30776","preferred_term":"Caproic acid"}],"identifier":"CHEBI:30776","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30776","ontology_label":"hexanoic acid","ontology_source":"CHEBI"},"preferred_term":"Caproic acid","sssom_rows":[{"data_row":630,"object_id":"CHEBI:30776","object_label":"hexanoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caproic_Acid","synonym_count":17} |
| ev-e82b528abf22d8a4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [646] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-232f5a016f8a99a8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Caproic_Acid; data-row positions=[630] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":630,"object_id":"CHEBI:30776","object_label":"hexanoic acid","other":"1-hexanoic acid&#124;1-pentanecarboxylic acid&#124;6:0&#124;CH3-[CH2]4-COOH&#124;Capronic acid&#124;Hexylic acid&#124;Pentanecarboxylic acid&#124;butylacetic acid&#124;hexoic acid&#124;n-Caproic acid&#124;n-hexanoic acid&#124;n-hexoic acid&#124;n-hexylic acid&#124;pentiformic acid&#124;pentylformic acid&#124;CAS:142-62-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Caproic_Acid","validation_method":"manual:apply_312_batch1&#124;GRADE&#124;2026-09-22"}] |
| ev-da3e14428024fe70 | docs/data/mapped_ingredients.csv; CSV lines=[648] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30776","line":648,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"16","ontology_id":"CHEBI:30776","preferred_term":"Caproic acid","total_occurrences":"16"}] |
| ev-199aa70fa6f3ace3 | reports/yaml_record_review/20261001T050143Z-Caproic_Acid.md; YAML Record Review: Caproic acid:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a4eb152fbf755218 | reports/yaml_record_review/Caproic_Acid.md; &#96;data/ingredients/mapped/Caproic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:39; Completeness:51; Recommended Edits:58 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f95507cea27041de | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[355,1778] | context_only | [{"current_record_sha256":"49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5","finding_id":"SEM:a863593ee1f4ad4a7a42","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5","finding_id":"SEM:801c1379c36a70d61e46","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-58e15ae153c20091 | data/ingredients/mapped/Caproic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[646],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30776","line":648,"mapping_status":"MAPPED","ontology_id":"CHEBI:30776","preferred_term":"Caproic acid"}],"identifier":"CHEBI:30776","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30776","ontology_label":"hexanoic acid","ontology_source":"CHEBI"},"preferred_term":"Caproic acid","sssom_rows":[{"data_row":630,"object_id":"CHEBI:30776","object_label":"hexanoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caproic_Acid","synonym_count":17} |
| ev-01427b2ecd8bd710 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-f1059d9657bfbc03] | context_only | Predecessor structured review finding f-f1059d9657bfbc03 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-caproic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Caproic_Acid (data/ingredients/mapped/Caproic_Acid.yaml)'
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
summary: Per-record structured review for Caproic_Acid (data/ingredients/mapped/Caproic_Acid.yaml,
  record-604f4ded295836c8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Caproic_Acid.yaml
    sha256: 49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5
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
  - path: reports/yaml_record_review/20261001T050143Z-Caproic_Acid.md
    sha256: dd86f48cb4af0edf6cf4d97c47d64391bc7ef2628db399a4e2a33ca3a00e41d2
    role: context
  - path: reports/yaml_record_review/Caproic_Acid.md
    sha256: 8455b08c196c5702604ad78c0a7e1e2f7d74f6311a846e6f6e3371a999d1601b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-604f4ded295836c8
  path: data/ingredients/mapped/Caproic_Acid.yaml
  label: Caproic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caproic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Caproic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Caproic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-604f4ded295836c8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-4aa1d97b46ff4b29
  - ev-e82b528abf22d8a4
  - ev-232f5a016f8a99a8
  - ev-da3e14428024fe70
  - ev-58e15ae153c20091
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-4aa1d97b46ff4b29
  - ev-f95507cea27041de
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-199aa70fa6f3ace3
  - ev-a4eb152fbf755218
  - ev-f95507cea27041de
  - ev-01427b2ecd8bd710
evidence:
- evidence_id: ev-4aa1d97b46ff4b29
  kind: record_content
  reference: data/ingredients/mapped/Caproic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[646],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30776","line":648,"mapping_status":"MAPPED","ontology_id":"CHEBI:30776","preferred_term":"Caproic
    acid"}],"identifier":"CHEBI:30776","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30776","ontology_label":"hexanoic
    acid","ontology_source":"CHEBI"},"preferred_term":"Caproic acid","sssom_rows":[{"data_row":630,"object_id":"CHEBI:30776","object_label":"hexanoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caproic_Acid","synonym_count":17}'
  snapshot_sha256: 49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5
- evidence_id: ev-e82b528abf22d8a4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [646]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-232f5a016f8a99a8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Caproic_Acid; data-row positions=[630]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":630,"object_id":"CHEBI:30776","object_label":"hexanoic
    acid","other":"1-hexanoic acid|1-pentanecarboxylic acid|6:0|CH3-[CH2]4-COOH|Capronic
    acid|Hexylic acid|Pentanecarboxylic acid|butylacetic acid|hexoic acid|n-Caproic
    acid|n-hexanoic acid|n-hexoic acid|n-hexylic acid|pentiformic acid|pentylformic
    acid|CAS:142-62-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Caproic_Acid","validation_method":"manual:apply_312_batch1|GRADE|2026-09-22"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-da3e14428024fe70
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[648]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30776","line":648,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"16","ontology_id":"CHEBI:30776","preferred_term":"Caproic
    acid","total_occurrences":"16"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-199aa70fa6f3ace3
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050143Z-Caproic_Acid.md
  locator: 'YAML Record Review: Caproic acid:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dd86f48cb4af0edf6cf4d97c47d64391bc7ef2628db399a4e2a33ca3a00e41d2
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Caproic_Acid.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI hexanoic acid identity passes, but CARBON_SOURCE is asserted from only provisional
    name-pattern evidence.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Caproic_Acid.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Caproic_Acid.yaml`,
    `just validate-terms data/ingredients/mapped/Caproic_Acid.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-a4eb152fbf755218
  kind: prior_review
  reference: reports/yaml_record_review/Caproic_Acid.md
  locator: '`data/ingredients/mapped/Caproic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:39; Completeness:51; Recommended Edits:58'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8455b08c196c5702604ad78c0a7e1e2f7d74f6311a846e6f6e3371a999d1601b
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Caproic_Acid.yaml`, remove\
    \ the unsupported\n  `CARBON_SOURCE` role unless a future curator can attach record-specific\n\
    \  evidence showing caproic acid served that role in the cited media.\n- Regenerate\
    \ `data/curated/mapped_ingredients.yaml`, docs data, and any role\n  exports that\
    \ consume the aggregate; prove the cleanup with strict validation\n  and round-trip\
    \ verification."
- evidence_id: ev-f95507cea27041de
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[355,1778]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5","finding_id":"SEM:a863593ee1f4ad4a7a42","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5","finding_id":"SEM:801c1379c36a70d61e46","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-58e15ae153c20091
  kind: record_content
  reference: data/ingredients/mapped/Caproic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[646],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30776","line":648,"mapping_status":"MAPPED","ontology_id":"CHEBI:30776","preferred_term":"Caproic
    acid"}],"identifier":"CHEBI:30776","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":16,"edge_count":16,"occurrences":16},"occurrence_statistics":{"media_count":16,"total_occurrences":16},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30776","ontology_label":"hexanoic
    acid","ontology_source":"CHEBI"},"preferred_term":"Caproic acid","sssom_rows":[{"data_row":630,"object_id":"CHEBI:30776","object_label":"hexanoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caproic_Acid","synonym_count":17}'
  snapshot_sha256: 49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5
- evidence_id: ev-01427b2ecd8bd710
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-f1059d9657bfbc03]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f1059d9657bfbc03 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-ac6d7144b90ce255
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-4aa1d97b46ff4b29
  - ev-e82b528abf22d8a4
  - ev-232f5a016f8a99a8
  - ev-da3e14428024fe70
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a2cc5241841d628d
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-199aa70fa6f3ace3
  - ev-a4eb152fbf755218
  - ev-4aa1d97b46ff4b29
  - ev-f95507cea27041de
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:43Z;
    reviewed SHA-256=49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5;
    current SHA-256=49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050143Z-Caproic_Acid.md","reports/yaml_record_review/Caproic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Caproic_Acid.md` after the record changed from 3a0e9bb0f34f0527ccc71b0e740d3582ac047b50bf32c45d600bd69b04a33373
    to 49dc203c14998eedd8f69e95d0d4a8541cdc449a2507bf3bb4a35b4fddb2c3d5; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-199aa70fa6f3ace3
    - ev-a4eb152fbf755218
    - ev-4aa1d97b46ff4b29
  - name: legacy-native-ids
    value: '["SEM:a863593ee1f4ad4a7a42","SEM:801c1379c36a70d61e46"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4aa1d97b46ff4b29
    - ev-199aa70fa6f3ace3
    - ev-a4eb152fbf755218
    - ev-f95507cea27041de
- assessment_id: a-58e15ae153c20091
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-199aa70fa6f3ace3
  - ev-a4eb152fbf755218
  - ev-58e15ae153c20091
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-199aa70fa6f3ace3
    - ev-a4eb152fbf755218
    - ev-58e15ae153c20091
findings:
- finding_id: rec-f-f1059d9657bfbc03
  issue_key: mim-reconciliation-role-support-604f4ded295836c8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Caproic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-604f4ded295836c8
  evidence_ids:
  - ev-199aa70fa6f3ace3
  - ev-a4eb152fbf755218
  - ev-58e15ae153c20091
  - ev-01427b2ecd8bd710
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caproic_Acid.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-f1059d9657bfbc03
actions:
- action_id: rec-action-f1059d9657bfbc03
  description: 'Reassess prediction-only role support: Caproic acid'
  finding_ids:
  - rec-f-f1059d9657bfbc03
  target_ids:
  - record-604f4ded295836c8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caproic_Acid.yaml
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
