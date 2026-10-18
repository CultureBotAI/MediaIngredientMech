# Per-record structured review: Anethole (data/ingredients/mapped/Anethole.yaml)

- Review: 20261017T083000Z-anethole
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Anethole (data/ingredients/mapped/Anethole.yaml, record-43b10222c45e6f6e, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Anethole.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Anethole.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-43b10222c45e6f6e | data/ingredients/mapped/Anethole.yaml | maintained | Anethole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-43b10222c45e6f6e | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-43b10222c45e6f6e | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-43b10222c45e6f6e | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-43b10222c45e6f6e.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-43b10222c45e6f6e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:17:18Z; reviewed SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d; current SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d; hash_changed=False. Reports=["reports/yaml_record_review/Anethole.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic anethole mapping and structure pass, but the stored CAS belongs to trans-anethole and the record exports that narrower isomer CAS on the broader CHEBI parent.

## Findings

### rec-f-a86a549e13ae5fc6: Historical review coverage and residual narrative: Anethole

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-43b10222c45e6f6e.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:17:18Z; reviewed SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d; current SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d; hash_changed=False. Reports=["reports/yaml_record_review/Anethole.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The generic anethole mapping and structure pass, but the stored CAS belongs to trans-anethole and the record exports that narrower isomer CAS on the broader CHEBI parent.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-946d797a0058c6fa | data/ingredients/mapped/Anethole.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[495],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2716","line":497,"mapping_status":"MAPPED","ontology_id":"CHEBI:2716","preferred_term":"Anethole"}],"identifier":"CHEBI:2716","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2716","ontology_label":"anethole","ontology_source":"CHEBI"},"preferred_term":"Anethole","sssom_rows":[{"data_row":382,"object_id":"CHEBI:2716","object_label":"anethole","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Anethole","synonym_count":1} |
| ev-230c701ccc0236cc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [495] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e9840cb8b00a87a0 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Anethole; data-row positions=[382] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":382,"object_id":"CHEBI:2716","object_label":"anethole","other":"1-methoxy-4-(prop-1-en-1-yl)benzene&#124;CAS:4180-23-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Anethole","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-1419a863c01e7744 | docs/data/mapped_ingredients.csv; CSV lines=[497] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:2716","line":497,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:2716","preferred_term":"Anethole","total_occurrences":"0"}] |
| ev-77c4fdf2a9cc8230 | reports/yaml_record_review/Anethole.md; &#96;data/ingredients/mapped/Anethole.yaml&#96;:2; Verdict:4; Identity:12; Validation:26; Evidence:47; Completeness:61; Recommended Edits:73 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-07079df15b81f743 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[259] | context_only | [{"current_record_sha256":"7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d","finding_id":"SEM:880a8b357e2e197b5099","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-anethole
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Anethole (data/ingredients/mapped/Anethole.yaml)'
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
summary: Per-record structured review for Anethole (data/ingredients/mapped/Anethole.yaml,
  record-43b10222c45e6f6e, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Anethole.yaml
    sha256: 7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d
    role: target
  - path: reviews/structured/20261011T024631Z-mim-reconcile-all-batch-03/review.yaml
    sha256: 6b3844c17bf3608ea8f73f824efec195e906ab8d2703fef4cd97fda04f0e65bf
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
  - path: reports/yaml_record_review/Anethole.md
    sha256: 3edfd0086e8a0f043f0f863636d4323e95d8826e8aac6b040804dc76945ea3eb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-43b10222c45e6f6e
  path: data/ingredients/mapped/Anethole.yaml
  label: Anethole
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Anethole.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Anethole.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Anethole.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-43b10222c45e6f6e
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-43b10222c45e6f6e
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-43b10222c45e6f6e
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-43b10222c45e6f6e
evidence:
- evidence_id: ev-946d797a0058c6fa
  kind: record_content
  reference: data/ingredients/mapped/Anethole.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[495],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:2716","line":497,"mapping_status":"MAPPED","ontology_id":"CHEBI:2716","preferred_term":"Anethole"}],"identifier":"CHEBI:2716","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:2716","ontology_label":"anethole","ontology_source":"CHEBI"},"preferred_term":"Anethole","sssom_rows":[{"data_row":382,"object_id":"CHEBI:2716","object_label":"anethole","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Anethole","synonym_count":1}'
  snapshot_sha256: 7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d
- evidence_id: ev-230c701ccc0236cc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [495]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e9840cb8b00a87a0
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Anethole; data-row positions=[382]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":382,"object_id":"CHEBI:2716","object_label":"anethole","other":"1-methoxy-4-(prop-1-en-1-yl)benzene|CAS:4180-23-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Anethole","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1419a863c01e7744
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[497]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:2716","line":497,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:2716","preferred_term":"Anethole","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-77c4fdf2a9cc8230
  kind: prior_review
  reference: reports/yaml_record_review/Anethole.md
  locator: '`data/ingredients/mapped/Anethole.yaml`:2; Verdict:4; Identity:12; Validation:26;
    Evidence:47; Completeness:61; Recommended Edits:73'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 3edfd0086e8a0f043f0f863636d4323e95d8826e8aac6b040804dc76945ea3eb
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Anethole.yaml`, either\
    \ promote the record to\n  `CHEBI:35616` `trans-anethole` and update its stereospecific\
    \ structure, or\n  replace the CAS with source-backed evidence for unqualified\
    \ `CHEBI:2716`\n  anethole.\n- Regenerate synchronized products, then rerun\n\
    \  `uv run --frozen python scripts/validate_strict.py`,\n  `uv run --frozen linkml-term-validator\
    \ validate-data data/ingredients/mapped/Anethole.yaml -s src/mediaingredientmech/schema/mediaingredientmech.yaml\
    \ -t IngredientRecord --labels`,\n  and `uv run --frozen python scripts/validate_sssom_invariants.py`."
- evidence_id: ev-07079df15b81f743
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[259]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d","finding_id":"SEM:880a8b357e2e197b5099","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c286c67fb5db9fac
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-43b10222c45e6f6e
  evidence_ids:
  - ev-946d797a0058c6fa
  - ev-230c701ccc0236cc
  - ev-e9840cb8b00a87a0
  - ev-1419a863c01e7744
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-3689b3611e9e7353
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43b10222c45e6f6e
  evidence_ids:
  - ev-77c4fdf2a9cc8230
  - ev-946d797a0058c6fa
  - ev-07079df15b81f743
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:17:18Z;
    reviewed SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d;
    current SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d;
    hash_changed=False. Reports=["reports/yaml_record_review/Anethole.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The generic anethole mapping
    and structure pass, but the stored CAS belongs to trans-anethole and the record
    exports that narrower isomer CAS on the broader CHEBI parent.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-77c4fdf2a9cc8230
    - ev-946d797a0058c6fa
  - name: legacy-native-ids
    value: '["SEM:880a8b357e2e197b5099"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-946d797a0058c6fa
    - ev-77c4fdf2a9cc8230
    - ev-07079df15b81f743
findings:
- finding_id: rec-f-a86a549e13ae5fc6
  issue_key: mim-reconciliation-historical-review-coverage-and-r-43b10222c45e6f6e
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Anethole'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T08:17:18Z;
    reviewed SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d;
    current SHA-256=7ff3a89ad8a2a940cf08aa66d14f3cdbd62867c7d64cfe78c56837b84cfaa70d;
    hash_changed=False. Reports=["reports/yaml_record_review/Anethole.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The generic anethole mapping
    and structure pass, but the stored CAS belongs to trans-anethole and the record
    exports that narrower isomer CAS on the broader CHEBI parent.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-43b10222c45e6f6e
  evidence_ids:
  - ev-77c4fdf2a9cc8230
  - ev-946d797a0058c6fa
  - ev-07079df15b81f743
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Anethole.yaml
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
  with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.
```
