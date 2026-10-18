# Per-record structured review: Gluconic_Acid (data/ingredients/mapped/Gluconic_Acid.yaml)

- Review: 20261017T083000Z-gluconic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Gluconic_Acid (data/ingredients/mapped/Gluconic_Acid.yaml, record-49566380546892e1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Gluconic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Gluconic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-49566380546892e1 | data/ingredients/mapped/Gluconic_Acid.yaml | maintained | Gluconic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-49566380546892e1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-49566380546892e1 | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-49566380546892e1 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-49566380546892e1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-49566380546892e1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:44:41Z; reviewed SHA-256=c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412; current SHA-256=c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412; hash_changed=False. Reports=["reports/yaml_record_review/Gluconic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact gluconic acid identity and final SSSOM row pass, but CARBON_SOURCE and ENERGY_SOURCE are computational.

### Historical provisional-role concern

evidence: concern. Targets: record-49566380546892e1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c9bceebc039693fd: Reassess prediction-only role support: Gluconic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-49566380546892e1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c9bceebc039693fd

Reassess prediction-only role support: Gluconic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-85654d675303bc38 | data/ingredients/mapped/Gluconic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1057],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:24266","line":1059,"mapping_status":"MAPPED","ontology_id":"CHEBI:24266","preferred_term":"Gluconic acid"}],"identifier":"CHEBI:24266","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:24266","ontology_label":"gluconic acid","ontology_source":"CHEBI"},"preferred_term":"Gluconic acid","sssom_rows":[{"data_row":1305,"object_id":"CHEBI:24266","object_label":"gluconic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gluconic_Acid","synonym_count":0} |
| ev-6b8bbc0f7718887a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1057] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-cacb7554feaf8e26 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Gluconic_Acid; data-row positions=[1305] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1305,"object_id":"CHEBI:24266","object_label":"gluconic acid","other":"CAS:526-95-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Gluconic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-8e47d45415aa3ef8 | docs/data/mapped_ingredients.csv; CSV lines=[1059] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:24266","line":1059,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:24266","preferred_term":"Gluconic acid","total_occurrences":"2"}] |
| ev-df75ef97142602bf | reports/yaml_record_review/Gluconic_Acid.md; &#96;data/ingredients/mapped/Gluconic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:33; Completeness:54; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ef201303e766aa81 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[664,1833,2085] | context_only | [{"current_record_sha256":"c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412","finding_id":"SEM:c4ec9897718c43728121","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412","finding_id":"SEM:68cbebb3dbe4ef2db62b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412","finding_id":"SEM:2d069f2ac443a535ed6d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-d173a50c63ea831d | data/ingredients/mapped/Gluconic_Acid.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-47e0425c400a1d40 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-c9bceebc039693fd] | context_only | Predecessor structured review finding f-c9bceebc039693fd in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-gluconic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Gluconic_Acid (data/ingredients/mapped/Gluconic_Acid.yaml)'
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
summary: Per-record structured review for Gluconic_Acid (data/ingredients/mapped/Gluconic_Acid.yaml,
  record-49566380546892e1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Gluconic_Acid.yaml
    sha256: c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Gluconic_Acid.md
    sha256: 6ba2ee657676eb3efe53ee476f78c6af302771ca3aeaf84bcf5e4cd405c23291
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-49566380546892e1
  path: data/ingredients/mapped/Gluconic_Acid.yaml
  label: Gluconic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gluconic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Gluconic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Gluconic_Acid.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-49566380546892e1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-49566380546892e1
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-49566380546892e1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-49566380546892e1
evidence:
- evidence_id: ev-85654d675303bc38
  kind: record_content
  reference: data/ingredients/mapped/Gluconic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1057],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:24266","line":1059,"mapping_status":"MAPPED","ontology_id":"CHEBI:24266","preferred_term":"Gluconic
    acid"}],"identifier":"CHEBI:24266","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:24266","ontology_label":"gluconic
    acid","ontology_source":"CHEBI"},"preferred_term":"Gluconic acid","sssom_rows":[{"data_row":1305,"object_id":"CHEBI:24266","object_label":"gluconic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gluconic_Acid","synonym_count":0}'
  snapshot_sha256: c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412
- evidence_id: ev-6b8bbc0f7718887a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1057]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-cacb7554feaf8e26
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Gluconic_Acid; data-row positions=[1305]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1305,"object_id":"CHEBI:24266","object_label":"gluconic
    acid","other":"CAS:526-95-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Gluconic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8e47d45415aa3ef8
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1059]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:24266","line":1059,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:24266","preferred_term":"Gluconic
    acid","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-df75ef97142602bf
  kind: prior_review
  reference: reports/yaml_record_review/Gluconic_Acid.md
  locator: '`data/ingredients/mapped/Gluconic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:33; Completeness:54; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6ba2ee657676eb3efe53ee476f78c6af302771ca3aeaf84bcf5e4cd405c23291
  quote: "Recommended Edits:\n- Major: replace `CARBON_SOURCE` and `ENERGY_SOURCE`\
    \ with source-backed\n  evidence or remove the roles, then rerun strict validation."
- evidence_id: ev-ef201303e766aa81
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[664,1833,2085]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412","finding_id":"SEM:c4ec9897718c43728121","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412","finding_id":"SEM:68cbebb3dbe4ef2db62b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412","finding_id":"SEM:2d069f2ac443a535ed6d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-d173a50c63ea831d
  kind: record_content
  reference: data/ingredients/mapped/Gluconic_Acid.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412
- evidence_id: ev-47e0425c400a1d40
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-c9bceebc039693fd]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c9bceebc039693fd in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-e2062d6440020040
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-49566380546892e1
  evidence_ids:
  - ev-85654d675303bc38
  - ev-6b8bbc0f7718887a
  - ev-cacb7554feaf8e26
  - ev-8e47d45415aa3ef8
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d002717517fe1a30
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-49566380546892e1
  evidence_ids:
  - ev-df75ef97142602bf
  - ev-85654d675303bc38
  - ev-ef201303e766aa81
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:44:41Z;
    reviewed SHA-256=c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412;
    current SHA-256=c5d8f1517e07217d02cbc5f9d0b49f3b5ab518a0850a273f865a2ee8e88a7412;
    hash_changed=False. Reports=["reports/yaml_record_review/Gluconic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact gluconic
    acid identity and final SSSOM row pass, but CARBON_SOURCE and ENERGY_SOURCE are
    computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-df75ef97142602bf
    - ev-85654d675303bc38
  - name: legacy-native-ids
    value: '["SEM:c4ec9897718c43728121","SEM:68cbebb3dbe4ef2db62b","SEM:2d069f2ac443a535ed6d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-85654d675303bc38
    - ev-df75ef97142602bf
    - ev-ef201303e766aa81
- assessment_id: a-d173a50c63ea831d
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-49566380546892e1
  evidence_ids:
  - ev-df75ef97142602bf
  - ev-d173a50c63ea831d
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-df75ef97142602bf
    - ev-d173a50c63ea831d
findings:
- finding_id: rec-f-c9bceebc039693fd
  issue_key: mim-reconciliation-role-support-49566380546892e1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Gluconic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-49566380546892e1
  evidence_ids:
  - ev-df75ef97142602bf
  - ev-d173a50c63ea831d
  - ev-47e0425c400a1d40
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gluconic_Acid.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-c9bceebc039693fd
actions:
- action_id: rec-action-c9bceebc039693fd
  description: 'Reassess prediction-only role support: Gluconic acid'
  finding_ids:
  - rec-f-c9bceebc039693fd
  target_ids:
  - record-49566380546892e1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gluconic_Acid.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
