# Per-record structured review: Fumaric_Acid (data/ingredients/mapped/Fumaric_Acid.yaml)

- Review: 20261017T083000Z-fumaric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fumaric_Acid (data/ingredients/mapped/Fumaric_Acid.yaml, record-ffc03c9ed47730de, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fumaric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fumaric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ffc03c9ed47730de | data/ingredients/mapped/Fumaric_Acid.yaml | maintained | Fumaric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ffc03c9ed47730de | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ffc03c9ed47730de | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ffc03c9ed47730de | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ffc03c9ed47730de.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ffc03c9ed47730de.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:11:13Z; reviewed SHA-256=3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4; current SHA-256=3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4; hash_changed=False. Reports=["reports/yaml_record_review/Fumaric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact fumaric acid identity and final SSSOM payload pass, but ENERGY_SOURCE is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-ffc03c9ed47730de.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-70d22957f8242796: Reassess prediction-only role support: Fumaric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-ffc03c9ed47730de.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-70d22957f8242796

Reassess prediction-only role support: Fumaric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0430d2151a413ca5 | data/ingredients/mapped/Fumaric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1028],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18012","line":1030,"mapping_status":"MAPPED","ontology_id":"CHEBI:18012","preferred_term":"Fumaric acid"}],"identifier":"CHEBI:18012","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18012","ontology_label":"fumaric acid","ontology_source":"CHEBI"},"preferred_term":"Fumaric acid","sssom_rows":[{"data_row":1253,"object_id":"CHEBI:18012","object_label":"fumaric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fumaric_Acid","synonym_count":13} |
| ev-6459bcb8d368f480 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1028] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d6afc95bdad01d93 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fumaric_Acid; data-row positions=[1253] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1253,"object_id":"CHEBI:18012","object_label":"fumaric acid","other":"(2E)-2-butenedioic acid&#124;(2E)-but-2-enedioic acid&#124;(E)-2-butenedioic acid&#124;E297&#124;Fumarsaeure&#124;trans-1,2-ethylenedicarboxylic acid&#124;trans-Butenedioic acid&#124;trans-but-2-enedioic acid&#124;trans-ethene-1,2-dioic acid&#124;CAS:110-17-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Fumaric_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d82a65c9af793cb4 | docs/data/mapped_ingredients.csv; CSV lines=[1030] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18012","line":1030,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:18012","preferred_term":"Fumaric acid","total_occurrences":"10"}] |
| ev-5cfae5525b4d35b7 | reports/yaml_record_review/Fumaric_Acid.md; &#96;data/ingredients/mapped/Fumaric_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:36; Completeness:60; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9c7e2f059c18a159 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[639,1486] | context_only | [{"current_record_sha256":"3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4","finding_id":"SEM:b4f8479ebf7e420546c9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4","finding_id":"SEM:9f55ba4c0a4b9f59df63","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-7d4904d9f1043e33 | data/ingredients/mapped/Fumaric_Acid.yaml; nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1028],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18012","line":1030,"mapping_status":"MAPPED","ontology_id":"CHEBI:18012","preferred_term":"Fumaric acid"}],"identifier":"CHEBI:18012","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18012","ontology_label":"fumaric acid","ontology_source":"CHEBI"},"preferred_term":"Fumaric acid","sssom_rows":[{"data_row":1253,"object_id":"CHEBI:18012","object_label":"fumaric acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fumaric_Acid","synonym_count":13} |
| ev-3fabc4ccb330da6e | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-70d22957f8242796] | context_only | Predecessor structured review finding f-70d22957f8242796 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fumaric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fumaric_Acid (data/ingredients/mapped/Fumaric_Acid.yaml)'
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
summary: Per-record structured review for Fumaric_Acid (data/ingredients/mapped/Fumaric_Acid.yaml,
  record-ffc03c9ed47730de, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fumaric_Acid.yaml
    sha256: 3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Fumaric_Acid.md
    sha256: 92c196a0bd1ceeb59a49aa107593fb2de14ed12def574454cf0b9f5512d97d6d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ffc03c9ed47730de
  path: data/ingredients/mapped/Fumaric_Acid.yaml
  label: Fumaric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fumaric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fumaric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fumaric_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ffc03c9ed47730de
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-0430d2151a413ca5
  - ev-6459bcb8d368f480
  - ev-d6afc95bdad01d93
  - ev-d82a65c9af793cb4
  - ev-7d4904d9f1043e33
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-0430d2151a413ca5
  - ev-9c7e2f059c18a159
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-5cfae5525b4d35b7
  - ev-9c7e2f059c18a159
  - ev-3fabc4ccb330da6e
evidence:
- evidence_id: ev-0430d2151a413ca5
  kind: record_content
  reference: data/ingredients/mapped/Fumaric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1028],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18012","line":1030,"mapping_status":"MAPPED","ontology_id":"CHEBI:18012","preferred_term":"Fumaric
    acid"}],"identifier":"CHEBI:18012","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18012","ontology_label":"fumaric
    acid","ontology_source":"CHEBI"},"preferred_term":"Fumaric acid","sssom_rows":[{"data_row":1253,"object_id":"CHEBI:18012","object_label":"fumaric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fumaric_Acid","synonym_count":13}'
  snapshot_sha256: 3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4
- evidence_id: ev-6459bcb8d368f480
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1028]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d6afc95bdad01d93
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fumaric_Acid; data-row positions=[1253]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1253,"object_id":"CHEBI:18012","object_label":"fumaric
    acid","other":"(2E)-2-butenedioic acid|(2E)-but-2-enedioic acid|(E)-2-butenedioic
    acid|E297|Fumarsaeure|trans-1,2-ethylenedicarboxylic acid|trans-Butenedioic acid|trans-but-2-enedioic
    acid|trans-ethene-1,2-dioic acid|CAS:110-17-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Fumaric_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d82a65c9af793cb4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1030]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18012","line":1030,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"10","ontology_id":"CHEBI:18012","preferred_term":"Fumaric
    acid","total_occurrences":"10"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5cfae5525b4d35b7
  kind: prior_review
  reference: reports/yaml_record_review/Fumaric_Acid.md
  locator: '`data/ingredients/mapped/Fumaric_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:36; Completeness:60; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 92c196a0bd1ceeb59a49aa107593fb2de14ed12def574454cf0b9f5512d97d6d
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.ENERGY_SOURCE`\
    \ in\n  `data/ingredients/mapped/Fumaric_Acid.yaml` with inspected source-backed\n\
    \  evidence for fumaric acid in media, or remove the unsupported role; then sync\n\
    \  `data/curated/mapped_ingredients.yaml` and rerun strict validation."
- evidence_id: ev-9c7e2f059c18a159
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[639,1486]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4","finding_id":"SEM:b4f8479ebf7e420546c9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4","finding_id":"SEM:9f55ba4c0a4b9f59df63","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-7d4904d9f1043e33
  kind: record_content
  reference: data/ingredients/mapped/Fumaric_Acid.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1028],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18012","line":1030,"mapping_status":"MAPPED","ontology_id":"CHEBI:18012","preferred_term":"Fumaric
    acid"}],"identifier":"CHEBI:18012","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":10,"edge_count":10,"occurrences":10},"occurrence_statistics":{"media_count":10,"total_occurrences":10},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18012","ontology_label":"fumaric
    acid","ontology_source":"CHEBI"},"preferred_term":"Fumaric acid","sssom_rows":[{"data_row":1253,"object_id":"CHEBI:18012","object_label":"fumaric
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fumaric_Acid","synonym_count":13}'
  snapshot_sha256: 3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4
- evidence_id: ev-3fabc4ccb330da6e
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-70d22957f8242796]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-70d22957f8242796 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-e2d5cdea7782c397
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-0430d2151a413ca5
  - ev-6459bcb8d368f480
  - ev-d6afc95bdad01d93
  - ev-d82a65c9af793cb4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-126ac658ac4fba28
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-5cfae5525b4d35b7
  - ev-0430d2151a413ca5
  - ev-9c7e2f059c18a159
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:11:13Z;
    reviewed SHA-256=3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4;
    current SHA-256=3082ea7a39992941222e75bc94137d888a7aae8b301dc8bb0fb31497ee78e3c4;
    hash_changed=False. Reports=["reports/yaml_record_review/Fumaric_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact fumaric
    acid identity and final SSSOM payload pass, but ENERGY_SOURCE is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5cfae5525b4d35b7
    - ev-0430d2151a413ca5
  - name: legacy-native-ids
    value: '["SEM:b4f8479ebf7e420546c9","SEM:9f55ba4c0a4b9f59df63"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0430d2151a413ca5
    - ev-5cfae5525b4d35b7
    - ev-9c7e2f059c18a159
- assessment_id: a-7d4904d9f1043e33
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-5cfae5525b4d35b7
  - ev-7d4904d9f1043e33
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5cfae5525b4d35b7
    - ev-7d4904d9f1043e33
findings:
- finding_id: rec-f-70d22957f8242796
  issue_key: mim-reconciliation-role-support-ffc03c9ed47730de
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Fumaric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ffc03c9ed47730de
  evidence_ids:
  - ev-5cfae5525b4d35b7
  - ev-7d4904d9f1043e33
  - ev-3fabc4ccb330da6e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fumaric_Acid.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-70d22957f8242796
actions:
- action_id: rec-action-70d22957f8242796
  description: 'Reassess prediction-only role support: Fumaric acid'
  finding_ids:
  - rec-f-70d22957f8242796
  target_ids:
  - record-ffc03c9ed47730de
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fumaric_Acid.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
