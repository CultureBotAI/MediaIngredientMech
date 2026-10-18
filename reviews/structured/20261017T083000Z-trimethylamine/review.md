# Per-record structured review: Trimethylamine (data/ingredients/mapped/Trimethylamine.yaml)

- Review: 20261017T083000Z-trimethylamine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trimethylamine (data/ingredients/mapped/Trimethylamine.yaml, record-37e38c2c988e53a5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trimethylamine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trimethylamine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-37e38c2c988e53a5 | data/ingredients/mapped/Trimethylamine.yaml | maintained | Trimethylamine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-37e38c2c988e53a5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-37e38c2c988e53a5 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-37e38c2c988e53a5 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-37e38c2c988e53a5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-37e38c2c988e53a5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:39:57Z; reviewed SHA-256=0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f; current SHA-256=0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f; hash_changed=False. Reports=["reports/yaml_record_review/Trimethylamine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity and final SSSOM row pass, but CARBON_SOURCE is provisional in-session LLM evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-37e38c2c988e53a5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e61004026eddb8db: Reassess prediction-only role support: Trimethylamine

major / open / confirmed; issue key: mim-reconciliation-role-support-37e38c2c988e53a5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e61004026eddb8db

Reassess prediction-only role support: Trimethylamine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d69cc03ee25aa2fb | data/ingredients/mapped/Trimethylamine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1996],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18139","line":1998,"mapping_status":"MAPPED","ontology_id":"CHEBI:18139","preferred_term":"Trimethylamine"}],"identifier":"CHEBI:18139","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18139","ontology_label":"trimethylamine","ontology_source":"CHEBI"},"preferred_term":"Trimethylamine","sssom_rows":[{"data_row":2828,"object_id":"CHEBI:18139","object_label":"trimethylamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trimethylamine","synonym_count":7} |
| ev-cf57ae8ea241cdba | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1996] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b80a94ebf6a196c9 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trimethylamine; data-row positions=[2828] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2828,"object_id":"CHEBI:18139","object_label":"trimethylamine","other":"(CH3)3N&#124;N(CH3)3&#124;N,N,N-trimethylamine&#124;N,N-Dimethylmethanamine&#124;NMe3&#124;Trimethylamin&#124;tridimethylaminomethane&#124;CAS:75-50-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Trimethylamine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-5e4f178af4e0c249 | docs/data/mapped_ingredients.csv; CSV lines=[1998] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18139","line":1998,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:18139","preferred_term":"Trimethylamine","total_occurrences":"4"}] |
| ev-996783a54614e041 | reports/yaml_record_review/Trimethylamine.md; &#96;data/ingredients/mapped/Trimethylamine.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:30; Issues:38; Major: &#96;CARBON_SOURCE&#96; is provisional in-session LLM evidence:40; Completeness:57; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8c93cbc35cd3f02b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1310,1685] | context_only | [{"current_record_sha256":"0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f","finding_id":"SEM:47014d2566dd7f7e203a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f","finding_id":"SEM:66ed6cd239b9b830ea44","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-aed019625e8749b1 | data/ingredients/mapped/Trimethylamine.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-88a4ecc515fb4b78 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-e61004026eddb8db] | context_only | Predecessor structured review finding f-e61004026eddb8db in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trimethylamine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trimethylamine (data/ingredients/mapped/Trimethylamine.yaml)'
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
summary: Per-record structured review for Trimethylamine (data/ingredients/mapped/Trimethylamine.yaml,
  record-37e38c2c988e53a5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trimethylamine.yaml
    sha256: 0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f
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
  - path: reports/yaml_record_review/Trimethylamine.md
    sha256: be1efa1fb5887979ef3579bd80d14b956b58162624514c065d411cff55ce79ab
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-37e38c2c988e53a5
  path: data/ingredients/mapped/Trimethylamine.yaml
  label: Trimethylamine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trimethylamine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trimethylamine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trimethylamine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-37e38c2c988e53a5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-37e38c2c988e53a5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-37e38c2c988e53a5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-37e38c2c988e53a5
evidence:
- evidence_id: ev-d69cc03ee25aa2fb
  kind: record_content
  reference: data/ingredients/mapped/Trimethylamine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1996],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18139","line":1998,"mapping_status":"MAPPED","ontology_id":"CHEBI:18139","preferred_term":"Trimethylamine"}],"identifier":"CHEBI:18139","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:18139","ontology_label":"trimethylamine","ontology_source":"CHEBI"},"preferred_term":"Trimethylamine","sssom_rows":[{"data_row":2828,"object_id":"CHEBI:18139","object_label":"trimethylamine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trimethylamine","synonym_count":7}'
  snapshot_sha256: 0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f
- evidence_id: ev-cf57ae8ea241cdba
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1996]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b80a94ebf6a196c9
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trimethylamine; data-row positions=[2828]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2828,"object_id":"CHEBI:18139","object_label":"trimethylamine","other":"(CH3)3N|N(CH3)3|N,N,N-trimethylamine|N,N-Dimethylmethanamine|NMe3|Trimethylamin|tridimethylaminomethane|CAS:75-50-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Trimethylamine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5e4f178af4e0c249
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1998]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18139","line":1998,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:18139","preferred_term":"Trimethylamine","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-996783a54614e041
  kind: prior_review
  reference: reports/yaml_record_review/Trimethylamine.md
  locator: '`data/ingredients/mapped/Trimethylamine.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:30; Issues:38; Major: `CARBON_SOURCE` is provisional in-session
    LLM evidence:40; Completeness:57; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: be1efa1fb5887979ef3579bd80d14b956b58162624514c065d411cff55ce79ab
  quote: "Issues:\n\n\nMajor: `CARBON_SOURCE` is provisional in-session LLM evidence:\n\
    The only role assertion is:\n\n```yaml\nnutritional_roles:\n- role: CARBON_SOURCE\n\
    \  confidence: 0.6\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Assigned by in-session Claude reasoning (no external API)\n\
    \    curator_note: Provisional in-session LLM role assignment; review recommended.\n\
    ```\n\nThe exact CHEBI and CAS identity do not independently curate the carbon-source\n\
    role.\n\nRecommended Edits:\n- Replace the `CARBON_SOURCE` computational prediction\
    \ with curated\n  database/literature evidence, or remove `nutritional_roles`\
    \ until such\n  support is added."
- evidence_id: ev-8c93cbc35cd3f02b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1310,1685]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f","finding_id":"SEM:47014d2566dd7f7e203a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f","finding_id":"SEM:66ed6cd239b9b830ea44","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-aed019625e8749b1
  kind: record_content
  reference: data/ingredients/mapped/Trimethylamine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: 0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f
- evidence_id: ev-88a4ecc515fb4b78
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-e61004026eddb8db]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e61004026eddb8db in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-3669f292ae1d3357
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-37e38c2c988e53a5
  evidence_ids:
  - ev-d69cc03ee25aa2fb
  - ev-cf57ae8ea241cdba
  - ev-b80a94ebf6a196c9
  - ev-5e4f178af4e0c249
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d4f497c62045cac1
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-37e38c2c988e53a5
  evidence_ids:
  - ev-996783a54614e041
  - ev-d69cc03ee25aa2fb
  - ev-8c93cbc35cd3f02b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:39:57Z;
    reviewed SHA-256=0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f;
    current SHA-256=0b2b5972faa7d1596ab3abfea5ffdc4ca08ef008907ff7eb18c4becb35e2a84f;
    hash_changed=False. Reports=["reports/yaml_record_review/Trimethylamine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity and final SSSOM row pass, but CARBON_SOURCE is provisional in-session
    LLM evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-996783a54614e041
    - ev-d69cc03ee25aa2fb
  - name: legacy-native-ids
    value: '["SEM:47014d2566dd7f7e203a","SEM:66ed6cd239b9b830ea44"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d69cc03ee25aa2fb
    - ev-996783a54614e041
    - ev-8c93cbc35cd3f02b
- assessment_id: a-aed019625e8749b1
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-37e38c2c988e53a5
  evidence_ids:
  - ev-996783a54614e041
  - ev-aed019625e8749b1
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-996783a54614e041
    - ev-aed019625e8749b1
findings:
- finding_id: rec-f-e61004026eddb8db
  issue_key: mim-reconciliation-role-support-37e38c2c988e53a5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Trimethylamine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-37e38c2c988e53a5
  evidence_ids:
  - ev-996783a54614e041
  - ev-aed019625e8749b1
  - ev-88a4ecc515fb4b78
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trimethylamine.yaml
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
    finding_id: f-e61004026eddb8db
actions:
- action_id: rec-action-e61004026eddb8db
  description: 'Reassess prediction-only role support: Trimethylamine'
  finding_ids:
  - rec-f-e61004026eddb8db
  target_ids:
  - record-37e38c2c988e53a5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trimethylamine.yaml
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
````
