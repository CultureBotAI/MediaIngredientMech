# Per-record structured review: Hydroxocobalamin_hydrochloride (data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml)

- Review: 20261017T083000Z-hydroxocobalamin-hydrochloride
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hydroxocobalamin_hydrochloride (data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml, record-8f7a34ad5e80e237, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-8f7a34ad5e80e237 | data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml | maintained | Hydroxocobalamin_hydrochloride |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-8f7a34ad5e80e237 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-8f7a34ad5e80e237 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-8f7a34ad5e80e237 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-8f7a34ad5e80e237.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-8f7a34ad5e80e237.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:54:17Z; reviewed SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f; current SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f; hash_changed=False. Reports=["reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT residual grounding and SSSOM row pass, but ingredient_type is missing.

## Findings

### rec-f-4cd402d5c8600aca: Historical review coverage and residual narrative: Hydroxocobalamin_hydrochloride

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-8f7a34ad5e80e237.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:54:17Z; reviewed SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f; current SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f; hash_changed=False. Reports=["reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact NCIT residual grounding and SSSOM row pass, but ingredient_type is missing.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-68c3292d41b28929 | data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2624],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C217966","line":2626,"mapping_status":"MAPPED","ontology_id":"NCIT:C217966","preferred_term":"hydroxocobalamin hydrochloride"}],"identifier":"NCIT:C217966","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"NCIT:C217966","ontology_label":"Hydroxocobalamin Hydrochloride","ontology_source":"NCIT"},"preferred_term":"hydroxocobalamin hydrochloride","sssom_rows":[{"data_row":1455,"object_id":"NCIT:C217966","object_label":"Hydroxocobalamin Hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydroxocobalamin_hydrochloride","synonym_count":0} |
| ev-6d4b3a0d8c3c4320 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2624] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8d04d3e35f11db12 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hydroxocobalamin_hydrochloride; data-row positions=[1455] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1455,"object_id":"NCIT:C217966","object_label":"Hydroxocobalamin Hydrochloride","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydroxocobalamin_hydrochloride","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-09-01"}] |
| ev-eacd5065c0d3af62 | docs/data/mapped_ingredients.csv; CSV lines=[2626] | supports | Published identity and count rows inspected: [{"identifier":"NCIT:C217966","line":2626,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"NCIT:C217966","preferred_term":"hydroxocobalamin hydrochloride","total_occurrences":"1"}] |
| ev-52053f012cb5fb25 | reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md; &#96;data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:35; Completeness:49; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-a71774a906a7adbf | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[741] | context_only | [{"current_record_sha256":"9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f","finding_id":"SEM:ab415e8bcdfd729075a1","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hydroxocobalamin-hydrochloride
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hydroxocobalamin_hydrochloride (data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml)'
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
summary: Per-record structured review for Hydroxocobalamin_hydrochloride (data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml,
  record-8f7a34ad5e80e237, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
    sha256: 9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f
    role: target
  - path: reviews/structured/20261011T024635Z-mim-reconcile-all-batch-07/review.yaml
    sha256: 408ad5bf1e58ddc25c06da54ed69bc719d6d61336a106fc7534b0954417618be
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
  - path: reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md
    sha256: 7597cc4e1cee618c99526b4a89c7bcc3ee17ac9f8255463e8f2abb0ee4480a3b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-8f7a34ad5e80e237
  path: data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
  label: Hydroxocobalamin_hydrochloride
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-8f7a34ad5e80e237
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-8f7a34ad5e80e237
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-8f7a34ad5e80e237
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-8f7a34ad5e80e237
evidence:
- evidence_id: ev-68c3292d41b28929
  kind: record_content
  reference: data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2624],"raw_equal":true},"docs_rows":[{"identifier":"NCIT:C217966","line":2626,"mapping_status":"MAPPED","ontology_id":"NCIT:C217966","preferred_term":"hydroxocobalamin
    hydrochloride"}],"identifier":"NCIT:C217966","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","match_level":"EXACT","ontology_id":"NCIT:C217966","ontology_label":"Hydroxocobalamin
    Hydrochloride","ontology_source":"NCIT"},"preferred_term":"hydroxocobalamin hydrochloride","sssom_rows":[{"data_row":1455,"object_id":"NCIT:C217966","object_label":"Hydroxocobalamin
    Hydrochloride","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hydroxocobalamin_hydrochloride","synonym_count":0}'
  snapshot_sha256: 9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f
- evidence_id: ev-6d4b3a0d8c3c4320
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2624]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8d04d3e35f11db12
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hydroxocobalamin_hydrochloride; data-row positions=[1455]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1455,"object_id":"NCIT:C217966","object_label":"Hydroxocobalamin
    Hydrochloride","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Hydroxocobalamin_hydrochloride","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-09-01"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-eacd5065c0d3af62
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2626]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"NCIT:C217966","line":2626,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"NCIT:C217966","preferred_term":"hydroxocobalamin
    hydrochloride","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-52053f012cb5fb25
  kind: prior_review
  reference: reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md
  locator: '`data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml`:2; Verdict:4;
    Identity:10; Validation:21; Evidence:35; Completeness:49; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 7597cc4e1cee618c99526b4a89c7bcc3ee17ac9f8255463e8f2abb0ee4480a3b
  quote: "Recommended Edits:\n- Minor: classify `Hydroxocobalamin_hydrochloride` with\
    \ the maintained\n  ingredient-type workflow, then rerun strict, round-trip, id-label,\
    \ component,\n  and SSSOM validation."
- evidence_id: ev-a71774a906a7adbf
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[741]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f","finding_id":"SEM:ab415e8bcdfd729075a1","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-aaf8c96c474b99b7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-8f7a34ad5e80e237
  evidence_ids:
  - ev-68c3292d41b28929
  - ev-6d4b3a0d8c3c4320
  - ev-8d04d3e35f11db12
  - ev-eacd5065c0d3af62
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d13e5d32710cf476
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f7a34ad5e80e237
  evidence_ids:
  - ev-52053f012cb5fb25
  - ev-68c3292d41b28929
  - ev-a71774a906a7adbf
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:54:17Z;
    reviewed SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f;
    current SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f;
    hash_changed=False. Reports=["reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    NCIT residual grounding and SSSOM row pass, but ingredient_type is missing.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-52053f012cb5fb25
    - ev-68c3292d41b28929
  - name: legacy-native-ids
    value: '["SEM:ab415e8bcdfd729075a1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-68c3292d41b28929
    - ev-52053f012cb5fb25
    - ev-a71774a906a7adbf
findings:
- finding_id: rec-f-4cd402d5c8600aca
  issue_key: mim-reconciliation-historical-review-coverage-and-r-8f7a34ad5e80e237
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Hydroxocobalamin_hydrochloride'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T19:54:17Z;
    reviewed SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f;
    current SHA-256=9a889cb2c5b37b0360914e1f9075aba2761c67c516cbe8e26899763c31ff3d7f;
    hash_changed=False. Reports=["reports/yaml_record_review/Hydroxocobalamin_hydrochloride.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    NCIT residual grounding and SSSOM row pass, but ingredient_type is missing.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-8f7a34ad5e80e237
  evidence_ids:
  - ev-52053f012cb5fb25
  - ev-68c3292d41b28929
  - ev-a71774a906a7adbf
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hydroxocobalamin_hydrochloride.yaml
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
  with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.
```
