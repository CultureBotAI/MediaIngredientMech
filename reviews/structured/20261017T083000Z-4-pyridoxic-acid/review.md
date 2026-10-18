# Per-record structured review: 4-Pyridoxic_Acid (data/ingredients/mapped/4-Pyridoxic_Acid.yaml)

- Review: 20261017T083000Z-4-pyridoxic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 4-Pyridoxic_Acid (data/ingredients/mapped/4-Pyridoxic_Acid.yaml, record-6ad3cf8f490598d1, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/4-Pyridoxic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/4-Pyridoxic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6ad3cf8f490598d1 | data/ingredients/mapped/4-Pyridoxic_Acid.yaml | maintained | 4-Pyridoxic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6ad3cf8f490598d1 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6ad3cf8f490598d1 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6ad3cf8f490598d1 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6ad3cf8f490598d1.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6ad3cf8f490598d1.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:18:15Z; reviewed SHA-256=869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3; current SHA-256=869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3; hash_changed=False. Reports=["reports/yaml_record_review/4-Pyridoxic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: CHEBI identity and chemistry pass, but the provisional VITAMIN_SOURCE role is only inferred from ChEBI ancestry and remains unreviewed on a vitamin B6 catabolite.

### Historical provisional-role concern

evidence: concern. Targets: record-6ad3cf8f490598d1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5811a740aa6bd953: Reassess prediction-only role support: 4-Pyridoxic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-6ad3cf8f490598d1.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5811a740aa6bd953

Reassess prediction-only role support: 4-Pyridoxic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cd49cc5a160f0f6a | data/ingredients/mapped/4-Pyridoxic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[387],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17405","line":389,"mapping_status":"MAPPED","ontology_id":"CHEBI:17405","preferred_term":"4-Pyridoxic acid"}],"identifier":"CHEBI:17405","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17405","ontology_label":"4-pyridoxic acid","ontology_source":"CHEBI"},"preferred_term":"4-Pyridoxic acid","sssom_rows":[{"data_row":189,"object_id":"CHEBI:17405","object_label":"4-pyridoxic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Pyridoxic_Acid","synonym_count":1} |
| ev-a8d9b2b33a8386aa | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [387] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-507f789f1f73e687 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:4-Pyridoxic_Acid; data-row positions=[189] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":189,"object_id":"CHEBI:17405","object_label":"4-pyridoxic acid","other":"3-hydroxy-5-(hydroxymethyl)-2-methylpyridine-4-carboxylic acid&#124;CAS:82-82-6","predicate_id":"skos:exactMatch","subject_id":"MIM:4-Pyridoxic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-3be0edfed5ae0597 | docs/data/mapped_ingredients.csv; CSV lines=[389] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17405","line":389,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17405","preferred_term":"4-Pyridoxic acid","total_occurrences":"0"}] |
| ev-a640e1b61ac1b816 | reports/yaml_record_review/4-Pyridoxic_Acid.md; &#96;data/ingredients/mapped/4-Pyridoxic_Acid.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:35; Completeness:57; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-1949bbdae1762927 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[149,2089] | context_only | [{"current_record_sha256":"869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3","finding_id":"SEM:d011aeb4740676006aa7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3","finding_id":"SEM:6ad5ed969f55efb33700","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0e7ea150801e578e | data/ingredients/mapped/4-Pyridoxic_Acid.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[387],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17405","line":389,"mapping_status":"MAPPED","ontology_id":"CHEBI:17405","preferred_term":"4-Pyridoxic acid"}],"identifier":"CHEBI:17405","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17405","ontology_label":"4-pyridoxic acid","ontology_source":"CHEBI"},"preferred_term":"4-Pyridoxic acid","sssom_rows":[{"data_row":189,"object_id":"CHEBI:17405","object_label":"4-pyridoxic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Pyridoxic_Acid","synonym_count":1} |
| ev-183cc8f521686e2a | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-5811a740aa6bd953] | context_only | Predecessor structured review finding f-5811a740aa6bd953 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-4-pyridoxic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 4-Pyridoxic_Acid (data/ingredients/mapped/4-Pyridoxic_Acid.yaml)'
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
summary: Per-record structured review for 4-Pyridoxic_Acid (data/ingredients/mapped/4-Pyridoxic_Acid.yaml,
  record-6ad3cf8f490598d1, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
    sha256: 869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/4-Pyridoxic_Acid.md
    sha256: 23a391c770004eccced4c3beb103ee332a5a9ce6ee48a652f77560d3f7cc5053
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6ad3cf8f490598d1
  path: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
  label: 4-Pyridoxic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/4-Pyridoxic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/4-Pyridoxic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6ad3cf8f490598d1
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-cd49cc5a160f0f6a
  - ev-a8d9b2b33a8386aa
  - ev-507f789f1f73e687
  - ev-3be0edfed5ae0597
  - ev-0e7ea150801e578e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-cd49cc5a160f0f6a
  - ev-1949bbdae1762927
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-a640e1b61ac1b816
  - ev-1949bbdae1762927
  - ev-183cc8f521686e2a
evidence:
- evidence_id: ev-cd49cc5a160f0f6a
  kind: record_content
  reference: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[387],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17405","line":389,"mapping_status":"MAPPED","ontology_id":"CHEBI:17405","preferred_term":"4-Pyridoxic
    acid"}],"identifier":"CHEBI:17405","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17405","ontology_label":"4-pyridoxic
    acid","ontology_source":"CHEBI"},"preferred_term":"4-Pyridoxic acid","sssom_rows":[{"data_row":189,"object_id":"CHEBI:17405","object_label":"4-pyridoxic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Pyridoxic_Acid","synonym_count":1}'
  snapshot_sha256: 869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3
- evidence_id: ev-a8d9b2b33a8386aa
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [387]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-507f789f1f73e687
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:4-Pyridoxic_Acid; data-row positions=[189]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":189,"object_id":"CHEBI:17405","object_label":"4-pyridoxic
    acid","other":"3-hydroxy-5-(hydroxymethyl)-2-methylpyridine-4-carboxylic acid|CAS:82-82-6","predicate_id":"skos:exactMatch","subject_id":"MIM:4-Pyridoxic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3be0edfed5ae0597
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[389]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17405","line":389,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17405","preferred_term":"4-Pyridoxic
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a640e1b61ac1b816
  kind: prior_review
  reference: reports/yaml_record_review/4-Pyridoxic_Acid.md
  locator: '`data/ingredients/mapped/4-Pyridoxic_Acid.yaml`:2; Verdict:4; Identity:10;
    Validation:24; Evidence:35; Completeness:57; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 23a391c770004eccced4c3beb103ee332a5a9ce6ee48a652f77560d3f7cc5053
  quote: 'Recommended Edits:

    Remove `nutritional_roles.VITAMIN_SOURCE`, or replace its evidence with a

    specific source showing 4-pyridoxic acid itself functions as a vitamin source
    in

    the curated medium context. Then resync the aggregate and rebuild docs.'
- evidence_id: ev-1949bbdae1762927
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[149,2089]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3","finding_id":"SEM:d011aeb4740676006aa7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3","finding_id":"SEM:6ad5ed969f55efb33700","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0e7ea150801e578e
  kind: record_content
  reference: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[387],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17405","line":389,"mapping_status":"MAPPED","ontology_id":"CHEBI:17405","preferred_term":"4-Pyridoxic
    acid"}],"identifier":"CHEBI:17405","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17405","ontology_label":"4-pyridoxic
    acid","ontology_source":"CHEBI"},"preferred_term":"4-Pyridoxic acid","sssom_rows":[{"data_row":189,"object_id":"CHEBI:17405","object_label":"4-pyridoxic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:4-Pyridoxic_Acid","synonym_count":1}'
  snapshot_sha256: 869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3
- evidence_id: ev-183cc8f521686e2a
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-5811a740aa6bd953]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5811a740aa6bd953 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-4ced3a7498bcc1c9
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-cd49cc5a160f0f6a
  - ev-a8d9b2b33a8386aa
  - ev-507f789f1f73e687
  - ev-3be0edfed5ae0597
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-1db05955f086dec2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-a640e1b61ac1b816
  - ev-cd49cc5a160f0f6a
  - ev-1949bbdae1762927
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:18:15Z;
    reviewed SHA-256=869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3;
    current SHA-256=869bee2538e8475c7993a2582fbd83adaec8087b22c56f4286908beaa74dd4b3;
    hash_changed=False. Reports=["reports/yaml_record_review/4-Pyridoxic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: CHEBI identity
    and chemistry pass, but the provisional VITAMIN_SOURCE role is only inferred from
    ChEBI ancestry and remains unreviewed on a vitamin B6 catabolite.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a640e1b61ac1b816
    - ev-cd49cc5a160f0f6a
  - name: legacy-native-ids
    value: '["SEM:d011aeb4740676006aa7","SEM:6ad5ed969f55efb33700"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cd49cc5a160f0f6a
    - ev-a640e1b61ac1b816
    - ev-1949bbdae1762927
- assessment_id: a-0e7ea150801e578e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-a640e1b61ac1b816
  - ev-0e7ea150801e578e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a640e1b61ac1b816
    - ev-0e7ea150801e578e
findings:
- finding_id: rec-f-5811a740aa6bd953
  issue_key: mim-reconciliation-role-support-6ad3cf8f490598d1
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 4-Pyridoxic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6ad3cf8f490598d1
  evidence_ids:
  - ev-a640e1b61ac1b816
  - ev-0e7ea150801e578e
  - ev-183cc8f521686e2a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
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
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-5811a740aa6bd953
actions:
- action_id: rec-action-5811a740aa6bd953
  description: 'Reassess prediction-only role support: 4-Pyridoxic acid'
  finding_ids:
  - rec-f-5811a740aa6bd953
  target_ids:
  - record-6ad3cf8f490598d1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/4-Pyridoxic_Acid.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
