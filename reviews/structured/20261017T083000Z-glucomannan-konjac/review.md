# Per-record structured review: Glucomannan_Konjac (data/ingredients/mapped/Glucomannan_Konjac.yaml)

- Review: 20261017T083000Z-glucomannan-konjac
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucomannan_Konjac (data/ingredients/mapped/Glucomannan_Konjac.yaml, record-dfcee132efbfd1e8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucomannan_Konjac.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucomannan_Konjac.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-dfcee132efbfd1e8 | data/ingredients/mapped/Glucomannan_Konjac.yaml | maintained | Glucomannan_Konjac |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-dfcee132efbfd1e8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-dfcee132efbfd1e8 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-dfcee132efbfd1e8 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-dfcee132efbfd1e8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-dfcee132efbfd1e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:41:23Z; reviewed SHA-256=059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9; current SHA-256=059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9; hash_changed=False. Reports=["reports/yaml_record_review/Glucomannan_Konjac.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS/local identity and broad glucomannan parent pass, but structure, final SSSOM synonyms, and CARBON_SOURCE need curation.

### Historical provisional-role concern

evidence: concern. Targets: record-dfcee132efbfd1e8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-d224f29d2b198935: Reassess prediction-only role support: Glucomannan (konjac)

major / open / confirmed; issue key: mim-reconciliation-role-support-dfcee132efbfd1e8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-d224f29d2b198935

Reassess prediction-only role support: Glucomannan (konjac)

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b9659f410e9c941d | data/ingredients/mapped/Glucomannan_Konjac.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1056],"raw_equal":true},"docs_rows":[{"identifier":"cas:11078-31-2","line":1058,"mapping_status":"MAPPED","ontology_id":"CHEBI:17020","preferred_term":"Glucomannan (konjac)"}],"identifier":"cas:11078-31-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17020","ontology_label":"glucomannan","ontology_source":"CHEBI"},"preferred_term":"Glucomannan (konjac)","sssom_rows":[{"data_row":1301,"object_id":"CHEBI:17020","object_label":"glucomannan","predicate_id":"skos:broadMatch"},{"data_row":1302,"object_id":"cas:11078-31-2","object_label":"Glucomannan (konjac)","predicate_id":"skos:exactMatch"},{"data_row":1303,"object_id":"kgmicrobe.compound:glucomannan_konjac","object_label":"Glucomannan (konjac)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucomannan_Konjac","synonym_count":1} |
| ev-fcb3f1c9ef6b220a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1056] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-2b8730d5a717e140 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucomannan_Konjac; data-row positions=[1301, 1302, 1303] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1301,"object_id":"CHEBI:17020","object_label":"glucomannan","other":"autoclaved, Glucomannan (konjac)","predicate_id":"skos:broadMatch","subject_id":"MIM:Glucomannan_Konjac","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1302,"object_id":"cas:11078-31-2","object_label":"Glucomannan (konjac)","other":"CAS:11078-31-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucomannan_Konjac","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":1303,"object_id":"kgmicrobe.compound:glucomannan_konjac","object_label":"Glucomannan (konjac)","other":"CAS:11078-31-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucomannan_Konjac","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-4d708e0433206fda | docs/data/mapped_ingredients.csv; CSV lines=[1058] | supports | Published identity and count rows inspected: [{"identifier":"cas:11078-31-2","line":1058,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17020","preferred_term":"Glucomannan (konjac)","total_occurrences":"0"}] |
| ev-64e584c343c206a1 | reports/yaml_record_review/Glucomannan_Konjac.md; &#96;data/ingredients/mapped/Glucomannan_Konjac.yaml&#96;:2; Verdict:4; Identity:12; Validation:23; Evidence:36; Completeness:62; Recommended Edits:68 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-53f32db520cfe6c0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[663,1423] | context_only | [{"current_record_sha256":"059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9","finding_id":"SEM:2a8f17ab29c2ac75c5c1","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9","finding_id":"SEM:5a74d07dac743f1efe8f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-8ecdc603d78528a4 | data/ingredients/mapped/Glucomannan_Konjac.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1056],"raw_equal":true},"docs_rows":[{"identifier":"cas:11078-31-2","line":1058,"mapping_status":"MAPPED","ontology_id":"CHEBI:17020","preferred_term":"Glucomannan (konjac)"}],"identifier":"cas:11078-31-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17020","ontology_label":"glucomannan","ontology_source":"CHEBI"},"preferred_term":"Glucomannan (konjac)","sssom_rows":[{"data_row":1301,"object_id":"CHEBI:17020","object_label":"glucomannan","predicate_id":"skos:broadMatch"},{"data_row":1302,"object_id":"cas:11078-31-2","object_label":"Glucomannan (konjac)","predicate_id":"skos:exactMatch"},{"data_row":1303,"object_id":"kgmicrobe.compound:glucomannan_konjac","object_label":"Glucomannan (konjac)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucomannan_Konjac","synonym_count":1} |
| ev-6a69045a647922d6 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-d224f29d2b198935] | context_only | Predecessor structured review finding f-d224f29d2b198935 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucomannan-konjac
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucomannan_Konjac (data/ingredients/mapped/Glucomannan_Konjac.yaml)'
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
summary: Per-record structured review for Glucomannan_Konjac (data/ingredients/mapped/Glucomannan_Konjac.yaml,
  record-dfcee132efbfd1e8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucomannan_Konjac.yaml
    sha256: 059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9
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
  - path: reports/yaml_record_review/Glucomannan_Konjac.md
    sha256: a20e17184f69ef7b8cbdfd224c7c8bd880b79d729c9a38afe9fa189ed7f53bad
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-dfcee132efbfd1e8
  path: data/ingredients/mapped/Glucomannan_Konjac.yaml
  label: Glucomannan_Konjac
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucomannan_Konjac.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucomannan_Konjac.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucomannan_Konjac.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-dfcee132efbfd1e8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-b9659f410e9c941d
  - ev-fcb3f1c9ef6b220a
  - ev-2b8730d5a717e140
  - ev-4d708e0433206fda
  - ev-8ecdc603d78528a4
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-b9659f410e9c941d
  - ev-53f32db520cfe6c0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-64e584c343c206a1
  - ev-53f32db520cfe6c0
  - ev-6a69045a647922d6
evidence:
- evidence_id: ev-b9659f410e9c941d
  kind: record_content
  reference: data/ingredients/mapped/Glucomannan_Konjac.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1056],"raw_equal":true},"docs_rows":[{"identifier":"cas:11078-31-2","line":1058,"mapping_status":"MAPPED","ontology_id":"CHEBI:17020","preferred_term":"Glucomannan
    (konjac)"}],"identifier":"cas:11078-31-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17020","ontology_label":"glucomannan","ontology_source":"CHEBI"},"preferred_term":"Glucomannan
    (konjac)","sssom_rows":[{"data_row":1301,"object_id":"CHEBI:17020","object_label":"glucomannan","predicate_id":"skos:broadMatch"},{"data_row":1302,"object_id":"cas:11078-31-2","object_label":"Glucomannan
    (konjac)","predicate_id":"skos:exactMatch"},{"data_row":1303,"object_id":"kgmicrobe.compound:glucomannan_konjac","object_label":"Glucomannan
    (konjac)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucomannan_Konjac","synonym_count":1}'
  snapshot_sha256: 059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9
- evidence_id: ev-fcb3f1c9ef6b220a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1056]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-2b8730d5a717e140
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucomannan_Konjac; data-row positions=[1301, 1302, 1303]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1301,"object_id":"CHEBI:17020","object_label":"glucomannan","other":"autoclaved,
    Glucomannan (konjac)","predicate_id":"skos:broadMatch","subject_id":"MIM:Glucomannan_Konjac","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1302,"object_id":"cas:11078-31-2","object_label":"Glucomannan
    (konjac)","other":"CAS:11078-31-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucomannan_Konjac","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":1303,"object_id":"kgmicrobe.compound:glucomannan_konjac","object_label":"Glucomannan
    (konjac)","other":"CAS:11078-31-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucomannan_Konjac","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-4d708e0433206fda
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1058]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:11078-31-2","line":1058,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17020","preferred_term":"Glucomannan
    (konjac)","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-64e584c343c206a1
  kind: prior_review
  reference: reports/yaml_record_review/Glucomannan_Konjac.md
  locator: '`data/ingredients/mapped/Glucomannan_Konjac.yaml`:2; Verdict:4; Identity:12;
    Validation:23; Evidence:36; Completeness:62; Recommended Edits:68'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a20e17184f69ef7b8cbdfd224c7c8bd880b79d729c9a38afe9fa189ed7f53bad
  quote: "Recommended Edits:\n- Major: remove or replace the PubChem finite-oligomer\
    \ structure fields unless\n  evidence shows they describe CAS `11078-31-2` rather\
    \ than just a representative\n  small glucomannan fragment.\n- Major: remove or\
    \ retag `autoclaved, Glucomannan (konjac)` so final SSSOM no\n  longer exports\
    \ process-qualified recipe text as a synonym, then regenerate\n  final SSSOM and\
    \ rerun SSSOM invariants.\n- Major: replace `CARBON_SOURCE` with source-backed\
    \ evidence or remove the role,\n  then rerun strict validation."
- evidence_id: ev-53f32db520cfe6c0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[663,1423]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9","finding_id":"SEM:2a8f17ab29c2ac75c5c1","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9","finding_id":"SEM:5a74d07dac743f1efe8f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-8ecdc603d78528a4
  kind: record_content
  reference: data/ingredients/mapped/Glucomannan_Konjac.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1056],"raw_equal":true},"docs_rows":[{"identifier":"cas:11078-31-2","line":1058,"mapping_status":"MAPPED","ontology_id":"CHEBI:17020","preferred_term":"Glucomannan
    (konjac)"}],"identifier":"cas:11078-31-2","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:17020","ontology_label":"glucomannan","ontology_source":"CHEBI"},"preferred_term":"Glucomannan
    (konjac)","sssom_rows":[{"data_row":1301,"object_id":"CHEBI:17020","object_label":"glucomannan","predicate_id":"skos:broadMatch"},{"data_row":1302,"object_id":"cas:11078-31-2","object_label":"Glucomannan
    (konjac)","predicate_id":"skos:exactMatch"},{"data_row":1303,"object_id":"kgmicrobe.compound:glucomannan_konjac","object_label":"Glucomannan
    (konjac)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucomannan_Konjac","synonym_count":1}'
  snapshot_sha256: 059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9
- evidence_id: ev-6a69045a647922d6
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-d224f29d2b198935]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-d224f29d2b198935 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-15fed9c4b634c0c6
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-b9659f410e9c941d
  - ev-fcb3f1c9ef6b220a
  - ev-2b8730d5a717e140
  - ev-4d708e0433206fda
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-524d183199b3f671
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-64e584c343c206a1
  - ev-b9659f410e9c941d
  - ev-53f32db520cfe6c0
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:41:23Z;
    reviewed SHA-256=059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9;
    current SHA-256=059075f17052db769b1cdc50bb2bcae61fcc28815cc96341ce28bd7ceddb2cd9;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucomannan_Konjac.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS/local
    identity and broad glucomannan parent pass, but structure, final SSSOM synonyms,
    and CARBON_SOURCE need curation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-64e584c343c206a1
    - ev-b9659f410e9c941d
  - name: legacy-native-ids
    value: '["SEM:2a8f17ab29c2ac75c5c1","SEM:5a74d07dac743f1efe8f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b9659f410e9c941d
    - ev-64e584c343c206a1
    - ev-53f32db520cfe6c0
- assessment_id: a-8ecdc603d78528a4
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-64e584c343c206a1
  - ev-8ecdc603d78528a4
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-64e584c343c206a1
    - ev-8ecdc603d78528a4
findings:
- finding_id: rec-f-d224f29d2b198935
  issue_key: mim-reconciliation-role-support-dfcee132efbfd1e8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Glucomannan (konjac)'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-dfcee132efbfd1e8
  evidence_ids:
  - ev-64e584c343c206a1
  - ev-8ecdc603d78528a4
  - ev-6a69045a647922d6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucomannan_Konjac.yaml
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
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-d224f29d2b198935
actions:
- action_id: rec-action-d224f29d2b198935
  description: 'Reassess prediction-only role support: Glucomannan (konjac)'
  finding_ids:
  - rec-f-d224f29d2b198935
  target_ids:
  - record-dfcee132efbfd1e8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucomannan_Konjac.yaml
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
