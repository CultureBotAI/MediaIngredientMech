# Per-record structured review: Aloin (data/ingredients/mapped/Aloin.yaml)

- Review: 20261017T083000Z-aloin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Aloin (data/ingredients/mapped/Aloin.yaml, record-3f729df3a55ada6f, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Aloin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Aloin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-3f729df3a55ada6f | data/ingredients/mapped/Aloin.yaml | maintained | Aloin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-3f729df3a55ada6f | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-3f729df3a55ada6f | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-3f729df3a55ada6f | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-3f729df3a55ada6f.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-3f729df3a55ada6f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z; reviewed SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5; current SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5; hash_changed=False. Reports=["reports/yaml_record_review/Aloin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate pass; one historical auto-backfill event has truncated structure prose.

## Findings

### rec-f-f4f0ce554810a48a: Historical review coverage and residual narrative: Aloin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-3f729df3a55ada6f.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z; reviewed SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5; current SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5; hash_changed=False. Reports=["reports/yaml_record_review/Aloin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI identity, CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate pass; one historical auto-backfill event has truncated structure prose.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-520f0816e78477d1 | data/ingredients/mapped/Aloin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:73222","line":475,"mapping_status":"MAPPED","ontology_id":"CHEBI:73222","preferred_term":"Aloin"}],"identifier":"CHEBI:73222","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:73222","ontology_label":"aloin","ontology_source":"CHEBI"},"preferred_term":"Aloin","sssom_rows":[{"data_row":331,"object_id":"CHEBI:73222","object_label":"aloin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Aloin","synonym_count":1} |
| ev-de46a311d1687d2b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [473] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-7f7c27ef375d9baa | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Aloin; data-row positions=[331] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":331,"object_id":"CHEBI:73222","object_label":"aloin","other":"(1S)-1,5-anhydro-1-[4,5-dihydroxy-2-(hydroxymethyl)-10-oxo-9,10-dihydroanthracen-9-yl]-D-glucitol&#124;CAS:5133-19-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Aloin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-33cdc9a02b133aff | docs/data/mapped_ingredients.csv; CSV lines=[475] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:73222","line":475,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73222","preferred_term":"Aloin","total_occurrences":"0"}] |
| ev-d8afeb3adc148408 | reports/yaml_record_review/Aloin.md; &#96;data/ingredients/mapped/Aloin.yaml&#96;:2; Verdict:4; Identity:11; Validation:27; Evidence:44; Completeness:58; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-35d76a4eb2a7f5aa | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[236] | context_only | [{"current_record_sha256":"f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5","finding_id":"SEM:255d7cb47996db9b4dd5","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-aloin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Aloin (data/ingredients/mapped/Aloin.yaml)'
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
summary: Per-record structured review for Aloin (data/ingredients/mapped/Aloin.yaml,
  record-3f729df3a55ada6f, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Aloin.yaml
    sha256: f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5
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
  - path: reports/yaml_record_review/Aloin.md
    sha256: a74db68ae63178b9e82d78417f429a7e1eb323670cbe07fa9112d6bdceae47c1
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-3f729df3a55ada6f
  path: data/ingredients/mapped/Aloin.yaml
  label: Aloin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Aloin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Aloin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Aloin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-3f729df3a55ada6f
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-3f729df3a55ada6f
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-3f729df3a55ada6f
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-3f729df3a55ada6f
evidence:
- evidence_id: ev-520f0816e78477d1
  kind: record_content
  reference: data/ingredients/mapped/Aloin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[473],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:73222","line":475,"mapping_status":"MAPPED","ontology_id":"CHEBI:73222","preferred_term":"Aloin"}],"identifier":"CHEBI:73222","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:73222","ontology_label":"aloin","ontology_source":"CHEBI"},"preferred_term":"Aloin","sssom_rows":[{"data_row":331,"object_id":"CHEBI:73222","object_label":"aloin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Aloin","synonym_count":1}'
  snapshot_sha256: f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5
- evidence_id: ev-de46a311d1687d2b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [473]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-7f7c27ef375d9baa
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Aloin; data-row positions=[331]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":331,"object_id":"CHEBI:73222","object_label":"aloin","other":"(1S)-1,5-anhydro-1-[4,5-dihydroxy-2-(hydroxymethyl)-10-oxo-9,10-dihydroanthracen-9-yl]-D-glucitol|CAS:5133-19-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Aloin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-33cdc9a02b133aff
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[475]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:73222","line":475,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:73222","preferred_term":"Aloin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-d8afeb3adc148408
  kind: prior_review
  reference: reports/yaml_record_review/Aloin.md
  locator: '`data/ingredients/mapped/Aloin.yaml`:2; Verdict:4; Identity:11; Validation:27;
    Evidence:44; Completeness:58; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a74db68ae63178b9e82d78417f429a7e1eb323670cbe07fa9112d6bdceae47c1
  quote: "Recommended Edits:\n- Optionally replace the truncated auto-backfill `changes`\
    \ prose in\n  `data/ingredients/mapped/Aloin.yaml` with a complete structure summary\
    \ or a\n  concise non-structural note. No identity, mapping, or exported SSSOM\
    \ change\n  is needed."
- evidence_id: ev-35d76a4eb2a7f5aa
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[236]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5","finding_id":"SEM:255d7cb47996db9b4dd5","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e105b606bd25d7d1
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-3f729df3a55ada6f
  evidence_ids:
  - ev-520f0816e78477d1
  - ev-de46a311d1687d2b
  - ev-7f7c27ef375d9baa
  - ev-33cdc9a02b133aff
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-704a5b6b9828778c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3f729df3a55ada6f
  evidence_ids:
  - ev-d8afeb3adc148408
  - ev-520f0816e78477d1
  - ev-35d76a4eb2a7f5aa
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z;
    reviewed SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5;
    current SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5;
    hash_changed=False. Reports=["reports/yaml_record_review/Aloin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI identity,
    CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate pass;
    one historical auto-backfill event has truncated structure prose.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-d8afeb3adc148408
    - ev-520f0816e78477d1
  - name: legacy-native-ids
    value: '["SEM:255d7cb47996db9b4dd5"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-520f0816e78477d1
    - ev-d8afeb3adc148408
    - ev-35d76a4eb2a7f5aa
findings:
- finding_id: rec-f-f4f0ce554810a48a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-3f729df3a55ada6f
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Aloin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T07:42:36Z;
    reviewed SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5;
    current SHA-256=f4caf35b4367f1752b54986f1b40d28da01cd08865cda82b15f6e4e664b3ccb5;
    hash_changed=False. Reports=["reports/yaml_record_review/Aloin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI identity,
    CAS, CultureBotHT source, chemistry, exact synonym, SSSOM row, and aggregate pass;
    one historical auto-backfill event has truncated structure prose.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-3f729df3a55ada6f
  evidence_ids:
  - ev-d8afeb3adc148408
  - ev-520f0816e78477d1
  - ev-35d76a4eb2a7f5aa
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Aloin.yaml
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
