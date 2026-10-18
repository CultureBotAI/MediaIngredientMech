# Per-record structured review: Alpha-Tocopherol (data/ingredients/mapped/Alpha-Tocopherol.yaml)

- Review: 20261017T083000Z-alpha-tocopherol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Alpha-Tocopherol (data/ingredients/mapped/Alpha-Tocopherol.yaml, record-4f275065c46c73b9, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Alpha-Tocopherol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Alpha-Tocopherol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4f275065c46c73b9 | data/ingredients/mapped/Alpha-Tocopherol.yaml | maintained | Alpha-Tocopherol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4f275065c46c73b9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-4f275065c46c73b9 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4f275065c46c73b9 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4f275065c46c73b9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4f275065c46c73b9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:45:29Z; reviewed SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f; current SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f; hash_changed=False. Reports=["reports/yaml_record_review/Alpha-Tocopherol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The all-R alpha-tocopherol identity and residual grounding pass, but the record lacks ingredient_type and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.

## Findings

### rec-f-af1c8c9dbfd74a6a: Historical review coverage and residual narrative: Alpha-Tocopherol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-4f275065c46c73b9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:45:29Z; reviewed SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f; current SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f; hash_changed=False. Reports=["reports/yaml_record_review/Alpha-Tocopherol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The all-R alpha-tocopherol identity and residual grounding pass, but the record lacks ingredient_type and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-1667960c68eefaf5 | data/ingredients/mapped/Alpha-Tocopherol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2534],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18145","line":2536,"mapping_status":"MAPPED","ontology_id":"CHEBI:18145","preferred_term":"alpha-Tocopherol"}],"identifier":"CHEBI:18145","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:18145","ontology_label":"(R,R,R)-alpha-tocopherol","ontology_source":"CHEBI"},"preferred_term":"alpha-Tocopherol","sssom_rows":[{"data_row":335,"object_id":"CHEBI:18145","object_label":"(R,R,R)-alpha-tocopherol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alpha-Tocopherol","synonym_count":0} |
| ev-09c13c0075436169 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2534] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-807fbca93b840e2b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Alpha-Tocopherol; data-row positions=[335] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":335,"object_id":"CHEBI:18145","object_label":"(R,R,R)-alpha-tocopherol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Alpha-Tocopherol","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-24a67435047c0b42 | docs/data/mapped_ingredients.csv; CSV lines=[2536] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18145","line":2536,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:18145","preferred_term":"alpha-Tocopherol","total_occurrences":"1"}] |
| ev-4139e67453663d0c | reports/yaml_record_review/Alpha-Tocopherol.md; &#96;data/ingredients/mapped/Alpha-Tocopherol.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:43; Completeness:62; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-edead61b47201416 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[239] | context_only | [{"current_record_sha256":"15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f","finding_id":"SEM:b96c8b2bc9cd35a1689d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-alpha-tocopherol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Alpha-Tocopherol (data/ingredients/mapped/Alpha-Tocopherol.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Alpha-Tocopherol (data/ingredients/mapped/Alpha-Tocopherol.yaml,
  record-4f275065c46c73b9, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Alpha-Tocopherol.yaml
    sha256: 15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f
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
  - path: reports/yaml_record_review/Alpha-Tocopherol.md
    sha256: 68f7142aa584aa8c6e6b59b25793f2956773ede02fb4a6fb039ce030b8b202d2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4f275065c46c73b9
  path: data/ingredients/mapped/Alpha-Tocopherol.yaml
  label: Alpha-Tocopherol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alpha-Tocopherol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Alpha-Tocopherol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Alpha-Tocopherol.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4f275065c46c73b9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4f275065c46c73b9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-4f275065c46c73b9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4f275065c46c73b9
evidence:
- evidence_id: ev-1667960c68eefaf5
  kind: record_content
  reference: data/ingredients/mapped/Alpha-Tocopherol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2534],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18145","line":2536,"mapping_status":"MAPPED","ontology_id":"CHEBI:18145","preferred_term":"alpha-Tocopherol"}],"identifier":"CHEBI:18145","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"CHEBI:18145","ontology_label":"(R,R,R)-alpha-tocopherol","ontology_source":"CHEBI"},"preferred_term":"alpha-Tocopherol","sssom_rows":[{"data_row":335,"object_id":"CHEBI:18145","object_label":"(R,R,R)-alpha-tocopherol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alpha-Tocopherol","synonym_count":0}'
  snapshot_sha256: 15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f
- evidence_id: ev-09c13c0075436169
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2534]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-807fbca93b840e2b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Alpha-Tocopherol; data-row positions=[335]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":335,"object_id":"CHEBI:18145","object_label":"(R,R,R)-alpha-tocopherol","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Alpha-Tocopherol","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-24a67435047c0b42
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2536]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18145","line":2536,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:18145","preferred_term":"alpha-Tocopherol","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4139e67453663d0c
  kind: prior_review
  reference: reports/yaml_record_review/Alpha-Tocopherol.md
  locator: '`data/ingredients/mapped/Alpha-Tocopherol.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:43; Completeness:62; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 68f7142aa584aa8c6e6b59b25793f2956773ede02fb4a6fb039ce030b8b202d2
  quote: "Recommended Edits:\n- Backfill `chemical_properties` in\n  `data/ingredients/mapped/Alpha-Tocopherol.yaml`\
    \ from `CHEBI:18145`.\n- Add `ingredient_type: SINGLE_INGREDIENT` and an audit\
    \ event reflecting the\n  classification.\n- Refresh CultureMech membership so\
    \ the one residual alpha-tocopherol recipe is\n  represented in `mappings/culturemech_recipe_membership.tsv`.\n\
    - Regenerate synchronized products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\
    \ `uv run linkml-term-validator validate-data data/ingredients/mapped/Alpha-Tocopherol.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-edead61b47201416
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[239]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f","finding_id":"SEM:b96c8b2bc9cd35a1689d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-3127440456919e90
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4f275065c46c73b9
  evidence_ids:
  - ev-1667960c68eefaf5
  - ev-09c13c0075436169
  - ev-807fbca93b840e2b
  - ev-24a67435047c0b42
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-dfd21685af0b2417
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4f275065c46c73b9
  evidence_ids:
  - ev-4139e67453663d0c
  - ev-1667960c68eefaf5
  - ev-edead61b47201416
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:45:29Z;
    reviewed SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f;
    current SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f;
    hash_changed=False. Reports=["reports/yaml_record_review/Alpha-Tocopherol.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The all-R
    alpha-tocopherol identity and residual grounding pass, but the record lacks ingredient_type
    and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4139e67453663d0c
    - ev-1667960c68eefaf5
  - name: legacy-native-ids
    value: '["SEM:b96c8b2bc9cd35a1689d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-1667960c68eefaf5
    - ev-4139e67453663d0c
    - ev-edead61b47201416
findings:
- finding_id: rec-f-af1c8c9dbfd74a6a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-4f275065c46c73b9
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Alpha-Tocopherol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:45:29Z;
    reviewed SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f;
    current SHA-256=15fe16c171507d86ebe9391cfc565708bed1104a97510071531983a80355ed8f;
    hash_changed=False. Reports=["reports/yaml_record_review/Alpha-Tocopherol.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The all-R
    alpha-tocopherol identity and residual grounding pass, but the record lacks ingredient_type
    and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4f275065c46c73b9
  evidence_ids:
  - ev-4139e67453663d0c
  - ev-1667960c68eefaf5
  - ev-edead61b47201416
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alpha-Tocopherol.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
