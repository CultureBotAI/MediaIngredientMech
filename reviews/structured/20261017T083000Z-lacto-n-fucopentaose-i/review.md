# Per-record structured review: Lacto-N-fucopentaose_I (data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml)

- Review: 20261017T083000Z-lacto-n-fucopentaose-i
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lacto-N-fucopentaose_I (data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml, record-3ab872238130ff8a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3ab872238130ff8a | data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml | maintained | Lacto-N-fucopentaose_I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3ab872238130ff8a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-3ab872238130ff8a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3ab872238130ff8a | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3ab872238130ff8a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3ab872238130ff8a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:42:25Z; reviewed SHA-256=c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614; current SHA-256=c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614; hash_changed=False. Reports=["reports/yaml_record_review/Lacto-N-fucopentaose_I.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS/MeSH grounding, exact CAS/registry rows, and PubChem structure pass, but CHEBI:61357 is a plausible exact candidate needing promotion or an explicit structural rejection and CARBON_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-3ab872238130ff8a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-45cb41fefec0b490: Reassess prediction-only role support: Lacto-N-fucopentaose I

major / open / confirmed; issue key: mim-reconciliation-role-support-3ab872238130ff8a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-45cb41fefec0b490

Reassess prediction-only role support: Lacto-N-fucopentaose I

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d58f967f2acc2b82 | data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1276],"raw_equal":true},"docs_rows":[{"identifier":"cas:7578-25-8","line":1278,"mapping_status":"MAPPED","ontology_id":"mesh:C045442","preferred_term":"Lacto-N-fucopentaose I"}],"identifier":"cas:7578-25-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C045442","ontology_label":"lacto-N-fucopentaose I","ontology_source":"MESH"},"preferred_term":"Lacto-N-fucopentaose I","sssom_rows":[{"data_row":1655,"object_id":"mesh:C045442","object_label":"lacto-N-fucopentaose I","predicate_id":"skos:broadMatch"},{"data_row":1656,"object_id":"cas:7578-25-8","object_label":"Lacto-N-fucopentaose I","predicate_id":"skos:exactMatch"},{"data_row":1657,"object_id":"kgmicrobe.compound:lacto-n-fucopentaose_i","object_label":"Lacto-N-fucopentaose I","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-fucopentaose_I","synonym_count":0} |
| ev-3b8d3d9eab94c373 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1276] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4f0b2c57dce31a93 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lacto-N-fucopentaose_I; data-row positions=[1655, 1656, 1657] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1655,"object_id":"mesh:C045442","object_label":"lacto-N-fucopentaose I","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Lacto-N-fucopentaose_I","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1656,"object_id":"cas:7578-25-8","object_label":"Lacto-N-fucopentaose I","other":"CAS:7578-25-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-fucopentaose_I","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1657,"object_id":"kgmicrobe.compound:lacto-n-fucopentaose_i","object_label":"Lacto-N-fucopentaose I","other":"CAS:7578-25-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-fucopentaose_I","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-2df791e88a4e6978 | docs/data/mapped_ingredients.csv; CSV lines=[1278] | supports | Published identity and count rows inspected: [{"identifier":"cas:7578-25-8","line":1278,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C045442","preferred_term":"Lacto-N-fucopentaose I","total_occurrences":"0"}] |
| ev-db6065ee801843ca | reports/yaml_record_review/Lacto-N-fucopentaose_I.md; &#96;data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:29; Completeness:52; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b00f98e8cef3a4e5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[845,1997] | context_only | [{"current_record_sha256":"c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614","finding_id":"SEM:f46b754e3b5a65290568","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614","finding_id":"SEM:224c07b206e0a2578497","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-0a5b3370a4cfc0d3 | data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1276],"raw_equal":true},"docs_rows":[{"identifier":"cas:7578-25-8","line":1278,"mapping_status":"MAPPED","ontology_id":"mesh:C045442","preferred_term":"Lacto-N-fucopentaose I"}],"identifier":"cas:7578-25-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C045442","ontology_label":"lacto-N-fucopentaose I","ontology_source":"MESH"},"preferred_term":"Lacto-N-fucopentaose I","sssom_rows":[{"data_row":1655,"object_id":"mesh:C045442","object_label":"lacto-N-fucopentaose I","predicate_id":"skos:broadMatch"},{"data_row":1656,"object_id":"cas:7578-25-8","object_label":"Lacto-N-fucopentaose I","predicate_id":"skos:exactMatch"},{"data_row":1657,"object_id":"kgmicrobe.compound:lacto-n-fucopentaose_i","object_label":"Lacto-N-fucopentaose I","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-fucopentaose_I","synonym_count":0} |
| ev-70b22e2671990215 | reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml; findings[finding_id=f-45cb41fefec0b490] | context_only | Predecessor structured review finding f-45cb41fefec0b490 in 20261011T024635Z-mim-reconcile-all-batch-07 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lacto-n-fucopentaose-i
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lacto-N-fucopentaose_I (data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml)'
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
summary: Per-record structured review for Lacto-N-fucopentaose_I (data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml,
  record-3ab872238130ff8a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
    sha256: c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614
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
  - path: reports/yaml_record_review/Lacto-N-fucopentaose_I.md
    sha256: 8551542b6639a3dc2d5550bae3512e1179bd9a8ed6c902430a0f6482b36421cb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3ab872238130ff8a
  path: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
  label: Lacto-N-fucopentaose_I
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3ab872238130ff8a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-d58f967f2acc2b82
  - ev-3b8d3d9eab94c373
  - ev-4f0b2c57dce31a93
  - ev-2df791e88a4e6978
  - ev-0a5b3370a4cfc0d3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-d58f967f2acc2b82
  - ev-b00f98e8cef3a4e5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-db6065ee801843ca
  - ev-b00f98e8cef3a4e5
  - ev-70b22e2671990215
evidence:
- evidence_id: ev-d58f967f2acc2b82
  kind: record_content
  reference: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1276],"raw_equal":true},"docs_rows":[{"identifier":"cas:7578-25-8","line":1278,"mapping_status":"MAPPED","ontology_id":"mesh:C045442","preferred_term":"Lacto-N-fucopentaose
    I"}],"identifier":"cas:7578-25-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C045442","ontology_label":"lacto-N-fucopentaose
    I","ontology_source":"MESH"},"preferred_term":"Lacto-N-fucopentaose I","sssom_rows":[{"data_row":1655,"object_id":"mesh:C045442","object_label":"lacto-N-fucopentaose
    I","predicate_id":"skos:broadMatch"},{"data_row":1656,"object_id":"cas:7578-25-8","object_label":"Lacto-N-fucopentaose
    I","predicate_id":"skos:exactMatch"},{"data_row":1657,"object_id":"kgmicrobe.compound:lacto-n-fucopentaose_i","object_label":"Lacto-N-fucopentaose
    I","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-fucopentaose_I","synonym_count":0}'
  snapshot_sha256: c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614
- evidence_id: ev-3b8d3d9eab94c373
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1276]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4f0b2c57dce31a93
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lacto-N-fucopentaose_I; data-row positions=[1655, 1656,
    1657]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1655,"object_id":"mesh:C045442","object_label":"lacto-N-fucopentaose
    I","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Lacto-N-fucopentaose_I","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1656,"object_id":"cas:7578-25-8","object_label":"Lacto-N-fucopentaose
    I","other":"CAS:7578-25-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-fucopentaose_I","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1657,"object_id":"kgmicrobe.compound:lacto-n-fucopentaose_i","object_label":"Lacto-N-fucopentaose
    I","other":"CAS:7578-25-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Lacto-N-fucopentaose_I","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2df791e88a4e6978
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1278]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:7578-25-8","line":1278,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C045442","preferred_term":"Lacto-N-fucopentaose
    I","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-db6065ee801843ca
  kind: prior_review
  reference: reports/yaml_record_review/Lacto-N-fucopentaose_I.md
  locator: '`data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:29; Completeness:52; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8551542b6639a3dc2d5550bae3512e1179bd9a8ed6c902430a0f6482b36421cb
  quote: "Recommended Edits:\n- Major: inspect `CHEBI:61357` against PubChem CID `16219579`;\
    \ then either\n  promote `data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml`\
    \ to exact CHEBI\n  grounding or add reviewed rejection/provenance explaining\
    \ why the CHEBI term\n  is structurally different from CAS RN `7578-25-8`.\n-\
    \ Major: either replace `nutritional_roles.CARBON_SOURCE` with inspected source\n\
    \  evidence for exact Lacto-N-fucopentaose I use, or remove the provisional role.\n\
    - Sync the aggregate copy and regenerate final SSSOM after any YAML changes;\n\
    \  rerun strict, product, component, and SSSOM validation."
- evidence_id: ev-b00f98e8cef3a4e5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[845,1997]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614","finding_id":"SEM:f46b754e3b5a65290568","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614","finding_id":"SEM:224c07b206e0a2578497","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-0a5b3370a4cfc0d3
  kind: record_content
  reference: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1276],"raw_equal":true},"docs_rows":[{"identifier":"cas:7578-25-8","line":1278,"mapping_status":"MAPPED","ontology_id":"mesh:C045442","preferred_term":"Lacto-N-fucopentaose
    I"}],"identifier":"cas:7578-25-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"mesh:C045442","ontology_label":"lacto-N-fucopentaose
    I","ontology_source":"MESH"},"preferred_term":"Lacto-N-fucopentaose I","sssom_rows":[{"data_row":1655,"object_id":"mesh:C045442","object_label":"lacto-N-fucopentaose
    I","predicate_id":"skos:broadMatch"},{"data_row":1656,"object_id":"cas:7578-25-8","object_label":"Lacto-N-fucopentaose
    I","predicate_id":"skos:exactMatch"},{"data_row":1657,"object_id":"kgmicrobe.compound:lacto-n-fucopentaose_i","object_label":"Lacto-N-fucopentaose
    I","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lacto-N-fucopentaose_I","synonym_count":0}'
  snapshot_sha256: c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614
- evidence_id: ev-70b22e2671990215
  kind: prior_review
  reference: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
  locator: findings[finding_id=f-45cb41fefec0b490]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-45cb41fefec0b490 in 20261011T024635Z-mim-reconcile-all-batch-07
  snapshot_sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
assessments:
- assessment_id: a-091efaeacec8f045
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-d58f967f2acc2b82
  - ev-3b8d3d9eab94c373
  - ev-4f0b2c57dce31a93
  - ev-2df791e88a4e6978
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-af29a92fa6bfdf57
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-db6065ee801843ca
  - ev-d58f967f2acc2b82
  - ev-b00f98e8cef3a4e5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T23:42:25Z;
    reviewed SHA-256=c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614;
    current SHA-256=c75dab7ba504cb80212788f2198517a1c28c0b62335c2a3b276879ce4fddf614;
    hash_changed=False. Reports=["reports/yaml_record_review/Lacto-N-fucopentaose_I.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS/MeSH
    grounding, exact CAS/registry rows, and PubChem structure pass, but CHEBI:61357
    is a plausible exact candidate needing promotion or an explicit structural rejection
    and CARBON_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-db6065ee801843ca
    - ev-d58f967f2acc2b82
  - name: legacy-native-ids
    value: '["SEM:f46b754e3b5a65290568","SEM:224c07b206e0a2578497"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d58f967f2acc2b82
    - ev-db6065ee801843ca
    - ev-b00f98e8cef3a4e5
- assessment_id: a-0a5b3370a4cfc0d3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-db6065ee801843ca
  - ev-0a5b3370a4cfc0d3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-db6065ee801843ca
    - ev-0a5b3370a4cfc0d3
findings:
- finding_id: rec-f-45cb41fefec0b490
  issue_key: mim-reconciliation-role-support-3ab872238130ff8a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Lacto-N-fucopentaose I'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-3ab872238130ff8a
  evidence_ids:
  - ev-db6065ee801843ca
  - ev-0a5b3370a4cfc0d3
  - ev-70b22e2671990215
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
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
    finding_id: f-45cb41fefec0b490
actions:
- action_id: rec-action-45cb41fefec0b490
  description: 'Reassess prediction-only role support: Lacto-N-fucopentaose I'
  finding_ids:
  - rec-f-45cb41fefec0b490
  target_ids:
  - record-3ab872238130ff8a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lacto-N-fucopentaose_I.yaml
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
