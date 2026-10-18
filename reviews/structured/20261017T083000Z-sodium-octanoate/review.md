# Per-record structured review: Sodium_Octanoate (data/ingredients/mapped/Sodium_Octanoate.yaml)

- Review: 20261017T083000Z-sodium-octanoate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Octanoate (data/ingredients/mapped/Sodium_Octanoate.yaml, record-489f5b29da7e508b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Octanoate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Octanoate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-489f5b29da7e508b | data/ingredients/mapped/Sodium_Octanoate.yaml | maintained | Sodium_Octanoate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-489f5b29da7e508b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-489f5b29da7e508b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-489f5b29da7e508b | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-489f5b29da7e508b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-489f5b29da7e508b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:33:17Z; reviewed SHA-256=7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2; current SHA-256=7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Octanoate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:132100 identity, CAS, synonyms, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-489f5b29da7e508b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-17ddf85eaa35dc7a: Reassess prediction-only role support: Sodium octanoate

major / open / confirmed; issue key: mim-reconciliation-role-support-489f5b29da7e508b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-17ddf85eaa35dc7a

Reassess prediction-only role support: Sodium octanoate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-27c96f47d871cd2c | data/ingredients/mapped/Sodium_Octanoate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1856],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132100","line":1858,"mapping_status":"MAPPED","ontology_id":"CHEBI:132100","preferred_term":"Sodium octanoate"}],"identifier":"CHEBI:132100","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132100","ontology_label":"sodium octanoate","ontology_source":"CHEBI"},"preferred_term":"Sodium octanoate","sssom_rows":[{"data_row":2584,"object_id":"CHEBI:132100","object_label":"sodium octanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Octanoate","synonym_count":6} |
| ev-7194c218e4ace7a2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1856] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-80019035ad652cf0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Octanoate; data-row positions=[2584] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2584,"object_id":"CHEBI:132100","object_label":"sodium octanoate","other":"Caprylic acid sodium salt&#124;Natrium octanoat&#124;Octanoic acid, sodium salt&#124;Sodium caprylate&#124;Sodium n-octanoate&#124;CAS:1984-06-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Octanoate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d4dede383c850e85 | docs/data/mapped_ingredients.csv; CSV lines=[1858] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:132100","line":1858,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:132100","preferred_term":"Sodium octanoate","total_occurrences":"5"}] |
| ev-6a13ad7a6fcd6c75 | reports/yaml_record_review/Sodium_Octanoate.md; &#96;data/ingredients/mapped/Sodium_Octanoate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:32; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-108bb44dffb42323 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1225,2058] | context_only | [{"current_record_sha256":"7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2","finding_id":"SEM:80e68002cb8f75f552fd","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2","finding_id":"SEM:fbb16ddd8677bebccfc8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-23f082a7b6892f84 | data/ingredients/mapped/Sodium_Octanoate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1856],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132100","line":1858,"mapping_status":"MAPPED","ontology_id":"CHEBI:132100","preferred_term":"Sodium octanoate"}],"identifier":"CHEBI:132100","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132100","ontology_label":"sodium octanoate","ontology_source":"CHEBI"},"preferred_term":"Sodium octanoate","sssom_rows":[{"data_row":2584,"object_id":"CHEBI:132100","object_label":"sodium octanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Octanoate","synonym_count":6} |
| ev-376170c3824c3300 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml; findings[finding_id=f-17ddf85eaa35dc7a] | context_only | Predecessor structured review finding f-17ddf85eaa35dc7a in 20261011T024638Z-mim-reconcile-all-batch-11 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-octanoate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Octanoate (data/ingredients/mapped/Sodium_Octanoate.yaml)'
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
summary: Per-record structured review for Sodium_Octanoate (data/ingredients/mapped/Sodium_Octanoate.yaml,
  record-489f5b29da7e508b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Octanoate.yaml
    sha256: 7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2
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
  - path: reports/yaml_record_review/Sodium_Octanoate.md
    sha256: 669feea9a7e6e5b2adb5b74106e20e79319f57e8c32269c650d2a88eb89958a1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-489f5b29da7e508b
  path: data/ingredients/mapped/Sodium_Octanoate.yaml
  label: Sodium_Octanoate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Octanoate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Octanoate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Octanoate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-489f5b29da7e508b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-27c96f47d871cd2c
  - ev-7194c218e4ace7a2
  - ev-80019035ad652cf0
  - ev-d4dede383c850e85
  - ev-23f082a7b6892f84
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-27c96f47d871cd2c
  - ev-108bb44dffb42323
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-6a13ad7a6fcd6c75
  - ev-108bb44dffb42323
  - ev-376170c3824c3300
evidence:
- evidence_id: ev-27c96f47d871cd2c
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Octanoate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1856],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132100","line":1858,"mapping_status":"MAPPED","ontology_id":"CHEBI:132100","preferred_term":"Sodium
    octanoate"}],"identifier":"CHEBI:132100","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132100","ontology_label":"sodium
    octanoate","ontology_source":"CHEBI"},"preferred_term":"Sodium octanoate","sssom_rows":[{"data_row":2584,"object_id":"CHEBI:132100","object_label":"sodium
    octanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Octanoate","synonym_count":6}'
  snapshot_sha256: 7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2
- evidence_id: ev-7194c218e4ace7a2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1856]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-80019035ad652cf0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Octanoate; data-row positions=[2584]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2584,"object_id":"CHEBI:132100","object_label":"sodium
    octanoate","other":"Caprylic acid sodium salt|Natrium octanoat|Octanoic acid,
    sodium salt|Sodium caprylate|Sodium n-octanoate|CAS:1984-06-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Octanoate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d4dede383c850e85
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1858]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:132100","line":1858,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:132100","preferred_term":"Sodium
    octanoate","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6a13ad7a6fcd6c75
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Octanoate.md
  locator: '`data/ingredients/mapped/Sodium_Octanoate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:32; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 669feea9a7e6e5b2adb5b74106e20e79319f57e8c32269c650d2a88eb89958a1
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Sodium_Octanoate.yaml`,\
    \ either replace the\n  provisional `COMPUTATIONAL_PREDICTION` role evidence with\
    \ checked\n  CultureMech source evidence for `Role: Carbon source`, or drop\n\
    \  `nutritional_roles.CARBON_SOURCE` if that original role cannot be recovered."
- evidence_id: ev-108bb44dffb42323
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1225,2058]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2","finding_id":"SEM:80e68002cb8f75f552fd","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2","finding_id":"SEM:fbb16ddd8677bebccfc8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-23f082a7b6892f84
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Octanoate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1856],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:132100","line":1858,"mapping_status":"MAPPED","ontology_id":"CHEBI:132100","preferred_term":"Sodium
    octanoate"}],"identifier":"CHEBI:132100","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:132100","ontology_label":"sodium
    octanoate","ontology_source":"CHEBI"},"preferred_term":"Sodium octanoate","sssom_rows":[{"data_row":2584,"object_id":"CHEBI:132100","object_label":"sodium
    octanoate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Octanoate","synonym_count":6}'
  snapshot_sha256: 7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2
- evidence_id: ev-376170c3824c3300
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
  locator: findings[finding_id=f-17ddf85eaa35dc7a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-17ddf85eaa35dc7a in 20261011T024638Z-mim-reconcile-all-batch-11
  snapshot_sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
assessments:
- assessment_id: a-d8e5a94a8f54286b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-27c96f47d871cd2c
  - ev-7194c218e4ace7a2
  - ev-80019035ad652cf0
  - ev-d4dede383c850e85
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0d6747a62297718b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-6a13ad7a6fcd6c75
  - ev-27c96f47d871cd2c
  - ev-108bb44dffb42323
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:33:17Z;
    reviewed SHA-256=7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2;
    current SHA-256=7e7f554bbb26400281ae30180749cbbe9a9ec579c3f33525d7ef018ff1988df2;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Octanoate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:132100 identity, CAS, synonyms, and final SSSOM row pass, but CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6a13ad7a6fcd6c75
    - ev-27c96f47d871cd2c
  - name: legacy-native-ids
    value: '["SEM:80e68002cb8f75f552fd","SEM:fbb16ddd8677bebccfc8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-27c96f47d871cd2c
    - ev-6a13ad7a6fcd6c75
    - ev-108bb44dffb42323
- assessment_id: a-23f082a7b6892f84
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-6a13ad7a6fcd6c75
  - ev-23f082a7b6892f84
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6a13ad7a6fcd6c75
    - ev-23f082a7b6892f84
findings:
- finding_id: rec-f-17ddf85eaa35dc7a
  issue_key: mim-reconciliation-role-support-489f5b29da7e508b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Sodium octanoate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-489f5b29da7e508b
  evidence_ids:
  - ev-6a13ad7a6fcd6c75
  - ev-23f082a7b6892f84
  - ev-376170c3824c3300
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Octanoate.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-11
    finding_id: f-17ddf85eaa35dc7a
actions:
- action_id: rec-action-17ddf85eaa35dc7a
  description: 'Reassess prediction-only role support: Sodium octanoate'
  finding_ids:
  - rec-f-17ddf85eaa35dc7a
  target_ids:
  - record-489f5b29da7e508b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Octanoate.yaml
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
