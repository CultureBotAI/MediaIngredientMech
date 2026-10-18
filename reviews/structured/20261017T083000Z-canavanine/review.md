# Per-record structured review: Canavanine (data/ingredients/mapped/Canavanine.yaml)

- Review: 20261017T083000Z-canavanine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Canavanine (data/ingredients/mapped/Canavanine.yaml, record-af26c70dab7b0731, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Canavanine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Canavanine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-af26c70dab7b0731 | data/ingredients/mapped/Canavanine.yaml | maintained | Canavanine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-af26c70dab7b0731 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-af26c70dab7b0731 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-af26c70dab7b0731 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-af26c70dab7b0731.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-af26c70dab7b0731.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:48:06Z; reviewed SHA-256=4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406; current SHA-256=4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406; hash_changed=False. Reports=["reports/yaml_record_review/Canavanine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-derived CHEBI L-canavanine identity passes, but AMINO_ACID_SOURCE is only a provisional ChEBI-ancestry prediction.

### Historical provisional-role concern

evidence: concern. Targets: record-af26c70dab7b0731.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-fc936e61e2d680e0: Reassess prediction-only role support: Canavanine

major / open / confirmed; issue key: mim-reconciliation-role-support-af26c70dab7b0731.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-fc936e61e2d680e0

Reassess prediction-only role support: Canavanine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-c4a8a890eebbab23 | data/ingredients/mapped/Canavanine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[641],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:609827","line":643,"mapping_status":"MAPPED","ontology_id":"CHEBI:609827","preferred_term":"Canavanine"}],"identifier":"CHEBI:609827","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:609827","ontology_label":"L-canavanine","ontology_source":"CHEBI"},"preferred_term":"Canavanine","sssom_rows":[{"data_row":624,"object_id":"CHEBI:609827","object_label":"L-canavanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Canavanine","synonym_count":1} |
| ev-fd3bd0e8bcb1e947 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [641] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-889dfca2248bf42b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Canavanine; data-row positions=[624] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":624,"object_id":"CHEBI:609827","object_label":"L-canavanine","other":"O-carbamimidamido-L-homoserine&#124;CAS:543-38-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Canavanine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-cf3a93f4763761d3 | docs/data/mapped_ingredients.csv; CSV lines=[643] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:609827","line":643,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:609827","preferred_term":"Canavanine","total_occurrences":"0"}] |
| ev-a25c87e4f1cbb99c | reports/yaml_record_review/Canavanine.md; &#96;data/ingredients/mapped/Canavanine.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:40; Completeness:55; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-71d20f8dbe0dacd1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[352,1764] | context_only | [{"current_record_sha256":"4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406","finding_id":"SEM:4a9ebafe04cbe661fe66","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406","finding_id":"SEM:5375b834e90becf5c7f0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b315e84d56573535 | data/ingredients/mapped/Canavanine.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[641],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:609827","line":643,"mapping_status":"MAPPED","ontology_id":"CHEBI:609827","preferred_term":"Canavanine"}],"identifier":"CHEBI:609827","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:609827","ontology_label":"L-canavanine","ontology_source":"CHEBI"},"preferred_term":"Canavanine","sssom_rows":[{"data_row":624,"object_id":"CHEBI:609827","object_label":"L-canavanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Canavanine","synonym_count":1} |
| ev-a57734eb8521388c | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-fc936e61e2d680e0] | context_only | Predecessor structured review finding f-fc936e61e2d680e0 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-canavanine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Canavanine (data/ingredients/mapped/Canavanine.yaml)'
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
summary: Per-record structured review for Canavanine (data/ingredients/mapped/Canavanine.yaml,
  record-af26c70dab7b0731, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Canavanine.yaml
    sha256: 4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406
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
  - path: reports/yaml_record_review/Canavanine.md
    sha256: 0083e8d127c3728b04c2f93e29d995f3e9f45c81edf5e265753db46d016e14f6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-af26c70dab7b0731
  path: data/ingredients/mapped/Canavanine.yaml
  label: Canavanine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Canavanine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Canavanine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Canavanine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-af26c70dab7b0731
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-c4a8a890eebbab23
  - ev-fd3bd0e8bcb1e947
  - ev-889dfca2248bf42b
  - ev-cf3a93f4763761d3
  - ev-b315e84d56573535
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-c4a8a890eebbab23
  - ev-71d20f8dbe0dacd1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-a25c87e4f1cbb99c
  - ev-71d20f8dbe0dacd1
  - ev-a57734eb8521388c
evidence:
- evidence_id: ev-c4a8a890eebbab23
  kind: record_content
  reference: data/ingredients/mapped/Canavanine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[641],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:609827","line":643,"mapping_status":"MAPPED","ontology_id":"CHEBI:609827","preferred_term":"Canavanine"}],"identifier":"CHEBI:609827","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:609827","ontology_label":"L-canavanine","ontology_source":"CHEBI"},"preferred_term":"Canavanine","sssom_rows":[{"data_row":624,"object_id":"CHEBI:609827","object_label":"L-canavanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Canavanine","synonym_count":1}'
  snapshot_sha256: 4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406
- evidence_id: ev-fd3bd0e8bcb1e947
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [641]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-889dfca2248bf42b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Canavanine; data-row positions=[624]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":624,"object_id":"CHEBI:609827","object_label":"L-canavanine","other":"O-carbamimidamido-L-homoserine|CAS:543-38-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Canavanine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cf3a93f4763761d3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[643]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:609827","line":643,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:609827","preferred_term":"Canavanine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a25c87e4f1cbb99c
  kind: prior_review
  reference: reports/yaml_record_review/Canavanine.md
  locator: '`data/ingredients/mapped/Canavanine.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:40; Completeness:55; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0083e8d127c3728b04c2f93e29d995f3e9f45c81edf5e265753db46d016e14f6
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Canavanine.yaml`, remove\n\
    \  `nutritional_roles.AMINO_ACID_SOURCE` unless a future curator can attach\n\
    \  compound-specific evidence for L-canavanine as an amino acid source in\n  microbial\
    \ media.\n- Regenerate `data/curated/mapped_ingredients.yaml`, docs data, and\
    \ any role\n  exports that consume the aggregate; prove the cleanup with strict\
    \ validation\n  and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-71d20f8dbe0dacd1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[352,1764]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406","finding_id":"SEM:4a9ebafe04cbe661fe66","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406","finding_id":"SEM:5375b834e90becf5c7f0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b315e84d56573535
  kind: record_content
  reference: data/ingredients/mapped/Canavanine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[641],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:609827","line":643,"mapping_status":"MAPPED","ontology_id":"CHEBI:609827","preferred_term":"Canavanine"}],"identifier":"CHEBI:609827","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:609827","ontology_label":"L-canavanine","ontology_source":"CHEBI"},"preferred_term":"Canavanine","sssom_rows":[{"data_row":624,"object_id":"CHEBI:609827","object_label":"L-canavanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Canavanine","synonym_count":1}'
  snapshot_sha256: 4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406
- evidence_id: ev-a57734eb8521388c
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-fc936e61e2d680e0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-fc936e61e2d680e0 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-5461e1c97db940f2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-c4a8a890eebbab23
  - ev-fd3bd0e8bcb1e947
  - ev-889dfca2248bf42b
  - ev-cf3a93f4763761d3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-808c8915924614b2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-a25c87e4f1cbb99c
  - ev-c4a8a890eebbab23
  - ev-71d20f8dbe0dacd1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:48:06Z;
    reviewed SHA-256=4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406;
    current SHA-256=4d210e28bcb4c51311c116ff7b6bac5047bd6e59e18409920af45dc0edf2b406;
    hash_changed=False. Reports=["reports/yaml_record_review/Canavanine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-derived
    CHEBI L-canavanine identity passes, but AMINO_ACID_SOURCE is only a provisional
    ChEBI-ancestry prediction.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a25c87e4f1cbb99c
    - ev-c4a8a890eebbab23
  - name: legacy-native-ids
    value: '["SEM:4a9ebafe04cbe661fe66","SEM:5375b834e90becf5c7f0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-c4a8a890eebbab23
    - ev-a25c87e4f1cbb99c
    - ev-71d20f8dbe0dacd1
- assessment_id: a-b315e84d56573535
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-a25c87e4f1cbb99c
  - ev-b315e84d56573535
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a25c87e4f1cbb99c
    - ev-b315e84d56573535
findings:
- finding_id: rec-f-fc936e61e2d680e0
  issue_key: mim-reconciliation-role-support-af26c70dab7b0731
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Canavanine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-af26c70dab7b0731
  evidence_ids:
  - ev-a25c87e4f1cbb99c
  - ev-b315e84d56573535
  - ev-a57734eb8521388c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Canavanine.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-fc936e61e2d680e0
actions:
- action_id: rec-action-fc936e61e2d680e0
  description: 'Reassess prediction-only role support: Canavanine'
  finding_ids:
  - rec-f-fc936e61e2d680e0
  target_ids:
  - record-af26c70dab7b0731
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Canavanine.yaml
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
