# Per-record structured review: D-Glucose-6-Phosphate_Sodium_Salt (data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml)

- Review: 20261017T083000Z-d-glucose-6-phosphate-sodium-salt
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-Glucose-6-Phosphate_Sodium_Salt (data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml, record-81f5cb7f2e8a65c8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-81f5cb7f2e8a65c8 | data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml | maintained | D-Glucose-6-Phosphate_Sodium_Salt |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-81f5cb7f2e8a65c8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-81f5cb7f2e8a65c8 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-81f5cb7f2e8a65c8 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-81f5cb7f2e8a65c8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-81f5cb7f2e8a65c8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:13:57Z; reviewed SHA-256=92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb; current SHA-256=92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb; hash_changed=False. Reports=["reports/yaml_record_review/D-Glucose-6-Phosphate_Sodium_Salt.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS primary, CHEBI parent, registry rows, 1/1 count, and final SSSOM payload pass, but the carbon role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-81f5cb7f2e8a65c8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-44650a010f98b824: Reassess prediction-only role support: D-Glucose-6-Phosphate sodium salt

major / open / confirmed; issue key: mim-reconciliation-role-support-81f5cb7f2e8a65c8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-44650a010f98b824

Reassess prediction-only role support: D-Glucose-6-Phosphate sodium salt

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-bbb24c2462f1762b | data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[813],"raw_equal":true},"docs_rows":[{"identifier":"cas:54010-71-8","line":815,"mapping_status":"MAPPED","ontology_id":"CHEBI:14314","preferred_term":"D-Glucose-6-Phosphate sodium salt"}],"identifier":"cas:54010-71-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:14314","ontology_label":"D-glucose 6-phosphate","ontology_source":"CHEBI"},"preferred_term":"D-Glucose-6-Phosphate sodium salt","sssom_rows":[{"data_row":889,"object_id":"CHEBI:14314","object_label":"D-glucose 6-phosphate","predicate_id":"skos:broadMatch"},{"data_row":890,"object_id":"cas:54010-71-8","object_label":"D-Glucose-6-Phosphate sodium salt","predicate_id":"skos:exactMatch"},{"data_row":891,"object_id":"kgmicrobe.compound:d-glucose-6-phosphate_sodium_salt","object_label":"D-Glucose-6-Phosphate sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","synonym_count":0} |
| ev-fb2b75b118a65f5a | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [813] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-525aee9175f24afc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-Glucose-6-Phosphate_Sodium_Salt; data-row positions=[889, 890, 891] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":889,"object_id":"CHEBI:14314","object_label":"D-glucose 6-phosphate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":890,"object_id":"cas:54010-71-8","object_label":"D-Glucose-6-Phosphate sodium salt","other":"CAS:54010-71-8","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":891,"object_id":"kgmicrobe.compound:d-glucose-6-phosphate_sodium_salt","object_label":"D-Glucose-6-Phosphate sodium salt","other":"CAS:54010-71-8","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-d0c312c3273a7580 | docs/data/mapped_ingredients.csv; CSV lines=[815] | supports | Published identity and count rows inspected: [{"identifier":"cas:54010-71-8","line":815,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:14314","preferred_term":"D-Glucose-6-Phosphate sodium salt","total_occurrences":"1"}] |
| ev-0db23a903fbc2d7f | reports/yaml_record_review/D-Glucose-6-Phosphate_Sodium_Salt.md; &#96;data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:47; Completeness:60; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a8ce0b2119c75039 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[467,1763] | context_only | [{"current_record_sha256":"92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb","finding_id":"SEM:55d9db6fe54b13ae16ea","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb","finding_id":"SEM:bb58bd8e676316c6d1e0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-c8a482092c0aa459 | data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[813],"raw_equal":true},"docs_rows":[{"identifier":"cas:54010-71-8","line":815,"mapping_status":"MAPPED","ontology_id":"CHEBI:14314","preferred_term":"D-Glucose-6-Phosphate sodium salt"}],"identifier":"cas:54010-71-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:14314","ontology_label":"D-glucose 6-phosphate","ontology_source":"CHEBI"},"preferred_term":"D-Glucose-6-Phosphate sodium salt","sssom_rows":[{"data_row":889,"object_id":"CHEBI:14314","object_label":"D-glucose 6-phosphate","predicate_id":"skos:broadMatch"},{"data_row":890,"object_id":"cas:54010-71-8","object_label":"D-Glucose-6-Phosphate sodium salt","predicate_id":"skos:exactMatch"},{"data_row":891,"object_id":"kgmicrobe.compound:d-glucose-6-phosphate_sodium_salt","object_label":"D-Glucose-6-Phosphate sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","synonym_count":0} |
| ev-bb16474ea0c5f168 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-44650a010f98b824] | context_only | Predecessor structured review finding f-44650a010f98b824 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-glucose-6-phosphate-sodium-salt
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-Glucose-6-Phosphate_Sodium_Salt (data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml)'
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
summary: Per-record structured review for D-Glucose-6-Phosphate_Sodium_Salt (data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml,
  record-81f5cb7f2e8a65c8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
    sha256: 92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb
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
  - path: reports/yaml_record_review/D-Glucose-6-Phosphate_Sodium_Salt.md
    sha256: 1b16c4e27de9699d9f453e679547e556a10a33362e4a6313bed3d3ebb5d15f25
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-81f5cb7f2e8a65c8
  path: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
  label: D-Glucose-6-Phosphate_Sodium_Salt
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-81f5cb7f2e8a65c8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-bbb24c2462f1762b
  - ev-fb2b75b118a65f5a
  - ev-525aee9175f24afc
  - ev-d0c312c3273a7580
  - ev-c8a482092c0aa459
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-bbb24c2462f1762b
  - ev-a8ce0b2119c75039
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-0db23a903fbc2d7f
  - ev-a8ce0b2119c75039
  - ev-bb16474ea0c5f168
evidence:
- evidence_id: ev-bbb24c2462f1762b
  kind: record_content
  reference: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[813],"raw_equal":true},"docs_rows":[{"identifier":"cas:54010-71-8","line":815,"mapping_status":"MAPPED","ontology_id":"CHEBI:14314","preferred_term":"D-Glucose-6-Phosphate
    sodium salt"}],"identifier":"cas:54010-71-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:14314","ontology_label":"D-glucose
    6-phosphate","ontology_source":"CHEBI"},"preferred_term":"D-Glucose-6-Phosphate
    sodium salt","sssom_rows":[{"data_row":889,"object_id":"CHEBI:14314","object_label":"D-glucose
    6-phosphate","predicate_id":"skos:broadMatch"},{"data_row":890,"object_id":"cas:54010-71-8","object_label":"D-Glucose-6-Phosphate
    sodium salt","predicate_id":"skos:exactMatch"},{"data_row":891,"object_id":"kgmicrobe.compound:d-glucose-6-phosphate_sodium_salt","object_label":"D-Glucose-6-Phosphate
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","synonym_count":0}'
  snapshot_sha256: 92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb
- evidence_id: ev-fb2b75b118a65f5a
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [813]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-525aee9175f24afc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-Glucose-6-Phosphate_Sodium_Salt; data-row positions=[889,
    890, 891]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":889,"object_id":"CHEBI:14314","object_label":"D-glucose
    6-phosphate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":890,"object_id":"cas:54010-71-8","object_label":"D-Glucose-6-Phosphate
    sodium salt","other":"CAS:54010-71-8","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":891,"object_id":"kgmicrobe.compound:d-glucose-6-phosphate_sodium_salt","object_label":"D-Glucose-6-Phosphate
    sodium salt","other":"CAS:54010-71-8","predicate_id":"skos:exactMatch","subject_id":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d0c312c3273a7580
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[815]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:54010-71-8","line":815,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:14314","preferred_term":"D-Glucose-6-Phosphate
    sodium salt","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0db23a903fbc2d7f
  kind: prior_review
  reference: reports/yaml_record_review/D-Glucose-6-Phosphate_Sodium_Salt.md
  locator: '`data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml`:2; Verdict:4;
    Identity:11; Validation:27; Evidence:47; Completeness:60; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1b16c4e27de9699d9f453e679547e556a10a33362e4a6313bed3d3ebb5d15f25
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml`,\
    \ either\n  replace the computational `CARBON_SOURCE` evidence with direct source-backed\n\
    \  media-role evidence for this sodium salt, or remove the role facet; then\n\
    \  rerun strict validation and the final SSSOM build."
- evidence_id: ev-a8ce0b2119c75039
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[467,1763]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb","finding_id":"SEM:55d9db6fe54b13ae16ea","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb","finding_id":"SEM:bb58bd8e676316c6d1e0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-c8a482092c0aa459
  kind: record_content
  reference: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[813],"raw_equal":true},"docs_rows":[{"identifier":"cas:54010-71-8","line":815,"mapping_status":"MAPPED","ontology_id":"CHEBI:14314","preferred_term":"D-Glucose-6-Phosphate
    sodium salt"}],"identifier":"cas:54010-71-8","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:14314","ontology_label":"D-glucose
    6-phosphate","ontology_source":"CHEBI"},"preferred_term":"D-Glucose-6-Phosphate
    sodium salt","sssom_rows":[{"data_row":889,"object_id":"CHEBI:14314","object_label":"D-glucose
    6-phosphate","predicate_id":"skos:broadMatch"},{"data_row":890,"object_id":"cas:54010-71-8","object_label":"D-Glucose-6-Phosphate
    sodium salt","predicate_id":"skos:exactMatch"},{"data_row":891,"object_id":"kgmicrobe.compound:d-glucose-6-phosphate_sodium_salt","object_label":"D-Glucose-6-Phosphate
    sodium salt","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-Glucose-6-Phosphate_Sodium_Salt","synonym_count":0}'
  snapshot_sha256: 92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb
- evidence_id: ev-bb16474ea0c5f168
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-44650a010f98b824]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-44650a010f98b824 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-38ed5dd9252798e0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-bbb24c2462f1762b
  - ev-fb2b75b118a65f5a
  - ev-525aee9175f24afc
  - ev-d0c312c3273a7580
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-69fd7a4a455ecd03
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-0db23a903fbc2d7f
  - ev-bbb24c2462f1762b
  - ev-a8ce0b2119c75039
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:13:57Z;
    reviewed SHA-256=92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb;
    current SHA-256=92e0e4a5be91c1d5be30056ba6e68de884b3f59aecc8281b4ccdf5cf26935feb;
    hash_changed=False. Reports=["reports/yaml_record_review/D-Glucose-6-Phosphate_Sodium_Salt.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CAS
    primary, CHEBI parent, registry rows, 1/1 count, and final SSSOM payload pass,
    but the carbon role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0db23a903fbc2d7f
    - ev-bbb24c2462f1762b
  - name: legacy-native-ids
    value: '["SEM:55d9db6fe54b13ae16ea","SEM:bb58bd8e676316c6d1e0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-bbb24c2462f1762b
    - ev-0db23a903fbc2d7f
    - ev-a8ce0b2119c75039
- assessment_id: a-c8a482092c0aa459
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-0db23a903fbc2d7f
  - ev-c8a482092c0aa459
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0db23a903fbc2d7f
    - ev-c8a482092c0aa459
findings:
- finding_id: rec-f-44650a010f98b824
  issue_key: mim-reconciliation-role-support-81f5cb7f2e8a65c8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Glucose-6-Phosphate sodium salt'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-81f5cb7f2e8a65c8
  evidence_ids:
  - ev-0db23a903fbc2d7f
  - ev-c8a482092c0aa459
  - ev-bb16474ea0c5f168
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
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
    finding_id: f-44650a010f98b824
actions:
- action_id: rec-action-44650a010f98b824
  description: 'Reassess prediction-only role support: D-Glucose-6-Phosphate sodium
    salt'
  finding_ids:
  - rec-f-44650a010f98b824
  target_ids:
  - record-81f5cb7f2e8a65c8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-Glucose-6-Phosphate_Sodium_Salt.yaml
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
