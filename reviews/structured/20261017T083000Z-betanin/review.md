# Per-record structured review: Betanin (data/ingredients/mapped/Betanin.yaml)

- Review: 20261017T083000Z-betanin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Betanin (data/ingredients/mapped/Betanin.yaml, record-fe74d3490c87e184, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Betanin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Betanin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fe74d3490c87e184 | data/ingredients/mapped/Betanin.yaml | maintained | Betanin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fe74d3490c87e184 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-fe74d3490c87e184 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fe74d3490c87e184 | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fe74d3490c87e184.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fe74d3490c87e184.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z; reviewed SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0; current SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0; hash_changed=False. Reports=["reports/yaml_record_review/Betanin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI Betanin identity, CAS, structure fields, SSSOM row, and aggregate copy pass, but chemical_properties.data_source is stale after the ChEBI structure backfill.

## Findings

### rec-f-786ff14d9f068737: Historical review coverage and residual narrative: Betanin

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-fe74d3490c87e184.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z; reviewed SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0; current SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0; hash_changed=False. Reports=["reports/yaml_record_review/Betanin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI Betanin identity, CAS, structure fields, SSSOM row, and aggregate copy pass, but chemical_properties.data_source is stale after the ChEBI structure backfill.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ca2f017d62075ca8 | data/ingredients/mapped/Betanin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[584],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3080","line":586,"mapping_status":"MAPPED","ontology_id":"CHEBI:3080","preferred_term":"Betanin"}],"identifier":"CHEBI:3080","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3080","ontology_label":"Betanin","ontology_source":"CHEBI"},"preferred_term":"Betanin","sssom_rows":[{"data_row":539,"object_id":"CHEBI:3080","object_label":"Betanin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Betanin","synonym_count":0} |
| ev-9621e3a7e35bc07f | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [584] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d5062ee5b1bc2cea | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Betanin; data-row positions=[539] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":539,"object_id":"CHEBI:3080","object_label":"Betanin","other":"CAS:7659-95-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Betanin","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-b786a3df308ee8ae | docs/data/mapped_ingredients.csv; CSV lines=[586] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3080","line":586,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3080","preferred_term":"Betanin","total_occurrences":"0"}] |
| ev-0121bc21e6c89514 | reports/yaml_record_review/Betanin.md; &#96;data/ingredients/mapped/Betanin.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:36; Completeness:50; Recommended Edits:59 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6c573652dbc95cb0 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[313] | context_only | [{"current_record_sha256":"dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0","finding_id":"SEM:1ba951bcffe9495496ab","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-betanin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Betanin (data/ingredients/mapped/Betanin.yaml)'
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
summary: Per-record structured review for Betanin (data/ingredients/mapped/Betanin.yaml,
  record-fe74d3490c87e184, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Betanin.yaml
    sha256: dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0
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
  - path: reports/yaml_record_review/Betanin.md
    sha256: 0eea7eba7c1fdc5958920ccfe5ac8e714dd5a3798426d5e939c5dd0e262c93d7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fe74d3490c87e184
  path: data/ingredients/mapped/Betanin.yaml
  label: Betanin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Betanin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Betanin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Betanin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fe74d3490c87e184
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fe74d3490c87e184
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-fe74d3490c87e184
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fe74d3490c87e184
evidence:
- evidence_id: ev-ca2f017d62075ca8
  kind: record_content
  reference: data/ingredients/mapped/Betanin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[584],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3080","line":586,"mapping_status":"MAPPED","ontology_id":"CHEBI:3080","preferred_term":"Betanin"}],"identifier":"CHEBI:3080","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3080","ontology_label":"Betanin","ontology_source":"CHEBI"},"preferred_term":"Betanin","sssom_rows":[{"data_row":539,"object_id":"CHEBI:3080","object_label":"Betanin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Betanin","synonym_count":0}'
  snapshot_sha256: dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0
- evidence_id: ev-9621e3a7e35bc07f
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [584]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d5062ee5b1bc2cea
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Betanin; data-row positions=[539]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":539,"object_id":"CHEBI:3080","object_label":"Betanin","other":"CAS:7659-95-2","predicate_id":"skos:exactMatch","subject_id":"MIM:Betanin","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b786a3df308ee8ae
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[586]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3080","line":586,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3080","preferred_term":"Betanin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0121bc21e6c89514
  kind: prior_review
  reference: reports/yaml_record_review/Betanin.md
  locator: '`data/ingredients/mapped/Betanin.yaml`:2; Verdict:4; Identity:11; Validation:23;
    Evidence:36; Completeness:50; Recommended Edits:59'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 0eea7eba7c1fdc5958920ccfe5ac8e714dd5a3798426d5e939c5dd0e262c93d7
  quote: "Recommended Edits:\n- Minor: update `data/ingredients/mapped/Betanin.yaml`\
    \ so the\n  `chemical_properties` provenance accurately names ChEBI as the source\
    \ for the\n  formula, InChI, and SMILES; then run `just sync-curated` and focused\n\
    \  strict/term validation."
- evidence_id: ev-6c573652dbc95cb0
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[313]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0","finding_id":"SEM:1ba951bcffe9495496ab","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-fbea3389a09dc520
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fe74d3490c87e184
  evidence_ids:
  - ev-ca2f017d62075ca8
  - ev-9621e3a7e35bc07f
  - ev-d5062ee5b1bc2cea
  - ev-b786a3df308ee8ae
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c069b44bd531a686
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fe74d3490c87e184
  evidence_ids:
  - ev-0121bc21e6c89514
  - ev-ca2f017d62075ca8
  - ev-6c573652dbc95cb0
  details: 'Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z;
    reviewed SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0;
    current SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0;
    hash_changed=False. Reports=["reports/yaml_record_review/Betanin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI Betanin
    identity, CAS, structure fields, SSSOM row, and aggregate copy pass, but chemical_properties.data_source
    is stale after the ChEBI structure backfill.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0121bc21e6c89514
    - ev-ca2f017d62075ca8
  - name: legacy-native-ids
    value: '["SEM:1ba951bcffe9495496ab"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ca2f017d62075ca8
    - ev-0121bc21e6c89514
    - ev-6c573652dbc95cb0
findings:
- finding_id: rec-f-786ff14d9f068737
  issue_key: mim-reconciliation-historical-review-coverage-and-r-fe74d3490c87e184
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Betanin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=minor; reviewed_at=2026-09-16T09:47:04Z;
    reviewed SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0;
    current SHA-256=dcf052f3e6d0d339e6a3d943180f06344594785aed9f27b0e7803140a09d45a0;
    hash_changed=False. Reports=["reports/yaml_record_review/Betanin.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI Betanin
    identity, CAS, structure fields, SSSOM row, and aggregate copy pass, but chemical_properties.data_source
    is stale after the ChEBI structure backfill.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fe74d3490c87e184
  evidence_ids:
  - ev-0121bc21e6c89514
  - ev-ca2f017d62075ca8
  - ev-6c573652dbc95cb0
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Betanin.yaml
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
