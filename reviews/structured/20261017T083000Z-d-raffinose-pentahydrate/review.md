# Per-record structured review: D-Raffinose_Pentahydrate (data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml)

- Review: 20261017T083000Z-d-raffinose-pentahydrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Raffinose_Pentahydrate (data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml, record-33582a299a07d746, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-33582a299a07d746 | data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml | maintained | D-Raffinose_Pentahydrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-33582a299a07d746 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-33582a299a07d746 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-33582a299a07d746 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-33582a299a07d746.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-33582a299a07d746.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:19:42Z; reviewed SHA-256=3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49; current SHA-256=3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49; hash_changed=False. Reports=["reports/yaml_record_review/D-Raffinose_Pentahydrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The pentahydrate CAS and structure pass, but CHEBI:189430 is now an exact pentahydrate term and the carbon role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-33582a299a07d746.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-8f31af00b5158419: Reassess prediction-only role support: D-Raffinose pentahydrate

major / open / confirmed; issue key: mim-reconciliation-role-support-33582a299a07d746.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-8f31af00b5158419

Reassess prediction-only role support: D-Raffinose pentahydrate

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-74d382c7d0ed9070 | data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[824],"raw_equal":true},"docs_rows":[{"identifier":"cas:17629-30-0","line":826,"mapping_status":"MAPPED","ontology_id":"CHEBI:189430","preferred_term":"D-Raffinose pentahydrate"}],"identifier":"cas:17629-30-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:189430","ontology_label":"Raffinose Pentahydrate","ontology_source":"CHEBI"},"preferred_term":"D-Raffinose pentahydrate","sssom_rows":[{"data_row":906,"object_id":"CHEBI:189430","object_label":"Raffinose Pentahydrate","predicate_id":"skos:broadMatch"},{"data_row":907,"object_id":"cas:17629-30-0","object_label":"D-Raffinose pentahydrate","predicate_id":"skos:exactMatch"},{"data_row":908,"object_id":"kgmicrobe.compound:d-raffinose_pentahydrate","object_label":"D-Raffinose pentahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Raffinose_Pentahydrate","synonym_count":1} |
| ev-6890dabdfef2ada8 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [824] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-297c3b68fd8ffe97 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Raffinose_Pentahydrate; data-row positions=[906, 907, 908] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":906,"object_id":"CHEBI:189430","object_label":"Raffinose Pentahydrate","other":"(2S,3R,4S,5R,6R)-2-[[(2R,3S,4S,5R,6R)-6-[(2S,3S,4S,5R)-3,4-dihydroxy-2,5-bis(hydroxymethyl)oxolan-2-yl]oxy-3,4,5-trihydroxyoxan-2-yl]methoxy]-6-(hydroxymethyl)oxane-3,4,5-triol;pentahydrate","predicate_id":"skos:broadMatch","subject_id":"MIM:D-Raffinose_Pentahydrate","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":907,"object_id":"cas:17629-30-0","object_label":"D-Raffinose pentahydrate","other":"CAS:17629-30-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Raffinose_Pentahydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":908,"object_id":"kgmicrobe.compound:d-raffinose_pentahydrate","object_label":"D-Raffinose pentahydrate","other":"CAS:17629-30-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Raffinose_Pentahydrate","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-c3bf0a0d1250ee2b | docs/data/mapped_ingredients.csv; CSV lines=[826] | supports | Published identity and count rows inspected: [{"identifier":"cas:17629-30-0","line":826,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:189430","preferred_term":"D-Raffinose pentahydrate","total_occurrences":"0"}] |
| ev-d321e73e176de72a | reports/yaml_record_review/D-Raffinose_Pentahydrate.md; &#96;data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml&#96;:2; Verdict:4; Identity:12; Validation:30; Evidence:49; Completeness:69; Recommended Edits:77 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a51f67c803a32983 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[476,1571] | context_only | [{"current_record_sha256":"3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49","finding_id":"SEM:167a4a3c3b13354872cd","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49","finding_id":"SEM:e7b4dba58cd6005df762","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-26caf769e191d1b6 | data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[824],"raw_equal":true},"docs_rows":[{"identifier":"cas:17629-30-0","line":826,"mapping_status":"MAPPED","ontology_id":"CHEBI:189430","preferred_term":"D-Raffinose pentahydrate"}],"identifier":"cas:17629-30-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:189430","ontology_label":"Raffinose Pentahydrate","ontology_source":"CHEBI"},"preferred_term":"D-Raffinose pentahydrate","sssom_rows":[{"data_row":906,"object_id":"CHEBI:189430","object_label":"Raffinose Pentahydrate","predicate_id":"skos:broadMatch"},{"data_row":907,"object_id":"cas:17629-30-0","object_label":"D-Raffinose pentahydrate","predicate_id":"skos:exactMatch"},{"data_row":908,"object_id":"kgmicrobe.compound:d-raffinose_pentahydrate","object_label":"D-Raffinose pentahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Raffinose_Pentahydrate","synonym_count":1} |
| ev-b194f10c355f911c | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-8f31af00b5158419] | context_only | Predecessor structured review finding f-8f31af00b5158419 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-raffinose-pentahydrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Raffinose_Pentahydrate (data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml)'
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
summary: Per-record structured review for D-Raffinose_Pentahydrate (data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml,
  record-33582a299a07d746, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
    sha256: 3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/D-Raffinose_Pentahydrate.md
    sha256: 1b2f1438d114a805d9840f9007f18a99d5c29d3a8cfcc97a66ce8c9d4206981e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-33582a299a07d746
  path: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
  label: D-Raffinose_Pentahydrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-33582a299a07d746
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-74d382c7d0ed9070
  - ev-6890dabdfef2ada8
  - ev-297c3b68fd8ffe97
  - ev-c3bf0a0d1250ee2b
  - ev-26caf769e191d1b6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-74d382c7d0ed9070
  - ev-a51f67c803a32983
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-d321e73e176de72a
  - ev-a51f67c803a32983
  - ev-b194f10c355f911c
evidence:
- evidence_id: ev-74d382c7d0ed9070
  kind: record_content
  reference: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[824],"raw_equal":true},"docs_rows":[{"identifier":"cas:17629-30-0","line":826,"mapping_status":"MAPPED","ontology_id":"CHEBI:189430","preferred_term":"D-Raffinose
    pentahydrate"}],"identifier":"cas:17629-30-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:189430","ontology_label":"Raffinose
    Pentahydrate","ontology_source":"CHEBI"},"preferred_term":"D-Raffinose pentahydrate","sssom_rows":[{"data_row":906,"object_id":"CHEBI:189430","object_label":"Raffinose
    Pentahydrate","predicate_id":"skos:broadMatch"},{"data_row":907,"object_id":"cas:17629-30-0","object_label":"D-Raffinose
    pentahydrate","predicate_id":"skos:exactMatch"},{"data_row":908,"object_id":"kgmicrobe.compound:d-raffinose_pentahydrate","object_label":"D-Raffinose
    pentahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Raffinose_Pentahydrate","synonym_count":1}'
  snapshot_sha256: 3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49
- evidence_id: ev-6890dabdfef2ada8
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [824]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-297c3b68fd8ffe97
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Raffinose_Pentahydrate; data-row positions=[906, 907,
    908]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":906,"object_id":"CHEBI:189430","object_label":"Raffinose
    Pentahydrate","other":"(2S,3R,4S,5R,6R)-2-[[(2R,3S,4S,5R,6R)-6-[(2S,3S,4S,5R)-3,4-dihydroxy-2,5-bis(hydroxymethyl)oxolan-2-yl]oxy-3,4,5-trihydroxyoxan-2-yl]methoxy]-6-(hydroxymethyl)oxane-3,4,5-triol;pentahydrate","predicate_id":"skos:broadMatch","subject_id":"MIM:D-Raffinose_Pentahydrate","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":907,"object_id":"cas:17629-30-0","object_label":"D-Raffinose
    pentahydrate","other":"CAS:17629-30-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Raffinose_Pentahydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":908,"object_id":"kgmicrobe.compound:d-raffinose_pentahydrate","object_label":"D-Raffinose
    pentahydrate","other":"CAS:17629-30-0","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Raffinose_Pentahydrate","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-c3bf0a0d1250ee2b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[826]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:17629-30-0","line":826,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:189430","preferred_term":"D-Raffinose
    pentahydrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d321e73e176de72a
  kind: prior_review
  reference: reports/yaml_record_review/D-Raffinose_Pentahydrate.md
  locator: '`data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml`:2; Verdict:4;
    Identity:12; Validation:30; Evidence:49; Completeness:69; Recommended Edits:77'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1b2f1438d114a805d9840f9007f18a99d5c29d3a8cfcc97a66ce8c9d4206981e
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml`,\
    \ promote the\n  record from `identifier: cas:17629-30-0` plus\n  `mapping_quality:\
    \ NARROW_MATCH` to CHEBI-primary exact identity at\n  `CHEBI:189430`; rerun synchronization\
    \ and regenerate final SSSOM so the\n  narrow parent and registry rows are replaced\
    \ by an exact\n  `MIM:D-Raffinose_Pentahydrate skos:exactMatch CHEBI:189430` row.\n\
    - Either replace the computational `CARBON_SOURCE` evidence with direct\n  CultureBotHT\
    \ or source-backed media-role evidence for this ingredient, or\n  remove the role\
    \ facet; then rerun strict validation and the final SSSOM\n  build."
- evidence_id: ev-a51f67c803a32983
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[476,1571]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49","finding_id":"SEM:167a4a3c3b13354872cd","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49","finding_id":"SEM:e7b4dba58cd6005df762","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-26caf769e191d1b6
  kind: record_content
  reference: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[824],"raw_equal":true},"docs_rows":[{"identifier":"cas:17629-30-0","line":826,"mapping_status":"MAPPED","ontology_id":"CHEBI:189430","preferred_term":"D-Raffinose
    pentahydrate"}],"identifier":"cas:17629-30-0","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:189430","ontology_label":"Raffinose
    Pentahydrate","ontology_source":"CHEBI"},"preferred_term":"D-Raffinose pentahydrate","sssom_rows":[{"data_row":906,"object_id":"CHEBI:189430","object_label":"Raffinose
    Pentahydrate","predicate_id":"skos:broadMatch"},{"data_row":907,"object_id":"cas:17629-30-0","object_label":"D-Raffinose
    pentahydrate","predicate_id":"skos:exactMatch"},{"data_row":908,"object_id":"kgmicrobe.compound:d-raffinose_pentahydrate","object_label":"D-Raffinose
    pentahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Raffinose_Pentahydrate","synonym_count":1}'
  snapshot_sha256: 3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49
- evidence_id: ev-b194f10c355f911c
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-8f31af00b5158419]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-8f31af00b5158419 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-13cd824c779ed1e0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-74d382c7d0ed9070
  - ev-6890dabdfef2ada8
  - ev-297c3b68fd8ffe97
  - ev-c3bf0a0d1250ee2b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d942477f6550f1f4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-d321e73e176de72a
  - ev-74d382c7d0ed9070
  - ev-a51f67c803a32983
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:19:42Z;
    reviewed SHA-256=3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49;
    current SHA-256=3b0200dd4a0b0e7127b13ba0a4b278c6faa094562534f9b72a4f4c4870b87c49;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Raffinose_Pentahydrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The pentahydrate
    CAS and structure pass, but CHEBI:189430 is now an exact pentahydrate term and
    the carbon role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d321e73e176de72a
    - ev-74d382c7d0ed9070
  - name: legacy-native-ids
    value: '["SEM:167a4a3c3b13354872cd","SEM:e7b4dba58cd6005df762"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-74d382c7d0ed9070
    - ev-d321e73e176de72a
    - ev-a51f67c803a32983
- assessment_id: a-26caf769e191d1b6
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-d321e73e176de72a
  - ev-26caf769e191d1b6
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d321e73e176de72a
    - ev-26caf769e191d1b6
findings:
- finding_id: rec-f-8f31af00b5158419
  issue_key: mim-reconciliation-role-support-33582a299a07d746
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Raffinose pentahydrate'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-33582a299a07d746
  evidence_ids:
  - ev-d321e73e176de72a
  - ev-26caf769e191d1b6
  - ev-b194f10c355f911c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-8f31af00b5158419
actions:
- action_id: rec-action-8f31af00b5158419
  description: 'Reassess prediction-only role support: D-Raffinose pentahydrate'
  finding_ids:
  - rec-f-8f31af00b5158419
  target_ids:
  - record-33582a299a07d746
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Raffinose_Pentahydrate.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
