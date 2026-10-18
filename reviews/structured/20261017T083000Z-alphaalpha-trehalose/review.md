# Per-record structured review: Alphaalpha-Trehalose (data/ingredients/mapped/Alphaalpha-Trehalose.yaml)

- Review: 20261017T083000Z-alphaalpha-trehalose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Alphaalpha-Trehalose (data/ingredients/mapped/Alphaalpha-Trehalose.yaml, record-83aad695bb32e6b1, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Alphaalpha-Trehalose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Alphaalpha-Trehalose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-83aad695bb32e6b1 | data/ingredients/mapped/Alphaalpha-Trehalose.yaml | maintained | Alphaalpha-Trehalose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-83aad695bb32e6b1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-83aad695bb32e6b1 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-83aad695bb32e6b1 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-83aad695bb32e6b1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-83aad695bb32e6b1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:52:17Z; reviewed SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54; current SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54; hash_changed=False. Reports=["reports/yaml_record_review/Alphaalpha-Trehalose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI grounding and restored residual evidence pass, but the record lacks ingredient_type and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.

## Findings

### rec-f-d75045044ac84534: Historical review coverage and residual narrative: Alphaalpha-Trehalose

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-83aad695bb32e6b1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:52:17Z; reviewed SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54; current SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54; hash_changed=False. Reports=["reports/yaml_record_review/Alphaalpha-Trehalose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI grounding and restored residual evidence pass, but the record lacks ingredient_type and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b3157fb2468131e2 | data/ingredients/mapped/Alphaalpha-Trehalose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2535],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16551","line":2537,"mapping_status":"MAPPED","ontology_id":"CHEBI:16551","preferred_term":"alpha,alpha-Trehalose"}],"identifier":"CHEBI:16551","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:16551","ontology_label":"alpha,alpha-trehalose","ontology_source":"CHEBI"},"preferred_term":"alpha,alpha-Trehalose","sssom_rows":[{"data_row":342,"object_id":"CHEBI:16551","object_label":"alpha,alpha-trehalose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alphaalpha-Trehalose","synonym_count":0} |
| ev-ecba8b7459912a44 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2535] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0642be602c5c84ce | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Alphaalpha-Trehalose; data-row positions=[342] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":342,"object_id":"CHEBI:16551","object_label":"alpha,alpha-trehalose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Alphaalpha-Trehalose","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-0c6f573f1480dad5 | docs/data/mapped_ingredients.csv; CSV lines=[2537] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16551","line":2537,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:16551","preferred_term":"alpha,alpha-Trehalose","total_occurrences":"1"}] |
| ev-1c020f8b62000af6 | reports/yaml_record_review/Alphaalpha-Trehalose.md; &#96;data/ingredients/mapped/Alphaalpha-Trehalose.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:47; Completeness:66; Recommended Edits:77 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-26f69177d8900d9e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[244] | context_only | [{"current_record_sha256":"514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54","finding_id":"SEM:92d1b5b95eea8a87cbf6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-alphaalpha-trehalose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Alphaalpha-Trehalose (data/ingredients/mapped/Alphaalpha-Trehalose.yaml)'
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
summary: Per-record structured review for Alphaalpha-Trehalose (data/ingredients/mapped/Alphaalpha-Trehalose.yaml,
  record-83aad695bb32e6b1, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Alphaalpha-Trehalose.yaml
    sha256: 514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54
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
  - path: reports/yaml_record_review/Alphaalpha-Trehalose.md
    sha256: f6e6025f685bb0cf2e6361f5fb7d61c112c114769e0effbe694333befc4967fb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-83aad695bb32e6b1
  path: data/ingredients/mapped/Alphaalpha-Trehalose.yaml
  label: Alphaalpha-Trehalose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alphaalpha-Trehalose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Alphaalpha-Trehalose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Alphaalpha-Trehalose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-83aad695bb32e6b1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-83aad695bb32e6b1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-83aad695bb32e6b1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-83aad695bb32e6b1
evidence:
- evidence_id: ev-b3157fb2468131e2
  kind: record_content
  reference: data/ingredients/mapped/Alphaalpha-Trehalose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2535],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16551","line":2537,"mapping_status":"MAPPED","ontology_id":"CHEBI:16551","preferred_term":"alpha,alpha-Trehalose"}],"identifier":"CHEBI:16551","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"CHEBI:16551","ontology_label":"alpha,alpha-trehalose","ontology_source":"CHEBI"},"preferred_term":"alpha,alpha-Trehalose","sssom_rows":[{"data_row":342,"object_id":"CHEBI:16551","object_label":"alpha,alpha-trehalose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Alphaalpha-Trehalose","synonym_count":0}'
  snapshot_sha256: 514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54
- evidence_id: ev-ecba8b7459912a44
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2535]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0642be602c5c84ce
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Alphaalpha-Trehalose; data-row positions=[342]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":342,"object_id":"CHEBI:16551","object_label":"alpha,alpha-trehalose","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Alphaalpha-Trehalose","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0c6f573f1480dad5
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2537]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16551","line":2537,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:16551","preferred_term":"alpha,alpha-Trehalose","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1c020f8b62000af6
  kind: prior_review
  reference: reports/yaml_record_review/Alphaalpha-Trehalose.md
  locator: '`data/ingredients/mapped/Alphaalpha-Trehalose.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:47; Completeness:66; Recommended Edits:77'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f6e6025f685bb0cf2e6361f5fb7d61c112c114769e0effbe694333befc4967fb
  quote: "Recommended Edits:\n- Backfill `chemical_properties` in\n  `data/ingredients/mapped/Alphaalpha-Trehalose.yaml`\
    \ from `CHEBI:16551`.\n- Add `ingredient_type: SINGLE_INGREDIENT` and an audit\
    \ event reflecting the\n  classification.\n- Refresh CultureMech membership so\
    \ the one residual alpha,alpha-trehalose\n  recipe is represented in `mappings/culturemech_recipe_membership.tsv`.\n\
    - Regenerate synchronized products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\
    \ `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/Alphaalpha-Trehalose.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_component_partonomy.py`,\
    \ and\n  `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-26f69177d8900d9e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[244]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54","finding_id":"SEM:92d1b5b95eea8a87cbf6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-959e4ac47aa16981
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-83aad695bb32e6b1
  evidence_ids:
  - ev-b3157fb2468131e2
  - ev-ecba8b7459912a44
  - ev-0642be602c5c84ce
  - ev-0c6f573f1480dad5
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-75fe714c95d7c641
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-83aad695bb32e6b1
  evidence_ids:
  - ev-1c020f8b62000af6
  - ev-b3157fb2468131e2
  - ev-26f69177d8900d9e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:52:17Z;
    reviewed SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54;
    current SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54;
    hash_changed=False. Reports=["reports/yaml_record_review/Alphaalpha-Trehalose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI grounding and restored residual evidence pass, but the record lacks ingredient_type
    and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1c020f8b62000af6
    - ev-b3157fb2468131e2
  - name: legacy-native-ids
    value: '["SEM:92d1b5b95eea8a87cbf6"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b3157fb2468131e2
    - ev-1c020f8b62000af6
    - ev-26f69177d8900d9e
findings:
- finding_id: rec-f-d75045044ac84534
  issue_key: mim-reconciliation-historical-review-coverage-and-r-83aad695bb32e6b1
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Alphaalpha-Trehalose'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:52:17Z;
    reviewed SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54;
    current SHA-256=514a863fd2b4161c3e67f612c80a14d0ffc661345708a3d34dcbc12887e83a54;
    hash_changed=False. Reports=["reports/yaml_record_review/Alphaalpha-Trehalose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI grounding and restored residual evidence pass, but the record lacks ingredient_type
    and ChEBI chemistry and its occurrence is missing from refreshed CultureMech membership.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-83aad695bb32e6b1
  evidence_ids:
  - ev-1c020f8b62000af6
  - ev-b3157fb2468131e2
  - ev-26f69177d8900d9e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Alphaalpha-Trehalose.yaml
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
