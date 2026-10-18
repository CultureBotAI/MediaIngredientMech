# Per-record structured review: 6-O-Acetyl-D-glucose (data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml)

- Review: 20261017T083000Z-6-o-acetyl-d-glucose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 6-O-Acetyl-D-glucose (data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml, record-5732b0b98ff0297d, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5732b0b98ff0297d | data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml | maintained | 6-O-Acetyl-D-glucose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5732b0b98ff0297d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5732b0b98ff0297d | Role assertions on nutritional_roles[0], nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5732b0b98ff0297d | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5732b0b98ff0297d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5732b0b98ff0297d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:45:16Z; reviewed SHA-256=38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c; current SHA-256=38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c; hash_changed=False. Reports=["reports/yaml_record_review/6-O-Acetyl-D-glucose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, exact synonym, chemistry, SSSOM, and aggregate pass, but the carbon-source and energy-source roles are only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-5732b0b98ff0297d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-541cb9ee80ea9cdb: Reassess prediction-only role support: 6-O-Acetyl-D-glucose

major / open / confirmed; issue key: mim-reconciliation-role-support-5732b0b98ff0297d.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-541cb9ee80ea9cdb

Reassess prediction-only role support: 6-O-Acetyl-D-glucose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-402b7982d9d86757 | data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[416],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17901","line":418,"mapping_status":"MAPPED","ontology_id":"CHEBI:17901","preferred_term":"6-O-Acetyl-D-glucose"}],"identifier":"CHEBI:17901","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17901","ontology_label":"6-O-acetyl-D-glucose","ontology_source":"CHEBI"},"preferred_term":"6-O-Acetyl-D-glucose","sssom_rows":[{"data_row":243,"object_id":"CHEBI:17901","object_label":"6-O-acetyl-D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:6-O-Acetyl-D-glucose","synonym_count":1} |
| ev-c4a2d1c9650de88f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [416] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9802fe000281629c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:6-O-Acetyl-D-glucose; data-row positions=[243] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":243,"object_id":"CHEBI:17901","object_label":"6-O-acetyl-D-glucose","other":"6-O-acetyl-D-glucopyranose&#124;CAS:7286-45-5","predicate_id":"skos:exactMatch","subject_id":"MIM:6-O-Acetyl-D-glucose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-6fd1cf3e5b9e9be7 | docs/data/mapped_ingredients.csv; CSV lines=[418] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17901","line":418,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17901","preferred_term":"6-O-Acetyl-D-glucose","total_occurrences":"0"}] |
| ev-d25d433fad6f3f7f | reports/yaml_record_review/6-O-Acetyl-D-glucose.md; &#96;data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:35; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-12d7b5b4744bbf06 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[172,1413,1622] | context_only | [{"current_record_sha256":"38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c","finding_id":"SEM:bc4a1639685155ef962d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c","finding_id":"SEM:3fa277310a18d027a386","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c","finding_id":"SEM:aefe1bcddb1722d079fb","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-5e3b5daebafa9efd | data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml; nutritional_roles[0], nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-866c11a0690c62d4 | reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml; findings[finding_id=f-541cb9ee80ea9cdb] | context_only | Predecessor structured review finding f-541cb9ee80ea9cdb in 20261011T024630Z-mim-reconcile-all-batch-02 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-6-o-acetyl-d-glucose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 6-O-Acetyl-D-glucose (data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml)'
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
summary: Per-record structured review for 6-O-Acetyl-D-glucose (data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml,
  record-5732b0b98ff0297d, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
    sha256: 38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c
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
  - path: reports/yaml_record_review/6-O-Acetyl-D-glucose.md
    sha256: 98787deea0fcc2158e6e597dfc8e77cd555fc983c8d4d078a56f9f4c5cac739a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5732b0b98ff0297d
  path: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
  label: 6-O-Acetyl-D-glucose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5732b0b98ff0297d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5732b0b98ff0297d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0], nutritional_roles[1] rely only
    on COMPUTATIONAL_PREDICTION or empty evidence.
  target_ids:
  - record-5732b0b98ff0297d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5732b0b98ff0297d
evidence:
- evidence_id: ev-402b7982d9d86757
  kind: record_content
  reference: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[416],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17901","line":418,"mapping_status":"MAPPED","ontology_id":"CHEBI:17901","preferred_term":"6-O-Acetyl-D-glucose"}],"identifier":"CHEBI:17901","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17901","ontology_label":"6-O-acetyl-D-glucose","ontology_source":"CHEBI"},"preferred_term":"6-O-Acetyl-D-glucose","sssom_rows":[{"data_row":243,"object_id":"CHEBI:17901","object_label":"6-O-acetyl-D-glucose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:6-O-Acetyl-D-glucose","synonym_count":1}'
  snapshot_sha256: 38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c
- evidence_id: ev-c4a2d1c9650de88f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [416]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9802fe000281629c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:6-O-Acetyl-D-glucose; data-row positions=[243]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":243,"object_id":"CHEBI:17901","object_label":"6-O-acetyl-D-glucose","other":"6-O-acetyl-D-glucopyranose|CAS:7286-45-5","predicate_id":"skos:exactMatch","subject_id":"MIM:6-O-Acetyl-D-glucose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6fd1cf3e5b9e9be7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[418]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17901","line":418,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:17901","preferred_term":"6-O-Acetyl-D-glucose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d25d433fad6f3f7f
  kind: prior_review
  reference: reports/yaml_record_review/6-O-Acetyl-D-glucose.md
  locator: '`data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:35; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 98787deea0fcc2158e6e597dfc8e77cd555fc983c8d4d078a56f9f4c5cac739a
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml`,\
    \ either remove the\n  provisional `CARBON_SOURCE` and `ENERGY_SOURCE` roles or\
    \ replace the\n  computational placeholders with source-backed evidence scoped\
    \ to\n  6-O-acetyl-D-glucose.\n- Rebuild `data/curated/mapped_ingredients.yaml`\
    \ and rerun strict validation,\n  SSSOM invariants, and the id/label correspondence\
    \ gate after the role edit."
- evidence_id: ev-12d7b5b4744bbf06
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[172,1413,1622]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c","finding_id":"SEM:bc4a1639685155ef962d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c","finding_id":"SEM:3fa277310a18d027a386","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c","finding_id":"SEM:aefe1bcddb1722d079fb","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-5e3b5daebafa9efd
  kind: record_content
  reference: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
  locator: nutritional_roles[0], nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}},{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c
- evidence_id: ev-866c11a0690c62d4
  kind: prior_review
  reference: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
  locator: findings[finding_id=f-541cb9ee80ea9cdb]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-541cb9ee80ea9cdb in 20261011T024630Z-mim-reconcile-all-batch-02
  snapshot_sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
assessments:
- assessment_id: a-d22ef67055d15d8e
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5732b0b98ff0297d
  evidence_ids:
  - ev-402b7982d9d86757
  - ev-c4a2d1c9650de88f
  - ev-9802fe000281629c
  - ev-6fd1cf3e5b9e9be7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7a679929f3f52a22
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5732b0b98ff0297d
  evidence_ids:
  - ev-d25d433fad6f3f7f
  - ev-402b7982d9d86757
  - ev-12d7b5b4744bbf06
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T06:45:16Z;
    reviewed SHA-256=38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c;
    current SHA-256=38cdc303f8d0473f059bf3d62092132692d95f70c04a671908f1a589a1a3fa7c;
    hash_changed=False. Reports=["reports/yaml_record_review/6-O-Acetyl-D-glucose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI identity, exact synonym, chemistry, SSSOM, and aggregate pass, but the carbon-source
    and energy-source roles are only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d25d433fad6f3f7f
    - ev-402b7982d9d86757
  - name: legacy-native-ids
    value: '["SEM:bc4a1639685155ef962d","SEM:3fa277310a18d027a386","SEM:aefe1bcddb1722d079fb"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-402b7982d9d86757
    - ev-d25d433fad6f3f7f
    - ev-12d7b5b4744bbf06
- assessment_id: a-5e3b5daebafa9efd
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5732b0b98ff0297d
  evidence_ids:
  - ev-d25d433fad6f3f7f
  - ev-5e3b5daebafa9efd
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d25d433fad6f3f7f
    - ev-5e3b5daebafa9efd
findings:
- finding_id: rec-f-541cb9ee80ea9cdb
  issue_key: mim-reconciliation-role-support-5732b0b98ff0297d
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: 6-O-Acetyl-D-glucose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5732b0b98ff0297d
  evidence_ids:
  - ev-d25d433fad6f3f7f
  - ev-5e3b5daebafa9efd
  - ev-866c11a0690c62d4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024630Z-mim-reconcile-all-batch-02
    finding_id: f-541cb9ee80ea9cdb
actions:
- action_id: rec-action-541cb9ee80ea9cdb
  description: 'Reassess prediction-only role support: 6-O-Acetyl-D-glucose'
  finding_ids:
  - rec-f-541cb9ee80ea9cdb
  target_ids:
  - record-5732b0b98ff0297d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/6-O-Acetyl-D-glucose.yaml
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
