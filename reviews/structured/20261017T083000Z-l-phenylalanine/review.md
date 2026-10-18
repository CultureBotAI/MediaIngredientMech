# Per-record structured review: L-phenylalanine (data/ingredients/mapped/L-phenylalanine.yaml)

- Review: 20261017T083000Z-l-phenylalanine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for L-phenylalanine (data/ingredients/mapped/L-phenylalanine.yaml, record-45c8405ecd20f314, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/L-phenylalanine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/L-phenylalanine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-45c8405ecd20f314 | data/ingredients/mapped/L-phenylalanine.yaml | maintained | L-phenylalanine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-45c8405ecd20f314 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-45c8405ecd20f314 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-45c8405ecd20f314 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-45c8405ecd20f314.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-45c8405ecd20f314.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:16:44Z; reviewed SHA-256=5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff; current SHA-256=5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff; hash_changed=False. Reports=["reports/yaml_record_review/L-phenylalanine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:17295 identity, CAS value, PubChem structure, and occurrence count pass, but final SSSOM exports generic Phenylalanine and AMINO_ACID_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-45c8405ecd20f314.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-aa07aa5201cd431e: Reassess prediction-only role support: L-Phenylalanine

major / open / confirmed; issue key: mim-reconciliation-role-support-45c8405ecd20f314.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-aa07aa5201cd431e

Reassess prediction-only role support: L-Phenylalanine

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ba6bcfb3cca2a250 | data/ingredients/mapped/L-phenylalanine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1256],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17295","line":1258,"mapping_status":"MAPPED","ontology_id":"CHEBI:17295","preferred_term":"L-Phenylalanine"}],"identifier":"CHEBI:17295","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":115,"edge_count":115,"occurrences":115},"occurrence_statistics":{"media_count":115,"total_occurrences":115},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17295","ontology_label":"L-phenylalanine","ontology_source":"CHEBI"},"preferred_term":"L-Phenylalanine","sssom_rows":[{"data_row":1632,"object_id":"CHEBI:17295","object_label":"L-phenylalanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-phenylalanine","synonym_count":7} |
| ev-cc0e7fc03d8129fb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1256] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-42f79a81e9b64be0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:L-phenylalanine; data-row positions=[1632] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1632,"object_id":"CHEBI:17295","object_label":"L-phenylalanine","other":"Phenylalanine&#124;(2S)-2-amino-3-phenylpropanoic acid&#124;(S)-2-Amino-3-phenylpropionic acid&#124;(S)-alpha-Amino-beta-phenylpropionic acid&#124;3-phenyl-L-alanine&#124;beta-phenyl-L-alanine&#124;CAS:63-91-2","predicate_id":"skos:exactMatch","subject_id":"MIM:L-phenylalanine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-cbf8eccf527de2bb | docs/data/mapped_ingredients.csv; CSV lines=[1258] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17295","line":1258,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"115","ontology_id":"CHEBI:17295","preferred_term":"L-Phenylalanine","total_occurrences":"115"}] |
| ev-4368f11527fe9576 | reports/yaml_record_review/L-phenylalanine.md; &#96;data/ingredients/mapped/L-phenylalanine.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:28; Completeness:48; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6bbc6788e5f665e4 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[830,1858] | context_only | [{"current_record_sha256":"5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff","finding_id":"SEM:a119d1dfcd328de67622","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff","finding_id":"SEM:e1fb366227d2575afe9b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a69a3f22bb8df716 | data/ingredients/mapped/L-phenylalanine.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-5facb62c8f23a9fe | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-aa07aa5201cd431e] | context_only | Predecessor structured review finding f-aa07aa5201cd431e in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-l-phenylalanine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: L-phenylalanine (data/ingredients/mapped/L-phenylalanine.yaml)'
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
summary: Per-record structured review for L-phenylalanine (data/ingredients/mapped/L-phenylalanine.yaml,
  record-45c8405ecd20f314, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/L-phenylalanine.yaml
    sha256: 5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/L-phenylalanine.md
    sha256: 25c7d3b81e49f24cc9a6860c6b085e4116d1aeb9f71d25c0c1876400d1756c6f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-45c8405ecd20f314
  path: data/ingredients/mapped/L-phenylalanine.yaml
  label: L-phenylalanine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-phenylalanine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/L-phenylalanine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/L-phenylalanine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-45c8405ecd20f314
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-45c8405ecd20f314
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-45c8405ecd20f314
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-45c8405ecd20f314
evidence:
- evidence_id: ev-ba6bcfb3cca2a250
  kind: record_content
  reference: data/ingredients/mapped/L-phenylalanine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1256],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17295","line":1258,"mapping_status":"MAPPED","ontology_id":"CHEBI:17295","preferred_term":"L-Phenylalanine"}],"identifier":"CHEBI:17295","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":115,"edge_count":115,"occurrences":115},"occurrence_statistics":{"media_count":115,"total_occurrences":115},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17295","ontology_label":"L-phenylalanine","ontology_source":"CHEBI"},"preferred_term":"L-Phenylalanine","sssom_rows":[{"data_row":1632,"object_id":"CHEBI:17295","object_label":"L-phenylalanine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:L-phenylalanine","synonym_count":7}'
  snapshot_sha256: 5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff
- evidence_id: ev-cc0e7fc03d8129fb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1256]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-42f79a81e9b64be0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:L-phenylalanine; data-row positions=[1632]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1632,"object_id":"CHEBI:17295","object_label":"L-phenylalanine","other":"Phenylalanine|(2S)-2-amino-3-phenylpropanoic
    acid|(S)-2-Amino-3-phenylpropionic acid|(S)-alpha-Amino-beta-phenylpropionic acid|3-phenyl-L-alanine|beta-phenyl-L-alanine|CAS:63-91-2","predicate_id":"skos:exactMatch","subject_id":"MIM:L-phenylalanine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cbf8eccf527de2bb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1258]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17295","line":1258,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"115","ontology_id":"CHEBI:17295","preferred_term":"L-Phenylalanine","total_occurrences":"115"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4368f11527fe9576
  kind: prior_review
  reference: reports/yaml_record_review/L-phenylalanine.md
  locator: '`data/ingredients/mapped/L-phenylalanine.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:28; Completeness:48; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 25c7d3b81e49f24cc9a6860c6b085e4116d1aeb9f71d25c0c1876400d1756c6f
  quote: "Recommended Edits:\n- Major: remove or demote `Phenylalanine` in\n  `data/ingredients/mapped/L-phenylalanine.yaml`;\
    \ keep the exact synonym\n  surface specific to `CHEBI:17295`.\n- Major: either\
    \ replace `nutritional_roles.AMINO_ACID_SOURCE` with inspected\n  source evidence\
    \ for exact L-phenylalanine use, or remove the provisional\n  role.\n- Sync the\
    \ aggregate copy and regenerate derived products after the YAML\n  changes; rerun\
    \ strict, term, round-trip, component, and SSSOM validation."
- evidence_id: ev-6bbc6788e5f665e4
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[830,1858]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff","finding_id":"SEM:a119d1dfcd328de67622","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff","finding_id":"SEM:e1fb366227d2575afe9b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a69a3f22bb8df716
  kind: record_content
  reference: data/ingredients/mapped/L-phenylalanine.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: 5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff
- evidence_id: ev-5facb62c8f23a9fe
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-aa07aa5201cd431e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-aa07aa5201cd431e in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-0a592ca93f76c627
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-45c8405ecd20f314
  evidence_ids:
  - ev-ba6bcfb3cca2a250
  - ev-cc0e7fc03d8129fb
  - ev-42f79a81e9b64be0
  - ev-cbf8eccf527de2bb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-720262830e850bb2
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-45c8405ecd20f314
  evidence_ids:
  - ev-4368f11527fe9576
  - ev-ba6bcfb3cca2a250
  - ev-6bbc6788e5f665e4
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:16:44Z;
    reviewed SHA-256=5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff;
    current SHA-256=5166757201c7bdfb2890e7292e80f78b318f4cf4f5e6bf8f6f5a3d3925f8cbff;
    hash_changed=False. Reports=["reports/yaml_record_review/L-phenylalanine.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:17295 identity, CAS value, PubChem structure, and occurrence count pass,
    but final SSSOM exports generic Phenylalanine and AMINO_ACID_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4368f11527fe9576
    - ev-ba6bcfb3cca2a250
  - name: legacy-native-ids
    value: '["SEM:a119d1dfcd328de67622","SEM:e1fb366227d2575afe9b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ba6bcfb3cca2a250
    - ev-4368f11527fe9576
    - ev-6bbc6788e5f665e4
- assessment_id: a-a69a3f22bb8df716
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-45c8405ecd20f314
  evidence_ids:
  - ev-4368f11527fe9576
  - ev-a69a3f22bb8df716
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4368f11527fe9576
    - ev-a69a3f22bb8df716
findings:
- finding_id: rec-f-aa07aa5201cd431e
  issue_key: mim-reconciliation-role-support-45c8405ecd20f314
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: L-Phenylalanine'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-45c8405ecd20f314
  evidence_ids:
  - ev-4368f11527fe9576
  - ev-a69a3f22bb8df716
  - ev-5facb62c8f23a9fe
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-phenylalanine.yaml
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
    review_id: 20261011T024635Z-mim-reconcile-all-batch-07
    finding_id: f-aa07aa5201cd431e
actions:
- action_id: rec-action-aa07aa5201cd431e
  description: 'Reassess prediction-only role support: L-Phenylalanine'
  finding_ids:
  - rec-f-aa07aa5201cd431e
  target_ids:
  - record-45c8405ecd20f314
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/L-phenylalanine.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
