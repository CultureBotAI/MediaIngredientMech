# Per-record structured review: Malt_Extract_Agar_Oxoid (data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml)

- Review: 20261017T083000Z-malt-extract-agar-oxoid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Malt_Extract_Agar_Oxoid (data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml, record-9f3e53b0698e9de0, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9f3e53b0698e9de0 | data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml | maintained | Malt_Extract_Agar_Oxoid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9f3e53b0698e9de0 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9f3e53b0698e9de0 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9f3e53b0698e9de0 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9f3e53b0698e9de0.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9f3e53b0698e9de0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:23:32Z; reviewed SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5; current SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5; hash_changed=False. Reports=["reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local exact Oxoid row and close FoodOn parent pass, but this supplier-specific malt-extract-agar formulation lacks component-level curation.

## Findings

### rec-f-2cfad7214fc6e5c4: Historical review coverage and residual narrative: Malt_Extract_Agar_Oxoid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9f3e53b0698e9de0.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:23:32Z; reviewed SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5; current SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5; hash_changed=False. Reports=["reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local exact Oxoid row and close FoodOn parent pass, but this supplier-specific malt-extract-agar formulation lacks component-level curation.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-f0e98109d9a2f851 | data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1336],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","line":1338,"mapping_status":"MAPPED","ontology_id":"FOODON:03301056","preferred_term":"Malt extract agar (Oxoid)"}],"identifier":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03301056","ontology_label":"malt extract","ontology_source":"FOODON"},"preferred_term":"Malt extract agar (Oxoid)","sssom_rows":[{"data_row":1761,"object_id":"FOODON:03301056","object_label":"malt extract","predicate_id":"skos:closeMatch"},{"data_row":1762,"object_id":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","object_label":"Malt extract agar (Oxoid)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Malt_Extract_Agar_Oxoid","synonym_count":1} |
| ev-94b3b0fc906ea94f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1336] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-01d390fd59e4fa76 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Malt_Extract_Agar_Oxoid; data-row positions=[1761,1762] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1761,"object_id":"FOODON:03301056","object_label":"malt extract","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Malt_Extract_Agar_Oxoid","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":1762,"object_id":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","object_label":"Malt extract agar (Oxoid)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Malt_Extract_Agar_Oxoid","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-7e3e66cf2f92438f | docs/data/mapped_ingredients.csv; CSV lines=[1338] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","line":1338,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"FOODON:03301056","preferred_term":"Malt extract agar (Oxoid)","total_occurrences":"1"}] |
| ev-7904af4a2df33ba8 | reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md; &#96;data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml&#96;:2; Verdict:4; Identity:13; Validation:25; Evidence:33; Completeness:47; Recommended Edits:54 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-0a907375f573876d | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[890] | context_only | [{"current_record_sha256":"7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5","finding_id":"SEM:27f6737f138aea83f791","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-malt-extract-agar-oxoid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Malt_Extract_Agar_Oxoid (data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml)'
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
summary: Per-record structured review for Malt_Extract_Agar_Oxoid (data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml,
  record-9f3e53b0698e9de0, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml
    sha256: 7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md
    sha256: b808c6f3c54efccdda570c7c4859b43b5a97b3b947349816664dbb6f0678c9ab
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9f3e53b0698e9de0
  path: data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml
  label: Malt_Extract_Agar_Oxoid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9f3e53b0698e9de0
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9f3e53b0698e9de0
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9f3e53b0698e9de0
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9f3e53b0698e9de0
evidence:
- evidence_id: ev-f0e98109d9a2f851
  kind: record_content
  reference: data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1336],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","line":1338,"mapping_status":"MAPPED","ontology_id":"FOODON:03301056","preferred_term":"Malt
    extract agar (Oxoid)"}],"identifier":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"CLOSE_MATCH","ontology_id":"FOODON:03301056","ontology_label":"malt
    extract","ontology_source":"FOODON"},"preferred_term":"Malt extract agar (Oxoid)","sssom_rows":[{"data_row":1761,"object_id":"FOODON:03301056","object_label":"malt
    extract","predicate_id":"skos:closeMatch"},{"data_row":1762,"object_id":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","object_label":"Malt
    extract agar (Oxoid)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Malt_Extract_Agar_Oxoid","synonym_count":1}'
  snapshot_sha256: 7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5
- evidence_id: ev-94b3b0fc906ea94f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1336]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-01d390fd59e4fa76
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Malt_Extract_Agar_Oxoid; data-row positions=[1761,1762]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1761,"object_id":"FOODON:03301056","object_label":"malt
    extract","other":"","predicate_id":"skos:closeMatch","subject_id":"MIM:Malt_Extract_Agar_Oxoid","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"},{"data_row":1762,"object_id":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","object_label":"Malt
    extract agar (Oxoid)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Malt_Extract_Agar_Oxoid","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7e3e66cf2f92438f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1338]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:malt_extract_agar_~28oxoid~29","line":1338,"mapping_quality":"CLOSE_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"FOODON:03301056","preferred_term":"Malt
    extract agar (Oxoid)","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7904af4a2df33ba8
  kind: prior_review
  reference: reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md
  locator: '`data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml`:2; Verdict:4; Identity:13;
    Validation:25; Evidence:33; Completeness:47; Recommended Edits:54'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b808c6f3c54efccdda570c7c4859b43b5a97b3b947349816664dbb6f0678c9ab
  quote: "Recommended Edits:\n- Transcribe component records and a `component_assertion`\
    \ from source evidence\n  for the Oxoid formulation, or add a reviewed note explaining\
    \ why the\n  formulation cannot be decomposed yet."
- evidence_id: ev-0a907375f573876d
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[890]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5","finding_id":"SEM:27f6737f138aea83f791","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-9c472999bd1bf11f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9f3e53b0698e9de0
  evidence_ids:
  - ev-f0e98109d9a2f851
  - ev-94b3b0fc906ea94f
  - ev-01d390fd59e4fa76
  - ev-7e3e66cf2f92438f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8709392ffb235174
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9f3e53b0698e9de0
  evidence_ids:
  - ev-7904af4a2df33ba8
  - ev-f0e98109d9a2f851
  - ev-0a907375f573876d
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:23:32Z;
    reviewed SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5;
    current SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5;
    hash_changed=False. Reports=["reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    exact Oxoid row and close FoodOn parent pass, but this supplier-specific malt-extract-agar
    formulation lacks component-level curation.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7904af4a2df33ba8
    - ev-f0e98109d9a2f851
  - name: legacy-native-ids
    value: '["SEM:27f6737f138aea83f791"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-f0e98109d9a2f851
    - ev-7904af4a2df33ba8
    - ev-0a907375f573876d
findings:
- finding_id: rec-f-2cfad7214fc6e5c4
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9f3e53b0698e9de0
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Malt_Extract_Agar_Oxoid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:23:32Z;
    reviewed SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5;
    current SHA-256=7f82fb491249f3a8a5460218d7a55b50e88519b511cf402b43f2cb6e2cd3e3f5;
    hash_changed=False. Reports=["reports/yaml_record_review/Malt_Extract_Agar_Oxoid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    exact Oxoid row and close FoodOn parent pass, but this supplier-specific malt-extract-agar
    formulation lacks component-level curation.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9f3e53b0698e9de0
  evidence_ids:
  - ev-7904af4a2df33ba8
  - ev-f0e98109d9a2f851
  - ev-0a907375f573876d
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Malt_Extract_Agar_Oxoid.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
