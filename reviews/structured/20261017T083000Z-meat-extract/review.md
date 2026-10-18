# Per-record structured review: Meat_Extract (data/ingredients/mapped/Meat_Extract.yaml)

- Review: 20261017T083000Z-meat-extract
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Meat_Extract (data/ingredients/mapped/Meat_Extract.yaml, record-882ed3028a53accf, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Meat_Extract.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Meat_Extract.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-882ed3028a53accf | data/ingredients/mapped/Meat_Extract.yaml | maintained | Meat_Extract |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-882ed3028a53accf | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-882ed3028a53accf | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-882ed3028a53accf | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-882ed3028a53accf.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-882ed3028a53accf.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:56:04Z; reviewed SHA-256=d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537; current SHA-256=d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537; hash_changed=False. Reports=["reports/yaml_record_review/Meat_Extract.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact FOODON:03315424 identity, occurrence count, mixture classification, and final SSSOM row pass, but PROTEIN_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-882ed3028a53accf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-333dc4439e2d91ac: Reassess prediction-only role support: Meat Extract

major / open / confirmed; issue key: mim-reconciliation-role-support-882ed3028a53accf.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-333dc4439e2d91ac

Reassess prediction-only role support: Meat Extract

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-4ffce4904e584ab6 | data/ingredients/mapped/Meat_Extract.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1354],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315424","line":1356,"mapping_status":"MAPPED","ontology_id":"FOODON:03315424","preferred_term":"Meat Extract"}],"identifier":"FOODON:03315424","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":777,"edge_count":777,"occurrences":777},"occurrence_statistics":{"media_count":777,"total_occurrences":777},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315424","ontology_label":"meat extract","ontology_source":"FOODON"},"preferred_term":"Meat Extract","sssom_rows":[{"data_row":1796,"object_id":"FOODON:03315424","object_label":"meat extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Meat_Extract","synonym_count":0} |
| ev-84474ed42a804481 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1354] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-422f7d5a0eb58018 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Meat_Extract; data-row positions=[1796] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1796,"object_id":"FOODON:03315424","object_label":"meat extract","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Meat_Extract","validation_method":"OLS:foodon&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-51d7a3f4b8f1bf02 | docs/data/mapped_ingredients.csv; CSV lines=[1356] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:03315424","line":1356,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"777","ontology_id":"FOODON:03315424","preferred_term":"Meat Extract","total_occurrences":"777"}] |
| ev-5b564740e5d47a96 | reports/yaml_record_review/Meat_Extract.md; &#96;data/ingredients/mapped/Meat_Extract.yaml&#96;:2; Verdict:4; Identity:12; Validation:21; Evidence:29; Completeness:37; Recommended Edits:44 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-740beed50e75df20 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[909,1946] | context_only | [{"current_record_sha256":"d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537","finding_id":"SEM:37299eb492f50006d131","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537","finding_id":"SEM:8eefa1eb034686ea60eb","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b519df65bcbc7dcf | data/ingredients/mapped/Meat_Extract.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1354],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315424","line":1356,"mapping_status":"MAPPED","ontology_id":"FOODON:03315424","preferred_term":"Meat Extract"}],"identifier":"FOODON:03315424","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":777,"edge_count":777,"occurrences":777},"occurrence_statistics":{"media_count":777,"total_occurrences":777},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315424","ontology_label":"meat extract","ontology_source":"FOODON"},"preferred_term":"Meat Extract","sssom_rows":[{"data_row":1796,"object_id":"FOODON:03315424","object_label":"meat extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Meat_Extract","synonym_count":0} |
| ev-3e30fd09eeeb4aba | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-333dc4439e2d91ac] | context_only | Predecessor structured review finding f-333dc4439e2d91ac in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-meat-extract
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Meat_Extract (data/ingredients/mapped/Meat_Extract.yaml)'
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
summary: Per-record structured review for Meat_Extract (data/ingredients/mapped/Meat_Extract.yaml,
  record-882ed3028a53accf, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Meat_Extract.yaml
    sha256: d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537
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
  - path: reports/yaml_record_review/Meat_Extract.md
    sha256: 4b569d84cd52aa1cf3b154122b603b377c8f019684e4fe71003a51f553a0c629
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-882ed3028a53accf
  path: data/ingredients/mapped/Meat_Extract.yaml
  label: Meat_Extract
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Meat_Extract.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Meat_Extract.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Meat_Extract.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-882ed3028a53accf
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-4ffce4904e584ab6
  - ev-84474ed42a804481
  - ev-422f7d5a0eb58018
  - ev-51d7a3f4b8f1bf02
  - ev-b519df65bcbc7dcf
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-4ffce4904e584ab6
  - ev-740beed50e75df20
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-5b564740e5d47a96
  - ev-740beed50e75df20
  - ev-3e30fd09eeeb4aba
evidence:
- evidence_id: ev-4ffce4904e584ab6
  kind: record_content
  reference: data/ingredients/mapped/Meat_Extract.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1354],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315424","line":1356,"mapping_status":"MAPPED","ontology_id":"FOODON:03315424","preferred_term":"Meat
    Extract"}],"identifier":"FOODON:03315424","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":777,"edge_count":777,"occurrences":777},"occurrence_statistics":{"media_count":777,"total_occurrences":777},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315424","ontology_label":"meat
    extract","ontology_source":"FOODON"},"preferred_term":"Meat Extract","sssom_rows":[{"data_row":1796,"object_id":"FOODON:03315424","object_label":"meat
    extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Meat_Extract","synonym_count":0}'
  snapshot_sha256: d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537
- evidence_id: ev-84474ed42a804481
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1354]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-422f7d5a0eb58018
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Meat_Extract; data-row positions=[1796]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1796,"object_id":"FOODON:03315424","object_label":"meat
    extract","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Meat_Extract","validation_method":"OLS:foodon|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-51d7a3f4b8f1bf02
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1356]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:03315424","line":1356,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"777","ontology_id":"FOODON:03315424","preferred_term":"Meat
    Extract","total_occurrences":"777"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-5b564740e5d47a96
  kind: prior_review
  reference: reports/yaml_record_review/Meat_Extract.md
  locator: '`data/ingredients/mapped/Meat_Extract.yaml`:2; Verdict:4; Identity:12;
    Validation:21; Evidence:29; Completeness:37; Recommended Edits:44'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 4b569d84cd52aa1cf3b154122b603b377c8f019684e4fe71003a51f553a0c629
  quote: "Recommended Edits:\n- Curate recipe or literature evidence for `PROTEIN_SOURCE`,\
    \ or remove the\n  provisional nutritional role."
- evidence_id: ev-740beed50e75df20
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[909,1946]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537","finding_id":"SEM:37299eb492f50006d131","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537","finding_id":"SEM:8eefa1eb034686ea60eb","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b519df65bcbc7dcf
  kind: record_content
  reference: data/ingredients/mapped/Meat_Extract.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1354],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:03315424","line":1356,"mapping_status":"MAPPED","ontology_id":"FOODON:03315424","preferred_term":"Meat
    Extract"}],"identifier":"FOODON:03315424","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":777,"edge_count":777,"occurrences":777},"occurrence_statistics":{"media_count":777,"total_occurrences":777},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"FOODON:03315424","ontology_label":"meat
    extract","ontology_source":"FOODON"},"preferred_term":"Meat Extract","sssom_rows":[{"data_row":1796,"object_id":"FOODON:03315424","object_label":"meat
    extract","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Meat_Extract","synonym_count":0}'
  snapshot_sha256: d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537
- evidence_id: ev-3e30fd09eeeb4aba
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-333dc4439e2d91ac]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-333dc4439e2d91ac in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-662e499815f456c0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-4ffce4904e584ab6
  - ev-84474ed42a804481
  - ev-422f7d5a0eb58018
  - ev-51d7a3f4b8f1bf02
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b946e3d774de5fd8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-5b564740e5d47a96
  - ev-4ffce4904e584ab6
  - ev-740beed50e75df20
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:56:04Z;
    reviewed SHA-256=d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537;
    current SHA-256=d5865b8096c2ef24bf18ed5f79f61982f25853d18195f5e141dc9d29bd930537;
    hash_changed=False. Reports=["reports/yaml_record_review/Meat_Extract.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact FOODON:03315424
    identity, occurrence count, mixture classification, and final SSSOM row pass,
    but PROTEIN_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5b564740e5d47a96
    - ev-4ffce4904e584ab6
  - name: legacy-native-ids
    value: '["SEM:37299eb492f50006d131","SEM:8eefa1eb034686ea60eb"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-4ffce4904e584ab6
    - ev-5b564740e5d47a96
    - ev-740beed50e75df20
- assessment_id: a-b519df65bcbc7dcf
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-5b564740e5d47a96
  - ev-b519df65bcbc7dcf
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-5b564740e5d47a96
    - ev-b519df65bcbc7dcf
findings:
- finding_id: rec-f-333dc4439e2d91ac
  issue_key: mim-reconciliation-role-support-882ed3028a53accf
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Meat Extract'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-882ed3028a53accf
  evidence_ids:
  - ev-5b564740e5d47a96
  - ev-b519df65bcbc7dcf
  - ev-3e30fd09eeeb4aba
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Meat_Extract.yaml
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
    finding_id: f-333dc4439e2d91ac
actions:
- action_id: rec-action-333dc4439e2d91ac
  description: 'Reassess prediction-only role support: Meat Extract'
  finding_ids:
  - rec-f-333dc4439e2d91ac
  target_ids:
  - record-882ed3028a53accf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Meat_Extract.yaml
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
