# Per-record structured review: Cephalosporin (data/ingredients/mapped/Cephalosporin.yaml)

- Review: 20261017T083000Z-cephalosporin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cephalosporin (data/ingredients/mapped/Cephalosporin.yaml, record-5d3f64f49518a707, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cephalosporin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cephalosporin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-5d3f64f49518a707 | data/ingredients/mapped/Cephalosporin.yaml | maintained | Cephalosporin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-5d3f64f49518a707 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-5d3f64f49518a707 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-5d3f64f49518a707 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-5d3f64f49518a707.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-5d3f64f49518a707.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:37:13Z; reviewed SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40; current SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40; hash_changed=False. Reports=["reports/yaml_record_review/Cephalosporin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI cephalosporin class identity passes, but the generic class record carries an over-specific InChI absent from the ChEBI class term.

## Findings

### rec-f-88664c8fca74aa48: Historical review coverage and residual narrative: Cephalosporin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-5d3f64f49518a707.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:37:13Z; reviewed SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40; current SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40; hash_changed=False. Reports=["reports/yaml_record_review/Cephalosporin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI cephalosporin class identity passes, but the generic class record carries an over-specific InChI absent from the ChEBI class term.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6a510393d98e463c | data/ingredients/mapped/Cephalosporin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2209],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:23066","line":2211,"mapping_status":"MAPPED","ontology_id":"CHEBI:23066","preferred_term":"Cephalosporin"}],"identifier":"CHEBI:23066","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":17,"source":"microbedecoder","source_columns":"BacDive_Antibiotic_resistance&#124;BacDive_Antibiotic_sensitivity"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:23066","ontology_label":"cephalosporin","ontology_source":"CHEBI"},"preferred_term":"Cephalosporin","sssom_rows":[{"data_row":716,"object_id":"CHEBI:23066","object_label":"cephalosporin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cephalosporin","synonym_count":0} |
| ev-06d5a018d5644b73 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2209] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-d275f17d0657c671 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cephalosporin; data-row positions=[716] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":716,"object_id":"CHEBI:23066","object_label":"cephalosporin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cephalosporin","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-440fd66ed2c1c2b4 | docs/data/mapped_ingredients.csv; CSV lines=[2211] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:23066","line":2211,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:23066","preferred_term":"Cephalosporin","total_occurrences":"0"}] |
| ev-2850fd352911a282 | reports/yaml_record_review/Cephalosporin.md; &#96;data/ingredients/mapped/Cephalosporin.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:39; Completeness:57; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f81b331730ddd240 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[393] | context_only | [{"current_record_sha256":"b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40","finding_id":"SEM:676edcefbc0bf5499bae","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cephalosporin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cephalosporin (data/ingredients/mapped/Cephalosporin.yaml)'
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
summary: Per-record structured review for Cephalosporin (data/ingredients/mapped/Cephalosporin.yaml,
  record-5d3f64f49518a707, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cephalosporin.yaml
    sha256: b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Cephalosporin.md
    sha256: cf6f53dfdd3d5b3948a2b15565600fc73134a102d4fe1cd039156ec66eba1107
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-5d3f64f49518a707
  path: data/ingredients/mapped/Cephalosporin.yaml
  label: Cephalosporin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cephalosporin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cephalosporin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cephalosporin.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-5d3f64f49518a707
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-5d3f64f49518a707
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-5d3f64f49518a707
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-5d3f64f49518a707
evidence:
- evidence_id: ev-6a510393d98e463c
  kind: record_content
  reference: data/ingredients/mapped/Cephalosporin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2209],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:23066","line":2211,"mapping_status":"MAPPED","ontology_id":"CHEBI:23066","preferred_term":"Cephalosporin"}],"identifier":"CHEBI:23066","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":17,"source":"microbedecoder","source_columns":"BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:23066","ontology_label":"cephalosporin","ontology_source":"CHEBI"},"preferred_term":"Cephalosporin","sssom_rows":[{"data_row":716,"object_id":"CHEBI:23066","object_label":"cephalosporin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cephalosporin","synonym_count":0}'
  snapshot_sha256: b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40
- evidence_id: ev-06d5a018d5644b73
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2209]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-d275f17d0657c671
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cephalosporin; data-row positions=[716]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":716,"object_id":"CHEBI:23066","object_label":"cephalosporin","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cephalosporin","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-440fd66ed2c1c2b4
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2211]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:23066","line":2211,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:23066","preferred_term":"Cephalosporin","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2850fd352911a282
  kind: prior_review
  reference: reports/yaml_record_review/Cephalosporin.md
  locator: '`data/ingredients/mapped/Cephalosporin.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:39; Completeness:57; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cf6f53dfdd3d5b3948a2b15565600fc73134a102d4fe1cd039156ec66eba1107
  quote: "Recommended Edits:\n- Major: remove `chemical_properties.inchi` from the\
    \ generic cephalosporin\n  class record, then rerun strict validation, SSSOM QC,\
    \ aggregate roundtrip,\n  and `git diff --check`."
- evidence_id: ev-f81b331730ddd240
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[393]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40","finding_id":"SEM:676edcefbc0bf5499bae","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-cd54f1bcf40e0d94
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-5d3f64f49518a707
  evidence_ids:
  - ev-6a510393d98e463c
  - ev-06d5a018d5644b73
  - ev-d275f17d0657c671
  - ev-440fd66ed2c1c2b4
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-eee59ef9b500637c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5d3f64f49518a707
  evidence_ids:
  - ev-2850fd352911a282
  - ev-6a510393d98e463c
  - ev-f81b331730ddd240
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:37:13Z;
    reviewed SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40;
    current SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40;
    hash_changed=False. Reports=["reports/yaml_record_review/Cephalosporin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ChEBI
    cephalosporin class identity passes, but the generic class record carries an over-specific
    InChI absent from the ChEBI class term.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2850fd352911a282
    - ev-6a510393d98e463c
  - name: legacy-native-ids
    value: '["SEM:676edcefbc0bf5499bae"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6a510393d98e463c
    - ev-2850fd352911a282
    - ev-f81b331730ddd240
findings:
- finding_id: rec-f-88664c8fca74aa48
  issue_key: mim-reconciliation-historical-review-coverage-and-r-5d3f64f49518a707
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Cephalosporin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:37:13Z;
    reviewed SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40;
    current SHA-256=b87cf8fc3a727b55d480ea022e4996949aced3f48f6feff6672f0fa31e530e40;
    hash_changed=False. Reports=["reports/yaml_record_review/Cephalosporin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ChEBI
    cephalosporin class identity passes, but the generic class record carries an over-specific
    InChI absent from the ChEBI class term.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-5d3f64f49518a707
  evidence_ids:
  - ev-2850fd352911a282
  - ev-6a510393d98e463c
  - ev-f81b331730ddd240
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cephalosporin.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
