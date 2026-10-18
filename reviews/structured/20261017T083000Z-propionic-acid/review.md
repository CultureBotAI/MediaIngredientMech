# Per-record structured review: Propionic_Acid (data/ingredients/mapped/Propionic_Acid.yaml)

- Review: 20261017T083000Z-propionic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Propionic_Acid (data/ingredients/mapped/Propionic_Acid.yaml, record-43c57f3514ddc0c6, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Propionic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Propionic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-43c57f3514ddc0c6 | data/ingredients/mapped/Propionic_Acid.yaml | maintained | Propionic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-43c57f3514ddc0c6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-43c57f3514ddc0c6 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-43c57f3514ddc0c6 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-43c57f3514ddc0c6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-43c57f3514ddc0c6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:43:30Z; reviewed SHA-256=692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7; current SHA-256=692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7; hash_changed=False. Reports=["reports/yaml_record_review/Propionic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:30768 propionic acid identity passes, but ENERGY_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-43c57f3514ddc0c6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-e7ae2f6b370f7bae: Reassess prediction-only role support: Propionic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-43c57f3514ddc0c6.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-e7ae2f6b370f7bae

Reassess prediction-only role support: Propionic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bdfe3ab027a699f4 | data/ingredients/mapped/Propionic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1708],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30768","line":1710,"mapping_status":"MAPPED","ontology_id":"CHEBI:30768","preferred_term":"Propionic acid"}],"identifier":"CHEBI:30768","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":37,"edge_count":37,"occurrences":37},"occurrence_statistics":{"media_count":37,"total_occurrences":37},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30768","ontology_label":"propionic acid","ontology_source":"CHEBI"},"preferred_term":"Propionic acid","sssom_rows":[{"data_row":2353,"object_id":"CHEBI:30768","object_label":"propionic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Propionic_Acid","synonym_count":14} |
| ev-2165ded31c72ad89 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1708] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-78e7ead5609534bc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Propionic_Acid; data-row positions=[2353] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2353,"object_id":"CHEBI:30768","object_label":"propionic acid","other":"CH3-CH2-COOH&#124;PROPANOIC ACID&#124;Propionsaeure&#124;acide propanoique&#124;acide propionique&#124;carboxyethane&#124;ethanecarboxylic acid&#124;ethylformic acid&#124;metacetonic acid&#124;methylacetic acid&#124;propioic acid&#124;propoic acid&#124;pseudoacetic acid&#124;CAS:79-09-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Propionic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-c1695668e3183a8a | docs/data/mapped_ingredients.csv; CSV lines=[1710] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:30768","line":1710,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"37","ontology_id":"CHEBI:30768","preferred_term":"Propionic acid","total_occurrences":"37"}] |
| ev-26ec6db141001183 | reports/yaml_record_review/Propionic_Acid.md; &#96;data/ingredients/mapped/Propionic_Acid.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0e7a8b4b59ea9e08 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1143,1660] | context_only | [{"current_record_sha256":"692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7","finding_id":"SEM:66a165fd204e122aa07e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7","finding_id":"SEM:61825b50e6a431697850","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-382df2e12b9acfcf | data/ingredients/mapped/Propionic_Acid.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-8834199bbf137924 | reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml; findings[finding_id=f-e7ae2f6b370f7bae] | context_only | Predecessor structured review finding f-e7ae2f6b370f7bae in 20261011T024638Z-mim-reconcile-all-batch-10 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-propionic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Propionic_Acid (data/ingredients/mapped/Propionic_Acid.yaml)'
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
summary: Per-record structured review for Propionic_Acid (data/ingredients/mapped/Propionic_Acid.yaml,
  record-43c57f3514ddc0c6, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Propionic_Acid.yaml
    sha256: 692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
    sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
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
  - path: reports/yaml_record_review/Propionic_Acid.md
    sha256: 0afc8e8a2e2f5911b78f9b0e08c5ce6b574dd76920bc57fc79e3f66b6741e7ba
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-43c57f3514ddc0c6
  path: data/ingredients/mapped/Propionic_Acid.yaml
  label: Propionic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Propionic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Propionic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Propionic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-43c57f3514ddc0c6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-43c57f3514ddc0c6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-43c57f3514ddc0c6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-10
    and semantic review dispositions on HEAD.
  target_ids:
  - record-43c57f3514ddc0c6
evidence:
- evidence_id: ev-bdfe3ab027a699f4
  kind: record_content
  reference: data/ingredients/mapped/Propionic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1708],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:30768","line":1710,"mapping_status":"MAPPED","ontology_id":"CHEBI:30768","preferred_term":"Propionic
    acid"}],"identifier":"CHEBI:30768","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":37,"edge_count":37,"occurrences":37},"occurrence_statistics":{"media_count":37,"total_occurrences":37},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:30768","ontology_label":"propionic
    acid","ontology_source":"CHEBI"},"preferred_term":"Propionic acid","sssom_rows":[{"data_row":2353,"object_id":"CHEBI:30768","object_label":"propionic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Propionic_Acid","synonym_count":14}'
  snapshot_sha256: 692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7
- evidence_id: ev-2165ded31c72ad89
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1708]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-78e7ead5609534bc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Propionic_Acid; data-row positions=[2353]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2353,"object_id":"CHEBI:30768","object_label":"propionic
    acid","other":"CH3-CH2-COOH|PROPANOIC ACID|Propionsaeure|acide propanoique|acide
    propionique|carboxyethane|ethanecarboxylic acid|ethylformic acid|metacetonic acid|methylacetic
    acid|propioic acid|propoic acid|pseudoacetic acid|CAS:79-09-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Propionic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c1695668e3183a8a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1710]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:30768","line":1710,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"37","ontology_id":"CHEBI:30768","preferred_term":"Propionic
    acid","total_occurrences":"37"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-26ec6db141001183
  kind: prior_review
  reference: reports/yaml_record_review/Propionic_Acid.md
  locator: '`data/ingredients/mapped/Propionic_Acid.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0afc8e8a2e2f5911b78f9b0e08c5ce6b574dd76920bc57fc79e3f66b6741e7ba
- evidence_id: ev-0e7a8b4b59ea9e08
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1143,1660]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7","finding_id":"SEM:66a165fd204e122aa07e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7","finding_id":"SEM:61825b50e6a431697850","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-382df2e12b9acfcf
  kind: record_content
  reference: data/ingredients/mapped/Propionic_Acid.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7
- evidence_id: ev-8834199bbf137924
  kind: prior_review
  reference: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-10/review.yaml
  locator: findings[finding_id=f-e7ae2f6b370f7bae]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-e7ae2f6b370f7bae in 20261011T024638Z-mim-reconcile-all-batch-10
  snapshot_sha256: 8c3aa2fca1269d1dbbf6117e85dea5b0de5047a8505841641245bd7ee99b936d
assessments:
- assessment_id: a-c7dd1240b734f034
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-43c57f3514ddc0c6
  evidence_ids:
  - ev-bdfe3ab027a699f4
  - ev-2165ded31c72ad89
  - ev-78e7ead5609534bc
  - ev-c1695668e3183a8a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-03a5f671e843a4aa
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43c57f3514ddc0c6
  evidence_ids:
  - ev-26ec6db141001183
  - ev-bdfe3ab027a699f4
  - ev-0e7a8b4b59ea9e08
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T10:43:30Z;
    reviewed SHA-256=692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7;
    current SHA-256=692dd05a261b65d660874ef1b910d609c4b4bcb9c41da730de02ae9a00d8cdc7;
    hash_changed=False. Reports=["reports/yaml_record_review/Propionic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:30768 propionic acid identity passes, but ENERGY_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-26ec6db141001183
    - ev-bdfe3ab027a699f4
  - name: legacy-native-ids
    value: '["SEM:66a165fd204e122aa07e","SEM:61825b50e6a431697850"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bdfe3ab027a699f4
    - ev-26ec6db141001183
    - ev-0e7a8b4b59ea9e08
- assessment_id: a-382df2e12b9acfcf
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-43c57f3514ddc0c6
  evidence_ids:
  - ev-26ec6db141001183
  - ev-382df2e12b9acfcf
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-26ec6db141001183
    - ev-382df2e12b9acfcf
findings:
- finding_id: rec-f-e7ae2f6b370f7bae
  issue_key: mim-reconciliation-role-support-43c57f3514ddc0c6
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Propionic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-43c57f3514ddc0c6
  evidence_ids:
  - ev-26ec6db141001183
  - ev-382df2e12b9acfcf
  - ev-8834199bbf137924
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Propionic_Acid.yaml
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
    review_id: 20261011T024638Z-mim-reconcile-all-batch-10
    finding_id: f-e7ae2f6b370f7bae
actions:
- action_id: rec-action-e7ae2f6b370f7bae
  description: 'Reassess prediction-only role support: Propionic acid'
  finding_ids:
  - rec-f-e7ae2f6b370f7bae
  target_ids:
  - record-43c57f3514ddc0c6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Propionic_Acid.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-10.
```
