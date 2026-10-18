# Per-record structured review: Cefaclor (data/ingredients/mapped/Cefaclor.yaml)

- Review: 20261017T083000Z-cefaclor
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cefaclor (data/ingredients/mapped/Cefaclor.yaml, record-8b79299063e9386c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cefaclor.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cefaclor.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8b79299063e9386c | data/ingredients/mapped/Cefaclor.yaml | maintained | Cefaclor |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8b79299063e9386c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8b79299063e9386c | Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8b79299063e9386c | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8b79299063e9386c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8b79299063e9386c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:19:29Z; reviewed SHA-256=bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356; current SHA-256=bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356; hash_changed=False. Reports=["reports/yaml_record_review/Cefaclor.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cefaclor identity passes, but SELECTIVE_AGENT is only a provisional name-pattern prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-8b79299063e9386c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-077870be4623f168: Reassess prediction-only role support: Cefaclor

major / open / confirmed; issue key: mim-reconciliation-role-support-8b79299063e9386c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-077870be4623f168

Reassess prediction-only role support: Cefaclor

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9229cb33c9f356ea | data/ingredients/mapped/Cefaclor.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[675],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3478","line":677,"mapping_status":"MAPPED","ontology_id":"CHEBI:3478","preferred_term":"Cefaclor"}],"identifier":"CHEBI:3478","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3478","ontology_label":"cefaclor","ontology_source":"CHEBI"},"preferred_term":"Cefaclor","sssom_rows":[{"data_row":676,"object_id":"CHEBI:3478","object_label":"cefaclor","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefaclor","synonym_count":2} |
| ev-d1671ac1ba60227c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [675] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-630fdce7c7ed319f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cefaclor; data-row positions=[676] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":676,"object_id":"CHEBI:3478","object_label":"cefaclor","other":"(6R,7R)-7-{[(2R)-2-amino-2-phenylacetyl]amino}-3-chloro-8-oxo-5-thia-1-azabicyclo[4.2.0]oct-2-ene-2-carboxylic acid&#124;7beta-{[(2R)-2-amino-2-phenylacetyl]amino}-3-chloro-3,4-didehydrocepham-4-carboxylic acid&#124;CAS:53994-73-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Cefaclor","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-1fb14fc88830db93 | docs/data/mapped_ingredients.csv; CSV lines=[677] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3478","line":677,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3478","preferred_term":"Cefaclor","total_occurrences":"0"}] |
| ev-0a68d3b7eb90f32c | reports/yaml_record_review/Cefaclor.md; &#96;data/ingredients/mapped/Cefaclor.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:38; Completeness:52; Recommended Edits:60 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2ffc44618ad12b0a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[377,1932] | context_only | [{"current_record_sha256":"bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356","finding_id":"SEM:cd80e20ba832e60060bf","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356","finding_id":"SEM:6940b4076a9350553d3b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-609c4e505dadbd38 | data/ingredients/mapped/Cefaclor.yaml; physicochemical_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[675],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3478","line":677,"mapping_status":"MAPPED","ontology_id":"CHEBI:3478","preferred_term":"Cefaclor"}],"identifier":"CHEBI:3478","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3478","ontology_label":"cefaclor","ontology_source":"CHEBI"},"preferred_term":"Cefaclor","sssom_rows":[{"data_row":676,"object_id":"CHEBI:3478","object_label":"cefaclor","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefaclor","synonym_count":2} |
| ev-fa95647a4183e8b3 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-077870be4623f168] | context_only | Predecessor structured review finding f-077870be4623f168 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cefaclor
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cefaclor (data/ingredients/mapped/Cefaclor.yaml)'
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
summary: Per-record structured review for Cefaclor (data/ingredients/mapped/Cefaclor.yaml,
  record-8b79299063e9386c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cefaclor.yaml
    sha256: bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356
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
  - path: reports/yaml_record_review/Cefaclor.md
    sha256: 32d629722cdb7fb4f37a2de7fb48e9243295955545ef523687d597bc58096e92
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8b79299063e9386c
  path: data/ingredients/mapped/Cefaclor.yaml
  label: Cefaclor
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cefaclor.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cefaclor.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cefaclor.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8b79299063e9386c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-9229cb33c9f356ea
  - ev-d1671ac1ba60227c
  - ev-630fdce7c7ed319f
  - ev-1fb14fc88830db93
  - ev-609c4e505dadbd38
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on physicochemical_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-9229cb33c9f356ea
  - ev-2ffc44618ad12b0a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-0a68d3b7eb90f32c
  - ev-2ffc44618ad12b0a
  - ev-fa95647a4183e8b3
evidence:
- evidence_id: ev-9229cb33c9f356ea
  kind: record_content
  reference: data/ingredients/mapped/Cefaclor.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[675],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3478","line":677,"mapping_status":"MAPPED","ontology_id":"CHEBI:3478","preferred_term":"Cefaclor"}],"identifier":"CHEBI:3478","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3478","ontology_label":"cefaclor","ontology_source":"CHEBI"},"preferred_term":"Cefaclor","sssom_rows":[{"data_row":676,"object_id":"CHEBI:3478","object_label":"cefaclor","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefaclor","synonym_count":2}'
  snapshot_sha256: bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356
- evidence_id: ev-d1671ac1ba60227c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [675]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-630fdce7c7ed319f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cefaclor; data-row positions=[676]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":676,"object_id":"CHEBI:3478","object_label":"cefaclor","other":"(6R,7R)-7-{[(2R)-2-amino-2-phenylacetyl]amino}-3-chloro-8-oxo-5-thia-1-azabicyclo[4.2.0]oct-2-ene-2-carboxylic
    acid|7beta-{[(2R)-2-amino-2-phenylacetyl]amino}-3-chloro-3,4-didehydrocepham-4-carboxylic
    acid|CAS:53994-73-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Cefaclor","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1fb14fc88830db93
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[677]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3478","line":677,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3478","preferred_term":"Cefaclor","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0a68d3b7eb90f32c
  kind: prior_review
  reference: reports/yaml_record_review/Cefaclor.md
  locator: '`data/ingredients/mapped/Cefaclor.yaml`:2; Verdict:4; Identity:12; Validation:23;
    Evidence:38; Completeness:52; Recommended Edits:60'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 32d629722cdb7fb4f37a2de7fb48e9243295955545ef523687d597bc58096e92
  quote: "Recommended Edits:\n- Major: either replace `physicochemical_roles.SELECTIVE_AGENT`\
    \ with inspected\n  evidence for cefaclor as a selective agent in this media scope,\
    \ or remove the\n  role, then rerun strict validation, SSSOM QC, aggregate roundtrip,\
    \ and\n  `git diff --check`."
- evidence_id: ev-2ffc44618ad12b0a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[377,1932]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356","finding_id":"SEM:cd80e20ba832e60060bf","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356","finding_id":"SEM:6940b4076a9350553d3b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-609c4e505dadbd38
  kind: record_content
  reference: data/ingredients/mapped/Cefaclor.yaml
  locator: physicochemical_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[675],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3478","line":677,"mapping_status":"MAPPED","ontology_id":"CHEBI:3478","preferred_term":"Cefaclor"}],"identifier":"CHEBI:3478","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3478","ontology_label":"cefaclor","ontology_source":"CHEBI"},"preferred_term":"Cefaclor","sssom_rows":[{"data_row":676,"object_id":"CHEBI:3478","object_label":"cefaclor","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cefaclor","synonym_count":2}'
  snapshot_sha256: bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356
- evidence_id: ev-fa95647a4183e8b3
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-077870be4623f168]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-077870be4623f168 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-b1d98b6a7f5d41a8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-9229cb33c9f356ea
  - ev-d1671ac1ba60227c
  - ev-630fdce7c7ed319f
  - ev-1fb14fc88830db93
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-064109bb0990063b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-0a68d3b7eb90f32c
  - ev-9229cb33c9f356ea
  - ev-2ffc44618ad12b0a
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:19:29Z;
    reviewed SHA-256=bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356;
    current SHA-256=bd2932f909178a265cdcadc548ccc6f0ae944fecb51789b9db2a62df96860356;
    hash_changed=False. Reports=["reports/yaml_record_review/Cefaclor.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI cefaclor
    identity passes, but SELECTIVE_AGENT is only a provisional name-pattern prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0a68d3b7eb90f32c
    - ev-9229cb33c9f356ea
  - name: legacy-native-ids
    value: '["SEM:cd80e20ba832e60060bf","SEM:6940b4076a9350553d3b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9229cb33c9f356ea
    - ev-0a68d3b7eb90f32c
    - ev-2ffc44618ad12b0a
- assessment_id: a-609c4e505dadbd38
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-0a68d3b7eb90f32c
  - ev-609c4e505dadbd38
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0a68d3b7eb90f32c
    - ev-609c4e505dadbd38
findings:
- finding_id: rec-f-077870be4623f168
  issue_key: mim-reconciliation-role-support-8b79299063e9386c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cefaclor'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8b79299063e9386c
  evidence_ids:
  - ev-0a68d3b7eb90f32c
  - ev-609c4e505dadbd38
  - ev-fa95647a4183e8b3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cefaclor.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-077870be4623f168
actions:
- action_id: rec-action-077870be4623f168
  description: 'Reassess prediction-only role support: Cefaclor'
  finding_ids:
  - rec-f-077870be4623f168
  target_ids:
  - record-8b79299063e9386c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cefaclor.yaml
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
