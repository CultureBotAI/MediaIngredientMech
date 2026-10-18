# Per-record structured review: Threonine (data/ingredients/mapped/Threonine.yaml)

- Review: 20261017T083000Z-threonine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Threonine (data/ingredients/mapped/Threonine.yaml, record-624dce7642fed75b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Threonine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Threonine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-624dce7642fed75b | data/ingredients/mapped/Threonine.yaml | maintained | Threonine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-624dce7642fed75b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-624dce7642fed75b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-624dce7642fed75b | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-624dce7642fed75b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-624dce7642fed75b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:47:02Z; reviewed SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd; current SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd; hash_changed=False. Reports=["reports/yaml_record_review/Threonine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26986 identity and final SSSOM row pass, but related stereo label DL-threonine leaks into final SSSOM other.

## Findings

### rec-f-c9460b6edd41c6d3: Historical review coverage and residual narrative: Threonine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-624dce7642fed75b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:47:02Z; reviewed SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd; current SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd; hash_changed=False. Reports=["reports/yaml_record_review/Threonine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26986 identity and final SSSOM row pass, but related stereo label DL-threonine leaks into final SSSOM other.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a6075c917e9809ee | data/ingredients/mapped/Threonine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2463],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26986","line":2465,"mapping_status":"MAPPED","ontology_id":"CHEBI:26986","preferred_term":"Threonine"}],"identifier":"CHEBI:26986","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":22,"edge_count":22,"occurrences":22},"occurrence_statistics":{"media_count":22,"source_occurrences":[{"count":31,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":22},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26986","ontology_label":"threonine","ontology_source":"CHEBI"},"preferred_term":"Threonine","sssom_rows":[{"data_row":2774,"object_id":"CHEBI:26986","object_label":"threonine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Threonine","synonym_count":1} |
| ev-759754e33ede7214 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2463] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-b9c82d13da5a5d99 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Threonine; data-row positions=[2774] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2774,"object_id":"CHEBI:26986","object_label":"threonine","other":"DL-threonine","predicate_id":"skos:exactMatch","subject_id":"MIM:Threonine","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-57adf55674ef9ef3 | docs/data/mapped_ingredients.csv; CSV lines=[2465] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:26986","line":2465,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"22","ontology_id":"CHEBI:26986","preferred_term":"Threonine","total_occurrences":"22"}] |
| ev-21f68d53250befe3 | reports/yaml_record_review/Threonine.md; &#96;data/ingredients/mapped/Threonine.yaml&#96;:2; Verdict:4; Identity:10; Validation:24; Evidence:34; Completeness:46; Recommended Edits:56 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-450448d0eba5c991 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1289] | context_only | [{"current_record_sha256":"abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd","finding_id":"SEM:33651f4c95447a3b0cde","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-threonine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Threonine (data/ingredients/mapped/Threonine.yaml)'
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
summary: Per-record structured review for Threonine (data/ingredients/mapped/Threonine.yaml,
  record-624dce7642fed75b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Threonine.yaml
    sha256: abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd
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
  - path: reports/yaml_record_review/Threonine.md
    sha256: 1ccf2b2e9f457aa45374e61ac22f73de760706f7458b1ba174ab3cf3551cd5bb
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-624dce7642fed75b
  path: data/ingredients/mapped/Threonine.yaml
  label: Threonine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Threonine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Threonine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Threonine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-624dce7642fed75b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-624dce7642fed75b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-624dce7642fed75b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-624dce7642fed75b
evidence:
- evidence_id: ev-a6075c917e9809ee
  kind: record_content
  reference: data/ingredients/mapped/Threonine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2463],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:26986","line":2465,"mapping_status":"MAPPED","ontology_id":"CHEBI:26986","preferred_term":"Threonine"}],"identifier":"CHEBI:26986","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":22,"edge_count":22,"occurrences":22},"occurrence_statistics":{"media_count":22,"source_occurrences":[{"count":31,"source":"microbedecoder","source_columns":"BacDive_Metabolite_utilization"}],"total_occurrences":22},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:26986","ontology_label":"threonine","ontology_source":"CHEBI"},"preferred_term":"Threonine","sssom_rows":[{"data_row":2774,"object_id":"CHEBI:26986","object_label":"threonine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Threonine","synonym_count":1}'
  snapshot_sha256: abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd
- evidence_id: ev-759754e33ede7214
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2463]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-b9c82d13da5a5d99
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Threonine; data-row positions=[2774]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2774,"object_id":"CHEBI:26986","object_label":"threonine","other":"DL-threonine","predicate_id":"skos:exactMatch","subject_id":"MIM:Threonine","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-57adf55674ef9ef3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2465]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:26986","line":2465,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"22","ontology_id":"CHEBI:26986","preferred_term":"Threonine","total_occurrences":"22"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-21f68d53250befe3
  kind: prior_review
  reference: reports/yaml_record_review/Threonine.md
  locator: '`data/ingredients/mapped/Threonine.yaml`:2; Verdict:4; Identity:10; Validation:24;
    Evidence:34; Completeness:46; Recommended Edits:56'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1ccf2b2e9f457aa45374e61ac22f73de760706f7458b1ba174ab3cf3551cd5bb
  quote: "Recommended Edits:\n- Major: update the SSSOM synonym export so `RELATED_SYNONYM`\
    \ values such as\n  `DL-threonine` do not publish in exact `other`, or rehome\
    \ the racemate to a\n  bounded exact record if exact upstream grounding is desired.\
    \ Then rerun\n  strict validation, term validation, SSSOM publication, synonym-row\
    \ review,\n  and `scripts/validate_sssom_invariants.py`."
- evidence_id: ev-450448d0eba5c991
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1289]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd","finding_id":"SEM:33651f4c95447a3b0cde","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c2d12355dcad41fc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-624dce7642fed75b
  evidence_ids:
  - ev-a6075c917e9809ee
  - ev-759754e33ede7214
  - ev-b9c82d13da5a5d99
  - ev-57adf55674ef9ef3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a4965a84a9592e3b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-624dce7642fed75b
  evidence_ids:
  - ev-21f68d53250befe3
  - ev-a6075c917e9809ee
  - ev-450448d0eba5c991
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:47:02Z;
    reviewed SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd;
    current SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd;
    hash_changed=False. Reports=["reports/yaml_record_review/Threonine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26986
    identity and final SSSOM row pass, but related stereo label DL-threonine leaks
    into final SSSOM other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-21f68d53250befe3
    - ev-a6075c917e9809ee
  - name: legacy-native-ids
    value: '["SEM:33651f4c95447a3b0cde"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a6075c917e9809ee
    - ev-21f68d53250befe3
    - ev-450448d0eba5c991
findings:
- finding_id: rec-f-c9460b6edd41c6d3
  issue_key: mim-reconciliation-historical-review-coverage-and-r-624dce7642fed75b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Threonine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T18:47:02Z;
    reviewed SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd;
    current SHA-256=abd229fe1bc7cd52408e8d6d1c2ce9abf3adc7b2a18f95dc714f4a20c3bb8fbd;
    hash_changed=False. Reports=["reports/yaml_record_review/Threonine.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI:26986
    identity and final SSSOM row pass, but related stereo label DL-threonine leaks
    into final SSSOM other.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-624dce7642fed75b
  evidence_ids:
  - ev-21f68d53250befe3
  - ev-a6075c917e9809ee
  - ev-450448d0eba5c991
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Threonine.yaml
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
