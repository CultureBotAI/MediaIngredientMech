# Per-record structured review: Sodium_Nitrate_070_M_Stock (data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml)

- Review: 20261017T083000Z-sodium-nitrate-070-m-stock
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Nitrate_070_M_Stock (data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml, record-b5edb89d2b1cc6bd, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-b5edb89d2b1cc6bd | data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml | maintained | Sodium_Nitrate_070_M_Stock |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-b5edb89d2b1cc6bd | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-b5edb89d2b1cc6bd | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-b5edb89d2b1cc6bd | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-b5edb89d2b1cc6bd.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-b5edb89d2b1cc6bd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:26:11Z; reviewed SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c; current SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The stock-solution parent and exact registry rows pass, but final SSSOM exports sodium-nitrate solute synonyms on the stock subject.

## Findings

### rec-f-44fe2ec69354cfdf: Historical review coverage and residual narrative: Sodium_Nitrate_070_M_Stock

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-b5edb89d2b1cc6bd.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:26:11Z; reviewed SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c; current SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The stock-solution parent and exact registry rows pass, but final SSSOM exports sodium-nitrate solute synonyms on the stock subject.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-dbc274124c484086 | data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1855],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","line":1857,"mapping_status":"MAPPED","ontology_id":"CHEBI:63005","preferred_term":"Sodium nitrate (0.70 M stock)"}],"identifier":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:63005","ontology_label":"sodium nitrate","ontology_source":"CHEBI"},"preferred_term":"Sodium nitrate (0.70 M stock)","sssom_rows":[{"data_row":2579,"object_id":"CHEBI:63005","object_label":"sodium nitrate","predicate_id":"skos:broadMatch"},{"data_row":2580,"object_id":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","object_label":"Sodium nitrate (0.70 M stock)","predicate_id":"skos:exactMatch"},{"data_row":2581,"object_id":"kgmicrobe.compound:sodium_nitrate_070_m_stock","object_label":"Sodium nitrate (0.70 M stock)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Nitrate_070_M_Stock","synonym_count":2} |
| ev-29d6c6beab82dbbc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1855] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c128f28dbc063fe3 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Nitrate_070_M_Stock; data-row positions=[2579,2580,2581] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2579,"object_id":"CHEBI:63005","object_label":"sodium nitrate","other":"NaNO3&#124;sodium trioxidonitrate(1-)","predicate_id":"skos:broadMatch","subject_id":"MIM:Sodium_Nitrate_070_M_Stock","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":2580,"object_id":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","object_label":"Sodium nitrate (0.70 M stock)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Nitrate_070_M_Stock","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"},{"data_row":2581,"object_id":"kgmicrobe.compound:sodium_nitrate_070_m_stock","object_label":"Sodium nitrate (0.70 M stock)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Nitrate_070_M_Stock","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-1d457b5586d2bace | docs/data/mapped_ingredients.csv; CSV lines=[1857] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","line":1857,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:63005","preferred_term":"Sodium nitrate (0.70 M stock)","total_occurrences":"1"}] |
| ev-82bda545fcc42a71 | reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md; &#96;data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-878bb86e75a035a7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1224] | context_only | [{"current_record_sha256":"eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c","finding_id":"SEM:3585c6eb4f9c56fab8b1","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-nitrate-070-m-stock
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Nitrate_070_M_Stock (data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml)'
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
summary: Per-record structured review for Sodium_Nitrate_070_M_Stock (data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml,
  record-b5edb89d2b1cc6bd, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    sha256: eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c
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
  - path: reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md
    sha256: ca35d0fea85a47b002468e2d4d4212b0747d3bc242fbee6e6d051be80c401175
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-b5edb89d2b1cc6bd
  path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
  label: Sodium_Nitrate_070_M_Stock
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-b5edb89d2b1cc6bd
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-b5edb89d2b1cc6bd
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-b5edb89d2b1cc6bd
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-b5edb89d2b1cc6bd
evidence:
- evidence_id: ev-dbc274124c484086
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1855],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","line":1857,"mapping_status":"MAPPED","ontology_id":"CHEBI:63005","preferred_term":"Sodium
    nitrate (0.70 M stock)"}],"identifier":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1,"edge_count":1,"occurrences":1},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:63005","ontology_label":"sodium
    nitrate","ontology_source":"CHEBI"},"preferred_term":"Sodium nitrate (0.70 M stock)","sssom_rows":[{"data_row":2579,"object_id":"CHEBI:63005","object_label":"sodium
    nitrate","predicate_id":"skos:broadMatch"},{"data_row":2580,"object_id":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","object_label":"Sodium
    nitrate (0.70 M stock)","predicate_id":"skos:exactMatch"},{"data_row":2581,"object_id":"kgmicrobe.compound:sodium_nitrate_070_m_stock","object_label":"Sodium
    nitrate (0.70 M stock)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Nitrate_070_M_Stock","synonym_count":2}'
  snapshot_sha256: eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c
- evidence_id: ev-29d6c6beab82dbbc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1855]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c128f28dbc063fe3
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Nitrate_070_M_Stock; data-row positions=[2579,2580,2581]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2579,"object_id":"CHEBI:63005","object_label":"sodium
    nitrate","other":"NaNO3|sodium trioxidonitrate(1-)","predicate_id":"skos:broadMatch","subject_id":"MIM:Sodium_Nitrate_070_M_Stock","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":2580,"object_id":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","object_label":"Sodium
    nitrate (0.70 M stock)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Nitrate_070_M_Stock","validation_method":"none|UNKNOWN_TERM|2026-07-07"},{"data_row":2581,"object_id":"kgmicrobe.compound:sodium_nitrate_070_m_stock","object_label":"Sodium
    nitrate (0.70 M stock)","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Nitrate_070_M_Stock","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-1d457b5586d2bace
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1857]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:sodium_nitrate_~28070_m_stock~29","line":1857,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"CHEBI:63005","preferred_term":"Sodium
    nitrate (0.70 M stock)","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-82bda545fcc42a71
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md
  locator: '`data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: ca35d0fea85a47b002468e2d4d4212b0747d3bc242fbee6e6d051be80c401175
- evidence_id: ev-878bb86e75a035a7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1224]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c","finding_id":"SEM:3585c6eb4f9c56fab8b1","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0595d44c2d3f89d7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-b5edb89d2b1cc6bd
  evidence_ids:
  - ev-dbc274124c484086
  - ev-29d6c6beab82dbbc
  - ev-c128f28dbc063fe3
  - ev-1d457b5586d2bace
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c068d21281fe255a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b5edb89d2b1cc6bd
  evidence_ids:
  - ev-82bda545fcc42a71
  - ev-dbc274124c484086
  - ev-878bb86e75a035a7
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:26:11Z;
    reviewed SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c;
    current SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The stock-solution
    parent and exact registry rows pass, but final SSSOM exports sodium-nitrate solute
    synonyms on the stock subject.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-82bda545fcc42a71
    - ev-dbc274124c484086
  - name: legacy-native-ids
    value: '["SEM:3585c6eb4f9c56fab8b1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-dbc274124c484086
    - ev-82bda545fcc42a71
    - ev-878bb86e75a035a7
findings:
- finding_id: rec-f-44fe2ec69354cfdf
  issue_key: mim-reconciliation-historical-review-coverage-and-r-b5edb89d2b1cc6bd
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sodium_Nitrate_070_M_Stock'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T15:26:11Z;
    reviewed SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c;
    current SHA-256=eca7428c811737e50f6146e617e8e6530a96c07d8be51069abf11aaf31aae98c;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Nitrate_070_M_Stock.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The stock-solution
    parent and exact registry rows pass, but final SSSOM exports sodium-nitrate solute
    synonyms on the stock subject.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-b5edb89d2b1cc6bd
  evidence_ids:
  - ev-82bda545fcc42a71
  - ev-dbc274124c484086
  - ev-878bb86e75a035a7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Nitrate_070_M_Stock.yaml
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
