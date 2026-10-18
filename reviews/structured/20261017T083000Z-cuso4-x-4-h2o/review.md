# Per-record structured review: Cuso4_X_4_H2o (data/ingredients/mapped/Cuso4_X_4_H2o.yaml)

- Review: 20261017T083000Z-cuso4-x-4-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cuso4_X_4_H2o (data/ingredients/mapped/Cuso4_X_4_H2o.yaml, record-5b8ceb5e216ceae4, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cuso4_X_4_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cuso4_X_4_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5b8ceb5e216ceae4 | data/ingredients/mapped/Cuso4_X_4_H2o.yaml | maintained | Cuso4_X_4_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5b8ceb5e216ceae4 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-5b8ceb5e216ceae4 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5b8ceb5e216ceae4 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5b8ceb5e216ceae4.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5b8ceb5e216ceae4.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:01Z; reviewed SHA-256=0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a; current SHA-256=0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050201Z-Cuso4_X_4_H2o.md","reports/yaml_record_review/Cuso4_X_4_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/Cuso4_X_4_H2o.md&#96; after the record changed from 72ea1934677ab340704d596bfb1a185d5bdc0bc1398386206b7a7837286de0d6 to 0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a; preserved the previous major finding floor pending targeted retirement.

### Historical provisional-role concern

evidence: concern. Targets: record-5b8ceb5e216ceae4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-c0ef64ea8e7f9b55: Reassess prediction-only role support: CuSO4 x 4 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-5b8ceb5e216ceae4.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-c0ef64ea8e7f9b55

Reassess prediction-only role support: CuSO4 x 4 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3091ce35cac21370 | data/ingredients/mapped/Cuso4_X_4_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2656],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","line":2658,"mapping_status":"MAPPED","ontology_id":"CHEBI:23414","preferred_term":"CuSO4 x 4 H2O"}],"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:23414","ontology_label":"copper(II) sulfate","ontology_source":"CHEBI"},"preferred_term":"CuSO4 x 4 H2O","sssom_rows":[{"data_row":854,"object_id":"CHEBI:23414","object_label":"copper(II) sulfate","predicate_id":"skos:closeMatch"},{"data_row":2983,"object_id":"kgmicrobe.compound:cuso4_x_4_h2o","object_label":"CuSO4 x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cuso4_X_4_H2o","synonym_count":5} |
| ev-c4f08a1ad9501417 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2656] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5b2771d885f8a81b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cuso4_X_4_H2o; data-row positions=[854, 2983] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":854,"object_id":"CHEBI:23414","object_label":"copper(II) sulfate","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Cuso4_X_4_H2o","validation_method":"manual:apply_312_batch3&#124;OTHER&#124;2026-09-22"},{"data_row":2983,"object_id":"kgmicrobe.compound:cuso4_x_4_h2o","object_label":"CuSO4 x 4 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cuso4_X_4_H2o","validation_method":"manual:apply_312_batch3&#124;REGISTRY&#124;2026-09-22"}] |
| ev-18079d6468781b10 | docs/data/mapped_ingredients.csv; CSV lines=[2658] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","line":2658,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:23414","preferred_term":"CuSO4 x 4 H2O","total_occurrences":"2"}] |
| ev-0ab955a9a1ac0385 | reports/yaml_record_review/20261001T050201Z-Cuso4_X_4_H2o.md; YAML Record Review: CuSO4 x 4 H2O:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3c027b6d1298d378 | reports/yaml_record_review/Cuso4_X_4_H2o.md; &#96;data/ingredients/mapped/Cuso4_X_4_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:46; Completeness:66; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c4f217aae45c9505 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[454,2073] | context_only | [{"current_record_sha256":"0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a","finding_id":"SEM:6a3efe512afc6b01bcbe","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a","finding_id":"SEM:d2f6774dd20cc69ab302","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-b8960b3ce20a3377 | data/ingredients/mapped/Cuso4_X_4_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2656],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","line":2658,"mapping_status":"MAPPED","ontology_id":"CHEBI:23414","preferred_term":"CuSO4 x 4 H2O"}],"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:23414","ontology_label":"copper(II) sulfate","ontology_source":"CHEBI"},"preferred_term":"CuSO4 x 4 H2O","sssom_rows":[{"data_row":854,"object_id":"CHEBI:23414","object_label":"copper(II) sulfate","predicate_id":"skos:closeMatch"},{"data_row":2983,"object_id":"kgmicrobe.compound:cuso4_x_4_h2o","object_label":"CuSO4 x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cuso4_X_4_H2o","synonym_count":5} |
| ev-57ed08e27429b6c3 | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-c0ef64ea8e7f9b55] | context_only | Predecessor structured review finding f-c0ef64ea8e7f9b55 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cuso4-x-4-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cuso4_X_4_H2o (data/ingredients/mapped/Cuso4_X_4_H2o.yaml)'
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
summary: Per-record structured review for Cuso4_X_4_H2o (data/ingredients/mapped/Cuso4_X_4_H2o.yaml,
  record-5b8ceb5e216ceae4, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
    sha256: 0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a
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
  - path: reports/yaml_record_review/20261001T050201Z-Cuso4_X_4_H2o.md
    sha256: ffc6f71991bf73b2847937762d34a9aa9542a0954f21d1659a508fd8edaeb53c
    role: context
  - path: reports/yaml_record_review/Cuso4_X_4_H2o.md
    sha256: f0e6af069c660b28d534c70e14b215cefef70836b5fa53bb72d2326bf745c91e
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5b8ceb5e216ceae4
  path: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
  label: Cuso4_X_4_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cuso4_X_4_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cuso4_X_4_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5b8ceb5e216ceae4
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-3091ce35cac21370
  - ev-c4f08a1ad9501417
  - ev-5b2771d885f8a81b
  - ev-18079d6468781b10
  - ev-b8960b3ce20a3377
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-3091ce35cac21370
  - ev-c4f217aae45c9505
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-0ab955a9a1ac0385
  - ev-3c027b6d1298d378
  - ev-c4f217aae45c9505
  - ev-57ed08e27429b6c3
evidence:
- evidence_id: ev-3091ce35cac21370
  kind: record_content
  reference: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2656],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","line":2658,"mapping_status":"MAPPED","ontology_id":"CHEBI:23414","preferred_term":"CuSO4
    x 4 H2O"}],"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:23414","ontology_label":"copper(II)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"CuSO4 x 4 H2O","sssom_rows":[{"data_row":854,"object_id":"CHEBI:23414","object_label":"copper(II)
    sulfate","predicate_id":"skos:closeMatch"},{"data_row":2983,"object_id":"kgmicrobe.compound:cuso4_x_4_h2o","object_label":"CuSO4
    x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cuso4_X_4_H2o","synonym_count":5}'
  snapshot_sha256: 0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a
- evidence_id: ev-c4f08a1ad9501417
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2656]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5b2771d885f8a81b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cuso4_X_4_H2o; data-row positions=[854, 2983]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":854,"object_id":"CHEBI:23414","object_label":"copper(II)
    sulfate","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Cuso4_X_4_H2o","validation_method":"manual:apply_312_batch3|OTHER|2026-09-22"},{"data_row":2983,"object_id":"kgmicrobe.compound:cuso4_x_4_h2o","object_label":"CuSO4
    x 4 H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cuso4_X_4_H2o","validation_method":"manual:apply_312_batch3|REGISTRY|2026-09-22"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-18079d6468781b10
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2658]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","line":2658,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:23414","preferred_term":"CuSO4
    x 4 H2O","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0ab955a9a1ac0385
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050201Z-Cuso4_X_4_H2o.md
  locator: 'YAML Record Review: CuSO4 x 4 H2O:2; Target:10; Validation:20; Identity
    and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56;
    Follow-up Checks:61; Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ffc6f71991bf73b2847937762d34a9aa9542a0954f21d1659a508fd8edaeb53c
  quote: 'Findings:

    - **major**: The previous finding set in `reports/yaml_record_review/Cuso4_X_4_H2o.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The copper
    sulfate tetrahydrate label still collapses onto anhydrous CHEBI:23414 with active
    anhydrous synonyms, structure fields, and occurrence counts.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/Cuso4_X_4_H2o.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/Cuso4_X_4_H2o.yaml`,
    `just validate-terms data/ingredients/mapped/Cuso4_X_4_H2o.yaml` where applicable,
    and `just qc-sssom`.'
- evidence_id: ev-3c027b6d1298d378
  kind: prior_review
  reference: reports/yaml_record_review/Cuso4_X_4_H2o.md
  locator: '`data/ingredients/mapped/Cuso4_X_4_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:27; Evidence:46; Completeness:66; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f0e6af069c660b28d534c70e14b215cefef70836b5fa53bb72d2326bf745c91e
  quote: "Recommended Edits:\n- Major: confirm MediaDive compound 1456 against its\
    \ original source; if it\n  actually meant the pentahydrate, correct it upstream\
    \ and refresh\n  CultureMech/MIM products.\n- Major: if the source label must\
    \ remain as written, mint a local\n  `kgmicrobe.compound` identifier, map `CHEBI:23414`\
    \ only as a close anhydrous\n  parent, remove anhydrous synonyms from resolving\
    \ `other`, and clear or\n  replace the anhydrous InChI/SMILES.\n- Major: recompute\
    \ the occurrence statistics after the identity is split so\n  this record no longer\
    \ inherits all 187 `CHEBI:23414` rows.\n- Major: replace the provisional `TRACE_ELEMENT`\
    \ role evidence with a\n  source-backed `DATABASE_ENTRY` if the local record is\
    \ retained.\n- Regenerate synchronized products and rerun strict validation, SSSOM\
    \ QC,\n  aggregate roundtrip, duplicate-identifier audit, and `git diff --check`."
- evidence_id: ev-c4f217aae45c9505
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[454,2073]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a","finding_id":"SEM:6a3efe512afc6b01bcbe","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a","finding_id":"SEM:d2f6774dd20cc69ab302","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-b8960b3ce20a3377
  kind: record_content
  reference: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2656],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","line":2658,"mapping_status":"MAPPED","ontology_id":"CHEBI:23414","preferred_term":"CuSO4
    x 4 H2O"}],"identifier":"kgmicrobe.compound:cuso4_x_4_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"total_occurrences":2},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"CHEBI:23414","ontology_label":"copper(II)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"CuSO4 x 4 H2O","sssom_rows":[{"data_row":854,"object_id":"CHEBI:23414","object_label":"copper(II)
    sulfate","predicate_id":"skos:closeMatch"},{"data_row":2983,"object_id":"kgmicrobe.compound:cuso4_x_4_h2o","object_label":"CuSO4
    x 4 H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cuso4_X_4_H2o","synonym_count":5}'
  snapshot_sha256: 0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a
- evidence_id: ev-57ed08e27429b6c3
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-c0ef64ea8e7f9b55]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-c0ef64ea8e7f9b55 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-16fb6a7abfaf0138
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-3091ce35cac21370
  - ev-c4f08a1ad9501417
  - ev-5b2771d885f8a81b
  - ev-18079d6468781b10
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-70e601953fbded18
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-0ab955a9a1ac0385
  - ev-3c027b6d1298d378
  - ev-3091ce35cac21370
  - ev-c4f217aae45c9505
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-10-01T05:02:01Z;
    reviewed SHA-256=0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a;
    current SHA-256=0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050201Z-Cuso4_X_4_H2o.md","reports/yaml_record_review/Cuso4_X_4_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/Cuso4_X_4_H2o.md` after the record changed from 72ea1934677ab340704d596bfb1a185d5bdc0bc1398386206b7a7837286de0d6
    to 0f6074f4283f77e4f4766b53973aefa46c247551d4b6f27252471892bd953d7a; preserved
    the previous major finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0ab955a9a1ac0385
    - ev-3c027b6d1298d378
    - ev-3091ce35cac21370
  - name: legacy-native-ids
    value: '["SEM:6a3efe512afc6b01bcbe","SEM:d2f6774dd20cc69ab302"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3091ce35cac21370
    - ev-0ab955a9a1ac0385
    - ev-3c027b6d1298d378
    - ev-c4f217aae45c9505
- assessment_id: a-b8960b3ce20a3377
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-0ab955a9a1ac0385
  - ev-3c027b6d1298d378
  - ev-b8960b3ce20a3377
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0ab955a9a1ac0385
    - ev-3c027b6d1298d378
    - ev-b8960b3ce20a3377
findings:
- finding_id: rec-f-c0ef64ea8e7f9b55
  issue_key: mim-reconciliation-role-support-5b8ceb5e216ceae4
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: CuSO4 x 4 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-5b8ceb5e216ceae4
  evidence_ids:
  - ev-0ab955a9a1ac0385
  - ev-3c027b6d1298d378
  - ev-b8960b3ce20a3377
  - ev-57ed08e27429b6c3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
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
    finding_id: f-c0ef64ea8e7f9b55
actions:
- action_id: rec-action-c0ef64ea8e7f9b55
  description: 'Reassess prediction-only role support: CuSO4 x 4 H2O'
  finding_ids:
  - rec-f-c0ef64ea8e7f9b55
  target_ids:
  - record-5b8ceb5e216ceae4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cuso4_X_4_H2o.yaml
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
