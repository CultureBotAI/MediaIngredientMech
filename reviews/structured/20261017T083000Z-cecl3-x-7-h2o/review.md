# Per-record structured review: Cecl3_X_7_H2o (data/ingredients/mapped/Cecl3_X_7_H2o.yaml)

- Review: 20261017T083000Z-cecl3-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cecl3_X_7_H2o (data/ingredients/mapped/Cecl3_X_7_H2o.yaml, record-e06c987d8ce4121b, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cecl3_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cecl3_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e06c987d8ce4121b | data/ingredients/mapped/Cecl3_X_7_H2o.yaml | maintained | Cecl3_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e06c987d8ce4121b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e06c987d8ce4121b | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e06c987d8ce4121b | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e06c987d8ce4121b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e06c987d8ce4121b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:47Z; reviewed SHA-256=333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241; current SHA-256=333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050147Z-Cecl3_X_7_H2o.md","reports/yaml_record_review/Cecl3_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Cecl3_X_7_H2o.md&#96; after the record changed from 5fe525c19fed3515a33501efd5bdc542ae31aa8029c13bc8d9b39683deb7e0e5 to 333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-e06c987d8ce4121b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-6e0434fd82129807: Reassess prediction-only role support: CeCl3 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-e06c987d8ce4121b.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-6e0434fd82129807

Reassess prediction-only role support: CeCl3 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8ff93c51b1c7fb9e | data/ingredients/mapped/Cecl3_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[671],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","line":673,"mapping_status":"MAPPED","ontology_id":"CHEBI:35458","preferred_term":"CeCl3 x 7 H2O"}],"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:35458","ontology_label":"cerium trichloride","ontology_source":"CHEBI"},"preferred_term":"CeCl3 x 7 H2O","sssom_rows":[{"data_row":671,"object_id":"CHEBI:35458","object_label":"cerium trichloride","predicate_id":"skos:closeMatch"},{"data_row":672,"object_id":"kgmicrobe.compound:cecl3_x_7_h2o","object_label":"CeCl3 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cecl3_X_7_H2o","synonym_count":3} |
| ev-4ea9c22ed0bbb6de | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [671] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0750e0116333ffb1 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cecl3_X_7_H2o; data-row positions=[671, 672] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":671,"object_id":"CHEBI:35458","object_label":"cerium trichloride","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Cecl3_X_7_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":672,"object_id":"kgmicrobe.compound:cecl3_x_7_h2o","object_label":"CeCl3 x 7 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cecl3_X_7_H2o","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-ad6be6922558f75a | docs/data/mapped_ingredients.csv; CSV lines=[673] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","line":673,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:35458","preferred_term":"CeCl3 x 7 H2O","total_occurrences":"4"}] |
| ev-f0a5acdc8cfa341c | reports/yaml_record_review/20261001T050147Z-Cecl3_X_7_H2o.md; YAML Record Review: CeCl3 x 7 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-8f0ea61e967cd24e | reports/yaml_record_review/Cecl3_X_7_H2o.md; &#96;data/ingredients/mapped/Cecl3_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:29; Evidence:44; Completeness:66; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d46a40c5e62c75e1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[376,1647] | context_only | [{"current_record_sha256":"333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241","finding_id":"SEM:2f3987a4be6b773942d6","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241","finding_id":"SEM:83529910b65f4d94305d","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b4125fd291fa0e49 | data/ingredients/mapped/Cecl3_X_7_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[671],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","line":673,"mapping_status":"MAPPED","ontology_id":"CHEBI:35458","preferred_term":"CeCl3 x 7 H2O"}],"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:35458","ontology_label":"cerium trichloride","ontology_source":"CHEBI"},"preferred_term":"CeCl3 x 7 H2O","sssom_rows":[{"data_row":671,"object_id":"CHEBI:35458","object_label":"cerium trichloride","predicate_id":"skos:closeMatch"},{"data_row":672,"object_id":"kgmicrobe.compound:cecl3_x_7_h2o","object_label":"CeCl3 x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cecl3_X_7_H2o","synonym_count":3} |
| ev-bf01590d4a3953bb | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-6e0434fd82129807] | context_only | Predecessor structured review finding f-6e0434fd82129807 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cecl3-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cecl3_X_7_H2o (data/ingredients/mapped/Cecl3_X_7_H2o.yaml)'
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
summary: Per-record structured review for Cecl3_X_7_H2o (data/ingredients/mapped/Cecl3_X_7_H2o.yaml,
  record-e06c987d8ce4121b, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
    sha256: 333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241
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
  - path: reports/yaml_record_review/20261001T050147Z-Cecl3_X_7_H2o.md
    sha256: ea6f5df5fa573978f5c299c7a398d0d1f11a4de22f7c45628f15343337b7da82
    role: context
  - path: reports/yaml_record_review/Cecl3_X_7_H2o.md
    sha256: 5fa320fbc5b5728d788ab79192006e1d495cd7cc36779c1269706ce54a93f6d7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e06c987d8ce4121b
  path: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
  label: Cecl3_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cecl3_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cecl3_X_7_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e06c987d8ce4121b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-8ff93c51b1c7fb9e
  - ev-4ea9c22ed0bbb6de
  - ev-0750e0116333ffb1
  - ev-ad6be6922558f75a
  - ev-b4125fd291fa0e49
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-8ff93c51b1c7fb9e
  - ev-d46a40c5e62c75e1
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-f0a5acdc8cfa341c
  - ev-8f0ea61e967cd24e
  - ev-d46a40c5e62c75e1
  - ev-bf01590d4a3953bb
evidence:
- evidence_id: ev-8ff93c51b1c7fb9e
  kind: record_content
  reference: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[671],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","line":673,"mapping_status":"MAPPED","ontology_id":"CHEBI:35458","preferred_term":"CeCl3
    x 7 H2O"}],"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:35458","ontology_label":"cerium
    trichloride","ontology_source":"CHEBI"},"preferred_term":"CeCl3 x 7 H2O","sssom_rows":[{"data_row":671,"object_id":"CHEBI:35458","object_label":"cerium
    trichloride","predicate_id":"skos:closeMatch"},{"data_row":672,"object_id":"kgmicrobe.compound:cecl3_x_7_h2o","object_label":"CeCl3
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cecl3_X_7_H2o","synonym_count":3}'
  snapshot_sha256: 333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241
- evidence_id: ev-4ea9c22ed0bbb6de
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [671]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0750e0116333ffb1
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cecl3_X_7_H2o; data-row positions=[671, 672]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":671,"object_id":"CHEBI:35458","object_label":"cerium
    trichloride","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Cecl3_X_7_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":672,"object_id":"kgmicrobe.compound:cecl3_x_7_h2o","object_label":"CeCl3
    x 7 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cecl3_X_7_H2o","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ad6be6922558f75a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[673]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","line":673,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"4","ontology_id":"CHEBI:35458","preferred_term":"CeCl3
    x 7 H2O","total_occurrences":"4"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f0a5acdc8cfa341c
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050147Z-Cecl3_X_7_H2o.md
  locator: 'YAML Record Review: CeCl3 x 7 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ea6f5df5fa573978f5c299c7a398d0d1f11a4de22f7c45628f15343337b7da82
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Cecl3_X_7_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The local
    heptahydrate identity passes, but anhydrous structure fields remain and TRACE_ELEMENT
    is only provisionally supported.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Cecl3_X_7_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Cecl3_X_7_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Cecl3_X_7_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-8f0ea61e967cd24e
  kind: prior_review
  reference: reports/yaml_record_review/Cecl3_X_7_H2o.md
  locator: '`data/ingredients/mapped/Cecl3_X_7_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:29; Evidence:44; Completeness:66; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5fa320fbc5b5728d788ab79192006e1d495cd7cc36779c1269706ce54a93f6d7
  quote: "Recommended Edits:\n- Major: either replace `chemical_properties` with fields\
    \ from inspected\n  evidence for cerium trichloride heptahydrate, or remove the\
    \ inherited\n  anhydrous `data_source`, `retrieval_date`, `molecular_formula`,\
    \ `inchi`, and\n  `smiles`.\n- Major: either replace `nutritional_roles.TRACE_ELEMENT`\
    \ with inspected\n  evidence for this hydrate as a trace element in media, or\
    \ remove the role,\n  then rerun strict validation, SSSOM QC, aggregate roundtrip,\
    \ hydrate audits,\n  and `git diff --check`."
- evidence_id: ev-d46a40c5e62c75e1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[376,1647]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241","finding_id":"SEM:2f3987a4be6b773942d6","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241","finding_id":"SEM:83529910b65f4d94305d","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b4125fd291fa0e49
  kind: record_content
  reference: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[671],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","line":673,"mapping_status":"MAPPED","ontology_id":"CHEBI:35458","preferred_term":"CeCl3
    x 7 H2O"}],"identifier":"kgmicrobe.compound:cecl3_x_7_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":4,"edge_count":4,"occurrences":4},"occurrence_statistics":{"media_count":4,"total_occurrences":4},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:35458","ontology_label":"cerium
    trichloride","ontology_source":"CHEBI"},"preferred_term":"CeCl3 x 7 H2O","sssom_rows":[{"data_row":671,"object_id":"CHEBI:35458","object_label":"cerium
    trichloride","predicate_id":"skos:closeMatch"},{"data_row":672,"object_id":"kgmicrobe.compound:cecl3_x_7_h2o","object_label":"CeCl3
    x 7 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cecl3_X_7_H2o","synonym_count":3}'
  snapshot_sha256: 333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241
- evidence_id: ev-bf01590d4a3953bb
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-6e0434fd82129807]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-6e0434fd82129807 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-26a0e27767af23b7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-8ff93c51b1c7fb9e
  - ev-4ea9c22ed0bbb6de
  - ev-0750e0116333ffb1
  - ev-ad6be6922558f75a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-b80618803629bc5f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-f0a5acdc8cfa341c
  - ev-8f0ea61e967cd24e
  - ev-8ff93c51b1c7fb9e
  - ev-d46a40c5e62c75e1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:01:47Z;
    reviewed SHA-256=333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241;
    current SHA-256=333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050147Z-Cecl3_X_7_H2o.md","reports/yaml_record_review/Cecl3_X_7_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Cecl3_X_7_H2o.md` after the record changed from 5fe525c19fed3515a33501efd5bdc542ae31aa8029c13bc8d9b39683deb7e0e5
    to 333ceb06fb21584f6a070220f10ba58595942564b0935143e412c60a4ec45241; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f0a5acdc8cfa341c
    - ev-8f0ea61e967cd24e
    - ev-8ff93c51b1c7fb9e
  - name: legacy-native-ids
    value: '["SEM:2f3987a4be6b773942d6","SEM:83529910b65f4d94305d"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8ff93c51b1c7fb9e
    - ev-f0a5acdc8cfa341c
    - ev-8f0ea61e967cd24e
    - ev-d46a40c5e62c75e1
- assessment_id: a-b4125fd291fa0e49
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-f0a5acdc8cfa341c
  - ev-8f0ea61e967cd24e
  - ev-b4125fd291fa0e49
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f0a5acdc8cfa341c
    - ev-8f0ea61e967cd24e
    - ev-b4125fd291fa0e49
findings:
- finding_id: rec-f-6e0434fd82129807
  issue_key: mim-reconciliation-role-support-e06c987d8ce4121b
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: CeCl3 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e06c987d8ce4121b
  evidence_ids:
  - ev-f0a5acdc8cfa341c
  - ev-8f0ea61e967cd24e
  - ev-b4125fd291fa0e49
  - ev-bf01590d4a3953bb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
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
    finding_id: f-6e0434fd82129807
actions:
- action_id: rec-action-6e0434fd82129807
  description: 'Reassess prediction-only role support: CeCl3 x 7 H2O'
  finding_ids:
  - rec-f-6e0434fd82129807
  target_ids:
  - record-e06c987d8ce4121b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cecl3_X_7_H2o.yaml
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
