# Per-record structured review: Verbascose (data/ingredients/mapped/Verbascose.yaml)

- Review: 20261017T083000Z-verbascose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Verbascose (data/ingredients/mapped/Verbascose.yaml, record-8c101bde81f709af, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Verbascose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Verbascose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8c101bde81f709af | data/ingredients/mapped/Verbascose.yaml | maintained | Verbascose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8c101bde81f709af | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8c101bde81f709af | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8c101bde81f709af | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8c101bde81f709af.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8c101bde81f709af.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:54:19Z; reviewed SHA-256=74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b; current SHA-256=74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b; hash_changed=False. Reports=["reports/yaml_record_review/Verbascose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity passes, but CARBON_SOURCE is still a provisional ChEBI-ancestry role.

### Historical provisional-role concern

evidence: concern. Targets: record-8c101bde81f709af.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4a924a9de3b1a02b: Reassess prediction-only role support: Verbascose

major / open / confirmed; issue key: mim-reconciliation-role-support-8c101bde81f709af.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4a924a9de3b1a02b

Reassess prediction-only role support: Verbascose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-49225d8e69f88e2c | data/ingredients/mapped/Verbascose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2042],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28586","line":2044,"mapping_status":"MAPPED","ontology_id":"CHEBI:28586","preferred_term":"Verbascose"}],"identifier":"CHEBI:28586","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28586","ontology_label":"verbascose","ontology_source":"CHEBI"},"preferred_term":"Verbascose","sssom_rows":[{"data_row":2899,"object_id":"CHEBI:28586","object_label":"verbascose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Verbascose","synonym_count":1} |
| ev-633565df91a1971d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2042] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-db9cc6a361f81484 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Verbascose; data-row positions=[2899] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2899,"object_id":"CHEBI:28586","object_label":"verbascose","other":"beta-D-fructofuranosyl alpha-D-galactopyranosyl-(1-&gt;6)-alpha-D-galactopyranosyl-(1-&gt;6)-alpha-D-galactopyranosyl-(1-&gt;6)-alpha-D-glucopyranoside&#124;CAS:546-62-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Verbascose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-85475f280d1c2aae | docs/data/mapped_ingredients.csv; CSV lines=[2044] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:28586","line":2044,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28586","preferred_term":"Verbascose","total_occurrences":"0"}] |
| ev-f71db8ff4cf77e2c | reports/yaml_record_review/Verbascose.md; &#96;data/ingredients/mapped/Verbascose.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:33; Issues:40; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d703bd486b46940b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1336,1531] | context_only | [{"current_record_sha256":"74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b","finding_id":"SEM:574f0e0162889e93d674","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b","finding_id":"SEM:cc5c231021bbaf6ad149","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-dcdc23a21c831b5e | data/ingredients/mapped/Verbascose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2042],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28586","line":2044,"mapping_status":"MAPPED","ontology_id":"CHEBI:28586","preferred_term":"Verbascose"}],"identifier":"CHEBI:28586","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28586","ontology_label":"verbascose","ontology_source":"CHEBI"},"preferred_term":"Verbascose","sssom_rows":[{"data_row":2899,"object_id":"CHEBI:28586","object_label":"verbascose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Verbascose","synonym_count":1} |
| ev-e2291827c6d5f30f | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-4a924a9de3b1a02b] | context_only | Predecessor structured review finding f-4a924a9de3b1a02b in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-verbascose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Verbascose (data/ingredients/mapped/Verbascose.yaml)'
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
summary: Per-record structured review for Verbascose (data/ingredients/mapped/Verbascose.yaml,
  record-8c101bde81f709af, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Verbascose.yaml
    sha256: 74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Verbascose.md
    sha256: 5151c0ec9c360ff2e069e99f22b1a9eb12f4d6f6294048523475bfbc8c0f843a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8c101bde81f709af
  path: data/ingredients/mapped/Verbascose.yaml
  label: Verbascose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Verbascose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Verbascose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Verbascose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8c101bde81f709af
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-49225d8e69f88e2c
  - ev-633565df91a1971d
  - ev-db9cc6a361f81484
  - ev-85475f280d1c2aae
  - ev-dcdc23a21c831b5e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-49225d8e69f88e2c
  - ev-d703bd486b46940b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-f71db8ff4cf77e2c
  - ev-d703bd486b46940b
  - ev-e2291827c6d5f30f
evidence:
- evidence_id: ev-49225d8e69f88e2c
  kind: record_content
  reference: data/ingredients/mapped/Verbascose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2042],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28586","line":2044,"mapping_status":"MAPPED","ontology_id":"CHEBI:28586","preferred_term":"Verbascose"}],"identifier":"CHEBI:28586","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28586","ontology_label":"verbascose","ontology_source":"CHEBI"},"preferred_term":"Verbascose","sssom_rows":[{"data_row":2899,"object_id":"CHEBI:28586","object_label":"verbascose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Verbascose","synonym_count":1}'
  snapshot_sha256: 74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b
- evidence_id: ev-633565df91a1971d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2042]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-db9cc6a361f81484
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Verbascose; data-row positions=[2899]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2899,"object_id":"CHEBI:28586","object_label":"verbascose","other":"beta-D-fructofuranosyl
    alpha-D-galactopyranosyl-(1->6)-alpha-D-galactopyranosyl-(1->6)-alpha-D-galactopyranosyl-(1->6)-alpha-D-glucopyranoside|CAS:546-62-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Verbascose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-85475f280d1c2aae
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2044]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:28586","line":2044,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:28586","preferred_term":"Verbascose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f71db8ff4cf77e2c
  kind: prior_review
  reference: reports/yaml_record_review/Verbascose.md
  locator: '`data/ingredients/mapped/Verbascose.yaml`:2; Verdict:4; Identity:10; Validation:23;
    Evidence:33; Issues:40; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5151c0ec9c360ff2e069e99f22b1a9eb12f4d6f6294048523475bfbc8c0f843a
  quote: "Issues:\n- Major: `nutritional_roles.CARBON_SOURCE` rests on\n  `COMPUTATIONAL_PREDICTION`\
    \ evidence from the ChEBI `CHEBI:16646`\n  carbohydrate closure, and its curator\
    \ note explicitly marks the role as\n  provisional.\n\nRecommended Edits:\n- Replace\
    \ or remove `data/ingredients/mapped/Verbascose.yaml`\n  `nutritional_roles.CARBON_SOURCE`;\
    \ keep it only if a maintained source\n  supports verbascose as a carbon source\
    \ in the specific media records that use\n  it, then rerun strict validation and\
    \ SSSOM invariant checks."
- evidence_id: ev-d703bd486b46940b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1336,1531]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b","finding_id":"SEM:574f0e0162889e93d674","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b","finding_id":"SEM:cc5c231021bbaf6ad149","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-dcdc23a21c831b5e
  kind: record_content
  reference: data/ingredients/mapped/Verbascose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2042],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:28586","line":2044,"mapping_status":"MAPPED","ontology_id":"CHEBI:28586","preferred_term":"Verbascose"}],"identifier":"CHEBI:28586","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:28586","ontology_label":"verbascose","ontology_source":"CHEBI"},"preferred_term":"Verbascose","sssom_rows":[{"data_row":2899,"object_id":"CHEBI:28586","object_label":"verbascose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Verbascose","synonym_count":1}'
  snapshot_sha256: 74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b
- evidence_id: ev-e2291827c6d5f30f
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-4a924a9de3b1a02b]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4a924a9de3b1a02b in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-f742cba1fd58b38d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-49225d8e69f88e2c
  - ev-633565df91a1971d
  - ev-db9cc6a361f81484
  - ev-85475f280d1c2aae
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-bce0048bad5709a9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-f71db8ff4cf77e2c
  - ev-49225d8e69f88e2c
  - ev-d703bd486b46940b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T20:54:19Z;
    reviewed SHA-256=74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b;
    current SHA-256=74418126fd006d67a5df15cbdde780f2394bc8f3115fa04f082668c30a11451b;
    hash_changed=False. Reports=["reports/yaml_record_review/Verbascose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity passes, but CARBON_SOURCE is still a provisional ChEBI-ancestry role.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f71db8ff4cf77e2c
    - ev-49225d8e69f88e2c
  - name: legacy-native-ids
    value: '["SEM:574f0e0162889e93d674","SEM:cc5c231021bbaf6ad149"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-49225d8e69f88e2c
    - ev-f71db8ff4cf77e2c
    - ev-d703bd486b46940b
- assessment_id: a-dcdc23a21c831b5e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-f71db8ff4cf77e2c
  - ev-dcdc23a21c831b5e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f71db8ff4cf77e2c
    - ev-dcdc23a21c831b5e
findings:
- finding_id: rec-f-4a924a9de3b1a02b
  issue_key: mim-reconciliation-role-support-8c101bde81f709af
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Verbascose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8c101bde81f709af
  evidence_ids:
  - ev-f71db8ff4cf77e2c
  - ev-dcdc23a21c831b5e
  - ev-e2291827c6d5f30f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Verbascose.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-4a924a9de3b1a02b
actions:
- action_id: rec-action-4a924a9de3b1a02b
  description: 'Reassess prediction-only role support: Verbascose'
  finding_ids:
  - rec-f-4a924a9de3b1a02b
  target_ids:
  - record-8c101bde81f709af
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Verbascose.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
```
