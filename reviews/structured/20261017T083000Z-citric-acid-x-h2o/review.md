# Per-record structured review: Citric_Acid_X_H2o (data/ingredients/mapped/Citric_Acid_X_H2o.yaml)

- Review: 20261017T083000Z-citric-acid-x-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Citric_Acid_X_H2o (data/ingredients/mapped/Citric_Acid_X_H2o.yaml, record-70cad0ed79a17905, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Citric_Acid_X_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Citric_Acid_X_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-70cad0ed79a17905 | data/ingredients/mapped/Citric_Acid_X_H2o.yaml | maintained | Citric_Acid_X_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-70cad0ed79a17905 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-70cad0ed79a17905 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-70cad0ed79a17905 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-70cad0ed79a17905.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-70cad0ed79a17905.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:15:13Z; reviewed SHA-256=75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963; current SHA-256=75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963; hash_changed=False. Reports=["reports/yaml_record_review/Citric_Acid_X_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI citric acid monohydrate identity and 8/8 count pass, but active monoanion synonyms and unsupported nutritional roles remain.

### Historical provisional-role concern

evidence: concern. Targets: record-70cad0ed79a17905.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4b6ce9af131d7a9f: Reassess prediction-only role support: Citric acid x H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-70cad0ed79a17905.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4b6ce9af131d7a9f

Reassess prediction-only role support: Citric acid x H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-698e1c6372735819 | data/ingredients/mapped/Citric_Acid_X_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[732],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31404","line":734,"mapping_status":"MAPPED","ontology_id":"CHEBI:31404","preferred_term":"Citric acid x H2O"}],"identifier":"CHEBI:31404","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31404","ontology_label":"Citric acid monohydrate","ontology_source":"CHEBI"},"preferred_term":"Citric acid x H2O","sssom_rows":[{"data_row":780,"object_id":"CHEBI:31404","object_label":"Citric acid monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citric_Acid_X_H2o","synonym_count":8} |
| ev-b92fc549fbfdec43 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [732] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-51300c413421683c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Citric_Acid_X_H2o; data-row positions=[780] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":780,"object_id":"CHEBI:31404","object_label":"Citric acid monohydrate","other":"Citric acid . H2O&#124;Citric acid\u00b7H2O&#124;H2cit&#124;citrate(1-)&#124;dihydrogen citrate&#124;Citric Acid\u2022H2O(Fisher A 104)&#124;CAS:5949-29-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Citric_Acid_X_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f37bff26bf180e07 | docs/data/mapped_ingredients.csv; CSV lines=[734] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:31404","line":734,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:31404","preferred_term":"Citric acid x H2O","total_occurrences":"8"}] |
| ev-037b9c1d6c79ac96 | reports/yaml_record_review/Citric_Acid_X_H2o.md; &#96;data/ingredients/mapped/Citric_Acid_X_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:25; Evidence:44; Completeness:70; Recommended Edits:78 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6e37523a1dd66254 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[421,1639,1822] | context_only | [{"current_record_sha256":"75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963","finding_id":"SEM:988b369fa53ce0a856f9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963","finding_id":"SEM:1973a5d6d3b034253ea0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963","finding_id":"SEM:1428e403a41156125079","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b647a95d5ffbde35 | data/ingredients/mapped/Citric_Acid_X_H2o.yaml; nutritional_roles[0], nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[732],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31404","line":734,"mapping_status":"MAPPED","ontology_id":"CHEBI:31404","preferred_term":"Citric acid x H2O"}],"identifier":"CHEBI:31404","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31404","ontology_label":"Citric acid monohydrate","ontology_source":"CHEBI"},"preferred_term":"Citric acid x H2O","sssom_rows":[{"data_row":780,"object_id":"CHEBI:31404","object_label":"Citric acid monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citric_Acid_X_H2o","synonym_count":8} |
| ev-56f19402451b631a | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-4b6ce9af131d7a9f] | context_only | Predecessor structured review finding f-4b6ce9af131d7a9f in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-citric-acid-x-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Citric_Acid_X_H2o (data/ingredients/mapped/Citric_Acid_X_H2o.yaml)'
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
summary: Per-record structured review for Citric_Acid_X_H2o (data/ingredients/mapped/Citric_Acid_X_H2o.yaml,
  record-70cad0ed79a17905, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
    sha256: 75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963
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
  - path: reports/yaml_record_review/Citric_Acid_X_H2o.md
    sha256: 431884fa219d4d344a2ecd6aa3d17022cd7c949022d074f42f6a7c934ff1f60d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-70cad0ed79a17905
  path: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
  label: Citric_Acid_X_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Citric_Acid_X_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Citric_Acid_X_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-70cad0ed79a17905
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-698e1c6372735819
  - ev-b92fc549fbfdec43
  - ev-51300c413421683c
  - ev-f37bff26bf180e07
  - ev-b647a95d5ffbde35
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-698e1c6372735819
  - ev-6e37523a1dd66254
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-037b9c1d6c79ac96
  - ev-6e37523a1dd66254
  - ev-56f19402451b631a
evidence:
- evidence_id: ev-698e1c6372735819
  kind: record_content
  reference: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[732],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31404","line":734,"mapping_status":"MAPPED","ontology_id":"CHEBI:31404","preferred_term":"Citric
    acid x H2O"}],"identifier":"CHEBI:31404","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31404","ontology_label":"Citric
    acid monohydrate","ontology_source":"CHEBI"},"preferred_term":"Citric acid x H2O","sssom_rows":[{"data_row":780,"object_id":"CHEBI:31404","object_label":"Citric
    acid monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citric_Acid_X_H2o","synonym_count":8}'
  snapshot_sha256: 75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963
- evidence_id: ev-b92fc549fbfdec43
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [732]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-51300c413421683c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Citric_Acid_X_H2o; data-row positions=[780]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":780,"object_id":"CHEBI:31404","object_label":"Citric
    acid monohydrate","other":"Citric acid . H2O|Citric acid\u00b7H2O|H2cit|citrate(1-)|dihydrogen
    citrate|Citric Acid\u2022H2O(Fisher A 104)|CAS:5949-29-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Citric_Acid_X_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f37bff26bf180e07
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[734]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:31404","line":734,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"8","ontology_id":"CHEBI:31404","preferred_term":"Citric
    acid x H2O","total_occurrences":"8"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-037b9c1d6c79ac96
  kind: prior_review
  reference: reports/yaml_record_review/Citric_Acid_X_H2o.md
  locator: '`data/ingredients/mapped/Citric_Acid_X_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:25; Evidence:44; Completeness:70; Recommended Edits:78'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 431884fa219d4d344a2ecd6aa3d17022cd7c949022d074f42f6a7c934ff1f60d
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Citric_Acid_X_H2o.yaml`,\
    \ remove or retype\n  `H2cit`, `citrate(1-)`, and `dihydrogen citrate` so monoanion\
    \ names no longer\n  resolve to the neutral monohydrate in final SSSOM and label-search\
    \ exports.\n- Major: either attach source evidence to `CARBON_SOURCE` and `ENERGY_SOURCE`\n\
    \  or remove the provisional role facets.\n- After the YAML edits, regenerate\
    \ the curated aggregate, final SSSOM, and docs\n  products, then rerun strict\
    \ validation and the SSSOM invariant checks."
- evidence_id: ev-6e37523a1dd66254
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[421,1639,1822]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963","finding_id":"SEM:988b369fa53ce0a856f9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963","finding_id":"SEM:1973a5d6d3b034253ea0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963","finding_id":"SEM:1428e403a41156125079","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b647a95d5ffbde35
  kind: record_content
  reference: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[732],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:31404","line":734,"mapping_status":"MAPPED","ontology_id":"CHEBI:31404","preferred_term":"Citric
    acid x H2O"}],"identifier":"CHEBI:31404","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":8,"edge_count":8,"occurrences":8},"occurrence_statistics":{"media_count":8,"total_occurrences":8},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:31404","ontology_label":"Citric
    acid monohydrate","ontology_source":"CHEBI"},"preferred_term":"Citric acid x H2O","sssom_rows":[{"data_row":780,"object_id":"CHEBI:31404","object_label":"Citric
    acid monohydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Citric_Acid_X_H2o","synonym_count":8}'
  snapshot_sha256: 75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963
- evidence_id: ev-56f19402451b631a
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-4b6ce9af131d7a9f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4b6ce9af131d7a9f in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-63bc499aa00b3709
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-698e1c6372735819
  - ev-b92fc549fbfdec43
  - ev-51300c413421683c
  - ev-f37bff26bf180e07
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-77f65ec0b6679913
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-037b9c1d6c79ac96
  - ev-698e1c6372735819
  - ev-6e37523a1dd66254
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:15:13Z;
    reviewed SHA-256=75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963;
    current SHA-256=75c89db7f05e0e7326f0c13908ef01ce265e42ae76beac714c1ef29ec00e6963;
    hash_changed=False. Reports=["reports/yaml_record_review/Citric_Acid_X_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI citric acid monohydrate identity and 8/8 count pass, but active monoanion
    synonyms and unsupported nutritional roles remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-037b9c1d6c79ac96
    - ev-698e1c6372735819
  - name: legacy-native-ids
    value: '["SEM:988b369fa53ce0a856f9","SEM:1973a5d6d3b034253ea0","SEM:1428e403a41156125079"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-698e1c6372735819
    - ev-037b9c1d6c79ac96
    - ev-6e37523a1dd66254
- assessment_id: a-b647a95d5ffbde35
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-037b9c1d6c79ac96
  - ev-b647a95d5ffbde35
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-037b9c1d6c79ac96
    - ev-b647a95d5ffbde35
findings:
- finding_id: rec-f-4b6ce9af131d7a9f
  issue_key: mim-reconciliation-role-support-70cad0ed79a17905
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Citric acid x H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-70cad0ed79a17905
  evidence_ids:
  - ev-037b9c1d6c79ac96
  - ev-b647a95d5ffbde35
  - ev-56f19402451b631a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-4b6ce9af131d7a9f
actions:
- action_id: rec-action-4b6ce9af131d7a9f
  description: 'Reassess prediction-only role support: Citric acid x H2O'
  finding_ids:
  - rec-f-4b6ce9af131d7a9f
  target_ids:
  - record-70cad0ed79a17905
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Citric_Acid_X_H2o.yaml
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
