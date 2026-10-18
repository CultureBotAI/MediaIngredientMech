# Per-record structured review: Kawain (data/ingredients/mapped/Kawain.yaml)

- Review: 20261017T083000Z-kawain
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Kawain (data/ingredients/mapped/Kawain.yaml, record-47c595f74a7e8ace, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Kawain.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Kawain.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-47c595f74a7e8ace | data/ingredients/mapped/Kawain.yaml | maintained | Kawain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-47c595f74a7e8ace | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-47c595f74a7e8ace | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-47c595f74a7e8ace | Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-47c595f74a7e8ace.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-47c595f74a7e8ace.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:35:37Z; reviewed SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59; current SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59; hash_changed=False. Reports=["reports/yaml_record_review/Kawain.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-specific regrounding to CHEBI:156288 and final SSSOM row pass, but the InChI and SMILES still describe the old stereospecific CHEBI:6117 form.

## Findings

### rec-f-216dfac887b1eb81: Historical review coverage and residual narrative: Kawain

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-47c595f74a7e8ace.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:35:37Z; reviewed SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59; current SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59; hash_changed=False. Reports=["reports/yaml_record_review/Kawain.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-specific regrounding to CHEBI:156288 and final SSSOM row pass, but the InChI and SMILES still describe the old stereospecific CHEBI:6117 form.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-24e8f9536e7a224d | data/ingredients/mapped/Kawain.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1198],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:156288","line":1200,"mapping_status":"MAPPED","ontology_id":"CHEBI:156288","preferred_term":"Kawain"}],"identifier":"CHEBI:156288","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:156288","ontology_label":"DL-kavain","ontology_source":"CHEBI"},"preferred_term":"Kawain","sssom_rows":[{"data_row":1542,"object_id":"CHEBI:156288","object_label":"DL-kavain","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kawain","synonym_count":0} |
| ev-534c8bba277de551 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1198] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-807348d6355c0e1b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Kawain; data-row positions=[1542] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1542,"object_id":"CHEBI:156288","object_label":"DL-kavain","other":"CAS:3155-48-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Kawain","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-8a3b6d90ef1ab521 | docs/data/mapped_ingredients.csv; CSV lines=[1200] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:156288","line":1200,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:156288","preferred_term":"Kawain","total_occurrences":"0"}] |
| ev-0153dc80452e538a | reports/yaml_record_review/Kawain.md; &#96;data/ingredients/mapped/Kawain.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:33; Completeness:55; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6cf7d8b5947a08cb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[769] | context_only | [{"current_record_sha256":"9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59","finding_id":"SEM:242b4b54eb52cb3930c0","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024635Z-mim-reconcile-all-batch-07.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-kawain
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Kawain (data/ingredients/mapped/Kawain.yaml)'
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
summary: Per-record structured review for Kawain (data/ingredients/mapped/Kawain.yaml,
  record-47c595f74a7e8ace, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Kawain.yaml
    sha256: 9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59
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
  - path: reports/yaml_record_review/Kawain.md
    sha256: c666d9f9bdb605454c38a67237d42cec080e1ace8653bac2b00ea5ad5169200c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-47c595f74a7e8ace
  path: data/ingredients/mapped/Kawain.yaml
  label: Kawain
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kawain.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Kawain.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Kawain.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-47c595f74a7e8ace
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-47c595f74a7e8ace
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-47c595f74a7e8ace
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024635Z-mim-reconcile-all-batch-07
    and semantic review dispositions on HEAD.
  target_ids:
  - record-47c595f74a7e8ace
evidence:
- evidence_id: ev-24e8f9536e7a224d
  kind: record_content
  reference: data/ingredients/mapped/Kawain.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1198],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:156288","line":1200,"mapping_status":"MAPPED","ontology_id":"CHEBI:156288","preferred_term":"Kawain"}],"identifier":"CHEBI:156288","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:156288","ontology_label":"DL-kavain","ontology_source":"CHEBI"},"preferred_term":"Kawain","sssom_rows":[{"data_row":1542,"object_id":"CHEBI:156288","object_label":"DL-kavain","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Kawain","synonym_count":0}'
  snapshot_sha256: 9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59
- evidence_id: ev-534c8bba277de551
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1198]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-807348d6355c0e1b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Kawain; data-row positions=[1542]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1542,"object_id":"CHEBI:156288","object_label":"DL-kavain","other":"CAS:3155-48-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Kawain","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8a3b6d90ef1ab521
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1200]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:156288","line":1200,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:156288","preferred_term":"Kawain","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-0153dc80452e538a
  kind: prior_review
  reference: reports/yaml_record_review/Kawain.md
  locator: '`data/ingredients/mapped/Kawain.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:33; Completeness:55; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c666d9f9bdb605454c38a67237d42cec080e1ace8653bac2b00ea5ad5169200c
  quote: "Recommended Edits:\n- Major: update or clear `chemical_properties.inchi`\
    \ and\n  `chemical_properties.smiles` in `data/ingredients/mapped/Kawain.yaml`\
    \ so they\n  no longer encode the old `CHEBI:6117` stereospecific form, then synchronize\n\
    \  the aggregate and rerun strict, term, round-trip, component, and SSSOM\n  validation."
- evidence_id: ev-6cf7d8b5947a08cb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[769]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59","finding_id":"SEM:242b4b54eb52cb3930c0","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-797e7d221124021c
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-47c595f74a7e8ace
  evidence_ids:
  - ev-24e8f9536e7a224d
  - ev-534c8bba277de551
  - ev-807348d6355c0e1b
  - ev-8a3b6d90ef1ab521
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-dbff9a44f18cb862
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-47c595f74a7e8ace
  evidence_ids:
  - ev-0153dc80452e538a
  - ev-24e8f9536e7a224d
  - ev-6cf7d8b5947a08cb
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:35:37Z;
    reviewed SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59;
    current SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59;
    hash_changed=False. Reports=["reports/yaml_record_review/Kawain.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS-specific regrounding
    to CHEBI:156288 and final SSSOM row pass, but the InChI and SMILES still describe
    the old stereospecific CHEBI:6117 form.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-0153dc80452e538a
    - ev-24e8f9536e7a224d
  - name: legacy-native-ids
    value: '["SEM:242b4b54eb52cb3930c0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-24e8f9536e7a224d
    - ev-0153dc80452e538a
    - ev-6cf7d8b5947a08cb
findings:
- finding_id: rec-f-216dfac887b1eb81
  issue_key: mim-reconciliation-historical-review-coverage-and-r-47c595f74a7e8ace
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Kawain'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T21:35:37Z;
    reviewed SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59;
    current SHA-256=9f28c9f655171897957290e0826fae55b956fb5825356fe906dbf591b55bbf59;
    hash_changed=False. Reports=["reports/yaml_record_review/Kawain.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The CAS-specific regrounding
    to CHEBI:156288 and final SSSOM row pass, but the InChI and SMILES still describe
    the old stereospecific CHEBI:6117 form.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-47c595f74a7e8ace
  evidence_ids:
  - ev-0153dc80452e538a
  - ev-24e8f9536e7a224d
  - ev-6cf7d8b5947a08cb
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Kawain.yaml
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
