# Per-record structured review: Sugar_Beet_Molasses (data/ingredients/mapped/Sugar_Beet_Molasses.yaml)

- Review: 20261017T083000Z-sugar-beet-molasses
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sugar_Beet_Molasses (data/ingredients/mapped/Sugar_Beet_Molasses.yaml, record-a38d4112c2079c88, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sugar_Beet_Molasses.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sugar_Beet_Molasses.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-a38d4112c2079c88 | data/ingredients/mapped/Sugar_Beet_Molasses.yaml | maintained | Sugar_Beet_Molasses |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-a38d4112c2079c88 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-a38d4112c2079c88 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-a38d4112c2079c88 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-a38d4112c2079c88.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-a38d4112c2079c88.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:53:36Z; reviewed SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5; current SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5; hash_changed=False. Reports=["reports/yaml_record_review/Sugar_Beet_Molasses.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: FOODON:00003412 is sugar beet root, not sugar beet molasses; a more specific FoodOn molasses term exists.

## Findings

### rec-f-4048a50d01492616: Historical review coverage and residual narrative: Sugar_Beet_Molasses

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-a38d4112c2079c88.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:53:36Z; reviewed SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5; current SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5; hash_changed=False. Reports=["reports/yaml_record_review/Sugar_Beet_Molasses.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: FOODON:00003412 is sugar beet root, not sugar beet molasses; a more specific FoodOn molasses term exists.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6efe726a416bd73a | data/ingredients/mapped/Sugar_Beet_Molasses.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1911],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:00003412","line":1913,"mapping_status":"MAPPED","ontology_id":"FOODON:00003412","preferred_term":"Sugar beet molasses"}],"identifier":"FOODON:00003412","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"FOODON:00003412","ontology_label":"sugar beet","ontology_source":"FOODON"},"preferred_term":"Sugar beet molasses","sssom_rows":[{"data_row":2666,"object_id":"FOODON:00003412","object_label":"sugar beet","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sugar_Beet_Molasses","synonym_count":1} |
| ev-bd3fc10897dc459e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1911] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-924e5630381defe2 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sugar_Beet_Molasses; data-row positions=[2666] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2666,"object_id":"FOODON:00003412","object_label":"sugar beet","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sugar_Beet_Molasses","validation_method":"OLS:foodon&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-ae1badd6ef86c24f | docs/data/mapped_ingredients.csv; CSV lines=[1913] | supports | Published identity and count rows inspected: [{"identifier":"FOODON:00003412","line":1913,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"FOODON:00003412","preferred_term":"Sugar beet molasses","total_occurrences":"3"}] |
| ev-05f5cd04de33ef15 | reports/yaml_record_review/Sugar_Beet_Molasses.md; &#96;data/ingredients/mapped/Sugar_Beet_Molasses.yaml&#96;:2; Verdict:4; Identity:10; Validation:18; Evidence:26; Completeness:36; Recommended Edits:44 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3573edf5a2a7d942 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1258] | context_only | [{"current_record_sha256":"64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5","finding_id":"SEM:5e53a5eb630049412c70","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sugar-beet-molasses
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sugar_Beet_Molasses (data/ingredients/mapped/Sugar_Beet_Molasses.yaml)'
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
summary: Per-record structured review for Sugar_Beet_Molasses (data/ingredients/mapped/Sugar_Beet_Molasses.yaml,
  record-a38d4112c2079c88, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sugar_Beet_Molasses.yaml
    sha256: 64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5
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
  - path: reports/yaml_record_review/Sugar_Beet_Molasses.md
    sha256: 9698af3bbb1e90a555fe52090a884a23f58c5385561a90aebcacba487735f7ca
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-a38d4112c2079c88
  path: data/ingredients/mapped/Sugar_Beet_Molasses.yaml
  label: Sugar_Beet_Molasses
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sugar_Beet_Molasses.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sugar_Beet_Molasses.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sugar_Beet_Molasses.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-a38d4112c2079c88
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-a38d4112c2079c88
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-a38d4112c2079c88
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-a38d4112c2079c88
evidence:
- evidence_id: ev-6efe726a416bd73a
  kind: record_content
  reference: data/ingredients/mapped/Sugar_Beet_Molasses.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1911],"raw_equal":true},"docs_rows":[{"identifier":"FOODON:00003412","line":1913,"mapping_status":"MAPPED","ontology_id":"FOODON:00003412","preferred_term":"Sugar
    beet molasses"}],"identifier":"FOODON:00003412","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"FOODON:00003412","ontology_label":"sugar
    beet","ontology_source":"FOODON"},"preferred_term":"Sugar beet molasses","sssom_rows":[{"data_row":2666,"object_id":"FOODON:00003412","object_label":"sugar
    beet","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sugar_Beet_Molasses","synonym_count":1}'
  snapshot_sha256: 64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5
- evidence_id: ev-bd3fc10897dc459e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1911]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-924e5630381defe2
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sugar_Beet_Molasses; data-row positions=[2666]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2666,"object_id":"FOODON:00003412","object_label":"sugar
    beet","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sugar_Beet_Molasses","validation_method":"OLS:foodon|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-ae1badd6ef86c24f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1913]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"FOODON:00003412","line":1913,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"FOODON:00003412","preferred_term":"Sugar
    beet molasses","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-05f5cd04de33ef15
  kind: prior_review
  reference: reports/yaml_record_review/Sugar_Beet_Molasses.md
  locator: '`data/ingredients/mapped/Sugar_Beet_Molasses.yaml`:2; Verdict:4; Identity:10;
    Validation:18; Evidence:26; Completeness:36; Recommended Edits:44'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9698af3bbb1e90a555fe52090a884a23f58c5385561a90aebcacba487735f7ca
  quote: "Recommended Edits:\n- Major: reground `data/ingredients/mapped/Sugar_Beet_Molasses.yaml`\
    \ from\n  `FOODON:00003412` to a molasses-specific term such as `FOODON:03543005`\
    \ if\n  live FoodOn confirms that term fits the source labels, then synchronize\
    \ the\n  aggregate and rebuild the final SSSOM row."
- evidence_id: ev-3573edf5a2a7d942
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1258]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5","finding_id":"SEM:5e53a5eb630049412c70","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-ba8b124dc8db3fe8
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-a38d4112c2079c88
  evidence_ids:
  - ev-6efe726a416bd73a
  - ev-bd3fc10897dc459e
  - ev-924e5630381defe2
  - ev-ae1badd6ef86c24f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4ab49d43811734c6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a38d4112c2079c88
  evidence_ids:
  - ev-05f5cd04de33ef15
  - ev-6efe726a416bd73a
  - ev-3573edf5a2a7d942
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:53:36Z;
    reviewed SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5;
    current SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5;
    hash_changed=False. Reports=["reports/yaml_record_review/Sugar_Beet_Molasses.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: FOODON:00003412
    is sugar beet root, not sugar beet molasses; a more specific FoodOn molasses term
    exists.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-05f5cd04de33ef15
    - ev-6efe726a416bd73a
  - name: legacy-native-ids
    value: '["SEM:5e53a5eb630049412c70"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6efe726a416bd73a
    - ev-05f5cd04de33ef15
    - ev-3573edf5a2a7d942
findings:
- finding_id: rec-f-4048a50d01492616
  issue_key: mim-reconciliation-historical-review-coverage-and-r-a38d4112c2079c88
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sugar_Beet_Molasses'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T16:53:36Z;
    reviewed SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5;
    current SHA-256=64a35d50a0df41bf8097f57af5a581c730d26e2895e82396df10d7aadf817ca5;
    hash_changed=False. Reports=["reports/yaml_record_review/Sugar_Beet_Molasses.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: FOODON:00003412
    is sugar beet root, not sugar beet molasses; a more specific FoodOn molasses term
    exists.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-a38d4112c2079c88
  evidence_ids:
  - ev-05f5cd04de33ef15
  - ev-6efe726a416bd73a
  - ev-3573edf5a2a7d942
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sugar_Beet_Molasses.yaml
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
