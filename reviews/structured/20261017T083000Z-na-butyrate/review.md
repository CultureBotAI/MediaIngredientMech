# Per-record structured review: Na-butyrate (data/ingredients/mapped/Na-butyrate.yaml)

- Review: 20261017T083000Z-na-butyrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-butyrate (data/ingredients/mapped/Na-butyrate.yaml, record-8dcd93f2a2216afa, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-butyrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-butyrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8dcd93f2a2216afa | data/ingredients/mapped/Na-butyrate.yaml | maintained | Na-butyrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8dcd93f2a2216afa | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8dcd93f2a2216afa | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8dcd93f2a2216afa | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8dcd93f2a2216afa.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8dcd93f2a2216afa.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:50:08Z; reviewed SHA-256=449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb; current SHA-256=449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb; hash_changed=False. Reports=["reports/yaml_record_review/Na-butyrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:64103 sodium butyrate identity, CAS provenance, structure, duplicate merge, and occurrence count pass, but role facets and one final synonym need cleanup.

### Historical provisional-role concern

evidence: concern. Targets: record-8dcd93f2a2216afa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9bfa18769c84a2f9: Reassess prediction-only role support: Na-butyrate

major / open / confirmed; issue key: mim-reconciliation-role-support-8dcd93f2a2216afa.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9bfa18769c84a2f9

Reassess prediction-only role support: Na-butyrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-94f6c426f6496324 | data/ingredients/mapped/Na-butyrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1462],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64103","line":1464,"mapping_status":"MAPPED","ontology_id":"CHEBI:64103","preferred_term":"Na-butyrate"}],"identifier":"CHEBI:64103","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":35,"edge_count":35,"occurrences":35},"occurrence_statistics":{"media_count":35,"total_occurrences":35},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:64103","ontology_label":"sodium butyrate","ontology_source":"CHEBI"},"preferred_term":"Na-butyrate","sssom_rows":[{"data_row":1964,"object_id":"CHEBI:64103","object_label":"sodium butyrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-butyrate","synonym_count":15} |
| ev-333a65ec740052ab | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1462] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cda36f1ea7588f3f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-butyrate; data-row positions=[1964] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1964,"object_id":"CHEBI:64103","object_label":"sodium butyrate","other":"1 M Sodium butyrate&#124;Butanoic acid, sodium salt&#124;Butanoic acid, sodium salt (1:1)&#124;Butyrate sodium&#124;Butyric acid sodium salt&#124;Butyric acid, sodium salt&#124;Sodium n-butyrate&#124;Sodium propanecarboxylate&#124;sodium butanoate&#124;Butyrate (sodium salt)&#124;CAS:156-54-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-butyrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-2029253c79a4ba66 | docs/data/mapped_ingredients.csv; CSV lines=[1464] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:64103","line":1464,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"35","ontology_id":"CHEBI:64103","preferred_term":"Na-butyrate","total_occurrences":"35"}] |
| ev-d7841a68d93adc25 | reports/yaml_record_review/Na-butyrate.md; &#96;data/ingredients/mapped/Na-butyrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9e96698c98bc4414 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[971,1533,2079] | context_only | [{"current_record_sha256":"449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb","finding_id":"SEM:601d24db948b4684247c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb","finding_id":"SEM:972a0ea1524b597af834","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb","finding_id":"SEM:e8ff197168d12dbdb08a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-9069bbf9100944c2 | data/ingredients/mapped/Na-butyrate.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-2c8c7c4713a2a4da | reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml; findings[finding_id=f-9bfa18769c84a2f9] | context_only | Predecessor structured review finding f-9bfa18769c84a2f9 in 20261011T024637Z-mim-reconcile-all-batch-09 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-butyrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-butyrate (data/ingredients/mapped/Na-butyrate.yaml)'
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
summary: Per-record structured review for Na-butyrate (data/ingredients/mapped/Na-butyrate.yaml,
  record-8dcd93f2a2216afa, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-butyrate.yaml
    sha256: 449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb
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
  - path: reports/yaml_record_review/Na-butyrate.md
    sha256: 8a3f4181449d3feb6fdabacc56bc813d3955b0e710fe3c97e19b5c476616f4af
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8dcd93f2a2216afa
  path: data/ingredients/mapped/Na-butyrate.yaml
  label: Na-butyrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-butyrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-butyrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-butyrate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8dcd93f2a2216afa
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8dcd93f2a2216afa
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-8dcd93f2a2216afa
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8dcd93f2a2216afa
evidence:
- evidence_id: ev-94f6c426f6496324
  kind: record_content
  reference: data/ingredients/mapped/Na-butyrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1462],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:64103","line":1464,"mapping_status":"MAPPED","ontology_id":"CHEBI:64103","preferred_term":"Na-butyrate"}],"identifier":"CHEBI:64103","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":35,"edge_count":35,"occurrences":35},"occurrence_statistics":{"media_count":35,"total_occurrences":35},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:64103","ontology_label":"sodium
    butyrate","ontology_source":"CHEBI"},"preferred_term":"Na-butyrate","sssom_rows":[{"data_row":1964,"object_id":"CHEBI:64103","object_label":"sodium
    butyrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-butyrate","synonym_count":15}'
  snapshot_sha256: 449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb
- evidence_id: ev-333a65ec740052ab
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1462]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cda36f1ea7588f3f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-butyrate; data-row positions=[1964]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1964,"object_id":"CHEBI:64103","object_label":"sodium
    butyrate","other":"1 M Sodium butyrate|Butanoic acid, sodium salt|Butanoic acid,
    sodium salt (1:1)|Butyrate sodium|Butyric acid sodium salt|Butyric acid, sodium
    salt|Sodium n-butyrate|Sodium propanecarboxylate|sodium butanoate|Butyrate (sodium
    salt)|CAS:156-54-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-butyrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2029253c79a4ba66
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1464]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:64103","line":1464,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"35","ontology_id":"CHEBI:64103","preferred_term":"Na-butyrate","total_occurrences":"35"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d7841a68d93adc25
  kind: prior_review
  reference: reports/yaml_record_review/Na-butyrate.md
  locator: '`data/ingredients/mapped/Na-butyrate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8a3f4181449d3feb6fdabacc56bc813d3955b0e710fe3c97e19b5c476616f4af
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Na-butyrate.yaml`,\
    \ either remove the\n  `CARBON_SOURCE` and `ENERGY_SOURCE` facets or replace the\
    \ computational\n  placeholders with source-backed evidence from maintained occurrence,\n\
    \  role-text, or literature inputs. Rerun strict validation after the role facet\n\
    \  change.\n- Major: demote or remove `1 M Sodium butyrate` from the publishable\
    \ exact\n  synonym set, then rebuild final SSSOM and re-run final SSSOM validation\
    \ plus\n  product label validation."
- evidence_id: ev-9e96698c98bc4414
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[971,1533,2079]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb","finding_id":"SEM:601d24db948b4684247c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb","finding_id":"SEM:972a0ea1524b597af834","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb","finding_id":"SEM:e8ff197168d12dbdb08a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-9069bbf9100944c2
  kind: record_content
  reference: data/ingredients/mapped/Na-butyrate.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb
- evidence_id: ev-2c8c7c4713a2a4da
  kind: prior_review
  reference: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
  locator: findings[finding_id=f-9bfa18769c84a2f9]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9bfa18769c84a2f9 in 20261011T024637Z-mim-reconcile-all-batch-09
  snapshot_sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
assessments:
- assessment_id: a-967de3dcb5db386b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8dcd93f2a2216afa
  evidence_ids:
  - ev-94f6c426f6496324
  - ev-333a65ec740052ab
  - ev-cda36f1ea7588f3f
  - ev-2029253c79a4ba66
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0f3c13588725a183
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8dcd93f2a2216afa
  evidence_ids:
  - ev-d7841a68d93adc25
  - ev-94f6c426f6496324
  - ev-9e96698c98bc4414
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:50:08Z;
    reviewed SHA-256=449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb;
    current SHA-256=449afed4f762a76adcda0f2dbfd14844f8726ef4bc1f579dfb2135b495f0e2fb;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-butyrate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:64103
    sodium butyrate identity, CAS provenance, structure, duplicate merge, and occurrence
    count pass, but role facets and one final synonym need cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d7841a68d93adc25
    - ev-94f6c426f6496324
  - name: legacy-native-ids
    value: '["SEM:601d24db948b4684247c","SEM:972a0ea1524b597af834","SEM:e8ff197168d12dbdb08a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-94f6c426f6496324
    - ev-d7841a68d93adc25
    - ev-9e96698c98bc4414
- assessment_id: a-9069bbf9100944c2
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8dcd93f2a2216afa
  evidence_ids:
  - ev-d7841a68d93adc25
  - ev-9069bbf9100944c2
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d7841a68d93adc25
    - ev-9069bbf9100944c2
findings:
- finding_id: rec-f-9bfa18769c84a2f9
  issue_key: mim-reconciliation-role-support-8dcd93f2a2216afa
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Na-butyrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8dcd93f2a2216afa
  evidence_ids:
  - ev-d7841a68d93adc25
  - ev-9069bbf9100944c2
  - ev-2c8c7c4713a2a4da
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-butyrate.yaml
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
    review_id: 20261011T024637Z-mim-reconcile-all-batch-09
    finding_id: f-9bfa18769c84a2f9
actions:
- action_id: rec-action-9bfa18769c84a2f9
  description: 'Reassess prediction-only role support: Na-butyrate'
  finding_ids:
  - rec-f-9bfa18769c84a2f9
  target_ids:
  - record-8dcd93f2a2216afa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-butyrate.yaml
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
