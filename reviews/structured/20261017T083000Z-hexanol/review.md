# Per-record structured review: Hexanol (data/ingredients/mapped/Hexanol.yaml)

- Review: 20261017T083000Z-hexanol
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Hexanol (data/ingredients/mapped/Hexanol.yaml, record-23f95378e448c9e8, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Hexanol.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Hexanol.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-23f95378e448c9e8 | data/ingredients/mapped/Hexanol.yaml | maintained | Hexanol |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-23f95378e448c9e8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-23f95378e448c9e8 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-23f95378e448c9e8 | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-23f95378e448c9e8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-23f95378e448c9e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:28:39Z; reviewed SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316; current SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316; hash_changed=False. Reports=["reports/yaml_record_review/Hexanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: CAS 111-27-3 fixes the record as 1-hexanol, but the exact ChEBI target is the broader positional-isomer hexanol class.

## Findings

### rec-f-2cfdfe2b911c3895: Historical review coverage and residual narrative: Hexanol

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-23f95378e448c9e8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:28:39Z; reviewed SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316; current SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316; hash_changed=False. Reports=["reports/yaml_record_review/Hexanol.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: CAS 111-27-3 fixes the record as 1-hexanol, but the exact ChEBI target is the broader positional-isomer hexanol class.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-368967d6a9ad416f | data/ingredients/mapped/Hexanol.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1127],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:143552","line":1129,"mapping_status":"MAPPED","ontology_id":"CHEBI:143552","preferred_term":"hexanol"}],"identifier":"CHEBI:143552","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:143552","ontology_label":"hexanol","ontology_source":"CHEBI"},"preferred_term":"hexanol","sssom_rows":[{"data_row":1430,"object_id":"CHEBI:143552","object_label":"hexanol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hexanol","synonym_count":0} |
| ev-d1fbabf885e8b2ed | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1127] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-794b25ed13254eb7 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Hexanol; data-row positions=[1430] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1430,"object_id":"CHEBI:143552","object_label":"hexanol","other":"CAS:111-27-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Hexanol","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-e864f04fd9b6ed54 | docs/data/mapped_ingredients.csv; CSV lines=[1129] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:143552","line":1129,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:143552","preferred_term":"hexanol","total_occurrences":"0"}] |
| ev-696bda2c7597daea | reports/yaml_record_review/Hexanol.md; &#96;data/ingredients/mapped/Hexanol.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:31; Completeness:47; Recommended Edits:55 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-51146b0f5c628bc7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[731] | context_only | [{"current_record_sha256":"fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316","finding_id":"SEM:76ee364e396c36af31b0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-hexanol
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Hexanol (data/ingredients/mapped/Hexanol.yaml)'
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
summary: Per-record structured review for Hexanol (data/ingredients/mapped/Hexanol.yaml,
  record-23f95378e448c9e8, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Hexanol.yaml
    sha256: fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316
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
  - path: reports/yaml_record_review/Hexanol.md
    sha256: 905e6c31fc9a21db533b9ab7c8bc3ced6c469baf3b0814d35bd16f4a1e505ab4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-23f95378e448c9e8
  path: data/ingredients/mapped/Hexanol.yaml
  label: Hexanol
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hexanol.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Hexanol.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Hexanol.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-23f95378e448c9e8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-23f95378e448c9e8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-23f95378e448c9e8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-23f95378e448c9e8
evidence:
- evidence_id: ev-368967d6a9ad416f
  kind: record_content
  reference: data/ingredients/mapped/Hexanol.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1127],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:143552","line":1129,"mapping_status":"MAPPED","ontology_id":"CHEBI:143552","preferred_term":"hexanol"}],"identifier":"CHEBI:143552","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:143552","ontology_label":"hexanol","ontology_source":"CHEBI"},"preferred_term":"hexanol","sssom_rows":[{"data_row":1430,"object_id":"CHEBI:143552","object_label":"hexanol","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Hexanol","synonym_count":0}'
  snapshot_sha256: fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316
- evidence_id: ev-d1fbabf885e8b2ed
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1127]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-794b25ed13254eb7
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Hexanol; data-row positions=[1430]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1430,"object_id":"CHEBI:143552","object_label":"hexanol","other":"CAS:111-27-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Hexanol","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-e864f04fd9b6ed54
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1129]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:143552","line":1129,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:143552","preferred_term":"hexanol","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-696bda2c7597daea
  kind: prior_review
  reference: reports/yaml_record_review/Hexanol.md
  locator: '`data/ingredients/mapped/Hexanol.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:31; Completeness:47; Recommended Edits:55'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 905e6c31fc9a21db533b9ab7c8bc3ced6c469baf3b0814d35bd16f4a1e505ab4
  quote: "Recommended Edits:\n- Major: remap the record from `CHEBI:143552` `hexanol`\
    \ to `CHEBI:87393`\n  `hexan-1-ol`, keep CAS `111-27-3`, backfill the 1-hexanol\
    \ formula/InChI/\n  SMILES, regenerate the final SSSOM row, and rerun strict,\
    \ term, round-trip,\n  id-label, and SSSOM validation."
- evidence_id: ev-51146b0f5c628bc7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[731]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316","finding_id":"SEM:76ee364e396c36af31b0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-25eb05f491e11443
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-23f95378e448c9e8
  evidence_ids:
  - ev-368967d6a9ad416f
  - ev-d1fbabf885e8b2ed
  - ev-794b25ed13254eb7
  - ev-e864f04fd9b6ed54
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f999e6c940d1a5a8
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-23f95378e448c9e8
  evidence_ids:
  - ev-696bda2c7597daea
  - ev-368967d6a9ad416f
  - ev-51146b0f5c628bc7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:28:39Z;
    reviewed SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316;
    current SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316;
    hash_changed=False. Reports=["reports/yaml_record_review/Hexanol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: CAS 111-27-3 fixes the
    record as 1-hexanol, but the exact ChEBI target is the broader positional-isomer
    hexanol class.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-696bda2c7597daea
    - ev-368967d6a9ad416f
  - name: legacy-native-ids
    value: '["SEM:76ee364e396c36af31b0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-368967d6a9ad416f
    - ev-696bda2c7597daea
    - ev-51146b0f5c628bc7
findings:
- finding_id: rec-f-2cfdfe2b911c3895
  issue_key: mim-reconciliation-historical-review-coverage-and-r-23f95378e448c9e8
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Hexanol'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T19:28:39Z;
    reviewed SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316;
    current SHA-256=fccfbc3e6e5309ca29b27077794e8e5c22df641b7b2f48692cc413253c546316;
    hash_changed=False. Reports=["reports/yaml_record_review/Hexanol.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: CAS 111-27-3 fixes the
    record as 1-hexanol, but the exact ChEBI target is the broader positional-isomer
    hexanol class.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-23f95378e448c9e8
  evidence_ids:
  - ev-696bda2c7597daea
  - ev-368967d6a9ad416f
  - ev-51146b0f5c628bc7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Hexanol.yaml
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
