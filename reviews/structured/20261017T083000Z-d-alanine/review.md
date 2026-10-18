# Per-record structured review: D-Alanine (data/ingredients/mapped/D-Alanine.yaml)

- Review: 20261017T083000Z-d-alanine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Alanine (data/ingredients/mapped/D-Alanine.yaml, record-8f6274d1b3a7635f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Alanine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Alanine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8f6274d1b3a7635f | data/ingredients/mapped/D-Alanine.yaml | maintained | D-Alanine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8f6274d1b3a7635f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8f6274d1b3a7635f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8f6274d1b3a7635f | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8f6274d1b3a7635f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8f6274d1b3a7635f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:09:03Z; reviewed SHA-256=339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605; current SHA-256=339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605; hash_changed=False. Reports=["reports/yaml_record_review/D-Alanine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, structure fields, 2/2 count, and final SSSOM row pass, but the amino-acid role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-8f6274d1b3a7635f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-df76804d00d9f88c: Reassess prediction-only role support: D-Alanine

major / open / confirmed; issue key: mim-reconciliation-role-support-8f6274d1b3a7635f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-df76804d00d9f88c

Reassess prediction-only role support: D-Alanine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0d50fa2c07fdb686 | data/ingredients/mapped/D-Alanine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[805],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15570","line":807,"mapping_status":"MAPPED","ontology_id":"CHEBI:15570","preferred_term":"D-Alanine"}],"identifier":"CHEBI:15570","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15570","ontology_label":"D-alanine","ontology_source":"CHEBI"},"preferred_term":"D-Alanine","sssom_rows":[{"data_row":876,"object_id":"CHEBI:15570","object_label":"D-alanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Alanine","synonym_count":0} |
| ev-bdc65ff401028c3c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [805] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a18487a84e6f31db | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Alanine; data-row positions=[876] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":876,"object_id":"CHEBI:15570","object_label":"D-alanine","other":"CAS:338-69-2","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Alanine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-d93a7023db543c99 | docs/data/mapped_ingredients.csv; CSV lines=[807] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15570","line":807,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:15570","preferred_term":"D-Alanine","total_occurrences":"2"}] |
| ev-2a4147f2a0a30d47 | reports/yaml_record_review/D-Alanine.md; &#96;data/ingredients/mapped/D-Alanine.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:43; Completeness:59; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6062cc4a1c0b6435 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[462,1913] | context_only | [{"current_record_sha256":"339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605","finding_id":"SEM:10354f7e487cc477b896","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605","finding_id":"SEM:fdcfbc1555e838b2e301","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d6b7e838bb8cf384 | data/ingredients/mapped/D-Alanine.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-c10c2abcc173f69f | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-df76804d00d9f88c] | context_only | Predecessor structured review finding f-df76804d00d9f88c in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-alanine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Alanine (data/ingredients/mapped/D-Alanine.yaml)'
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
summary: Per-record structured review for D-Alanine (data/ingredients/mapped/D-Alanine.yaml,
  record-8f6274d1b3a7635f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Alanine.yaml
    sha256: 339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-Alanine.md
    sha256: a7ab9fc65ff8fc0bae2836cbd9474a22e39c1ef86c4a8f2c64928c1accfbb147
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8f6274d1b3a7635f
  path: data/ingredients/mapped/D-Alanine.yaml
  label: D-Alanine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Alanine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Alanine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Alanine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8f6274d1b3a7635f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8f6274d1b3a7635f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8f6274d1b3a7635f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8f6274d1b3a7635f
evidence:
- evidence_id: ev-0d50fa2c07fdb686
  kind: record_content
  reference: data/ingredients/mapped/D-Alanine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[805],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15570","line":807,"mapping_status":"MAPPED","ontology_id":"CHEBI:15570","preferred_term":"D-Alanine"}],"identifier":"CHEBI:15570","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15570","ontology_label":"D-alanine","ontology_source":"CHEBI"},"preferred_term":"D-Alanine","sssom_rows":[{"data_row":876,"object_id":"CHEBI:15570","object_label":"D-alanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Alanine","synonym_count":0}'
  snapshot_sha256: 339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605
- evidence_id: ev-bdc65ff401028c3c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [805]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a18487a84e6f31db
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Alanine; data-row positions=[876]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":876,"object_id":"CHEBI:15570","object_label":"D-alanine","other":"CAS:338-69-2","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Alanine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d93a7023db543c99
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[807]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15570","line":807,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:15570","preferred_term":"D-Alanine","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2a4147f2a0a30d47
  kind: prior_review
  reference: reports/yaml_record_review/D-Alanine.md
  locator: '`data/ingredients/mapped/D-Alanine.yaml`:2; Verdict:4; Identity:11; Validation:24;
    Evidence:43; Completeness:59; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a7ab9fc65ff8fc0bae2836cbd9474a22e39c1ef86c4a8f2c64928c1accfbb147
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Alanine.yaml`, either\
    \ replace the computational\n  `AMINO_ACID_SOURCE` evidence with direct CultureBotHT\
    \ or source-backed\n  media-role evidence for this ingredient, or remove the role\
    \ facet; then rerun\n  strict validation and the final SSSOM build."
- evidence_id: ev-6062cc4a1c0b6435
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[462,1913]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605","finding_id":"SEM:10354f7e487cc477b896","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605","finding_id":"SEM:fdcfbc1555e838b2e301","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d6b7e838bb8cf384
  kind: record_content
  reference: data/ingredients/mapped/D-Alanine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605
- evidence_id: ev-c10c2abcc173f69f
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-df76804d00d9f88c]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-df76804d00d9f88c in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-ab474afcfe8b5378
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8f6274d1b3a7635f
  evidence_ids:
  - ev-0d50fa2c07fdb686
  - ev-bdc65ff401028c3c
  - ev-a18487a84e6f31db
  - ev-d93a7023db543c99
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-5e16db01a410b185
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f6274d1b3a7635f
  evidence_ids:
  - ev-2a4147f2a0a30d47
  - ev-0d50fa2c07fdb686
  - ev-6062cc4a1c0b6435
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:09:03Z;
    reviewed SHA-256=339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605;
    current SHA-256=339e66c0d8cd147d235511dc025429b213cd70036bc987966c5f923ac02a1605;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Alanine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, structure fields, 2/2 count, and final SSSOM row pass, but the amino-acid
    role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2a4147f2a0a30d47
    - ev-0d50fa2c07fdb686
  - name: legacy-native-ids
    value: '["SEM:10354f7e487cc477b896","SEM:fdcfbc1555e838b2e301"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0d50fa2c07fdb686
    - ev-2a4147f2a0a30d47
    - ev-6062cc4a1c0b6435
- assessment_id: a-d6b7e838bb8cf384
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8f6274d1b3a7635f
  evidence_ids:
  - ev-2a4147f2a0a30d47
  - ev-d6b7e838bb8cf384
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2a4147f2a0a30d47
    - ev-d6b7e838bb8cf384
findings:
- finding_id: rec-f-df76804d00d9f88c
  issue_key: mim-reconciliation-role-support-8f6274d1b3a7635f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Alanine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8f6274d1b3a7635f
  evidence_ids:
  - ev-2a4147f2a0a30d47
  - ev-d6b7e838bb8cf384
  - ev-c10c2abcc173f69f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Alanine.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-df76804d00d9f88c
actions:
- action_id: rec-action-df76804d00d9f88c
  description: 'Reassess prediction-only role support: D-Alanine'
  finding_ids:
  - rec-f-df76804d00d9f88c
  target_ids:
  - record-8f6274d1b3a7635f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Alanine.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
