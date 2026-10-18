# Per-record structured review: Cocl2_X_2_H2o (data/ingredients/mapped/Cocl2_X_2_H2o.yaml)

- Review: 20261017T083000Z-cocl2-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cocl2_X_2_H2o (data/ingredients/mapped/Cocl2_X_2_H2o.yaml, record-e6bce3f910a889a5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cocl2_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cocl2_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e6bce3f910a889a5 | data/ingredients/mapped/Cocl2_X_2_H2o.yaml | maintained | Cocl2_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e6bce3f910a889a5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e6bce3f910a889a5 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e6bce3f910a889a5 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e6bce3f910a889a5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e6bce3f910a889a5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:55Z; reviewed SHA-256=2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3; current SHA-256=f73cf9c10032f8eba85a5b14a067c541a44ff1722fbb727e0a8223a5f4a1424d; hash_changed=True. Reports=["reports/yaml_record_review/20261001T050155Z-Cocl2_X_2_H2o.md","reports/yaml_record_review/Cocl2_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Cocl2_X_2_H2o.md&#96; after the record changed from a46da48c9462ac8fe0edff72ca633ab0c78f3bd5a397819f57558fbee1ce9d63 to 2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-e6bce3f910a889a5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-17673d435c44a42f: Reassess prediction-only role support: CoCl2 x 2 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-e6bce3f910a889a5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-17673d435c44a42f

Reassess prediction-only role support: CoCl2 x 2 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-78096087a68d920c | data/ingredients/mapped/Cocl2_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[744],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cocl2_x_2_h2o","line":746,"mapping_status":"MAPPED","ontology_id":"CHEBI:35696","preferred_term":"CoCl2 x 2 H2O"}],"identifier":"kgmicrobe.compound:cocl2_x_2_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:35696","ontology_label":"cobalt dichloride","ontology_source":"CHEBI"},"preferred_term":"CoCl2 x 2 H2O","sssom_rows":[{"data_row":797,"object_id":"CHEBI:35696","object_label":"cobalt dichloride","predicate_id":"skos:closeMatch"},{"data_row":798,"object_id":"kgmicrobe.compound:cocl2_x_2_h2o","object_label":"CoCl2 x 2 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cocl2_X_2_H2o","synonym_count":10} |
| ev-b43c6d7fadfb672c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [744] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-54d836426573e9b4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cocl2_X_2_H2o; data-row positions=[797,798] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":797,"object_id":"CHEBI:35696","object_label":"cobalt dichloride","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Cocl2_X_2_H2o","validation_method":"manual:retire_wrong_form_names&#124;OTHER&#124;2026-09-23"},{"data_row":798,"object_id":"kgmicrobe.compound:cocl2_x_2_h2o","object_label":"CoCl2 x 2 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cocl2_X_2_H2o","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-5aafe38288d69829 | docs/data/mapped_ingredients.csv; CSV lines=[746] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cocl2_x_2_h2o","line":746,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:35696","preferred_term":"CoCl2 x 2 H2O","total_occurrences":"5"}] |
| ev-527fa867b57fc618 | reports/yaml_record_review/20261001T050155Z-Cocl2_X_2_H2o.md; YAML Record Review: CoCl2 x 2 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c5f7d88ce196388f | reports/yaml_record_review/Cocl2_X_2_H2o.md; &#96;data/ingredients/mapped/Cocl2_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:30; Evidence:50; Completeness:70; Recommended Edits:78 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e12aa4528ba436ad | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[432,1697] | context_only | [{"current_record_sha256":"2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3","finding_id":"SEM:058def08fac3452ea333","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3","finding_id":"SEM:580e6cd11e334eed70c7","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-bcba250dc15ca4ca | data/ingredients/mapped/Cocl2_X_2_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-009e3f3cfdfdb16c | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-17673d435c44a42f] | context_only | Predecessor structured review finding f-17673d435c44a42f in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cocl2-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cocl2_X_2_H2o (data/ingredients/mapped/Cocl2_X_2_H2o.yaml)'
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
summary: Per-record structured review for Cocl2_X_2_H2o (data/ingredients/mapped/Cocl2_X_2_H2o.yaml,
  record-e6bce3f910a889a5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
    sha256: f73cf9c10032f8eba85a5b14a067c541a44ff1722fbb727e0a8223a5f4a1424d
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/20261001T050155Z-Cocl2_X_2_H2o.md
    sha256: b74230d7179d9ab6e33a9d1e99f2a8378a4948cf79d33fbc8e0516734e4e446d
    role: context
  - path: reports/yaml_record_review/Cocl2_X_2_H2o.md
    sha256: 5dfe992e69530bc0daba515d9a4b35db9240d1af48d73ab23785a42f0fec98d2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e6bce3f910a889a5
  path: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
  label: Cocl2_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cocl2_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cocl2_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e6bce3f910a889a5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e6bce3f910a889a5
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e6bce3f910a889a5
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e6bce3f910a889a5
evidence:
- evidence_id: ev-78096087a68d920c
  kind: record_content
  reference: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[744],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cocl2_x_2_h2o","line":746,"mapping_status":"MAPPED","ontology_id":"CHEBI:35696","preferred_term":"CoCl2
    x 2 H2O"}],"identifier":"kgmicrobe.compound:cocl2_x_2_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:35696","ontology_label":"cobalt
    dichloride","ontology_source":"CHEBI"},"preferred_term":"CoCl2 x 2 H2O","sssom_rows":[{"data_row":797,"object_id":"CHEBI:35696","object_label":"cobalt
    dichloride","predicate_id":"skos:closeMatch"},{"data_row":798,"object_id":"kgmicrobe.compound:cocl2_x_2_h2o","object_label":"CoCl2
    x 2 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cocl2_X_2_H2o","synonym_count":10}'
  snapshot_sha256: f73cf9c10032f8eba85a5b14a067c541a44ff1722fbb727e0a8223a5f4a1424d
- evidence_id: ev-b43c6d7fadfb672c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [744]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-54d836426573e9b4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cocl2_X_2_H2o; data-row positions=[797,798]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":797,"object_id":"CHEBI:35696","object_label":"cobalt
    dichloride","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Cocl2_X_2_H2o","validation_method":"manual:retire_wrong_form_names|OTHER|2026-09-23"},{"data_row":798,"object_id":"kgmicrobe.compound:cocl2_x_2_h2o","object_label":"CoCl2
    x 2 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cocl2_X_2_H2o","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5aafe38288d69829
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[746]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cocl2_x_2_h2o","line":746,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:35696","preferred_term":"CoCl2
    x 2 H2O","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-527fa867b57fc618
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050155Z-Cocl2_X_2_H2o.md
  locator: 'YAML Record Review: CoCl2 x 2 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b74230d7179d9ab6e33a9d1e99f2a8378a4948cf79d33fbc8e0516734e4e446d
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Cocl2_X_2_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The local
    cobalt dichloride dihydrate identity and 5/5 count pass, but active anhydrous
    structure fields, anhydrous synonyms, and a provisional role remain.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Cocl2_X_2_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Cocl2_X_2_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Cocl2_X_2_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-c5f7d88ce196388f
  kind: prior_review
  reference: reports/yaml_record_review/Cocl2_X_2_H2o.md
  locator: '`data/ingredients/mapped/Cocl2_X_2_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:30; Evidence:50; Completeness:70; Recommended Edits:78'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5dfe992e69530bc0daba515d9a4b35db9240d1af48d73ab23785a42f0fec98d2
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Cocl2_X_2_H2o.yaml`,\
    \ remove or correct the\n  anhydrous InChI/SMILES fields, remove the anhydrous\
    \ cobalt chloride exact\n  synonyms, and either replace `nutritional_roles.TRACE_ELEMENT`\
    \ with inspected\n  evidence for the dihydrate in this media scope or remove the\
    \ role.\n- Regenerate synchronized products and rerun strict validation, SSSOM\
    \ QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-e12aa4528ba436ad
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[432,1697]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3","finding_id":"SEM:058def08fac3452ea333","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3","finding_id":"SEM:580e6cd11e334eed70c7","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-bcba250dc15ca4ca
  kind: record_content
  reference: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: f73cf9c10032f8eba85a5b14a067c541a44ff1722fbb727e0a8223a5f4a1424d
- evidence_id: ev-009e3f3cfdfdb16c
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-17673d435c44a42f]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-17673d435c44a42f in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-12166689869a2b67
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e6bce3f910a889a5
  evidence_ids:
  - ev-78096087a68d920c
  - ev-b43c6d7fadfb672c
  - ev-54d836426573e9b4
  - ev-5aafe38288d69829
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3e1b264ef6f4ae77
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e6bce3f910a889a5
  evidence_ids:
  - ev-527fa867b57fc618
  - ev-c5f7d88ce196388f
  - ev-78096087a68d920c
  - ev-e12aa4528ba436ad
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:55Z;
    reviewed SHA-256=2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3;
    current SHA-256=f73cf9c10032f8eba85a5b14a067c541a44ff1722fbb727e0a8223a5f4a1424d;
    hash_changed=True. Reports=["reports/yaml_record_review/20261001T050155Z-Cocl2_X_2_H2o.md","reports/yaml_record_review/Cocl2_X_2_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Cocl2_X_2_H2o.md` after the record changed from a46da48c9462ac8fe0edff72ca633ab0c78f3bd5a397819f57558fbee1ce9d63
    to 2ceb41745b08d8db408350eb5e0ad38a933df6224ebac60a81ce2a2085f647e3; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-527fa867b57fc618
    - ev-c5f7d88ce196388f
    - ev-78096087a68d920c
  - name: legacy-native-ids
    value: '["SEM:058def08fac3452ea333","SEM:580e6cd11e334eed70c7"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-78096087a68d920c
    - ev-527fa867b57fc618
    - ev-c5f7d88ce196388f
    - ev-e12aa4528ba436ad
- assessment_id: a-bcba250dc15ca4ca
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e6bce3f910a889a5
  evidence_ids:
  - ev-527fa867b57fc618
  - ev-c5f7d88ce196388f
  - ev-bcba250dc15ca4ca
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-527fa867b57fc618
    - ev-c5f7d88ce196388f
    - ev-bcba250dc15ca4ca
findings:
- finding_id: rec-f-17673d435c44a42f
  issue_key: mim-reconciliation-role-support-e6bce3f910a889a5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: CoCl2 x 2 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e6bce3f910a889a5
  evidence_ids:
  - ev-527fa867b57fc618
  - ev-c5f7d88ce196388f
  - ev-bcba250dc15ca4ca
  - ev-009e3f3cfdfdb16c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-17673d435c44a42f
actions:
- action_id: rec-action-17673d435c44a42f
  description: 'Reassess prediction-only role support: CoCl2 x 2 H2O'
  finding_ids:
  - rec-f-17673d435c44a42f
  target_ids:
  - record-e6bce3f910a889a5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cocl2_X_2_H2o.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
