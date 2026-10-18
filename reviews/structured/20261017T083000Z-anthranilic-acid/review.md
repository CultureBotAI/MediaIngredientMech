# Per-record structured review: Anthranilic_Acid (data/ingredients/mapped/Anthranilic_Acid.yaml)

- Review: 20261017T083000Z-anthranilic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Anthranilic_Acid (data/ingredients/mapped/Anthranilic_Acid.yaml, record-94dc8813fc32724f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Anthranilic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Anthranilic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-94dc8813fc32724f | data/ingredients/mapped/Anthranilic_Acid.yaml | maintained | Anthranilic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-94dc8813fc32724f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-94dc8813fc32724f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-94dc8813fc32724f | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-94dc8813fc32724f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-94dc8813fc32724f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:21:03Z; reviewed SHA-256=6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d; current SHA-256=6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d; hash_changed=False. Reports=["reports/yaml_record_review/Anthranilic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, formula, exact synonym, SSSOM row, and aggregate copy pass, but the amino-acid-source role is only a provisional ChEBI-ancestry inference.

### Historical provisional-role concern

evidence: concern. Targets: record-94dc8813fc32724f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-aad8ae815c136be2: Reassess prediction-only role support: anthranilic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-94dc8813fc32724f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-aad8ae815c136be2

Reassess prediction-only role support: anthranilic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-291d1d3698de4192 | data/ingredients/mapped/Anthranilic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[500],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30754","line":502,"mapping_status":"MAPPED","ontology_id":"CHEBI:30754","preferred_term":"anthranilic acid"}],"identifier":"CHEBI:30754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30754","ontology_label":"anthranilic acid","ontology_source":"CHEBI"},"preferred_term":"anthranilic acid","sssom_rows":[{"data_row":392,"object_id":"CHEBI:30754","object_label":"anthranilic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Anthranilic_Acid","synonym_count":1} |
| ev-1c7ffe0158e63732 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [500] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-190ec91f000af36d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Anthranilic_Acid; data-row positions=[392] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":392,"object_id":"CHEBI:30754","object_label":"anthranilic acid","other":"2-AMINOBENZOIC ACID&#124;CAS:118-92-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Anthranilic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-17168d4383751b8b | docs/data/mapped_ingredients.csv; CSV lines=[502] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30754","line":502,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30754","preferred_term":"anthranilic acid","total_occurrences":"0"}] |
| ev-c75866279d21bfb7 | reports/yaml_record_review/Anthranilic_Acid.md; &#96;data/ingredients/mapped/Anthranilic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:41; Completeness:63; Recommended Edits:72 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b261dc7fc4956d81 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[264,1472] | context_only | [{"current_record_sha256":"6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d","finding_id":"SEM:60e9c30415090bd62c5f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d","finding_id":"SEM:d3269fcdca28bf03d707","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-6cc3f73ed08bbf5b | data/ingredients/mapped/Anthranilic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[500],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30754","line":502,"mapping_status":"MAPPED","ontology_id":"CHEBI:30754","preferred_term":"anthranilic acid"}],"identifier":"CHEBI:30754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30754","ontology_label":"anthranilic acid","ontology_source":"CHEBI"},"preferred_term":"anthranilic acid","sssom_rows":[{"data_row":392,"object_id":"CHEBI:30754","object_label":"anthranilic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Anthranilic_Acid","synonym_count":1} |
| ev-ce81f42d12994794 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-aad8ae815c136be2] | context_only | Predecessor structured review finding f-aad8ae815c136be2 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-anthranilic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Anthranilic_Acid (data/ingredients/mapped/Anthranilic_Acid.yaml)'
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
summary: Per-record structured review for Anthranilic_Acid (data/ingredients/mapped/Anthranilic_Acid.yaml,
  record-94dc8813fc32724f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Anthranilic_Acid.yaml
    sha256: 6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d
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
  - path: reports/yaml_record_review/Anthranilic_Acid.md
    sha256: 0264ea6b90ae549df9399dc59b8a178ff4099196a0bf36652164fd4f4c0bdbfc
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-94dc8813fc32724f
  path: data/ingredients/mapped/Anthranilic_Acid.yaml
  label: Anthranilic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Anthranilic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Anthranilic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Anthranilic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-94dc8813fc32724f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-291d1d3698de4192
  - ev-1c7ffe0158e63732
  - ev-190ec91f000af36d
  - ev-17168d4383751b8b
  - ev-6cc3f73ed08bbf5b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-291d1d3698de4192
  - ev-b261dc7fc4956d81
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-c75866279d21bfb7
  - ev-b261dc7fc4956d81
  - ev-ce81f42d12994794
evidence:
- evidence_id: ev-291d1d3698de4192
  kind: record_content
  reference: data/ingredients/mapped/Anthranilic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[500],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30754","line":502,"mapping_status":"MAPPED","ontology_id":"CHEBI:30754","preferred_term":"anthranilic
    acid"}],"identifier":"CHEBI:30754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30754","ontology_label":"anthranilic
    acid","ontology_source":"CHEBI"},"preferred_term":"anthranilic acid","sssom_rows":[{"data_row":392,"object_id":"CHEBI:30754","object_label":"anthranilic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Anthranilic_Acid","synonym_count":1}'
  snapshot_sha256: 6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d
- evidence_id: ev-1c7ffe0158e63732
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [500]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-190ec91f000af36d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Anthranilic_Acid; data-row positions=[392]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":392,"object_id":"CHEBI:30754","object_label":"anthranilic
    acid","other":"2-AMINOBENZOIC ACID|CAS:118-92-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Anthranilic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-17168d4383751b8b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[502]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30754","line":502,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30754","preferred_term":"anthranilic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c75866279d21bfb7
  kind: prior_review
  reference: reports/yaml_record_review/Anthranilic_Acid.md
  locator: '`data/ingredients/mapped/Anthranilic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:41; Completeness:63; Recommended Edits:72'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0264ea6b90ae549df9399dc59b8a178ff4099196a0bf36652164fd4f4c0bdbfc
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Anthranilic_Acid.yaml`,\
    \ remove\n  `nutritional_roles.AMINO_ACID_SOURCE` unless a direct medium source\
    \ shows that\n  anthranilic acid is being used as an amino acid source in this\
    \ corpus.\n- Regenerate synchronized products, then rerun\n  `uv run --frozen\
    \ python scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/Anthranilic_Acid.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-b261dc7fc4956d81
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[264,1472]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d","finding_id":"SEM:60e9c30415090bd62c5f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d","finding_id":"SEM:d3269fcdca28bf03d707","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-6cc3f73ed08bbf5b
  kind: record_content
  reference: data/ingredients/mapped/Anthranilic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[500],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30754","line":502,"mapping_status":"MAPPED","ontology_id":"CHEBI:30754","preferred_term":"anthranilic
    acid"}],"identifier":"CHEBI:30754","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30754","ontology_label":"anthranilic
    acid","ontology_source":"CHEBI"},"preferred_term":"anthranilic acid","sssom_rows":[{"data_row":392,"object_id":"CHEBI:30754","object_label":"anthranilic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Anthranilic_Acid","synonym_count":1}'
  snapshot_sha256: 6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d
- evidence_id: ev-ce81f42d12994794
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-aad8ae815c136be2]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-aad8ae815c136be2 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-d285dee0eb4e09d9
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-291d1d3698de4192
  - ev-1c7ffe0158e63732
  - ev-190ec91f000af36d
  - ev-17168d4383751b8b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d294008503094c09
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-c75866279d21bfb7
  - ev-291d1d3698de4192
  - ev-b261dc7fc4956d81
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:21:03Z;
    reviewed SHA-256=6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d;
    current SHA-256=6cfdf0a1d449d6473560116cbf05523a4c31f86d233dca0a4ac88c58217d050d;
    hash_changed=False. Reports=["reports/yaml_record_review/Anthranilic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, CAS, formula, exact synonym, SSSOM row, and aggregate copy pass,
    but the amino-acid-source role is only a provisional ChEBI-ancestry inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c75866279d21bfb7
    - ev-291d1d3698de4192
  - name: legacy-native-ids
    value: '["SEM:60e9c30415090bd62c5f","SEM:d3269fcdca28bf03d707"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-291d1d3698de4192
    - ev-c75866279d21bfb7
    - ev-b261dc7fc4956d81
- assessment_id: a-6cc3f73ed08bbf5b
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-c75866279d21bfb7
  - ev-6cc3f73ed08bbf5b
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c75866279d21bfb7
    - ev-6cc3f73ed08bbf5b
findings:
- finding_id: rec-f-aad8ae815c136be2
  issue_key: mim-reconciliation-role-support-94dc8813fc32724f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: anthranilic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-94dc8813fc32724f
  evidence_ids:
  - ev-c75866279d21bfb7
  - ev-6cc3f73ed08bbf5b
  - ev-ce81f42d12994794
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Anthranilic_Acid.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-aad8ae815c136be2
actions:
- action_id: rec-action-aad8ae815c136be2
  description: 'Reassess prediction-only role support: anthranilic acid'
  finding_ids:
  - rec-f-aad8ae815c136be2
  target_ids:
  - record-94dc8813fc32724f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Anthranilic_Acid.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
