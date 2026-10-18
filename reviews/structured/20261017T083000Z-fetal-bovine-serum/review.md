# Per-record structured review: Fetal_Bovine_Serum (data/ingredients/mapped/Fetal_Bovine_Serum.yaml)

- Review: 20261017T083000Z-fetal-bovine-serum
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fetal_Bovine_Serum (data/ingredients/mapped/Fetal_Bovine_Serum.yaml, record-a90502a3343e71f1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fetal_Bovine_Serum.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fetal_Bovine_Serum.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a90502a3343e71f1 | data/ingredients/mapped/Fetal_Bovine_Serum.yaml | maintained | Fetal_Bovine_Serum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a90502a3343e71f1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-a90502a3343e71f1 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a90502a3343e71f1 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a90502a3343e71f1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a90502a3343e71f1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z; reviewed SHA-256=adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f; current SHA-256=adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f; hash_changed=False. Reports=["reports/yaml_record_review/Fetal_Bovine_Serum.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact fetal-bovine-serum identity and aliases pass, but PROTEIN_SOURCE is computational and the serum is typed as SINGLE_INGREDIENT.

### Historical provisional-role concern

evidence: concern. Targets: record-a90502a3343e71f1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-62ba48c0722286ea: Reassess prediction-only role support: Fetal bovine serum

major / open / confirmed; issue key: mim-reconciliation-role-support-a90502a3343e71f1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-62ba48c0722286ea

Reassess prediction-only role support: Fetal bovine serum

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a2c16a49f75c80d7 | data/ingredients/mapped/Fetal_Bovine_Serum.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1003],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C113696","line":1005,"mapping_status":"MAPPED","ontology_id":"NCIT:C113696","preferred_term":"Fetal bovine serum"}],"identifier":"NCIT:C113696","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":122,"edge_count":122,"occurrences":122},"occurrence_statistics":{"media_count":122,"total_occurrences":122},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C113696","ontology_label":"Fetal Bovine Serum","ontology_source":"NCIT"},"preferred_term":"Fetal bovine serum","sssom_rows":[{"data_row":1205,"object_id":"NCIT:C113696","object_label":"Fetal Bovine Serum","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fetal_Bovine_Serum","synonym_count":3} |
| ev-bb8474abf3cc23d9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1003] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d97914f7d575157e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fetal_Bovine_Serum; data-row positions=[1205] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1205,"object_id":"NCIT:C113696","object_label":"Fetal Bovine Serum","other":"FBS&#124;Fetal Bovine Serum (ATCC 30-2020)","predicate_id":"skos:exactMatch","subject_id":"MIM:Fetal_Bovine_Serum","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-960b4069dcdaa77a | docs/data/mapped_ingredients.csv; CSV lines=[1005] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C113696","line":1005,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"122","ontology_id":"NCIT:C113696","preferred_term":"Fetal bovine serum","total_occurrences":"122"}] |
| ev-302aa2c4c19b786f | reports/yaml_record_review/Fetal_Bovine_Serum.md; &#96;data/ingredients/mapped/Fetal_Bovine_Serum.yaml&#96;:2; Verdict:4; Identity:12; Validation:27; Evidence:37; Completeness:69; Recommended Edits:79 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-77d8eb63170c4b9a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[612,1911] | context_only | [{"current_record_sha256":"adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f","finding_id":"SEM:ac69aebb23443acd4b25","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f","finding_id":"SEM:487edc1d3ad68c67a7fd","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-ff75aa18a3f6d267 | data/ingredients/mapped/Fetal_Bovine_Serum.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1003],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C113696","line":1005,"mapping_status":"MAPPED","ontology_id":"NCIT:C113696","preferred_term":"Fetal bovine serum"}],"identifier":"NCIT:C113696","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":122,"edge_count":122,"occurrences":122},"occurrence_statistics":{"media_count":122,"total_occurrences":122},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C113696","ontology_label":"Fetal Bovine Serum","ontology_source":"NCIT"},"preferred_term":"Fetal bovine serum","sssom_rows":[{"data_row":1205,"object_id":"NCIT:C113696","object_label":"Fetal Bovine Serum","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fetal_Bovine_Serum","synonym_count":3} |
| ev-0658011a39d7dfcf | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-62ba48c0722286ea] | context_only | Predecessor structured review finding f-62ba48c0722286ea in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fetal-bovine-serum
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fetal_Bovine_Serum (data/ingredients/mapped/Fetal_Bovine_Serum.yaml)'
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
summary: Per-record structured review for Fetal_Bovine_Serum (data/ingredients/mapped/Fetal_Bovine_Serum.yaml,
  record-a90502a3343e71f1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
    sha256: adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f
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
  - path: reports/yaml_record_review/Fetal_Bovine_Serum.md
    sha256: 63c4482742c4594706f4a47210dc196158dc4d9158fd0c71a4c3e9e390748682
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a90502a3343e71f1
  path: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
  label: Fetal_Bovine_Serum
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fetal_Bovine_Serum.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fetal_Bovine_Serum.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a90502a3343e71f1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-a2c16a49f75c80d7
  - ev-bb8474abf3cc23d9
  - ev-d97914f7d575157e
  - ev-960b4069dcdaa77a
  - ev-ff75aa18a3f6d267
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-a2c16a49f75c80d7
  - ev-77d8eb63170c4b9a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-302aa2c4c19b786f
  - ev-77d8eb63170c4b9a
  - ev-0658011a39d7dfcf
evidence:
- evidence_id: ev-a2c16a49f75c80d7
  kind: record_content
  reference: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1003],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C113696","line":1005,"mapping_status":"MAPPED","ontology_id":"NCIT:C113696","preferred_term":"Fetal
    bovine serum"}],"identifier":"NCIT:C113696","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":122,"edge_count":122,"occurrences":122},"occurrence_statistics":{"media_count":122,"total_occurrences":122},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C113696","ontology_label":"Fetal
    Bovine Serum","ontology_source":"NCIT"},"preferred_term":"Fetal bovine serum","sssom_rows":[{"data_row":1205,"object_id":"NCIT:C113696","object_label":"Fetal
    Bovine Serum","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fetal_Bovine_Serum","synonym_count":3}'
  snapshot_sha256: adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f
- evidence_id: ev-bb8474abf3cc23d9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1003]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d97914f7d575157e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fetal_Bovine_Serum; data-row positions=[1205]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1205,"object_id":"NCIT:C113696","object_label":"Fetal
    Bovine Serum","other":"FBS|Fetal Bovine Serum (ATCC 30-2020)","predicate_id":"skos:exactMatch","subject_id":"MIM:Fetal_Bovine_Serum","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-960b4069dcdaa77a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1005]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C113696","line":1005,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"122","ontology_id":"NCIT:C113696","preferred_term":"Fetal
    bovine serum","total_occurrences":"122"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-302aa2c4c19b786f
  kind: prior_review
  reference: reports/yaml_record_review/Fetal_Bovine_Serum.md
  locator: '`data/ingredients/mapped/Fetal_Bovine_Serum.yaml`:2; Verdict:4; Identity:12;
    Validation:27; Evidence:37; Completeness:69; Recommended Edits:79'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 63c4482742c4594706f4a47210dc196158dc4d9158fd0c71a4c3e9e390748682
  quote: "Recommended Edits:\n- Major: replace or remove `nutritional_roles.PROTEIN_SOURCE`\
    \ in\n  `data/ingredients/mapped/Fetal_Bovine_Serum.yaml`; keep the role only\
    \ if a\n  source explicitly supports fetal bovine serum as a protein source.\n\
    - Major: change `ingredient_type` on the same record from `SINGLE_INGREDIENT`\n\
    \  to the curator-confirmed mixture type, likely `UNDEFINED_MIXTURE`, then sync\n\
    \  `data/curated/mapped_ingredients.yaml` and rerun strict validation plus the\n\
    \  final SSSOM invariant gates."
- evidence_id: ev-77d8eb63170c4b9a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[612,1911]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f","finding_id":"SEM:ac69aebb23443acd4b25","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f","finding_id":"SEM:487edc1d3ad68c67a7fd","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ff75aa18a3f6d267
  kind: record_content
  reference: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1003],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C113696","line":1005,"mapping_status":"MAPPED","ontology_id":"NCIT:C113696","preferred_term":"Fetal
    bovine serum"}],"identifier":"NCIT:C113696","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":122,"edge_count":122,"occurrences":122},"occurrence_statistics":{"media_count":122,"total_occurrences":122},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"NCIT:C113696","ontology_label":"Fetal
    Bovine Serum","ontology_source":"NCIT"},"preferred_term":"Fetal bovine serum","sssom_rows":[{"data_row":1205,"object_id":"NCIT:C113696","object_label":"Fetal
    Bovine Serum","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fetal_Bovine_Serum","synonym_count":3}'
  snapshot_sha256: adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f
- evidence_id: ev-0658011a39d7dfcf
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-62ba48c0722286ea]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-62ba48c0722286ea in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-5ef14e580a821c11
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-a2c16a49f75c80d7
  - ev-bb8474abf3cc23d9
  - ev-d97914f7d575157e
  - ev-960b4069dcdaa77a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6735c056d8b8c571
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-302aa2c4c19b786f
  - ev-a2c16a49f75c80d7
  - ev-77d8eb63170c4b9a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:35:23Z;
    reviewed SHA-256=adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f;
    current SHA-256=adb576c3fda65e0329bdab829eb8a14e07ea1bdcb75a2fa7078dcff49c29b73f;
    hash_changed=False. Reports=["reports/yaml_record_review/Fetal_Bovine_Serum.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    fetal-bovine-serum identity and aliases pass, but PROTEIN_SOURCE is computational
    and the serum is typed as SINGLE_INGREDIENT.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-302aa2c4c19b786f
    - ev-a2c16a49f75c80d7
  - name: legacy-native-ids
    value: '["SEM:ac69aebb23443acd4b25","SEM:487edc1d3ad68c67a7fd"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a2c16a49f75c80d7
    - ev-302aa2c4c19b786f
    - ev-77d8eb63170c4b9a
- assessment_id: a-ff75aa18a3f6d267
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-302aa2c4c19b786f
  - ev-ff75aa18a3f6d267
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-302aa2c4c19b786f
    - ev-ff75aa18a3f6d267
findings:
- finding_id: rec-f-62ba48c0722286ea
  issue_key: mim-reconciliation-role-support-a90502a3343e71f1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Fetal bovine serum'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-a90502a3343e71f1
  evidence_ids:
  - ev-302aa2c4c19b786f
  - ev-ff75aa18a3f6d267
  - ev-0658011a39d7dfcf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-62ba48c0722286ea
actions:
- action_id: rec-action-62ba48c0722286ea
  description: 'Reassess prediction-only role support: Fetal bovine serum'
  finding_ids:
  - rec-f-62ba48c0722286ea
  target_ids:
  - record-a90502a3343e71f1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fetal_Bovine_Serum.yaml
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
