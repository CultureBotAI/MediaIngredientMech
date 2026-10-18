# Per-record structured review: Na-silicate (data/ingredients/mapped/Na-silicate.yaml)

- Review: 20261017T083000Z-na-silicate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na-silicate (data/ingredients/mapped/Na-silicate.yaml, record-c2e60be54e8ad32b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na-silicate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na-silicate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c2e60be54e8ad32b | data/ingredients/mapped/Na-silicate.yaml | maintained | Na-silicate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c2e60be54e8ad32b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-c2e60be54e8ad32b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c2e60be54e8ad32b | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c2e60be54e8ad32b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c2e60be54e8ad32b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:58:04Z; reviewed SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2; current SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2; hash_changed=False. Reports=["reports/yaml_record_review/Na-silicate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:60720 sodium silicate identity, CAS-backed structure, mineral role, and hydrate synonym rejection pass, but final SSSOM publishes a numbered source artifact.

## Findings

### rec-f-fd83fb7c1f69e4ef: Historical review coverage and residual narrative: Na-silicate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-c2e60be54e8ad32b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:58:04Z; reviewed SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2; current SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2; hash_changed=False. Reports=["reports/yaml_record_review/Na-silicate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:60720 sodium silicate identity, CAS-backed structure, mineral role, and hydrate synonym rejection pass, but final SSSOM publishes a numbered source artifact.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2476594bfad7b1e6 | data/ingredients/mapped/Na-silicate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:60720","line":1475,"mapping_status":"MAPPED","ontology_id":"CHEBI:60720","preferred_term":"Na-silicate"}],"identifier":"CHEBI:60720","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":218,"edge_count":218,"occurrences":218},"occurrence_statistics":{"media_count":218,"total_occurrences":218},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:60720","ontology_label":"sodium silicate","ontology_source":"CHEBI"},"preferred_term":"Na-silicate","sssom_rows":[{"data_row":1977,"object_id":"CHEBI:60720","object_label":"sodium silicate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-silicate","synonym_count":10} |
| ev-8b6db2c4ba866be0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1473] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9db722587c53ee4d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na-silicate; data-row positions=[1977] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1977,"object_id":"CHEBI:60720","object_label":"sodium silicate","other":"(5)  Sodium metasilicate&#124;Na silicate&#124;Sodium polysilicate&#124;Sodium sesquisilicate&#124;Sodium silicate glass&#124;Sodium siliconate&#124;disodium oxosilanediolate&#124;CAS:1344-09-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-silicate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-01a7acfb4a34ce2e | docs/data/mapped_ingredients.csv; CSV lines=[1475] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:60720","line":1475,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"218","ontology_id":"CHEBI:60720","preferred_term":"Na-silicate","total_occurrences":"218"}] |
| ev-1db8ca471d68774b | reports/yaml_record_review/Na-silicate.md; &#96;data/ingredients/mapped/Na-silicate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:27; Completeness:41; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-5d2b5b07594f3262 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[980] | context_only | [{"current_record_sha256":"5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2","finding_id":"SEM:057896b36eeb591b1654","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na-silicate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na-silicate (data/ingredients/mapped/Na-silicate.yaml)'
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
summary: Per-record structured review for Na-silicate (data/ingredients/mapped/Na-silicate.yaml,
  record-c2e60be54e8ad32b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na-silicate.yaml
    sha256: 5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Na-silicate.md
    sha256: f69e3f7946fdb2269432ab9c17b4e9eaf031da332d6581b96bf2329f482e874f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c2e60be54e8ad32b
  path: data/ingredients/mapped/Na-silicate.yaml
  label: Na-silicate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-silicate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na-silicate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na-silicate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c2e60be54e8ad32b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c2e60be54e8ad32b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-c2e60be54e8ad32b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c2e60be54e8ad32b
evidence:
- evidence_id: ev-2476594bfad7b1e6
  kind: record_content
  reference: data/ingredients/mapped/Na-silicate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:60720","line":1475,"mapping_status":"MAPPED","ontology_id":"CHEBI:60720","preferred_term":"Na-silicate"}],"identifier":"CHEBI:60720","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":218,"edge_count":218,"occurrences":218},"occurrence_statistics":{"media_count":218,"total_occurrences":218},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:60720","ontology_label":"sodium
    silicate","ontology_source":"CHEBI"},"preferred_term":"Na-silicate","sssom_rows":[{"data_row":1977,"object_id":"CHEBI:60720","object_label":"sodium
    silicate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Na-silicate","synonym_count":10}'
  snapshot_sha256: 5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2
- evidence_id: ev-8b6db2c4ba866be0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1473]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9db722587c53ee4d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na-silicate; data-row positions=[1977]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1977,"object_id":"CHEBI:60720","object_label":"sodium
    silicate","other":"(5)  Sodium metasilicate|Na silicate|Sodium polysilicate|Sodium
    sesquisilicate|Sodium silicate glass|Sodium siliconate|disodium oxosilanediolate|CAS:1344-09-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Na-silicate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-01a7acfb4a34ce2e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1475]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:60720","line":1475,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"218","ontology_id":"CHEBI:60720","preferred_term":"Na-silicate","total_occurrences":"218"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-1db8ca471d68774b
  kind: prior_review
  reference: reports/yaml_record_review/Na-silicate.md
  locator: '`data/ingredients/mapped/Na-silicate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:27; Completeness:41; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f69e3f7946fdb2269432ab9c17b4e9eaf031da332d6581b96bf2329f482e874f
  quote: "Recommended Edits:\n- Major: demote `(5)  Sodium metasilicate` in\n  `data/ingredients/mapped/Na-silicate.yaml`\
    \ so it remains source provenance\n  rather than a publishable exact synonym,\
    \ then rebuild final SSSOM and re-run\n  final SSSOM validation plus product label\
    \ validation."
- evidence_id: ev-5d2b5b07594f3262
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[980]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2","finding_id":"SEM:057896b36eeb591b1654","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e2bae4b157b12a42
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c2e60be54e8ad32b
  evidence_ids:
  - ev-2476594bfad7b1e6
  - ev-8b6db2c4ba866be0
  - ev-9db722587c53ee4d
  - ev-01a7acfb4a34ce2e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-edfe6130862ab9f9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c2e60be54e8ad32b
  evidence_ids:
  - ev-1db8ca471d68774b
  - ev-2476594bfad7b1e6
  - ev-5d2b5b07594f3262
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:58:04Z;
    reviewed SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2;
    current SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-silicate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:60720
    sodium silicate identity, CAS-backed structure, mineral role, and hydrate synonym
    rejection pass, but final SSSOM publishes a numbered source artifact.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-1db8ca471d68774b
    - ev-2476594bfad7b1e6
  - name: legacy-native-ids
    value: '["SEM:057896b36eeb591b1654"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2476594bfad7b1e6
    - ev-1db8ca471d68774b
    - ev-5d2b5b07594f3262
findings:
- finding_id: rec-f-fd83fb7c1f69e4ef
  issue_key: mim-reconciliation-historical-review-coverage-and-r-c2e60be54e8ad32b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na-silicate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T04:58:04Z;
    reviewed SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2;
    current SHA-256=5655d72545f3b5e0d55759fcada4bf9e516fa3a66287590f4f6fc2cc1e91c2e2;
    hash_changed=False. Reports=["reports/yaml_record_review/Na-silicate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:60720
    sodium silicate identity, CAS-backed structure, mineral role, and hydrate synonym
    rejection pass, but final SSSOM publishes a numbered source artifact.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c2e60be54e8ad32b
  evidence_ids:
  - ev-1db8ca471d68774b
  - ev-2476594bfad7b1e6
  - ev-5d2b5b07594f3262
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na-silicate.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
