# Per-record structured review: Lacto-N-tetraose (data/ingredients/mapped/Lacto-N-tetraose.yaml)

- Review: 20261017T083000Z-lacto-n-tetraose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lacto-N-tetraose (data/ingredients/mapped/Lacto-N-tetraose.yaml, record-0bd86fd49afdabe0, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lacto-N-tetraose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lacto-N-tetraose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0bd86fd49afdabe0 | data/ingredients/mapped/Lacto-N-tetraose.yaml | maintained | Lacto-N-tetraose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0bd86fd49afdabe0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0bd86fd49afdabe0 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0bd86fd49afdabe0 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0bd86fd49afdabe0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0bd86fd49afdabe0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:49:27Z; reviewed SHA-256=b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c; current SHA-256=b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c; hash_changed=False. Reports=["reports/yaml_record_review/Lacto-N-tetraose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed CHEBI:30248 identity, CAS value, PubChem structure, synonym, and final CHEBI/CAS rows pass, but CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-0bd86fd49afdabe0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-9ffce1c41e8d002d: Reassess prediction-only role support: Lacto-N-tetraose

major / open / confirmed; issue key: mim-reconciliation-role-support-0bd86fd49afdabe0.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-9ffce1c41e8d002d

Reassess prediction-only role support: Lacto-N-tetraose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a73b46c20848f822 | data/ingredients/mapped/Lacto-N-tetraose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1280],"raw_equal":true},"docs_rows":[{"identifier":"cas:14116-68-8","line":1282,"mapping_status":"MAPPED","ontology_id":"CHEBI:30248","preferred_term":"Lacto-N-tetraose"}],"identifier":"cas:14116-68-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30248","ontology_label":"beta-D-Gal-(1-&gt;3)-beta-D-GlcNAc-(1-&gt;3)-beta-D-Gal-(1-&gt;4)-D-Glc","ontology_source":"CHEBI"},"preferred_term":"Lacto-N-tetraose","sssom_rows":[{"data_row":1663,"object_id":"CHEBI:30248","object_label":"beta-D-Gal-(1-&gt;3)-beta-D-GlcNAc-(1-&gt;3)-beta-D-Gal-(1-&gt;4)-D-Glc","predicate_id":"skos:exactMatch"},{"data_row":1664,"object_id":"cas:14116-68-8","object_label":"Lacto-N-tetraose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-tetraose","synonym_count":1} |
| ev-9d363b4460ea8564 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1280] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-354a393f4c318bc5 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lacto-N-tetraose; data-row positions=[1663,1664] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1663,"object_id":"CHEBI:30248","object_label":"beta-D-Gal-(1-&gt;3)-beta-D-GlcNAc-(1-&gt;3)-beta-D-Gal-(1-&gt;4)-D-Glc","other":"beta-D-galactopyranosyl-(1-&gt;3)-2-acetamido-2-deoxy-beta-D-glucopyranosyl-(1-&gt;3)-beta-D-galactopyranosyl-(1-&gt;4)-D-glucopyranose&#124;CAS:14116-68-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-tetraose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"},{"data_row":1664,"object_id":"cas:14116-68-8","object_label":"Lacto-N-tetraose","other":"CAS:14116-68-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-tetraose","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-054be0cb98562b99 | docs/data/mapped_ingredients.csv; CSV lines=[1282] | supports | Published identity and count rows inspected: [{"identifier":"cas:14116-68-8","line":1282,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30248","preferred_term":"Lacto-N-tetraose","total_occurrences":"0"}] |
| ev-19e7a98a3bc1e203 | reports/yaml_record_review/Lacto-N-tetraose.md; &#96;data/ingredients/mapped/Lacto-N-tetraose.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:29; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3a5775c0f8465361 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[849,1767] | context_only | [{"current_record_sha256":"b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c","finding_id":"SEM:39587ff77e841af5062b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c","finding_id":"SEM:0c8561eda02f83b003c2","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f627955212127c25 | data/ingredients/mapped/Lacto-N-tetraose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-31d48517d1c29e40 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-9ffce1c41e8d002d] | context_only | Predecessor structured review finding f-9ffce1c41e8d002d in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lacto-n-tetraose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lacto-N-tetraose (data/ingredients/mapped/Lacto-N-tetraose.yaml)'
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
summary: Per-record structured review for Lacto-N-tetraose (data/ingredients/mapped/Lacto-N-tetraose.yaml,
  record-0bd86fd49afdabe0, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lacto-N-tetraose.yaml
    sha256: b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c
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
  - path: reports/yaml_record_review/Lacto-N-tetraose.md
    sha256: 1ddd1d9f6e1e722b464416505bb58fe37cbf51d6e804e8b3076c4865b6badf38
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0bd86fd49afdabe0
  path: data/ingredients/mapped/Lacto-N-tetraose.yaml
  label: Lacto-N-tetraose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-tetraose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lacto-N-tetraose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lacto-N-tetraose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0bd86fd49afdabe0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0bd86fd49afdabe0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0bd86fd49afdabe0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0bd86fd49afdabe0
evidence:
- evidence_id: ev-a73b46c20848f822
  kind: record_content
  reference: data/ingredients/mapped/Lacto-N-tetraose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1280],"raw_equal":true},"docs_rows":[{"identifier":"cas:14116-68-8","line":1282,"mapping_status":"MAPPED","ontology_id":"CHEBI:30248","preferred_term":"Lacto-N-tetraose"}],"identifier":"cas:14116-68-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:30248","ontology_label":"beta-D-Gal-(1->3)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc","ontology_source":"CHEBI"},"preferred_term":"Lacto-N-tetraose","sssom_rows":[{"data_row":1663,"object_id":"CHEBI:30248","object_label":"beta-D-Gal-(1->3)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc","predicate_id":"skos:exactMatch"},{"data_row":1664,"object_id":"cas:14116-68-8","object_label":"Lacto-N-tetraose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-tetraose","synonym_count":1}'
  snapshot_sha256: b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c
- evidence_id: ev-9d363b4460ea8564
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1280]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-354a393f4c318bc5
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lacto-N-tetraose; data-row positions=[1663,1664]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1663,"object_id":"CHEBI:30248","object_label":"beta-D-Gal-(1->3)-beta-D-GlcNAc-(1->3)-beta-D-Gal-(1->4)-D-Glc","other":"beta-D-galactopyranosyl-(1->3)-2-acetamido-2-deoxy-beta-D-glucopyranosyl-(1->3)-beta-D-galactopyranosyl-(1->4)-D-glucopyranose|CAS:14116-68-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-tetraose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"},{"data_row":1664,"object_id":"cas:14116-68-8","object_label":"Lacto-N-tetraose","other":"CAS:14116-68-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-tetraose","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-054be0cb98562b99
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1282]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:14116-68-8","line":1282,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:30248","preferred_term":"Lacto-N-tetraose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-19e7a98a3bc1e203
  kind: prior_review
  reference: reports/yaml_record_review/Lacto-N-tetraose.md
  locator: '`data/ingredients/mapped/Lacto-N-tetraose.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:29; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1ddd1d9f6e1e722b464416505bb58fe37cbf51d6e804e8b3076c4865b6badf38
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ in\n  `data/ingredients/mapped/Lacto-N-tetraose.yaml` with inspected source\
    \ evidence\n  for exact Lacto-N-tetraose use, or remove the provisional role.\n\
    - Sync the aggregate copy and regenerate derived products after the YAML\n  changes;\
    \ rerun strict, product, component, and SSSOM validation."
- evidence_id: ev-3a5775c0f8465361
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[849,1767]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c","finding_id":"SEM:39587ff77e841af5062b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c","finding_id":"SEM:0c8561eda02f83b003c2","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f627955212127c25
  kind: record_content
  reference: data/ingredients/mapped/Lacto-N-tetraose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c
- evidence_id: ev-31d48517d1c29e40
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-9ffce1c41e8d002d]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-9ffce1c41e8d002d in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-b9ed2e8e8e9f2f9e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0bd86fd49afdabe0
  evidence_ids:
  - ev-a73b46c20848f822
  - ev-9d363b4460ea8564
  - ev-354a393f4c318bc5
  - ev-054be0cb98562b99
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-00de13738f841cd6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0bd86fd49afdabe0
  evidence_ids:
  - ev-19e7a98a3bc1e203
  - ev-a73b46c20848f822
  - ev-3a5775c0f8465361
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:49:27Z;
    reviewed SHA-256=b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c;
    current SHA-256=b7a73255b1615fc39beb8a126f306dd4c504706482864408a2d9fde96f050e9c;
    hash_changed=False. Reports=["reports/yaml_record_review/Lacto-N-tetraose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS-backed
    CHEBI:30248 identity, CAS value, PubChem structure, synonym, and final CHEBI/CAS
    rows pass, but CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-19e7a98a3bc1e203
    - ev-a73b46c20848f822
  - name: legacy-native-ids
    value: '["SEM:39587ff77e841af5062b","SEM:0c8561eda02f83b003c2"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a73b46c20848f822
    - ev-19e7a98a3bc1e203
    - ev-3a5775c0f8465361
- assessment_id: a-f627955212127c25
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0bd86fd49afdabe0
  evidence_ids:
  - ev-19e7a98a3bc1e203
  - ev-f627955212127c25
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-19e7a98a3bc1e203
    - ev-f627955212127c25
findings:
- finding_id: rec-f-9ffce1c41e8d002d
  issue_key: mim-reconciliation-role-support-0bd86fd49afdabe0
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lacto-N-tetraose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0bd86fd49afdabe0
  evidence_ids:
  - ev-19e7a98a3bc1e203
  - ev-f627955212127c25
  - ev-31d48517d1c29e40
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-tetraose.yaml
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
    finding_id: f-9ffce1c41e8d002d
actions:
- action_id: rec-action-9ffce1c41e8d002d
  description: 'Reassess prediction-only role support: Lacto-N-tetraose'
  finding_ids:
  - rec-f-9ffce1c41e8d002d
  target_ids:
  - record-0bd86fd49afdabe0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-tetraose.yaml
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
