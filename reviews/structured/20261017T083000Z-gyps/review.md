# Per-record structured review: GYPS (data/ingredients/mapped/GYPS.yaml)

- Review: 20261017T083000Z-gyps
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for GYPS (data/ingredients/mapped/GYPS.yaml, record-1a11b8f19e6c14c8, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/GYPS.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/GYPS.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-1a11b8f19e6c14c8 | data/ingredients/mapped/GYPS.yaml | maintained | GYPS |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-1a11b8f19e6c14c8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-1a11b8f19e6c14c8 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-1a11b8f19e6c14c8 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-1a11b8f19e6c14c8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-1a11b8f19e6c14c8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:02:22Z; reviewed SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; current SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050222Z-GYPS.md","reports/yaml_record_review/GYPS.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/GYPS.md&#96; after the record changed from 5350629f1b8d5282d374363962b0e495378c1da8a1fdc791c36a8cc2774e2c80 to 36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; preserved the previous minor finding floor pending targeted retirement.

## Findings

### rec-f-f70a4e5f2e3b0fc5: Historical review coverage and residual narrative: GYPS

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-1a11b8f19e6c14c8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:02:22Z; reviewed SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; current SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; hash_changed=False. Reports=["reports/yaml_record_review/20261001T050222Z-GYPS.md","reports/yaml_record_review/GYPS.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: Refreshed &#96;reports/yaml_record_review/GYPS.md&#96; after the record changed from 5350629f1b8d5282d374363962b0e495378c1da8a1fdc791c36a8cc2774e2c80 to 36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; preserved the previous minor finding floor pending targeted retirement.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-42bc1806bb5fbd9e | data/ingredients/mapped/GYPS.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[30],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:gyps","line":32,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:gyps","preferred_term":"GYPS"}],"identifier":"kgmicrobe.ingredient:gyps","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:gyps","ontology_label":"GYPS","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"GYPS","sssom_rows":[{"data_row":1267,"object_id":"kgmicrobe.ingredient:gyps","object_label":"GYPS","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:GYPS","synonym_count":1} |
| ev-488ee7ff57bc8ef5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [30] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0222a8bb93b1bc27 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:GYPS; data-row positions=[1267] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1267,"object_id":"kgmicrobe.ingredient:gyps","object_label":"GYPS","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:GYPS","validation_method":"manual:move_mapped_out_of_unmapped_collection&#124;MOVED&#124;2026-08-15"}] |
| ev-2a6b703d74f00987 | docs/data/mapped_ingredients.csv; CSV lines=[32] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:gyps","line":32,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:gyps","preferred_term":"GYPS","total_occurrences":"0"}] |
| ev-e81fcd1c89979094 | reports/yaml_record_review/20261001T050222Z-GYPS.md; YAML Record Review: GYPS:2; Target:10; Validation:20; Identity and Grounding:27; Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61; Additional Notes:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-9b9b457b84c77f39 | reports/yaml_record_review/GYPS.md; &#96;data/ingredients/mapped/GYPS.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:35; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4f367d4efddaaa18 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[645,1495,1607,1693,1742,2106] | context_only | [{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:371318bdaca080a7c800","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:a678a1a16dc0e665c32e","kind":"component_source_scope","resolution_reason":"Exact raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621) defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:2bdb2591fbe0efba3ad9","kind":"component_source_scope","resolution_reason":"Exact raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621) defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:729a37e00fa2167464cc","kind":"component_source_scope","resolution_reason":"Exact raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621) defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:11ab73ddc99dd155bb56","kind":"component_source_scope","resolution_reason":"Exact raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621) defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:36b4aac6cb7a8a5c88fc","kind":"ambiguous_abbreviation","resolution_reason":"Exact raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621) defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-gyps
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: GYPS (data/ingredients/mapped/GYPS.yaml)'
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
native_verdict: mapping_status=MAPPED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for GYPS (data/ingredients/mapped/GYPS.yaml,
  record-1a11b8f19e6c14c8, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/GYPS.yaml
    sha256: 36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e
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
  - path: reports/yaml_record_review/20261001T050222Z-GYPS.md
    sha256: aecea3abaae3df95c16e1f880ff3b5d391ed40d99405de0ac4c0c780d34df89d
    role: context
  - path: reports/yaml_record_review/GYPS.md
    sha256: 6307426ac3b925f8af1b21836224891fd1bd5c66d74ff4bc9b237007cdaee5db
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-1a11b8f19e6c14c8
  path: data/ingredients/mapped/GYPS.yaml
  label: GYPS
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/GYPS.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/GYPS.yaml covering
    current record state, role evidence support, published surfaces, and residual
    historical review claims.
  selection: Single record data/ingredients/mapped/GYPS.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-1a11b8f19e6c14c8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-1a11b8f19e6c14c8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-1a11b8f19e6c14c8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-1a11b8f19e6c14c8
evidence:
- evidence_id: ev-42bc1806bb5fbd9e
  kind: record_content
  reference: data/ingredients/mapped/GYPS.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[30],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:gyps","line":32,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:gyps","preferred_term":"GYPS"}],"identifier":"kgmicrobe.ingredient:gyps","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"bergey:substrates"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:gyps","ontology_label":"GYPS","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"GYPS","sssom_rows":[{"data_row":1267,"object_id":"kgmicrobe.ingredient:gyps","object_label":"GYPS","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:GYPS","synonym_count":1}'
  snapshot_sha256: 36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e
- evidence_id: ev-488ee7ff57bc8ef5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [30]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0222a8bb93b1bc27
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:GYPS; data-row positions=[1267]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1267,"object_id":"kgmicrobe.ingredient:gyps","object_label":"GYPS","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:GYPS","validation_method":"manual:move_mapped_out_of_unmapped_collection|MOVED|2026-08-15"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-2a6b703d74f00987
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[32]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:gyps","line":32,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"kgmicrobe.ingredient:gyps","preferred_term":"GYPS","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e81fcd1c89979094
  kind: prior_review
  reference: reports/yaml_record_review/20261001T050222Z-GYPS.md
  locator: 'YAML Record Review: GYPS:2; Target:10; Validation:20; Identity and Grounding:27;
    Evidence:36; Completeness:46; Findings:52; Recommended Edits:56; Follow-up Checks:61;
    Additional Notes:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: aecea3abaae3df95c16e1f880ff3b5d391ed40d99405de0ac4c0c780d34df89d
  quote: 'Findings:

    - **minor**: The previous finding set in `reports/yaml_record_review/GYPS.md`
    was tied to the prior record content; carry it forward as an unresolved curation
    floor until a targeted current review retires it. Previous summary: The local
    decomposed GYPS identity, components, CultureMech link, and final SSSOM row pass,
    but top-level notes remain stale.


    Recommended Edits:

    - Resolve or explicitly retire the findings provisionally carried forward from
    `reports/yaml_record_review/GYPS.md`.

    - After any edit, run `just sync-curated`, `just validate-strict data/ingredients/mapped/GYPS.yaml`,
    `just validate-terms data/ingredients/mapped/GYPS.yaml` where applicable, and
    `just qc-sssom`.'
- evidence_id: ev-9b9b457b84c77f39
  kind: prior_review
  reference: reports/yaml_record_review/GYPS.md
  locator: '`data/ingredients/mapped/GYPS.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:35; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6307426ac3b925f8af1b21836224891fd1bd5c66d74ff4bc9b237007cdaee5db
  quote: "Recommended Edits:\n- Minor: refresh the top-level `notes` in\n  `data/ingredients/mapped/GYPS.yaml`\
    \ and\n  `data/curated/mapped_ingredients.yaml` so it summarizes the mapped\n\
    \  local-registry identity rather than the old unresolved-import state."
- evidence_id: ev-4f367d4efddaaa18
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[645,1495,1607,1693,1742,2106]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:371318bdaca080a7c800","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:a678a1a16dc0e665c32e","kind":"component_source_scope","resolution_reason":"Exact
    raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621)
    defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four
    current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:2bdb2591fbe0efba3ad9","kind":"component_source_scope","resolution_reason":"Exact
    raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621)
    defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four
    current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:729a37e00fa2167464cc","kind":"component_source_scope","resolution_reason":"Exact
    raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621)
    defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four
    current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:11ab73ddc99dd155bb56","kind":"component_source_scope","resolution_reason":"Exact
    raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621)
    defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four
    current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"},{"current_record_sha256":"36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e","finding_id":"SEM:36b4aac6cb7a8a5c88fc","kind":"ambiguous_abbreviation","resolution_reason":"Exact
    raw source context is Caminicella sporogenes. Alain et al. 2002 p1622 (doi:10.1099/00207713-52-5-1621)
    defines glucose/yeast extract/peptone/sulfur medium; starch was incorrect. Four
    current parts are a partial recipe transcription, not a universal GYPS composition.","resolution_status":"RESOLVED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-d96c529e0d2c63a0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-1a11b8f19e6c14c8
  evidence_ids:
  - ev-42bc1806bb5fbd9e
  - ev-488ee7ff57bc8ef5
  - ev-0222a8bb93b1bc27
  - ev-2a6b703d74f00987
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e2ff5f669ef285ba
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1a11b8f19e6c14c8
  evidence_ids:
  - ev-e81fcd1c89979094
  - ev-9b9b457b84c77f39
  - ev-42bc1806bb5fbd9e
  - ev-4f367d4efddaaa18
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:02:22Z;
    reviewed SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e;
    current SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050222Z-GYPS.md","reports/yaml_record_review/GYPS.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/GYPS.md` after the record changed from 5350629f1b8d5282d374363962b0e495378c1da8a1fdc791c36a8cc2774e2c80
    to 36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; preserved
    the previous minor finding floor pending targeted retirement.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e81fcd1c89979094
    - ev-9b9b457b84c77f39
    - ev-42bc1806bb5fbd9e
  - name: legacy-native-ids
    value: '["SEM:371318bdaca080a7c800","SEM:a678a1a16dc0e665c32e","SEM:2bdb2591fbe0efba3ad9","SEM:729a37e00fa2167464cc","SEM:11ab73ddc99dd155bb56","SEM:36b4aac6cb7a8a5c88fc"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-42bc1806bb5fbd9e
    - ev-e81fcd1c89979094
    - ev-9b9b457b84c77f39
    - ev-4f367d4efddaaa18
findings:
- finding_id: rec-f-f70a4e5f2e3b0fc5
  issue_key: mim-reconciliation-historical-review-coverage-and-r-1a11b8f19e6c14c8
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: GYPS'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-10-01T05:02:22Z;
    reviewed SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e;
    current SHA-256=36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e;
    hash_changed=False. Reports=["reports/yaml_record_review/20261001T050222Z-GYPS.md","reports/yaml_record_review/GYPS.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: Refreshed
    `reports/yaml_record_review/GYPS.md` after the record changed from 5350629f1b8d5282d374363962b0e495378c1da8a1fdc791c36a8cc2774e2c80
    to 36840ca128760eb0ac542753d24d155fd1ebb6ccd8229be130953a0d01f2cf6e; preserved
    the previous minor finding floor pending targeted retirement.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-1a11b8f19e6c14c8
  evidence_ids:
  - ev-e81fcd1c89979094
  - ev-9b9b457b84c77f39
  - ev-42bc1806bb5fbd9e
  - ev-4f367d4efddaaa18
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/GYPS.yaml
    role: maintained ingredient
  field_paths:
  - curation_history
  tags:
  - reconciliation
  - bundle-by-owner
  - historical-review-coverage-and-r
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions: []
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
