# Per-record structured review: Nisin (data/ingredients/mapped/Nisin.yaml)

- Review: 20261017T083000Z-nisin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nisin (data/ingredients/mapped/Nisin.yaml, record-6c8878c6a593030a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nisin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nisin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6c8878c6a593030a | data/ingredients/mapped/Nisin.yaml | maintained | Nisin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6c8878c6a593030a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6c8878c6a593030a | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6c8878c6a593030a | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6c8878c6a593030a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6c8878c6a593030a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:44:08Z; reviewed SHA-256=aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45; current SHA-256=aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45; hash_changed=False. Reports=["reports/yaml_record_review/Nisin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:71629 nisin identity passes, but SELECTIVE_AGENT is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-6c8878c6a593030a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-57a8f7b8d656041c: Reassess prediction-only role support: Nisin

major / open / confirmed; issue key: mim-reconciliation-role-support-6c8878c6a593030a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-57a8f7b8d656041c

Reassess prediction-only role support: Nisin

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cf186d4f1ee5fc28 | data/ingredients/mapped/Nisin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1563],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:71629","line":1565,"mapping_status":"MAPPED","ontology_id":"CHEBI:71629","preferred_term":"Nisin"}],"identifier":"CHEBI:71629","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:71629","ontology_label":"nisin","ontology_source":"CHEBI"},"preferred_term":"Nisin","sssom_rows":[{"data_row":2095,"object_id":"CHEBI:71629","object_label":"nisin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nisin","synonym_count":1} |
| ev-79cebfad0cbff769 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1563] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-1a141104d6b00e05 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nisin; data-row positions=[2095] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2095,"object_id":"CHEBI:71629","object_label":"nisin","other":"N-{[(1S,4S,7S,8S,11R,14S,17R,20S)-7-{[N(2)-({(3R,9S,12S,15S,21S,22S)-21-[(N(2)-{[(6R,9S,10S,15aS)-10-({[(3R,6S,12S,15S)-12-[(2S)-butan-2-yl]-6-isobutyl-15-{[(2Z)-2-(L-isoleucylamino)but-2-enoyl]amino}-9-methylene-5,8,11,14-tetraoxo-1-thia-4,7,10,13-tetraazacyclohexadecan-3-yl]carbonyl}amino)-9-methyl-1,4,11-trioxododecahydro-1H,9H-pyrrolo[2,1-i][1,4,7,10]thiatriazacyclotridecin-6-yl]carbonyl}-L-lysyl)amino]-12-isobutyl-15,22-dimethyl-9-[2-(methylsulfanyl)ethyl]-5,8,11,14,17,20-hexaoxo-1-thia-4,7,10,13,16,19-hexaazacyclodocosan-3-yl}carbonyl)-L-asparaginyl-L-methionyl-L-lysyl]amino}-14-(1H-imidazol-5-ylmethyl)-4,8,20-trimethyl-3,6,12,15,21-pentaoxo-9,19-dithia-2,5,13,16,22-pentaazabicyclo[9.9.2]docos-17-yl]carbonyl}-L-seryl-L-isoleucyl-L-histidyl-N-(3-{[(1S)-5-amino-1-carboxypentyl]amino}-3-oxoprop-1-en-2-yl)-L-valinamide&#124;CAS:1414-45-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Nisin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-dd25eb99ec0c8b79 | docs/data/mapped_ingredients.csv; CSV lines=[1565] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:71629","line":1565,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:71629","preferred_term":"Nisin","total_occurrences":"0"}] |
| ev-78071e9cb2e59bb6 | reports/yaml_record_review/Nisin.md; &#96;data/ingredients/mapped/Nisin.yaml&#96;:2; Verdict:4; Identity:10; Validation:19; Evidence:26; Completeness:39; Recommended Edits:45 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-dfca13454f8b5a1a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1061,1466] | context_only | [{"current_record_sha256":"aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45","finding_id":"SEM:e1644c13b67860c547be","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45","finding_id":"SEM:b6ca26c4a311208e0475","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2f0232123f6a7ac3 | data/ingredients/mapped/Nisin.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1563],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:71629","line":1565,"mapping_status":"MAPPED","ontology_id":"CHEBI:71629","preferred_term":"Nisin"}],"identifier":"CHEBI:71629","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:71629","ontology_label":"nisin","ontology_source":"CHEBI"},"preferred_term":"Nisin","sssom_rows":[{"data_row":2095,"object_id":"CHEBI:71629","object_label":"nisin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nisin","synonym_count":1} |
| ev-42190bcce2765865 | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-57a8f7b8d656041c] | context_only | Predecessor structured review finding f-57a8f7b8d656041c in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nisin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nisin (data/ingredients/mapped/Nisin.yaml)'
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
summary: Per-record structured review for Nisin (data/ingredients/mapped/Nisin.yaml,
  record-6c8878c6a593030a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nisin.yaml
    sha256: aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Nisin.md
    sha256: 3ee715fe4d1845922eec7a418d952fba48f11e7d66867589fa51aa6dea1573a3
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6c8878c6a593030a
  path: data/ingredients/mapped/Nisin.yaml
  label: Nisin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nisin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nisin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nisin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6c8878c6a593030a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-cf186d4f1ee5fc28
  - ev-79cebfad0cbff769
  - ev-1a141104d6b00e05
  - ev-dd25eb99ec0c8b79
  - ev-2f0232123f6a7ac3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-cf186d4f1ee5fc28
  - ev-dfca13454f8b5a1a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-78071e9cb2e59bb6
  - ev-dfca13454f8b5a1a
  - ev-42190bcce2765865
evidence:
- evidence_id: ev-cf186d4f1ee5fc28
  kind: record_content
  reference: data/ingredients/mapped/Nisin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1563],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:71629","line":1565,"mapping_status":"MAPPED","ontology_id":"CHEBI:71629","preferred_term":"Nisin"}],"identifier":"CHEBI:71629","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:71629","ontology_label":"nisin","ontology_source":"CHEBI"},"preferred_term":"Nisin","sssom_rows":[{"data_row":2095,"object_id":"CHEBI:71629","object_label":"nisin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nisin","synonym_count":1}'
  snapshot_sha256: aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45
- evidence_id: ev-79cebfad0cbff769
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1563]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-1a141104d6b00e05
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nisin; data-row positions=[2095]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2095,"object_id":"CHEBI:71629","object_label":"nisin","other":"N-{[(1S,4S,7S,8S,11R,14S,17R,20S)-7-{[N(2)-({(3R,9S,12S,15S,21S,22S)-21-[(N(2)-{[(6R,9S,10S,15aS)-10-({[(3R,6S,12S,15S)-12-[(2S)-butan-2-yl]-6-isobutyl-15-{[(2Z)-2-(L-isoleucylamino)but-2-enoyl]amino}-9-methylene-5,8,11,14-tetraoxo-1-thia-4,7,10,13-tetraazacyclohexadecan-3-yl]carbonyl}amino)-9-methyl-1,4,11-trioxododecahydro-1H,9H-pyrrolo[2,1-i][1,4,7,10]thiatriazacyclotridecin-6-yl]carbonyl}-L-lysyl)amino]-12-isobutyl-15,22-dimethyl-9-[2-(methylsulfanyl)ethyl]-5,8,11,14,17,20-hexaoxo-1-thia-4,7,10,13,16,19-hexaazacyclodocosan-3-yl}carbonyl)-L-asparaginyl-L-methionyl-L-lysyl]amino}-14-(1H-imidazol-5-ylmethyl)-4,8,20-trimethyl-3,6,12,15,21-pentaoxo-9,19-dithia-2,5,13,16,22-pentaazabicyclo[9.9.2]docos-17-yl]carbonyl}-L-seryl-L-isoleucyl-L-histidyl-N-(3-{[(1S)-5-amino-1-carboxypentyl]amino}-3-oxoprop-1-en-2-yl)-L-valinamide|CAS:1414-45-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Nisin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-dd25eb99ec0c8b79
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1565]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:71629","line":1565,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:71629","preferred_term":"Nisin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-78071e9cb2e59bb6
  kind: prior_review
  reference: reports/yaml_record_review/Nisin.md
  locator: '`data/ingredients/mapped/Nisin.yaml`:2; Verdict:4; Identity:10; Validation:19;
    Evidence:26; Completeness:39; Recommended Edits:45'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3ee715fe4d1845922eec7a418d952fba48f11e7d66867589fa51aa6dea1573a3
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nisin.yaml`, replace\
    \ the provisional\n  `SELECTIVE_AGENT` role with inspected claim-level evidence\
    \ or remove it."
- evidence_id: ev-dfca13454f8b5a1a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1061,1466]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45","finding_id":"SEM:e1644c13b67860c547be","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45","finding_id":"SEM:b6ca26c4a311208e0475","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2f0232123f6a7ac3
  kind: record_content
  reference: data/ingredients/mapped/Nisin.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1563],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:71629","line":1565,"mapping_status":"MAPPED","ontology_id":"CHEBI:71629","preferred_term":"Nisin"}],"identifier":"CHEBI:71629","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:71629","ontology_label":"nisin","ontology_source":"CHEBI"},"preferred_term":"Nisin","sssom_rows":[{"data_row":2095,"object_id":"CHEBI:71629","object_label":"nisin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nisin","synonym_count":1}'
  snapshot_sha256: aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45
- evidence_id: ev-42190bcce2765865
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-57a8f7b8d656041c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-57a8f7b8d656041c in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-252c975825e6246b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-cf186d4f1ee5fc28
  - ev-79cebfad0cbff769
  - ev-1a141104d6b00e05
  - ev-dd25eb99ec0c8b79
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a5aa1b309dd625f5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-78071e9cb2e59bb6
  - ev-cf186d4f1ee5fc28
  - ev-dfca13454f8b5a1a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:44:08Z;
    reviewed SHA-256=aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45;
    current SHA-256=aeb6ded6b1375ed852b3a3c2a4c5954d0123fb5b398263121a8a96bca6d03b45;
    hash_changed=False. Reports=["reports/yaml_record_review/Nisin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:71629 nisin
    identity passes, but SELECTIVE_AGENT is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-78071e9cb2e59bb6
    - ev-cf186d4f1ee5fc28
  - name: legacy-native-ids
    value: '["SEM:e1644c13b67860c547be","SEM:b6ca26c4a311208e0475"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cf186d4f1ee5fc28
    - ev-78071e9cb2e59bb6
    - ev-dfca13454f8b5a1a
- assessment_id: a-2f0232123f6a7ac3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-78071e9cb2e59bb6
  - ev-2f0232123f6a7ac3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-78071e9cb2e59bb6
    - ev-2f0232123f6a7ac3
findings:
- finding_id: rec-f-57a8f7b8d656041c
  issue_key: mim-reconciliation-role-support-6c8878c6a593030a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Nisin'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6c8878c6a593030a
  evidence_ids:
  - ev-78071e9cb2e59bb6
  - ev-2f0232123f6a7ac3
  - ev-42190bcce2765865
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nisin.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-57a8f7b8d656041c
actions:
- action_id: rec-action-57a8f7b8d656041c
  description: 'Reassess prediction-only role support: Nisin'
  finding_ids:
  - rec-f-57a8f7b8d656041c
  target_ids:
  - record-6c8878c6a593030a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nisin.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
