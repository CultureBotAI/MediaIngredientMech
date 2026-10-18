# Per-record structured review: D-fructose (data/ingredients/mapped/D-fructose.yaml)

- Review: 20261017T083000Z-d-fructose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-fructose (data/ingredients/mapped/D-fructose.yaml, record-ae8efc7cf6fc5c77, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-fructose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-fructose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ae8efc7cf6fc5c77 | data/ingredients/mapped/D-fructose.yaml | maintained | D-fructose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ae8efc7cf6fc5c77 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-ae8efc7cf6fc5c77 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ae8efc7cf6fc5c77 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ae8efc7cf6fc5c77.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ae8efc7cf6fc5c77.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:06Z; reviewed SHA-256=05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e; current SHA-256=05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050206Z-D-fructose.md","reports/yaml_record_review/D-fructose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/D-fructose.md&#96; after the record changed from 2c443404266f5d8e8260d733e235e3d7ee6293519afa8bf0e9afca231be8abfb to 05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-ae8efc7cf6fc5c77.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-ed25667ba2cf7e98: Reassess prediction-only role support: D-Fructose

major / open / confirmed; issue key: mim-reconciliation-role-support-ae8efc7cf6fc5c77.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-ed25667ba2cf7e98

Reassess prediction-only role support: D-Fructose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0c41798cf0191686 | data/ingredients/mapped/D-fructose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[832],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15824","line":834,"mapping_status":"MAPPED","ontology_id":"CHEBI:15824","preferred_term":"D-Fructose"}],"identifier":"CHEBI:15824","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":53,"edge_count":53,"occurrences":53},"occurrence_statistics":{"media_count":53,"total_occurrences":53},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15824","ontology_label":"D-fructose","ontology_source":"CHEBI"},"preferred_term":"D-Fructose","sssom_rows":[{"data_row":928,"object_id":"CHEBI:15824","object_label":"D-fructose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-fructose","synonym_count":9} |
| ev-24f87b350ab731fb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [832] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-313753c68f54d274 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-fructose; data-row positions=[928] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":928,"object_id":"CHEBI:15824","object_label":"D-fructose","other":"(-)-D-fructose&#124;(2)-d-fructose&#124;D-Fru&#124;D-arabino-hex-2-ulose&#124;D-laevulose&#124;Laevulose&#124;CAS:57-48-7","predicate_id":"skos:exactMatch","subject_id":"MIM:D-fructose","validation_method":"manual:retire_wrong_form_names&#124;OTHER&#124;2026-09-23"}] |
| ev-fcd2e2c5c6f99a6f | docs/data/mapped_ingredients.csv; CSV lines=[834] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15824","line":834,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"53","ontology_id":"CHEBI:15824","preferred_term":"D-Fructose","total_occurrences":"53"}] |
| ev-1a98de84302cef15 | reports/yaml_record_review/20261001T050206Z-D-fructose.md; YAML Record Review: D-Fructose:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bb1929287b073175 | reports/yaml_record_review/D-fructose.md; &#96;data/ingredients/mapped/D-fructose.yaml&#96;:2; Verdict:4; Identity:12; Validation:26; Evidence:46; Completeness:67; Recommended Edits:74 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3f91abe79741eb89 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[492,1752] | context_only | [{"current_record_sha256":"05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e","finding_id":"SEM:2b5b31e7bad35cdff218","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e","finding_id":"SEM:cab4036a5927a7a1af55","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-2a39d5467c6e9812 | data/ingredients/mapped/D-fructose.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-7dfe0e98fdb022aa | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-ed25667ba2cf7e98] | context_only | Predecessor structured review finding f-ed25667ba2cf7e98 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-fructose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-fructose (data/ingredients/mapped/D-fructose.yaml)'
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
summary: Per-record structured review for D-fructose (data/ingredients/mapped/D-fructose.yaml,
  record-ae8efc7cf6fc5c77, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-fructose.yaml
    sha256: 05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e
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
  - path: reports/yaml_record_review/20261001T050206Z-D-fructose.md
    sha256: 6ae8ffd93a303cd21203754603dbef45635033499443a12de74a02e3038c944c
    role: context
  - path: reports/yaml_record_review/D-fructose.md
    sha256: dc349f2aaaede3028b405c59c53c787b2ffa8fd34335c34e1664f7d145d25326
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ae8efc7cf6fc5c77
  path: data/ingredients/mapped/D-fructose.yaml
  label: D-fructose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-fructose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-fructose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-fructose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ae8efc7cf6fc5c77
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ae8efc7cf6fc5c77
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-ae8efc7cf6fc5c77
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ae8efc7cf6fc5c77
evidence:
- evidence_id: ev-0c41798cf0191686
  kind: record_content
  reference: data/ingredients/mapped/D-fructose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[832],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15824","line":834,"mapping_status":"MAPPED","ontology_id":"CHEBI:15824","preferred_term":"D-Fructose"}],"identifier":"CHEBI:15824","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":53,"edge_count":53,"occurrences":53},"occurrence_statistics":{"media_count":53,"total_occurrences":53},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15824","ontology_label":"D-fructose","ontology_source":"CHEBI"},"preferred_term":"D-Fructose","sssom_rows":[{"data_row":928,"object_id":"CHEBI:15824","object_label":"D-fructose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-fructose","synonym_count":9}'
  snapshot_sha256: 05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e
- evidence_id: ev-24f87b350ab731fb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [832]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-313753c68f54d274
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-fructose; data-row positions=[928]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":928,"object_id":"CHEBI:15824","object_label":"D-fructose","other":"(-)-D-fructose|(2)-d-fructose|D-Fru|D-arabino-hex-2-ulose|D-laevulose|Laevulose|CAS:57-48-7","predicate_id":"skos:exactMatch","subject_id":"MIM:D-fructose","validation_method":"manual:retire_wrong_form_names|OTHER|2026-09-23"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-fcd2e2c5c6f99a6f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[834]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15824","line":834,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"53","ontology_id":"CHEBI:15824","preferred_term":"D-Fructose","total_occurrences":"53"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1a98de84302cef15
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050206Z-D-fructose.md
  locator: 'YAML Record Review: D-Fructose:2; Target:10; Validation:20; Identity and
    Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6ae8ffd93a303cd21203754603dbef45635033499443a12de74a02e3038c944c
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/D-fructose.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The exact
    CHEBI identity, 53/53 count, and CultureMech carbon role pass, but final SSSOM
    exports Optional ingredient and the energy role is computational.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/D-fructose.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/D-fructose.yaml`,
    `just validate-terms data/ingredients/mapped/D-fructose.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-bb1929287b073175
  kind: prior_review
  reference: reports/yaml_record_review/D-fructose.md
  locator: '`data/ingredients/mapped/D-fructose.yaml`:2; Verdict:4; Identity:12; Validation:26;
    Evidence:46; Completeness:67; Recommended Edits:74'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: dc349f2aaaede3028b405c59c53c787b2ffa8fd34335c34e1664f7d145d25326
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/D-fructose.yaml`,\
    \ demote or reject the\n  `Optional ingredient` `RAW_TEXT` synonym so the final\
    \ SSSOM `other` field no\n  longer exports it for `MIM:D-fructose`; rebuild the\
    \ final SSSOM and rerun the\n  SSSOM/product validators.\n- Major: either replace\
    \ the computational `ENERGY_SOURCE` evidence with direct,\n  source-backed evidence\
    \ for D-fructose as an energy source or remove that role\n  facet; then rerun\
    \ strict validation and the final SSSOM gates."
- evidence_id: ev-3f91abe79741eb89
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[492,1752]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e","finding_id":"SEM:2b5b31e7bad35cdff218","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e","finding_id":"SEM:cab4036a5927a7a1af55","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-2a39d5467c6e9812
  kind: record_content
  reference: data/ingredients/mapped/D-fructose.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: 05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e
- evidence_id: ev-7dfe0e98fdb022aa
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-ed25667ba2cf7e98]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-ed25667ba2cf7e98 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-8d1bd60d3c272ed8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ae8efc7cf6fc5c77
  evidence_ids:
  - ev-0c41798cf0191686
  - ev-24f87b350ab731fb
  - ev-313753c68f54d274
  - ev-fcd2e2c5c6f99a6f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e3191f0e1bafe5fd
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ae8efc7cf6fc5c77
  evidence_ids:
  - ev-1a98de84302cef15
  - ev-bb1929287b073175
  - ev-0c41798cf0191686
  - ev-3f91abe79741eb89
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:06Z;
    reviewed SHA-256=05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e;
    current SHA-256=05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050206Z-D-fructose.md","reports/yaml_record_review/D-fructose.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/D-fructose.md` after the record changed from 2c443404266f5d8e8260d733e235e3d7ee6293519afa8bf0e9afca231be8abfb
    to 05b9d5a79984d5afd90077147ed421ce227ea80946344db298c80e985f8f718e; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1a98de84302cef15
    - ev-bb1929287b073175
    - ev-0c41798cf0191686
  - name: legacy-native-ids
    value: '["SEM:2b5b31e7bad35cdff218","SEM:cab4036a5927a7a1af55"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0c41798cf0191686
    - ev-1a98de84302cef15
    - ev-bb1929287b073175
    - ev-3f91abe79741eb89
- assessment_id: a-2a39d5467c6e9812
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ae8efc7cf6fc5c77
  evidence_ids:
  - ev-1a98de84302cef15
  - ev-bb1929287b073175
  - ev-2a39d5467c6e9812
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1a98de84302cef15
    - ev-bb1929287b073175
    - ev-2a39d5467c6e9812
findings:
- finding_id: rec-f-ed25667ba2cf7e98
  issue_key: mim-reconciliation-role-support-ae8efc7cf6fc5c77
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: D-Fructose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-ae8efc7cf6fc5c77
  evidence_ids:
  - ev-1a98de84302cef15
  - ev-bb1929287b073175
  - ev-2a39d5467c6e9812
  - ev-7dfe0e98fdb022aa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-fructose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-ed25667ba2cf7e98
actions:
- action_id: rec-action-ed25667ba2cf7e98
  description: 'Reassess prediction-only role support: D-Fructose'
  finding_ids:
  - rec-f-ed25667ba2cf7e98
  target_ids:
  - record-ae8efc7cf6fc5c77
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-fructose.yaml
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
