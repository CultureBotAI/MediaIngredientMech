# Per-record structured review: 5-aminovaleric_Acid (data/ingredients/mapped/5-aminovaleric_Acid.yaml)

- Review: 20261017T083000Z-5-aminovaleric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 5-aminovaleric_Acid (data/ingredients/mapped/5-aminovaleric_Acid.yaml, record-cc478da880ac5316, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/5-aminovaleric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/5-aminovaleric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-cc478da880ac5316 | data/ingredients/mapped/5-aminovaleric_Acid.yaml | maintained | 5-aminovaleric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-cc478da880ac5316 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-cc478da880ac5316 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-cc478da880ac5316 | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-cc478da880ac5316.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-cc478da880ac5316.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:38:34Z; reviewed SHA-256=c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7; current SHA-256=c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7; hash_changed=False. Reports=["reports/yaml_record_review/5-aminovaleric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, chemistry, occurrence count, and SSSOM pass, but two exact synonyms name the wrong positional isomer and the amino-acid-source role is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-cc478da880ac5316.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-69171a0d99b66f6d: Reassess prediction-only role support: 5-Aminovaleric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-cc478da880ac5316.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-69171a0d99b66f6d

Reassess prediction-only role support: 5-Aminovaleric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-9227fd7df2326fa1 | data/ingredients/mapped/5-aminovaleric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[410],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15887","line":412,"mapping_status":"MAPPED","ontology_id":"CHEBI:15887","preferred_term":"5-Aminovaleric acid"}],"identifier":"CHEBI:15887","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15887","ontology_label":"5-aminopentanoic acid","ontology_source":"CHEBI"},"preferred_term":"5-Aminovaleric acid","sssom_rows":[{"data_row":231,"object_id":"CHEBI:15887","object_label":"5-aminopentanoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:5-aminovaleric_Acid","synonym_count":8} |
| ev-bb4f871a1adea2bf | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [410] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b2d7bc380b31fd8b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:5-aminovaleric_Acid; data-row positions=[231] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":231,"object_id":"CHEBI:15887","object_label":"5-aminopentanoic acid","other":"4-aminovalerate&#124;4-aminovaleric acid&#124;5-amino-n-valeric acid&#124;DANVA&#124;delta-Amino-n-valeric acid&#124;delta-aminovaleric acid&#124;5-Aminopentanoate&#124;CAS:660-88-8","predicate_id":"skos:exactMatch","subject_id":"MIM:5-aminovaleric_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-96b312acd8abf763 | docs/data/mapped_ingredients.csv; CSV lines=[412] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15887","line":412,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:15887","preferred_term":"5-Aminovaleric acid","total_occurrences":"5"}] |
| ev-577736780a96c1f5 | reports/yaml_record_review/5-aminovaleric_Acid.md; &#96;data/ingredients/mapped/5-aminovaleric_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:35; Completeness:62; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b97fa1499bb99d06 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[164,2093] | context_only | [{"current_record_sha256":"c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7","finding_id":"SEM:c030410361ae21786909","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7","finding_id":"SEM:6597e839062c8826f85b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-3fbd82cbe1a4b3b9 | data/ingredients/mapped/5-aminovaleric_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-9abc48a8bf03aab5 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-69171a0d99b66f6d] | context_only | Predecessor structured review finding f-69171a0d99b66f6d in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-5-aminovaleric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 5-aminovaleric_Acid (data/ingredients/mapped/5-aminovaleric_Acid.yaml)'
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
summary: Per-record structured review for 5-aminovaleric_Acid (data/ingredients/mapped/5-aminovaleric_Acid.yaml,
  record-cc478da880ac5316, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/5-aminovaleric_Acid.yaml
    sha256: c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7
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
  - path: reports/yaml_record_review/5-aminovaleric_Acid.md
    sha256: 47327ab7d9f2f77bd32c5cb4795ae1da460cfb23fef65a18c765a844e9816df1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-cc478da880ac5316
  path: data/ingredients/mapped/5-aminovaleric_Acid.yaml
  label: 5-aminovaleric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-aminovaleric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/5-aminovaleric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/5-aminovaleric_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-cc478da880ac5316
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-cc478da880ac5316
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-cc478da880ac5316
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-cc478da880ac5316
evidence:
- evidence_id: ev-9227fd7df2326fa1
  kind: record_content
  reference: data/ingredients/mapped/5-aminovaleric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[410],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15887","line":412,"mapping_status":"MAPPED","ontology_id":"CHEBI:15887","preferred_term":"5-Aminovaleric
    acid"}],"identifier":"CHEBI:15887","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15887","ontology_label":"5-aminopentanoic
    acid","ontology_source":"CHEBI"},"preferred_term":"5-Aminovaleric acid","sssom_rows":[{"data_row":231,"object_id":"CHEBI:15887","object_label":"5-aminopentanoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:5-aminovaleric_Acid","synonym_count":8}'
  snapshot_sha256: c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7
- evidence_id: ev-bb4f871a1adea2bf
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [410]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b2d7bc380b31fd8b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:5-aminovaleric_Acid; data-row positions=[231]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":231,"object_id":"CHEBI:15887","object_label":"5-aminopentanoic
    acid","other":"4-aminovalerate|4-aminovaleric acid|5-amino-n-valeric acid|DANVA|delta-Amino-n-valeric
    acid|delta-aminovaleric acid|5-Aminopentanoate|CAS:660-88-8","predicate_id":"skos:exactMatch","subject_id":"MIM:5-aminovaleric_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-96b312acd8abf763
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[412]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15887","line":412,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:15887","preferred_term":"5-Aminovaleric
    acid","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-577736780a96c1f5
  kind: prior_review
  reference: reports/yaml_record_review/5-aminovaleric_Acid.md
  locator: '`data/ingredients/mapped/5-aminovaleric_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:35; Completeness:62; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 47327ab7d9f2f77bd32c5cb4795ae1da460cfb23fef65a18c765a844e9816df1
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/5-aminovaleric_Acid.yaml`,\
    \ remove\n  `4-aminovalerate` and `4-aminovaleric acid` from `synonyms`; rebuild\n\
    \  `mappings/ingredient_mappings.sssom.tsv` and the aggregate\n  `data/curated/mapped_ingredients.yaml`.\n\
    - In the same maintained YAML, either remove the provisional\n  `AMINO_ACID_SOURCE`\
    \ role or replace the computational placeholder with\n  source-backed evidence\
    \ scoped to 5-aminovaleric acid; rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen python scripts/validate_sssom_invariants.py`, and\n  `uv run\
    \ --frozen python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`\n\
    \  after the edit."
- evidence_id: ev-b97fa1499bb99d06
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[164,2093]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7","finding_id":"SEM:c030410361ae21786909","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7","finding_id":"SEM:6597e839062c8826f85b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-3fbd82cbe1a4b3b9
  kind: record_content
  reference: data/ingredients/mapped/5-aminovaleric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7
- evidence_id: ev-9abc48a8bf03aab5
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-69171a0d99b66f6d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-69171a0d99b66f6d in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-223858372021d203
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-cc478da880ac5316
  evidence_ids:
  - ev-9227fd7df2326fa1
  - ev-bb4f871a1adea2bf
  - ev-b2d7bc380b31fd8b
  - ev-96b312acd8abf763
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c2fd136f7b64f71a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-cc478da880ac5316
  evidence_ids:
  - ev-577736780a96c1f5
  - ev-9227fd7df2326fa1
  - ev-b97fa1499bb99d06
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:38:34Z;
    reviewed SHA-256=c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7;
    current SHA-256=c619f43c8d0bab3cf84ebb74359aa9d005b56e118ba3ef4639d3702b340d8df7;
    hash_changed=False. Reports=["reports/yaml_record_review/5-aminovaleric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, CAS, chemistry, occurrence count, and SSSOM pass, but two exact
    synonyms name the wrong positional isomer and the amino-acid-source role is only
    provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-577736780a96c1f5
    - ev-9227fd7df2326fa1
  - name: legacy-native-ids
    value: '["SEM:c030410361ae21786909","SEM:6597e839062c8826f85b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-9227fd7df2326fa1
    - ev-577736780a96c1f5
    - ev-b97fa1499bb99d06
- assessment_id: a-3fbd82cbe1a4b3b9
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cc478da880ac5316
  evidence_ids:
  - ev-577736780a96c1f5
  - ev-3fbd82cbe1a4b3b9
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-577736780a96c1f5
    - ev-3fbd82cbe1a4b3b9
findings:
- finding_id: rec-f-69171a0d99b66f6d
  issue_key: mim-reconciliation-role-support-cc478da880ac5316
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 5-Aminovaleric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-cc478da880ac5316
  evidence_ids:
  - ev-577736780a96c1f5
  - ev-3fbd82cbe1a4b3b9
  - ev-9abc48a8bf03aab5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-aminovaleric_Acid.yaml
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
    finding_id: f-69171a0d99b66f6d
actions:
- action_id: rec-action-69171a0d99b66f6d
  description: 'Reassess prediction-only role support: 5-Aminovaleric acid'
  finding_ids:
  - rec-f-69171a0d99b66f6d
  target_ids:
  - record-cc478da880ac5316
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/5-aminovaleric_Acid.yaml
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
