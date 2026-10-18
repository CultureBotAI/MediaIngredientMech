# Per-record structured review: 3-aminobutyric_Acid (data/ingredients/mapped/3-aminobutyric_Acid.yaml)

- Review: 20261017T083000Z-3-aminobutyric-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-aminobutyric_Acid (data/ingredients/mapped/3-aminobutyric_Acid.yaml, record-47c2920d224faf2b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-aminobutyric_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-aminobutyric_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-47c2920d224faf2b | data/ingredients/mapped/3-aminobutyric_Acid.yaml | maintained | 3-aminobutyric_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-47c2920d224faf2b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-47c2920d224faf2b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-47c2920d224faf2b | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-47c2920d224faf2b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-47c2920d224faf2b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:03:57Z; reviewed SHA-256=e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb; current SHA-256=e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb; hash_changed=False. Reports=["reports/yaml_record_review/3-aminobutyric_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded CHEBI identity, chemistry, SSSOM, and aggregate pass, but AMINO_ACID_SOURCE is only supported by provisional ChEBI-ancestry evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-47c2920d224faf2b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9fe530523e44cef0: Reassess prediction-only role support: 3-aminobutyric acid

major / open / confirmed; issue key: mim-reconciliation-role-support-47c2920d224faf2b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9fe530523e44cef0

Reassess prediction-only role support: 3-aminobutyric acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-645ad8f1903bd80a | data/ingredients/mapped/3-aminobutyric_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[360],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37081","line":362,"mapping_status":"MAPPED","ontology_id":"CHEBI:37081","preferred_term":"3-aminobutyric acid"}],"identifier":"CHEBI:37081","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:37081","ontology_label":"3-aminobutanoic acid","ontology_source":"CHEBI"},"preferred_term":"3-aminobutyric acid","sssom_rows":[{"data_row":138,"object_id":"CHEBI:37081","object_label":"3-aminobutanoic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-aminobutyric_Acid","synonym_count":0} |
| ev-599754836ec5cb03 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [360] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-da5bf51ba87cb8b8 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-aminobutyric_Acid; data-row positions=[138] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":138,"object_id":"CHEBI:37081","object_label":"3-aminobutanoic acid","other":"CAS:541-48-0","predicate_id":"skos:exactMatch","subject_id":"MIM:3-aminobutyric_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-b6ce211d4a0196eb | docs/data/mapped_ingredients.csv; CSV lines=[362] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:37081","line":362,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37081","preferred_term":"3-aminobutyric acid","total_occurrences":"0"}] |
| ev-f2c54cc66c765313 | reports/yaml_record_review/3-aminobutyric_Acid.md; &#96;data/ingredients/mapped/3-aminobutyric_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:39; Completeness:53; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-98c1dd396716b9ce | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[115,2016] | context_only | [{"current_record_sha256":"e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb","finding_id":"SEM:ef6e2871a65f26ef7d10","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb","finding_id":"SEM:d97eae1b048eeae3b0ca","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a7b3064dc946043e | data/ingredients/mapped/3-aminobutyric_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-b65916e23b83addb | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-9fe530523e44cef0] | context_only | Predecessor structured review finding f-9fe530523e44cef0 in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-aminobutyric-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-aminobutyric_Acid (data/ingredients/mapped/3-aminobutyric_Acid.yaml)'
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
summary: Per-record structured review for 3-aminobutyric_Acid (data/ingredients/mapped/3-aminobutyric_Acid.yaml,
  record-47c2920d224faf2b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-aminobutyric_Acid.yaml
    sha256: e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb
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
  - path: reports/yaml_record_review/3-aminobutyric_Acid.md
    sha256: 45a93822b10d8026a3ef811a16351f955684905172a141a90cee57791bf87c9f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-47c2920d224faf2b
  path: data/ingredients/mapped/3-aminobutyric_Acid.yaml
  label: 3-aminobutyric_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-aminobutyric_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-aminobutyric_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-aminobutyric_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-47c2920d224faf2b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-47c2920d224faf2b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-47c2920d224faf2b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-47c2920d224faf2b
evidence:
- evidence_id: ev-645ad8f1903bd80a
  kind: record_content
  reference: data/ingredients/mapped/3-aminobutyric_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[360],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37081","line":362,"mapping_status":"MAPPED","ontology_id":"CHEBI:37081","preferred_term":"3-aminobutyric
    acid"}],"identifier":"CHEBI:37081","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:37081","ontology_label":"3-aminobutanoic
    acid","ontology_source":"CHEBI"},"preferred_term":"3-aminobutyric acid","sssom_rows":[{"data_row":138,"object_id":"CHEBI:37081","object_label":"3-aminobutanoic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-aminobutyric_Acid","synonym_count":0}'
  snapshot_sha256: e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb
- evidence_id: ev-599754836ec5cb03
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [360]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-da5bf51ba87cb8b8
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-aminobutyric_Acid; data-row positions=[138]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":138,"object_id":"CHEBI:37081","object_label":"3-aminobutanoic
    acid","other":"CAS:541-48-0","predicate_id":"skos:exactMatch","subject_id":"MIM:3-aminobutyric_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b6ce211d4a0196eb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[362]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:37081","line":362,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37081","preferred_term":"3-aminobutyric
    acid","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f2c54cc66c765313
  kind: prior_review
  reference: reports/yaml_record_review/3-aminobutyric_Acid.md
  locator: '`data/ingredients/mapped/3-aminobutyric_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:39; Completeness:53; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 45a93822b10d8026a3ef811a16351f955684905172a141a90cee57791bf87c9f
  quote: "Recommended Edits:\n1. In `data/ingredients/mapped/3-aminobutyric_Acid.yaml`,\
    \ remove\n   `nutritional_roles.AMINO_ACID_SOURCE` or replace it with direct evidence\
    \ that\n   the neutral acid is used as a culture-medium amino-acid source.\n2.\
    \ Optionally add directly supported synonyms such as `beta-aminobutyric acid`\n\
    \   and `BABA` while keeping racemate-specific labels off this neutral generic\n\
    \   acid unless exact-form evidence supports them.\n3. Run the per-record strict\
    \ validator, compare the record against\n   `data/curated/mapped_ingredients.yaml`,\
    \ rebuild the SSSOM/docs with the\n   maintained generators, and then rerun the\
    \ whole-corpus SSSOM and flat-export\n   checks."
- evidence_id: ev-98c1dd396716b9ce
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[115,2016]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb","finding_id":"SEM:ef6e2871a65f26ef7d10","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb","finding_id":"SEM:d97eae1b048eeae3b0ca","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a7b3064dc946043e
  kind: record_content
  reference: data/ingredients/mapped/3-aminobutyric_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb
- evidence_id: ev-b65916e23b83addb
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-9fe530523e44cef0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9fe530523e44cef0 in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-4dd3700b5e63840c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-47c2920d224faf2b
  evidence_ids:
  - ev-645ad8f1903bd80a
  - ev-599754836ec5cb03
  - ev-da5bf51ba87cb8b8
  - ev-b6ce211d4a0196eb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-fbf2268b0e76f7c0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-47c2920d224faf2b
  evidence_ids:
  - ev-f2c54cc66c765313
  - ev-645ad8f1903bd80a
  - ev-98c1dd396716b9ce
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:03:57Z;
    reviewed SHA-256=e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb;
    current SHA-256=e251b753d79dc0f3f45ccb1ffbb9a82fc61134d23c630d183a4616c93e4b72cb;
    hash_changed=False. Reports=["reports/yaml_record_review/3-aminobutyric_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Active CAS-grounded
    CHEBI identity, chemistry, SSSOM, and aggregate pass, but AMINO_ACID_SOURCE is
    only supported by provisional ChEBI-ancestry evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f2c54cc66c765313
    - ev-645ad8f1903bd80a
  - name: legacy-native-ids
    value: '["SEM:ef6e2871a65f26ef7d10","SEM:d97eae1b048eeae3b0ca"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-645ad8f1903bd80a
    - ev-f2c54cc66c765313
    - ev-98c1dd396716b9ce
- assessment_id: a-a7b3064dc946043e
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-47c2920d224faf2b
  evidence_ids:
  - ev-f2c54cc66c765313
  - ev-a7b3064dc946043e
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f2c54cc66c765313
    - ev-a7b3064dc946043e
findings:
- finding_id: rec-f-9fe530523e44cef0
  issue_key: mim-reconciliation-role-support-47c2920d224faf2b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 3-aminobutyric acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-47c2920d224faf2b
  evidence_ids:
  - ev-f2c54cc66c765313
  - ev-a7b3064dc946043e
  - ev-b65916e23b83addb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-aminobutyric_Acid.yaml
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
    finding_id: f-9fe530523e44cef0
actions:
- action_id: rec-action-9fe530523e44cef0
  description: 'Reassess prediction-only role support: 3-aminobutyric acid'
  finding_ids:
  - rec-f-9fe530523e44cef0
  target_ids:
  - record-47c2920d224faf2b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-aminobutyric_Acid.yaml
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
