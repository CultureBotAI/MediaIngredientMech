# Per-record structured review: Maltohexaose (data/ingredients/mapped/Maltohexaose.yaml)

- Review: 20261017T083000Z-maltohexaose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Maltohexaose (data/ingredients/mapped/Maltohexaose.yaml, record-8d7b3864d8438b73, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Maltohexaose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Maltohexaose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8d7b3864d8438b73 | data/ingredients/mapped/Maltohexaose.yaml | maintained | Maltohexaose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8d7b3864d8438b73 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-8d7b3864d8438b73 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8d7b3864d8438b73 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8d7b3864d8438b73.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8d7b3864d8438b73.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:27:59Z; reviewed SHA-256=48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d; current SHA-256=48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d; hash_changed=False. Reports=["reports/yaml_record_review/Maltohexaose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, structure, exact IUPAC synonym, and final SSSOM row pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-8d7b3864d8438b73.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-4e5f6ddf2a5bc16a: Reassess prediction-only role support: Maltohexaose

major / open / confirmed; issue key: mim-reconciliation-role-support-8d7b3864d8438b73.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-4e5f6ddf2a5bc16a

Reassess prediction-only role support: Maltohexaose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-50cb3076047d5313 | data/ingredients/mapped/Maltohexaose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1340],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27445","line":1342,"mapping_status":"MAPPED","ontology_id":"CHEBI:27445","preferred_term":"Maltohexaose"}],"identifier":"CHEBI:27445","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27445","ontology_label":"maltohexaose","ontology_source":"CHEBI"},"preferred_term":"Maltohexaose","sssom_rows":[{"data_row":1767,"object_id":"CHEBI:27445","object_label":"maltohexaose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltohexaose","synonym_count":1} |
| ev-4e6751bf0f549aae | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1340] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9fd3e30f4525f4b6 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Maltohexaose; data-row positions=[1767] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1767,"object_id":"CHEBI:27445","object_label":"maltohexaose","other":"alpha-D-glucopyranosyl-(1-&gt;4)-alpha-D-glucopyranosyl-(1-&gt;4)-alpha-D-glucopyranosyl-(1-&gt;4)-alpha-D-glucopyranosyl-(1-&gt;4)-alpha-D-glucopyranosyl-(1-&gt;4)-D-glucose&#124;CAS:34620-77-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Maltohexaose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-471609fb5d1a63c7 | docs/data/mapped_ingredients.csv; CSV lines=[1342] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27445","line":1342,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27445","preferred_term":"Maltohexaose","total_occurrences":"0"}] |
| ev-b3e143e6b33a4bcd | reports/yaml_record_review/Maltohexaose.md; &#96;data/ingredients/mapped/Maltohexaose.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:30; Completeness:40; Recommended Edits:47 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-24a591919b3eee2e | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[894,1378] | context_only | [{"current_record_sha256":"48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d","finding_id":"SEM:e5098cc1ffe087192d90","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d","finding_id":"SEM:ab763c1d4f960e971b6b","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-618a38aa4709f06a | data/ingredients/mapped/Maltohexaose.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1340],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27445","line":1342,"mapping_status":"MAPPED","ontology_id":"CHEBI:27445","preferred_term":"Maltohexaose"}],"identifier":"CHEBI:27445","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27445","ontology_label":"maltohexaose","ontology_source":"CHEBI"},"preferred_term":"Maltohexaose","sssom_rows":[{"data_row":1767,"object_id":"CHEBI:27445","object_label":"maltohexaose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltohexaose","synonym_count":1} |
| ev-3f34d207db1bf01c | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-4e5f6ddf2a5bc16a] | context_only | Predecessor structured review finding f-4e5f6ddf2a5bc16a in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-maltohexaose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Maltohexaose (data/ingredients/mapped/Maltohexaose.yaml)'
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
summary: Per-record structured review for Maltohexaose (data/ingredients/mapped/Maltohexaose.yaml,
  record-8d7b3864d8438b73, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Maltohexaose.yaml
    sha256: 48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Maltohexaose.md
    sha256: d5ef89bf6f189ff1c73b8942511ae4eb9fc217bf0d496b900b84bd0a4ace010a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8d7b3864d8438b73
  path: data/ingredients/mapped/Maltohexaose.yaml
  label: Maltohexaose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltohexaose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Maltohexaose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Maltohexaose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8d7b3864d8438b73
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-50cb3076047d5313
  - ev-4e6751bf0f549aae
  - ev-9fd3e30f4525f4b6
  - ev-471609fb5d1a63c7
  - ev-618a38aa4709f06a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-50cb3076047d5313
  - ev-24a591919b3eee2e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-b3e143e6b33a4bcd
  - ev-24a591919b3eee2e
  - ev-3f34d207db1bf01c
evidence:
- evidence_id: ev-50cb3076047d5313
  kind: record_content
  reference: data/ingredients/mapped/Maltohexaose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1340],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27445","line":1342,"mapping_status":"MAPPED","ontology_id":"CHEBI:27445","preferred_term":"Maltohexaose"}],"identifier":"CHEBI:27445","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27445","ontology_label":"maltohexaose","ontology_source":"CHEBI"},"preferred_term":"Maltohexaose","sssom_rows":[{"data_row":1767,"object_id":"CHEBI:27445","object_label":"maltohexaose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltohexaose","synonym_count":1}'
  snapshot_sha256: 48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d
- evidence_id: ev-4e6751bf0f549aae
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1340]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9fd3e30f4525f4b6
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Maltohexaose; data-row positions=[1767]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1767,"object_id":"CHEBI:27445","object_label":"maltohexaose","other":"alpha-D-glucopyranosyl-(1->4)-alpha-D-glucopyranosyl-(1->4)-alpha-D-glucopyranosyl-(1->4)-alpha-D-glucopyranosyl-(1->4)-alpha-D-glucopyranosyl-(1->4)-D-glucose|CAS:34620-77-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Maltohexaose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-471609fb5d1a63c7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1342]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27445","line":1342,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:27445","preferred_term":"Maltohexaose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b3e143e6b33a4bcd
  kind: prior_review
  reference: reports/yaml_record_review/Maltohexaose.md
  locator: '`data/ingredients/mapped/Maltohexaose.yaml`:2; Verdict:4; Identity:12;
    Validation:23; Evidence:30; Completeness:40; Recommended Edits:47'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: d5ef89bf6f189ff1c73b8942511ae4eb9fc217bf0d496b900b84bd0a4ace010a
  quote: "Recommended Edits:\n- Remove `CARBON_SOURCE` unless source-backed evidence\
    \ for maltohexaose as a\n  media carbon source can be attached."
- evidence_id: ev-24a591919b3eee2e
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[894,1378]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d","finding_id":"SEM:e5098cc1ffe087192d90","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d","finding_id":"SEM:ab763c1d4f960e971b6b","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-618a38aa4709f06a
  kind: record_content
  reference: data/ingredients/mapped/Maltohexaose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1340],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27445","line":1342,"mapping_status":"MAPPED","ontology_id":"CHEBI:27445","preferred_term":"Maltohexaose"}],"identifier":"CHEBI:27445","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27445","ontology_label":"maltohexaose","ontology_source":"CHEBI"},"preferred_term":"Maltohexaose","sssom_rows":[{"data_row":1767,"object_id":"CHEBI:27445","object_label":"maltohexaose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltohexaose","synonym_count":1}'
  snapshot_sha256: 48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d
- evidence_id: ev-3f34d207db1bf01c
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-4e5f6ddf2a5bc16a]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-4e5f6ddf2a5bc16a in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-ac718f63b9e0d4e2
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-50cb3076047d5313
  - ev-4e6751bf0f549aae
  - ev-9fd3e30f4525f4b6
  - ev-471609fb5d1a63c7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b1e440ae07636648
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-b3e143e6b33a4bcd
  - ev-50cb3076047d5313
  - ev-24a591919b3eee2e
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:27:59Z;
    reviewed SHA-256=48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d;
    current SHA-256=48c3e3879cf58700589fcc96f8430388714905cb3280db1450585db29868bc4d;
    hash_changed=False. Reports=["reports/yaml_record_review/Maltohexaose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity, CAS, structure, exact IUPAC synonym, and final SSSOM row pass, but CARBON_SOURCE
    is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b3e143e6b33a4bcd
    - ev-50cb3076047d5313
  - name: legacy-native-ids
    value: '["SEM:e5098cc1ffe087192d90","SEM:ab763c1d4f960e971b6b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-50cb3076047d5313
    - ev-b3e143e6b33a4bcd
    - ev-24a591919b3eee2e
- assessment_id: a-618a38aa4709f06a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-b3e143e6b33a4bcd
  - ev-618a38aa4709f06a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b3e143e6b33a4bcd
    - ev-618a38aa4709f06a
findings:
- finding_id: rec-f-4e5f6ddf2a5bc16a
  issue_key: mim-reconciliation-role-support-8d7b3864d8438b73
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Maltohexaose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-8d7b3864d8438b73
  evidence_ids:
  - ev-b3e143e6b33a4bcd
  - ev-618a38aa4709f06a
  - ev-3f34d207db1bf01c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltohexaose.yaml
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
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-4e5f6ddf2a5bc16a
actions:
- action_id: rec-action-4e5f6ddf2a5bc16a
  description: 'Reassess prediction-only role support: Maltohexaose'
  finding_ids:
  - rec-f-4e5f6ddf2a5bc16a
  target_ids:
  - record-8d7b3864d8438b73
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltohexaose.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
