# Per-record structured review: Arabitol (data/ingredients/mapped/Arabitol.yaml)

- Review: 20261017T083000Z-arabitol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Arabitol (data/ingredients/mapped/Arabitol.yaml, record-ce478baac929216f, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Arabitol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Arabitol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ce478baac929216f | data/ingredients/mapped/Arabitol.yaml | maintained | Arabitol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ce478baac929216f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ce478baac929216f | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ce478baac929216f | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ce478baac929216f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ce478baac929216f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:35:24Z; reviewed SHA-256=046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370; current SHA-256=046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370; hash_changed=False. Reports=["reports/yaml_record_review/Arabitol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-backed L-arabinitol identity, L-form synonyms, CultureMech memberships, and MicrobeDecoder merge pass, but the carbon-source role is only a provisional ChEBI-ancestry inference.

### Historical provisional-role concern

evidence: concern. Targets: record-ce478baac929216f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-5d4ecdd3361b6dd2: Reassess prediction-only role support: Arabitol

major / open / confirmed; issue key: mim-reconciliation-role-support-ce478baac929216f.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-5d4ecdd3361b6dd2

Reassess prediction-only role support: Arabitol

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-24749b39f8fc3a3e | data/ingredients/mapped/Arabitol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[510],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18403","line":512,"mapping_status":"MAPPED","ontology_id":"CHEBI:18403","preferred_term":"Arabitol"}],"identifier":"CHEBI:18403","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18403","ontology_label":"L-arabinitol","ontology_source":"CHEBI"},"preferred_term":"Arabitol","sssom_rows":[{"data_row":419,"object_id":"CHEBI:18403","object_label":"L-arabinitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Arabitol","synonym_count":6} |
| ev-37d5f3c2a2a76af6 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [510] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fcd31e8650ed952d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Arabitol; data-row positions=[419] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":419,"object_id":"CHEBI:18403","object_label":"L-arabinitol","other":"L-Arabinol&#124;L-Arabitol&#124;L-Lyxitol&#124;L-arabitol (L-arabinitol)&#124;(+)-L-lyxitol&#124;CAS:7643-75-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Arabitol","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-bc5f6cd041aec013 | docs/data/mapped_ingredients.csv; CSV lines=[512] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:18403","line":512,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:18403","preferred_term":"Arabitol","total_occurrences":"4"}] |
| ev-c1cb392047f596f8 | reports/yaml_record_review/Arabitol.md; &#96;data/ingredients/mapped/Arabitol.yaml&#96;:2; Verdict:4; Identity:11; Validation:28; Evidence:46; Completeness:68; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-da0fa44e846c8a9d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[275,1408] | context_only | [{"current_record_sha256":"046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370","finding_id":"SEM:e8934c3b8b16be6cfee5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370","finding_id":"SEM:77b2ae729b28225eadc8","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-64251d1d30ff26eb | data/ingredients/mapped/Arabitol.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[510],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18403","line":512,"mapping_status":"MAPPED","ontology_id":"CHEBI:18403","preferred_term":"Arabitol"}],"identifier":"CHEBI:18403","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18403","ontology_label":"L-arabinitol","ontology_source":"CHEBI"},"preferred_term":"Arabitol","sssom_rows":[{"data_row":419,"object_id":"CHEBI:18403","object_label":"L-arabinitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Arabitol","synonym_count":6} |
| ev-223882e9854469ae | reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml; findings[finding_id=f-5d4ecdd3361b6dd2] | context_only | Predecessor structured review finding f-5d4ecdd3361b6dd2 in 20261011T024631Z-mim-reconcile-all-batch-03 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-arabitol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Arabitol (data/ingredients/mapped/Arabitol.yaml)'
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
summary: Per-record structured review for Arabitol (data/ingredients/mapped/Arabitol.yaml,
  record-ce478baac929216f, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Arabitol.yaml
    sha256: 046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Arabitol.md
    sha256: 475cd02f17eb085525ec9aeef7a3cd596ff453a8232993444f6935a478f58434
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ce478baac929216f
  path: data/ingredients/mapped/Arabitol.yaml
  label: Arabitol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Arabitol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Arabitol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Arabitol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ce478baac929216f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-24749b39f8fc3a3e
  - ev-37d5f3c2a2a76af6
  - ev-fcd31e8650ed952d
  - ev-bc5f6cd041aec013
  - ev-64251d1d30ff26eb
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-24749b39f8fc3a3e
  - ev-da0fa44e846c8a9d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-c1cb392047f596f8
  - ev-da0fa44e846c8a9d
  - ev-223882e9854469ae
evidence:
- evidence_id: ev-24749b39f8fc3a3e
  kind: record_content
  reference: data/ingredients/mapped/Arabitol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[510],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18403","line":512,"mapping_status":"MAPPED","ontology_id":"CHEBI:18403","preferred_term":"Arabitol"}],"identifier":"CHEBI:18403","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18403","ontology_label":"L-arabinitol","ontology_source":"CHEBI"},"preferred_term":"Arabitol","sssom_rows":[{"data_row":419,"object_id":"CHEBI:18403","object_label":"L-arabinitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Arabitol","synonym_count":6}'
  snapshot_sha256: 046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370
- evidence_id: ev-37d5f3c2a2a76af6
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [510]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fcd31e8650ed952d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Arabitol; data-row positions=[419]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":419,"object_id":"CHEBI:18403","object_label":"L-arabinitol","other":"L-Arabinol|L-Arabitol|L-Lyxitol|L-arabitol
    (L-arabinitol)|(+)-L-lyxitol|CAS:7643-75-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Arabitol","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bc5f6cd041aec013
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[512]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:18403","line":512,"mapping_quality":"CAS_RN_LOOKUP","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:18403","preferred_term":"Arabitol","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c1cb392047f596f8
  kind: prior_review
  reference: reports/yaml_record_review/Arabitol.md
  locator: '`data/ingredients/mapped/Arabitol.yaml`:2; Verdict:4; Identity:11; Validation:28;
    Evidence:46; Completeness:68; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 475cd02f17eb085525ec9aeef7a3cd596ff453a8232993444f6935a478f58434
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Arabitol.yaml`, remove\n\
    \  `nutritional_roles.CARBON_SOURCE` unless direct source evidence for\n  L-arabinitol\
    \ as a carbon source is attached to that role.\n- Regenerate synchronized products,\
    \ then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n  `uv run\
    \ linkml-term-validator validate-data data/ingredients/mapped/Arabitol.yaml -s\
    \ src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-da0fa44e846c8a9d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[275,1408]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370","finding_id":"SEM:e8934c3b8b16be6cfee5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370","finding_id":"SEM:77b2ae729b28225eadc8","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-64251d1d30ff26eb
  kind: record_content
  reference: data/ingredients/mapped/Arabitol.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[510],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:18403","line":512,"mapping_status":"MAPPED","ontology_id":"CHEBI:18403","preferred_term":"Arabitol"}],"identifier":"CHEBI:18403","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CAS_RN_LOOKUP","ontology_id":"CHEBI:18403","ontology_label":"L-arabinitol","ontology_source":"CHEBI"},"preferred_term":"Arabitol","sssom_rows":[{"data_row":419,"object_id":"CHEBI:18403","object_label":"L-arabinitol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Arabitol","synonym_count":6}'
  snapshot_sha256: 046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370
- evidence_id: ev-223882e9854469ae
  kind: prior_review
  reference: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
  locator: findings[finding_id=f-5d4ecdd3361b6dd2]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-5d4ecdd3361b6dd2 in 20261011T024631Z-mim-reconcile-all-batch-03
  snapshot_sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
assessments:
- assessment_id: a-2adede7e70910dbb
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-24749b39f8fc3a3e
  - ev-37d5f3c2a2a76af6
  - ev-fcd31e8650ed952d
  - ev-bc5f6cd041aec013
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9cd21a517859e90b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-c1cb392047f596f8
  - ev-24749b39f8fc3a3e
  - ev-da0fa44e846c8a9d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:35:24Z;
    reviewed SHA-256=046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370;
    current SHA-256=046401fe5681668f663a4e09ff4676c4f3b1f1758e1f2057be28bde3e4d32370;
    hash_changed=False. Reports=["reports/yaml_record_review/Arabitol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS-backed L-arabinitol
    identity, L-form synonyms, CultureMech memberships, and MicrobeDecoder merge pass,
    but the carbon-source role is only a provisional ChEBI-ancestry inference.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c1cb392047f596f8
    - ev-24749b39f8fc3a3e
  - name: legacy-native-ids
    value: '["SEM:e8934c3b8b16be6cfee5","SEM:77b2ae729b28225eadc8"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-24749b39f8fc3a3e
    - ev-c1cb392047f596f8
    - ev-da0fa44e846c8a9d
- assessment_id: a-64251d1d30ff26eb
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-c1cb392047f596f8
  - ev-64251d1d30ff26eb
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c1cb392047f596f8
    - ev-64251d1d30ff26eb
findings:
- finding_id: rec-f-5d4ecdd3361b6dd2
  issue_key: mim-reconciliation-role-support-ce478baac929216f
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Arabitol'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ce478baac929216f
  evidence_ids:
  - ev-c1cb392047f596f8
  - ev-64251d1d30ff26eb
  - ev-223882e9854469ae
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Arabitol.yaml
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
    review_id: 20261011T024631Z-mim-reconcile-all-batch-03
    finding_id: f-5d4ecdd3361b6dd2
actions:
- action_id: rec-action-5d4ecdd3361b6dd2
  description: 'Reassess prediction-only role support: Arabitol'
  finding_ids:
  - rec-f-5d4ecdd3361b6dd2
  target_ids:
  - record-ce478baac929216f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Arabitol.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
