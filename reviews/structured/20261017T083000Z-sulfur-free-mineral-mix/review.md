# Per-record structured review: Sulfur_Free_Mineral_Mix (data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml)

- Review: 20261017T083000Z-sulfur-free-mineral-mix
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sulfur_Free_Mineral_Mix (data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml, record-49fbfc04cb0dea5d, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-49fbfc04cb0dea5d | data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml | maintained | Sulfur_Free_Mineral_Mix |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-49fbfc04cb0dea5d | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-49fbfc04cb0dea5d | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-49fbfc04cb0dea5d | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-49fbfc04cb0dea5d.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-49fbfc04cb0dea5d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:23:58Z; reviewed SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab; current SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab; hash_changed=False. Reports=["reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity and SSSOM row pass, but the mapped stock lacks its pending component-level recipe.

## Findings

### rec-f-ffa2bbbc91760bb0: Historical review coverage and residual narrative: Sulfur_Free_Mineral_Mix

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-49fbfc04cb0dea5d.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:23:58Z; reviewed SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab; current SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab; hash_changed=False. Reports=["reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity and SSSOM row pass, but the mapped stock lacks its pending component-level recipe.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b077c2d6da7afc25 | data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[91],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sulfur_free_mineral_mix","line":93,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","preferred_term":"Sulfur free mineral mix"}],"identifier":"kgmicrobe.ingredient:sulfur_free_mineral_mix","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","ontology_label":"Sulfur free mineral mix","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Sulfur free mineral mix","sssom_rows":[{"data_row":2695,"object_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","object_label":"Sulfur free mineral mix","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sulfur_Free_Mineral_Mix","synonym_count":1} |
| ev-5438890d8660945e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [91] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5e61332671e3ea56 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sulfur_Free_Mineral_Mix; data-row positions=[2695] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2695,"object_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","object_label":"Sulfur free mineral mix","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sulfur_Free_Mineral_Mix","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-09-02"}] |
| ev-d25138333df9d02a | docs/data/mapped_ingredients.csv; CSV lines=[93] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:sulfur_free_mineral_mix","line":93,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","preferred_term":"Sulfur free mineral mix","total_occurrences":"1"}] |
| ev-ae175debd9dd6118 | reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md; &#96;data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:37; Completeness:54; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bbe56141be0124b1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1263] | context_only | [{"current_record_sha256":"d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab","finding_id":"SEM:9834503edf9295a1404f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sulfur-free-mineral-mix
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sulfur_Free_Mineral_Mix (data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml)'
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
summary: Per-record structured review for Sulfur_Free_Mineral_Mix (data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml,
  record-49fbfc04cb0dea5d, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml
    sha256: d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md
    sha256: 9b498717c17292ba89341b7c22690b3e64c7329d831f68062fa122c560d0d1be
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-49fbfc04cb0dea5d
  path: data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml
  label: Sulfur_Free_Mineral_Mix
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-49fbfc04cb0dea5d
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-49fbfc04cb0dea5d
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-49fbfc04cb0dea5d
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-49fbfc04cb0dea5d
evidence:
- evidence_id: ev-b077c2d6da7afc25
  kind: record_content
  reference: data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[91],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sulfur_free_mineral_mix","line":93,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","preferred_term":"Sulfur
    free mineral mix"}],"identifier":"kgmicrobe.ingredient:sulfur_free_mineral_mix","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","ontology_label":"Sulfur
    free mineral mix","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Sulfur
    free mineral mix","sssom_rows":[{"data_row":2695,"object_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","object_label":"Sulfur
    free mineral mix","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sulfur_Free_Mineral_Mix","synonym_count":1}'
  snapshot_sha256: d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab
- evidence_id: ev-5438890d8660945e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [91]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5e61332671e3ea56
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sulfur_Free_Mineral_Mix; data-row positions=[2695]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2695,"object_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","object_label":"Sulfur
    free mineral mix","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sulfur_Free_Mineral_Mix","validation_method":"none|UNKNOWN_TERM|2026-09-02"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d25138333df9d02a
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[93]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:sulfur_free_mineral_mix","line":93,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:sulfur_free_mineral_mix","preferred_term":"Sulfur
    free mineral mix","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ae175debd9dd6118
  kind: prior_review
  reference: reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md
  locator: '`data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:37; Completeness:54; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9b498717c17292ba89341b7c22690b3e64c7329d831f68062fa122c560d0d1be
  quote: "Recommended Edits:\n- Major: transcribe the maintained CultureBotHT recipe\
    \ for `Sulfur free mineral\n  mix` into `data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml`,\
    \ adding the\n  component list, `component_assertion`, and any source-backed mineral\
    \ role\n  that the recipe supports.\n- Major: rerun `uv run --frozen python scripts/validate_component_partonomy.py`\n\
    \  and the normal generated-product build after curation so the aggregate and\n\
    \  docs carry the complete stock decomposition."
- evidence_id: ev-bbe56141be0124b1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1263]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab","finding_id":"SEM:9834503edf9295a1404f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-7af7c4eac01c0508
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-49fbfc04cb0dea5d
  evidence_ids:
  - ev-b077c2d6da7afc25
  - ev-5438890d8660945e
  - ev-5e61332671e3ea56
  - ev-d25138333df9d02a
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-20a6c301cc9875ec
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-49fbfc04cb0dea5d
  evidence_ids:
  - ev-ae175debd9dd6118
  - ev-b077c2d6da7afc25
  - ev-bbe56141be0124b1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:23:58Z;
    reviewed SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab;
    current SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab;
    hash_changed=False. Reports=["reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity and SSSOM row pass, but the mapped stock lacks its pending component-level
    recipe.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ae175debd9dd6118
    - ev-b077c2d6da7afc25
  - name: legacy-native-ids
    value: '["SEM:9834503edf9295a1404f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b077c2d6da7afc25
    - ev-ae175debd9dd6118
    - ev-bbe56141be0124b1
findings:
- finding_id: rec-f-ffa2bbbc91760bb0
  issue_key: mim-reconciliation-historical-review-coverage-and-r-49fbfc04cb0dea5d
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sulfur_Free_Mineral_Mix'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T17:23:58Z;
    reviewed SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab;
    current SHA-256=d7248c7d9c6209a3e00ae22148824a3015953ee6d4ba8200000746ebdc3107ab;
    hash_changed=False. Reports=["reports/yaml_record_review/Sulfur_Free_Mineral_Mix.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    stock identity and SSSOM row pass, but the mapped stock lacks its pending component-level
    recipe.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-49fbfc04cb0dea5d
  evidence_ids:
  - ev-ae175debd9dd6118
  - ev-b077c2d6da7afc25
  - ev-bbe56141be0124b1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sulfur_Free_Mineral_Mix.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
