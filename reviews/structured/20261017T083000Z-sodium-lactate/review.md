# Per-record structured review: Sodium_Lactate (data/ingredients/mapped/Sodium_Lactate.yaml)

- Review: 20261017T083000Z-sodium-lactate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Lactate (data/ingredients/mapped/Sodium_Lactate.yaml, record-7835366638448a62, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Lactate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Lactate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7835366638448a62 | data/ingredients/mapped/Sodium_Lactate.yaml | maintained | Sodium_Lactate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7835366638448a62 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-7835366638448a62 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7835366638448a62 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7835366638448a62.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7835366638448a62.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:22:24Z; reviewed SHA-256=56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6; current SHA-256=56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Lactate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:75228 identity, CAS, carbon role, and structure pass, but final SSSOM exports concentration labels and ENERGY_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-7835366638448a62.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-1f2105e73357b890: Reassess prediction-only role support: Sodium lactate

major / open / confirmed; issue key: mim-reconciliation-role-support-7835366638448a62.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-1f2105e73357b890

Reassess prediction-only role support: Sodium lactate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b7c8361101fd4ae9 | data/ingredients/mapped/Sodium_Lactate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1847],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75228","line":1849,"mapping_status":"MAPPED","ontology_id":"CHEBI:75228","preferred_term":"Sodium lactate"}],"identifier":"CHEBI:75228","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":283,"edge_count":283,"occurrences":283},"occurrence_statistics":{"media_count":283,"total_occurrences":283},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75228","ontology_label":"sodium lactate","ontology_source":"CHEBI"},"preferred_term":"Sodium lactate","sssom_rows":[{"data_row":2574,"object_id":"CHEBI:75228","object_label":"sodium lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Lactate","synonym_count":29} |
| ev-91fd4dbf9a330e81 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1847] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-082d3a509ff5ed9c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Lactate; data-row positions=[2574] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2574,"object_id":"CHEBI:75228","object_label":"sodium lactate","other":"1 M Sodium lactate&#124;2-Hydroxypropanoic acid, monosodium salt&#124;DL-Na-lactate&#124;E325&#124;Lactic acid sodium salt&#124;Lactic acid, monosodium salt&#124;Mediject L&#124;Monosodium 2-hydroxypropanoate&#124;Monosodium lactate&#124;Na-(DL)-lactate&#124;Na-DL-lactate&#124;Sodium alpha-hydroxypropionate&#124;sodium 2-hydroxypropanoate&#124;Na-lactate&#124;Sodium DL-lactate&#124;Lactate (sodium salt)&#124;1 % Sodium Lactate&#124;D,L-lactic acid, sodium salt&#124;CAS:72-17-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Lactate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-b81b6aff4b92723c | docs/data/mapped_ingredients.csv; CSV lines=[1849] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75228","line":1849,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"283","ontology_id":"CHEBI:75228","preferred_term":"Sodium lactate","total_occurrences":"283"}] |
| ev-8837ac710e866881 | reports/yaml_record_review/Sodium_Lactate.md; &#96;data/ingredients/mapped/Sodium_Lactate.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-823664cca56b93c5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1220,1996] | context_only | [{"current_record_sha256":"56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6","finding_id":"SEM:eca76ae60af955e41359","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6","finding_id":"SEM:99d18fbacb8a4994abe1","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d5e7097a882d2940 | data/ingredients/mapped/Sodium_Lactate.yaml; nutritional_roles[1] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1847],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75228","line":1849,"mapping_status":"MAPPED","ontology_id":"CHEBI:75228","preferred_term":"Sodium lactate"}],"identifier":"CHEBI:75228","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":283,"edge_count":283,"occurrences":283},"occurrence_statistics":{"media_count":283,"total_occurrences":283},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75228","ontology_label":"sodium lactate","ontology_source":"CHEBI"},"preferred_term":"Sodium lactate","sssom_rows":[{"data_row":2574,"object_id":"CHEBI:75228","object_label":"sodium lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Lactate","synonym_count":29} |
| ev-d9ce9395fdbde69f | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-1f2105e73357b890] | context_only | Predecessor structured review finding f-1f2105e73357b890 in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-lactate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Lactate (data/ingredients/mapped/Sodium_Lactate.yaml)'
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
summary: Per-record structured review for Sodium_Lactate (data/ingredients/mapped/Sodium_Lactate.yaml,
  record-7835366638448a62, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Lactate.yaml
    sha256: 56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sodium_Lactate.md
    sha256: 991f55c0fb56df71a51a92e9b0a830f21a667ffad7a9a6f89d39caeef394e3f9
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7835366638448a62
  path: data/ingredients/mapped/Sodium_Lactate.yaml
  label: Sodium_Lactate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Lactate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Lactate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Lactate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7835366638448a62
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-b7c8361101fd4ae9
  - ev-91fd4dbf9a330e81
  - ev-082d3a509ff5ed9c
  - ev-b81b6aff4b92723c
  - ev-d5e7097a882d2940
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-b7c8361101fd4ae9
  - ev-823664cca56b93c5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-8837ac710e866881
  - ev-823664cca56b93c5
  - ev-d9ce9395fdbde69f
evidence:
- evidence_id: ev-b7c8361101fd4ae9
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Lactate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1847],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75228","line":1849,"mapping_status":"MAPPED","ontology_id":"CHEBI:75228","preferred_term":"Sodium
    lactate"}],"identifier":"CHEBI:75228","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":283,"edge_count":283,"occurrences":283},"occurrence_statistics":{"media_count":283,"total_occurrences":283},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75228","ontology_label":"sodium
    lactate","ontology_source":"CHEBI"},"preferred_term":"Sodium lactate","sssom_rows":[{"data_row":2574,"object_id":"CHEBI:75228","object_label":"sodium
    lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Lactate","synonym_count":29}'
  snapshot_sha256: 56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6
- evidence_id: ev-91fd4dbf9a330e81
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1847]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-082d3a509ff5ed9c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Lactate; data-row positions=[2574]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2574,"object_id":"CHEBI:75228","object_label":"sodium
    lactate","other":"1 M Sodium lactate|2-Hydroxypropanoic acid, monosodium salt|DL-Na-lactate|E325|Lactic
    acid sodium salt|Lactic acid, monosodium salt|Mediject L|Monosodium 2-hydroxypropanoate|Monosodium
    lactate|Na-(DL)-lactate|Na-DL-lactate|Sodium alpha-hydroxypropionate|sodium 2-hydroxypropanoate|Na-lactate|Sodium
    DL-lactate|Lactate (sodium salt)|1 % Sodium Lactate|D,L-lactic acid, sodium salt|CAS:72-17-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Lactate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b81b6aff4b92723c
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1849]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75228","line":1849,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"283","ontology_id":"CHEBI:75228","preferred_term":"Sodium
    lactate","total_occurrences":"283"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8837ac710e866881
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Lactate.md
  locator: '`data/ingredients/mapped/Sodium_Lactate.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 991f55c0fb56df71a51a92e9b0a830f21a667ffad7a9a6f89d39caeef394e3f9
- evidence_id: ev-823664cca56b93c5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1220,1996]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6","finding_id":"SEM:eca76ae60af955e41359","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6","finding_id":"SEM:99d18fbacb8a4994abe1","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d5e7097a882d2940
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Lactate.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1847],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75228","line":1849,"mapping_status":"MAPPED","ontology_id":"CHEBI:75228","preferred_term":"Sodium
    lactate"}],"identifier":"CHEBI:75228","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":283,"edge_count":283,"occurrences":283},"occurrence_statistics":{"media_count":283,"total_occurrences":283},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:75228","ontology_label":"sodium
    lactate","ontology_source":"CHEBI"},"preferred_term":"Sodium lactate","sssom_rows":[{"data_row":2574,"object_id":"CHEBI:75228","object_label":"sodium
    lactate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Lactate","synonym_count":29}'
  snapshot_sha256: 56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6
- evidence_id: ev-d9ce9395fdbde69f
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-1f2105e73357b890]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-1f2105e73357b890 in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-5db81d32d565f0c8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-b7c8361101fd4ae9
  - ev-91fd4dbf9a330e81
  - ev-082d3a509ff5ed9c
  - ev-b81b6aff4b92723c
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4a6de63a958c7fe1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-8837ac710e866881
  - ev-b7c8361101fd4ae9
  - ev-823664cca56b93c5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:22:24Z;
    reviewed SHA-256=56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6;
    current SHA-256=56bf2419bf87002c162021c48c4a2c97392a0f97243bd2013d78a4a62e5f69a6;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Lactate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:75228 identity, CAS, carbon role, and structure pass, but final SSSOM exports
    concentration labels and ENERGY_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8837ac710e866881
    - ev-b7c8361101fd4ae9
  - name: legacy-native-ids
    value: '["SEM:eca76ae60af955e41359","SEM:99d18fbacb8a4994abe1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b7c8361101fd4ae9
    - ev-8837ac710e866881
    - ev-823664cca56b93c5
- assessment_id: a-d5e7097a882d2940
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-8837ac710e866881
  - ev-d5e7097a882d2940
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8837ac710e866881
    - ev-d5e7097a882d2940
findings:
- finding_id: rec-f-1f2105e73357b890
  issue_key: mim-reconciliation-role-support-7835366638448a62
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sodium lactate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-7835366638448a62
  evidence_ids:
  - ev-8837ac710e866881
  - ev-d5e7097a882d2940
  - ev-d9ce9395fdbde69f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Lactate.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-1f2105e73357b890
actions:
- action_id: rec-action-1f2105e73357b890
  description: 'Reassess prediction-only role support: Sodium lactate'
  finding_ids:
  - rec-f-1f2105e73357b890
  target_ids:
  - record-7835366638448a62
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Lactate.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
