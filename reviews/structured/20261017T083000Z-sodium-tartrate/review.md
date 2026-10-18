# Per-record structured review: Sodium_Tartrate (data/ingredients/mapped/Sodium_Tartrate.yaml)

- Review: 20261017T083000Z-sodium-tartrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Tartrate (data/ingredients/mapped/Sodium_Tartrate.yaml, record-9dfe7b5234312ae6, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Tartrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Tartrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-9dfe7b5234312ae6 | data/ingredients/mapped/Sodium_Tartrate.yaml | maintained | Sodium_Tartrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-9dfe7b5234312ae6 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-9dfe7b5234312ae6 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-9dfe7b5234312ae6 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-9dfe7b5234312ae6.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-9dfe7b5234312ae6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:50:08Z; reviewed SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1; current SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Tartrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63017 identity, CAS, merged Na-tartrate label, and final SSSOM row pass, but CARBON_SOURCE is not supported by its Mineral evidence.

## Findings

### rec-f-5fabacd77c2fbae4: Historical review coverage and residual narrative: Sodium_Tartrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-9dfe7b5234312ae6.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:50:08Z; reviewed SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1; current SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Tartrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63017 identity, CAS, merged Na-tartrate label, and final SSSOM row pass, but CARBON_SOURCE is not supported by its Mineral evidence.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-a23c39941c56c4cd | data/ingredients/mapped/Sodium_Tartrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1872],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63017","line":1874,"mapping_status":"MAPPED","ontology_id":"CHEBI:63017","preferred_term":"Sodium tartrate"}],"identifier":"CHEBI:63017","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":25,"edge_count":25,"occurrences":25},"occurrence_statistics":{"media_count":25,"total_occurrences":25},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63017","ontology_label":"sodium L-tartrate","ontology_source":"CHEBI"},"preferred_term":"Sodium tartrate","sssom_rows":[{"data_row":2608,"object_id":"CHEBI:63017","object_label":"sodium L-tartrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Tartrate","synonym_count":15} |
| ev-dc0fefd7e61cf1ef | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1872] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-92b627062fc0e508 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Tartrate; data-row positions=[2608] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2608,"object_id":"CHEBI:63017","object_label":"sodium L-tartrate","other":"(R-(R*,R*))-2,3-dihydroxybutanedioic acid, disodium salt&#124;Bisodium tartrate&#124;Disodium L-(+)-tartrate&#124;Disodium salt of L-(+)-tartaric acid&#124;Sodium L-(+)-tartrate&#124;Tartaric acid, disodium salt&#124;disodium (2R,3R)-2,3-dihydroxybutanedioate&#124;disodium (R-(R*,R*))-2,3-dihydroxybutanedioate&#124;disodium tartrate&#124;Na-tartrate&#124;CAS:868-18-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Tartrate","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-73c849935df64ece | docs/data/mapped_ingredients.csv; CSV lines=[1874] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63017","line":1874,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"25","ontology_id":"CHEBI:63017","preferred_term":"Sodium tartrate","total_occurrences":"25"}] |
| ev-8d4a136b64ce18c6 | reports/yaml_record_review/Sodium_Tartrate.md; &#96;data/ingredients/mapped/Sodium_Tartrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:20; Evidence:30; Completeness:45; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ceaf70c2a513c357 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1234] | context_only | [{"current_record_sha256":"5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1","finding_id":"SEM:f242accf8b38d1407d94","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-tartrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Tartrate (data/ingredients/mapped/Sodium_Tartrate.yaml)'
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
summary: Per-record structured review for Sodium_Tartrate (data/ingredients/mapped/Sodium_Tartrate.yaml,
  record-9dfe7b5234312ae6, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Tartrate.yaml
    sha256: 5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1
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
  - path: reports/yaml_record_review/Sodium_Tartrate.md
    sha256: 5bced5dfd22ca5074abbda048834b0a7ca1bc73b73b717ac29026bba0e48b1b0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-9dfe7b5234312ae6
  path: data/ingredients/mapped/Sodium_Tartrate.yaml
  label: Sodium_Tartrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Tartrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Tartrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Tartrate.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-9dfe7b5234312ae6
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-9dfe7b5234312ae6
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-9dfe7b5234312ae6
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-9dfe7b5234312ae6
evidence:
- evidence_id: ev-a23c39941c56c4cd
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Tartrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1872],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63017","line":1874,"mapping_status":"MAPPED","ontology_id":"CHEBI:63017","preferred_term":"Sodium
    tartrate"}],"identifier":"CHEBI:63017","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":25,"edge_count":25,"occurrences":25},"occurrence_statistics":{"media_count":25,"total_occurrences":25},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63017","ontology_label":"sodium
    L-tartrate","ontology_source":"CHEBI"},"preferred_term":"Sodium tartrate","sssom_rows":[{"data_row":2608,"object_id":"CHEBI:63017","object_label":"sodium
    L-tartrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Tartrate","synonym_count":15}'
  snapshot_sha256: 5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1
- evidence_id: ev-dc0fefd7e61cf1ef
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1872]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-92b627062fc0e508
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Tartrate; data-row positions=[2608]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2608,"object_id":"CHEBI:63017","object_label":"sodium
    L-tartrate","other":"(R-(R*,R*))-2,3-dihydroxybutanedioic acid, disodium salt|Bisodium
    tartrate|Disodium L-(+)-tartrate|Disodium salt of L-(+)-tartaric acid|Sodium L-(+)-tartrate|Tartaric
    acid, disodium salt|disodium (2R,3R)-2,3-dihydroxybutanedioate|disodium (R-(R*,R*))-2,3-dihydroxybutanedioate|disodium
    tartrate|Na-tartrate|CAS:868-18-8","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Tartrate","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-73c849935df64ece
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1874]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63017","line":1874,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"25","ontology_id":"CHEBI:63017","preferred_term":"Sodium
    tartrate","total_occurrences":"25"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8d4a136b64ce18c6
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Tartrate.md
  locator: '`data/ingredients/mapped/Sodium_Tartrate.yaml`:2; Verdict:4; Identity:11;
    Validation:20; Evidence:30; Completeness:45; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5bced5dfd22ca5074abbda048834b0a7ca1bc73b73b717ac29026bba0e48b1b0
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Sodium_Tartrate.yaml`,\
    \ remove\n  `nutritional_roles.CARBON_SOURCE` unless checked source evidence supports\n\
    \  that role for sodium L-tartrate."
- evidence_id: ev-ceaf70c2a513c357
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1234]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1","finding_id":"SEM:f242accf8b38d1407d94","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-8c9816c4ecff60a4
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-9dfe7b5234312ae6
  evidence_ids:
  - ev-a23c39941c56c4cd
  - ev-dc0fefd7e61cf1ef
  - ev-92b627062fc0e508
  - ev-73c849935df64ece
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-cc7d2f7f8bfd698b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9dfe7b5234312ae6
  evidence_ids:
  - ev-8d4a136b64ce18c6
  - ev-a23c39941c56c4cd
  - ev-ceaf70c2a513c357
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:50:08Z;
    reviewed SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1;
    current SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Tartrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:63017 identity, CAS, merged Na-tartrate label, and final SSSOM row pass,
    but CARBON_SOURCE is not supported by its Mineral evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8d4a136b64ce18c6
    - ev-a23c39941c56c4cd
  - name: legacy-native-ids
    value: '["SEM:f242accf8b38d1407d94"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-a23c39941c56c4cd
    - ev-8d4a136b64ce18c6
    - ev-ceaf70c2a513c357
findings:
- finding_id: rec-f-5fabacd77c2fbae4
  issue_key: mim-reconciliation-historical-review-coverage-and-r-9dfe7b5234312ae6
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sodium_Tartrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:50:08Z;
    reviewed SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1;
    current SHA-256=5cb59f73fef83d0cd22e6f4fc9051d6c42d04dea7b14ce5ee30a70009955bab1;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Tartrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI:63017 identity, CAS, merged Na-tartrate label, and final SSSOM row pass,
    but CARBON_SOURCE is not supported by its Mineral evidence.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-9dfe7b5234312ae6
  evidence_ids:
  - ev-8d4a136b64ce18c6
  - ev-a23c39941c56c4cd
  - ev-ceaf70c2a513c357
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Tartrate.yaml
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
