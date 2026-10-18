# Per-record structured review: D-ornithine (data/ingredients/mapped/D-ornithine.yaml)

- Review: 20261017T083000Z-d-ornithine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for D-ornithine (data/ingredients/mapped/D-ornithine.yaml, record-729874d5fc636261, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/D-ornithine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/D-ornithine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-729874d5fc636261 | data/ingredients/mapped/D-ornithine.yaml | maintained | D-ornithine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-729874d5fc636261 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-729874d5fc636261 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-729874d5fc636261 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-729874d5fc636261.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-729874d5fc636261.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:51:49Z; reviewed SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8; current SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8; hash_changed=False. Reports=["reports/yaml_record_review/D-ornithine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity and BacDive source-occurrence count pass, but final SSSOM exports (+)-l-ornithine for a D-ornithine subject.

## Findings

### rec-f-f24b1024208ec01f: Historical review coverage and residual narrative: D-ornithine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-729874d5fc636261.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:51:49Z; reviewed SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8; current SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8; hash_changed=False. Reports=["reports/yaml_record_review/D-ornithine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity and BacDive source-occurrence count pass, but final SSSOM exports (+)-l-ornithine for a D-ornithine subject.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-3b877adf32af9489 | data/ingredients/mapped/D-ornithine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2239],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16176","line":2241,"mapping_status":"MAPPED","ontology_id":"CHEBI:16176","preferred_term":"D-ornithine"}],"identifier":"CHEBI:16176","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16176","ontology_label":"D-ornithine","ontology_source":"CHEBI"},"preferred_term":"D-ornithine","sssom_rows":[{"data_row":949,"object_id":"CHEBI:16176","object_label":"D-ornithine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-ornithine","synonym_count":1} |
| ev-81793eec481fec67 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2239] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-fddd389fbfe55b9f | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:D-ornithine; data-row positions=[949] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":949,"object_id":"CHEBI:16176","object_label":"D-ornithine","other":"(+)-l-ornithine","predicate_id":"skos:exactMatch","subject_id":"MIM:D-ornithine","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-403a9f762b66bc2f | docs/data/mapped_ingredients.csv; CSV lines=[2241] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:16176","line":2241,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16176","preferred_term":"D-ornithine","total_occurrences":"0"}] |
| ev-6bc186731c9f4981 | reports/yaml_record_review/D-ornithine.md; &#96;data/ingredients/mapped/D-ornithine.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:42; Completeness:59; Recommended Edits:69 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-e28b854c44479ca1 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[505] | context_only | [{"current_record_sha256":"55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8","finding_id":"SEM:026e8a619a1fe3f94d9f","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-d-ornithine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: D-ornithine (data/ingredients/mapped/D-ornithine.yaml)'
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
summary: Per-record structured review for D-ornithine (data/ingredients/mapped/D-ornithine.yaml,
  record-729874d5fc636261, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/D-ornithine.yaml
    sha256: 55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8
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
  - path: reports/yaml_record_review/D-ornithine.md
    sha256: 6c443e9e31af31e98fcb9b863e16596c22d689212ac0031c68984be09ad76458
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-729874d5fc636261
  path: data/ingredients/mapped/D-ornithine.yaml
  label: D-ornithine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-ornithine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/D-ornithine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/D-ornithine.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-729874d5fc636261
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-729874d5fc636261
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-729874d5fc636261
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-729874d5fc636261
evidence:
- evidence_id: ev-3b877adf32af9489
  kind: record_content
  reference: data/ingredients/mapped/D-ornithine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2239],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:16176","line":2241,"mapping_status":"MAPPED","ontology_id":"CHEBI:16176","preferred_term":"D-ornithine"}],"identifier":"CHEBI:16176","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":1,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:16176","ontology_label":"D-ornithine","ontology_source":"CHEBI"},"preferred_term":"D-ornithine","sssom_rows":[{"data_row":949,"object_id":"CHEBI:16176","object_label":"D-ornithine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:D-ornithine","synonym_count":1}'
  snapshot_sha256: 55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8
- evidence_id: ev-81793eec481fec67
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2239]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-fddd389fbfe55b9f
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:D-ornithine; data-row positions=[949]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":949,"object_id":"CHEBI:16176","object_label":"D-ornithine","other":"(+)-l-ornithine","predicate_id":"skos:exactMatch","subject_id":"MIM:D-ornithine","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-403a9f762b66bc2f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2241]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:16176","line":2241,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:16176","preferred_term":"D-ornithine","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6bc186731c9f4981
  kind: prior_review
  reference: reports/yaml_record_review/D-ornithine.md
  locator: '`data/ingredients/mapped/D-ornithine.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:42; Completeness:59; Recommended Edits:69'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6c443e9e31af31e98fcb9b863e16596c22d689212ac0031c68984be09ad76458
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/D-ornithine.yaml`, remove\n\
    \  `(+)-l-ornithine` from the active synonym list or convert it into rejected\n\
    \  provenance so the SSSOM builder drops it from `other`.\n- Regenerate synchronized\
    \ curated and SSSOM products, then rerun\n  `uv run --frozen python scripts/validate_strict.py`,\n\
    \  `uv run --frozen linkml-term-validator validate-data data/ingredients/mapped/D-ornithine.yaml\
    \ -s src/mediaingredientmech/schema/mediaingredientmech.yaml -t IngredientRecord\
    \ --labels`,\n  `uv run --frozen python scripts/validate_id_label_correspondence.py\
    \ -c conf/id_label_targets.yaml`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-e28b854c44479ca1
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[505]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8","finding_id":"SEM:026e8a619a1fe3f94d9f","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0626bbf96d5e4cc1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-729874d5fc636261
  evidence_ids:
  - ev-3b877adf32af9489
  - ev-81793eec481fec67
  - ev-fddd389fbfe55b9f
  - ev-403a9f762b66bc2f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f3a141c0f9f6daf5
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-729874d5fc636261
  evidence_ids:
  - ev-6bc186731c9f4981
  - ev-3b877adf32af9489
  - ev-e28b854c44479ca1
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:51:49Z;
    reviewed SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8;
    current SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8;
    hash_changed=False. Reports=["reports/yaml_record_review/D-ornithine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity and BacDive source-occurrence count pass, but final SSSOM exports (+)-l-ornithine
    for a D-ornithine subject.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6bc186731c9f4981
    - ev-3b877adf32af9489
  - name: legacy-native-ids
    value: '["SEM:026e8a619a1fe3f94d9f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-3b877adf32af9489
    - ev-6bc186731c9f4981
    - ev-e28b854c44479ca1
findings:
- finding_id: rec-f-f24b1024208ec01f
  issue_key: mim-reconciliation-historical-review-coverage-and-r-729874d5fc636261
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: D-ornithine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T13:51:49Z;
    reviewed SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8;
    current SHA-256=55aa5160434fbeee70487c37c51d56996596da384bc06c12c58c8c0f9166eac8;
    hash_changed=False. Reports=["reports/yaml_record_review/D-ornithine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    identity and BacDive source-occurrence count pass, but final SSSOM exports (+)-l-ornithine
    for a D-ornithine subject.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-729874d5fc636261
  evidence_ids:
  - ev-6bc186731c9f4981
  - ev-3b877adf32af9489
  - ev-e28b854c44479ca1
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/D-ornithine.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
