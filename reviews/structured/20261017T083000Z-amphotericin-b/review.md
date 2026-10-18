# Per-record structured review: Amphotericin_B (data/ingredients/mapped/Amphotericin_B.yaml)

- Review: 20261017T083000Z-amphotericin-b
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Amphotericin_B (data/ingredients/mapped/Amphotericin_B.yaml, record-393c64df47c2a3c4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Amphotericin_B.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Amphotericin_B.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-393c64df47c2a3c4 | data/ingredients/mapped/Amphotericin_B.yaml | maintained | Amphotericin_B |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-393c64df47c2a3c4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-393c64df47c2a3c4 | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-393c64df47c2a3c4 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-393c64df47c2a3c4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-393c64df47c2a3c4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z; reviewed SHA-256=fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1; current SHA-256=fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1; hash_changed=False. Reports=["reports/yaml_record_review/Amphotericin_B.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, chemistry, memberships, row-review confirmation, and SSSOM row pass, but a liposomal formulation is exact and CultureMech metadata remains in synonyms.

### Historical provisional-role concern

evidence: concern. Targets: record-393c64df47c2a3c4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-b5597493c3b6490a: Reassess prediction-only role support: Amphotericin B

major / open / confirmed; issue key: mim-reconciliation-role-support-393c64df47c2a3c4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-b5597493c3b6490a

Reassess prediction-only role support: Amphotericin B

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-815730128b28d358 | data/ingredients/mapped/Amphotericin_B.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[488],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2682","line":490,"mapping_status":"MAPPED","ontology_id":"CHEBI:2682","preferred_term":"Amphotericin B"}],"identifier":"CHEBI:2682","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2682","ontology_label":"amphotericin B","ontology_source":"CHEBI"},"preferred_term":"Amphotericin B","sssom_rows":[{"data_row":372,"object_id":"CHEBI:2682","object_label":"amphotericin B","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_B","synonym_count":8} |
| ev-c6039f8b379d5564 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [488] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d0c68e47eff06092 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Amphotericin_B; data-row positions=[372] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":372,"object_id":"CHEBI:2682","object_label":"amphotericin B","other":"(1R,3S,5R,6R,9R,11R,15S,16R,17R,18S,19E,21E,23E,25E,27E,29E,31E,33R,35S,36R,37S)-33-[(3-amino-3,6-dideoxy-beta-D-mannopyranosyl)oxy]-1,3,5,6,9,11,17,37-octahydroxy-15,16,18-trimethyl-13-oxo-14,39-dioxabicyclo[33.3.1]nonatriaconta-19,21,23,25,27,29,31-heptaene-36-carboxylic acid&#124;AMPH-B&#124;Amphotericine B&#124;Liposomal Amphotericin B&#124;amfotericina B&#124;amphotericinum B&#124;Amphotericin B (5 mg/ml DMSO)&#124;CAS:1397-89-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Amphotericin_B","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-56c44853b1a6e204 | docs/data/mapped_ingredients.csv; CSV lines=[490] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:2682","line":490,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:2682","preferred_term":"Amphotericin B","total_occurrences":"4"}] |
| ev-a9b621064014f2a0 | reports/yaml_record_review/Amphotericin_B.md; &#96;data/ingredients/mapped/Amphotericin_B.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:40; Completeness:64; Recommended Edits:74 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7093a4c5dfc5d0f1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[254,2068] | context_only | [{"current_record_sha256":"fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1","finding_id":"SEM:df754481e882060092ed","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1","finding_id":"SEM:f7eb031bf9d2a9fca728","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9ca457381986bb42 | data/ingredients/mapped/Amphotericin_B.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[488],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2682","line":490,"mapping_status":"MAPPED","ontology_id":"CHEBI:2682","preferred_term":"Amphotericin B"}],"identifier":"CHEBI:2682","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2682","ontology_label":"amphotericin B","ontology_source":"CHEBI"},"preferred_term":"Amphotericin B","sssom_rows":[{"data_row":372,"object_id":"CHEBI:2682","object_label":"amphotericin B","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_B","synonym_count":8} |
| ev-2e000a3717394d76 | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-b5597493c3b6490a] | context_only | Predecessor structured review finding f-b5597493c3b6490a in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-amphotericin-b
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Amphotericin_B (data/ingredients/mapped/Amphotericin_B.yaml)'
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
summary: Per-record structured review for Amphotericin_B (data/ingredients/mapped/Amphotericin_B.yaml,
  record-393c64df47c2a3c4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Amphotericin_B.yaml
    sha256: fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1
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
  - path: reports/yaml_record_review/Amphotericin_B.md
    sha256: a491c151bfbca5888adb596897237cd9ab7456f434f164c7108ed09a6cc859c4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-393c64df47c2a3c4
  path: data/ingredients/mapped/Amphotericin_B.yaml
  label: Amphotericin_B
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amphotericin_B.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Amphotericin_B.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Amphotericin_B.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-393c64df47c2a3c4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-815730128b28d358
  - ev-c6039f8b379d5564
  - ev-d0c68e47eff06092
  - ev-56c44853b1a6e204
  - ev-9ca457381986bb42
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-815730128b28d358
  - ev-7093a4c5dfc5d0f1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-a9b621064014f2a0
  - ev-7093a4c5dfc5d0f1
  - ev-2e000a3717394d76
evidence:
- evidence_id: ev-815730128b28d358
  kind: record_content
  reference: data/ingredients/mapped/Amphotericin_B.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[488],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2682","line":490,"mapping_status":"MAPPED","ontology_id":"CHEBI:2682","preferred_term":"Amphotericin
    B"}],"identifier":"CHEBI:2682","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2682","ontology_label":"amphotericin
    B","ontology_source":"CHEBI"},"preferred_term":"Amphotericin B","sssom_rows":[{"data_row":372,"object_id":"CHEBI:2682","object_label":"amphotericin
    B","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_B","synonym_count":8}'
  snapshot_sha256: fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1
- evidence_id: ev-c6039f8b379d5564
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [488]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d0c68e47eff06092
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Amphotericin_B; data-row positions=[372]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":372,"object_id":"CHEBI:2682","object_label":"amphotericin
    B","other":"(1R,3S,5R,6R,9R,11R,15S,16R,17R,18S,19E,21E,23E,25E,27E,29E,31E,33R,35S,36R,37S)-33-[(3-amino-3,6-dideoxy-beta-D-mannopyranosyl)oxy]-1,3,5,6,9,11,17,37-octahydroxy-15,16,18-trimethyl-13-oxo-14,39-dioxabicyclo[33.3.1]nonatriaconta-19,21,23,25,27,29,31-heptaene-36-carboxylic
    acid|AMPH-B|Amphotericine B|Liposomal Amphotericin B|amfotericina B|amphotericinum
    B|Amphotericin B (5 mg/ml DMSO)|CAS:1397-89-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Amphotericin_B","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-56c44853b1a6e204
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[490]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:2682","line":490,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:2682","preferred_term":"Amphotericin
    B","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a9b621064014f2a0
  kind: prior_review
  reference: reports/yaml_record_review/Amphotericin_B.md
  locator: '`data/ingredients/mapped/Amphotericin_B.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:40; Completeness:64; Recommended Edits:74'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a491c151bfbca5888adb596897237cd9ab7456f434f164c7108ed09a6cc859c4
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Amphotericin_B.yaml`,\
    \ remove or reject\n  `Liposomal Amphotericin B` so a formulation is not exported\
    \ as an exact\n  synonym of `CHEBI:2682`.\n- Remove the `Role: Antimicrobial agent`\
    \ raw synonym from the synonym list.\n- Replace the provisional `SELECTIVE_AGENT`\
    \ assignment with source-backed\n  evidence, or remove it.\n- Regenerate synchronized\
    \ products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Amphotericin_B.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-7093a4c5dfc5d0f1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[254,2068]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1","finding_id":"SEM:df754481e882060092ed","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1","finding_id":"SEM:f7eb031bf9d2a9fca728","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9ca457381986bb42
  kind: record_content
  reference: data/ingredients/mapped/Amphotericin_B.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[488],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2682","line":490,"mapping_status":"MAPPED","ontology_id":"CHEBI:2682","preferred_term":"Amphotericin
    B"}],"identifier":"CHEBI:2682","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2682","ontology_label":"amphotericin
    B","ontology_source":"CHEBI"},"preferred_term":"Amphotericin B","sssom_rows":[{"data_row":372,"object_id":"CHEBI:2682","object_label":"amphotericin
    B","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Amphotericin_B","synonym_count":8}'
  snapshot_sha256: fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1
- evidence_id: ev-2e000a3717394d76
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-b5597493c3b6490a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-b5597493c3b6490a in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-7db2c9d16130e702
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-815730128b28d358
  - ev-c6039f8b379d5564
  - ev-d0c68e47eff06092
  - ev-56c44853b1a6e204
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3228e5feea3ffa77
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-a9b621064014f2a0
  - ev-815730128b28d358
  - ev-7093a4c5dfc5d0f1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:11:33Z;
    reviewed SHA-256=fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1;
    current SHA-256=fc5f6bc5528bc5d761e4aa1a6e53fca4619b9967833aa41fd19fbf01c2ff40f1;
    hash_changed=False. Reports=["reports/yaml_record_review/Amphotericin_B.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, CAS, chemistry, memberships, row-review confirmation, and SSSOM
    row pass, but a liposomal formulation is exact and CultureMech metadata remains
    in synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a9b621064014f2a0
    - ev-815730128b28d358
  - name: legacy-native-ids
    value: '["SEM:df754481e882060092ed","SEM:f7eb031bf9d2a9fca728"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-815730128b28d358
    - ev-a9b621064014f2a0
    - ev-7093a4c5dfc5d0f1
- assessment_id: a-9ca457381986bb42
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-a9b621064014f2a0
  - ev-9ca457381986bb42
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a9b621064014f2a0
    - ev-9ca457381986bb42
findings:
- finding_id: rec-f-b5597493c3b6490a
  issue_key: mim-reconciliation-role-support-393c64df47c2a3c4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Amphotericin B'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-393c64df47c2a3c4
  evidence_ids:
  - ev-a9b621064014f2a0
  - ev-9ca457381986bb42
  - ev-2e000a3717394d76
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amphotericin_B.yaml
    role: maintained ingredient
  field_paths:
  - physicochemical_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-b5597493c3b6490a
actions:
- action_id: rec-action-b5597493c3b6490a
  description: 'Reassess prediction-only role support: Amphotericin B'
  finding_ids:
  - rec-f-b5597493c3b6490a
  target_ids:
  - record-393c64df47c2a3c4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Amphotericin_B.yaml
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
