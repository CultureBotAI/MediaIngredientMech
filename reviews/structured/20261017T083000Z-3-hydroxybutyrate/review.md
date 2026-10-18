# Per-record structured review: 3-hydroxybutyrate (data/ingredients/mapped/3-hydroxybutyrate.yaml)

- Review: 20261017T083000Z-3-hydroxybutyrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for 3-hydroxybutyrate (data/ingredients/mapped/3-hydroxybutyrate.yaml, record-7ddaae0e8b094eac, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/3-hydroxybutyrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/3-hydroxybutyrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7ddaae0e8b094eac | data/ingredients/mapped/3-hydroxybutyrate.yaml | maintained | 3-hydroxybutyrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7ddaae0e8b094eac | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-7ddaae0e8b094eac | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7ddaae0e8b094eac | Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7ddaae0e8b094eac.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7ddaae0e8b094eac.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T10:45:31Z; reviewed SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d; current SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d; hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybutyrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI anion identity, beta-hydroxybutyrate alias, SSSOM row, and MicrobeDecoder occurrence provenance pass; stale advisory rows remain.

## Findings

### rec-f-54959c7c0ace740e: Historical review coverage and residual narrative: 3-hydroxybutyrate

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-7ddaae0e8b094eac.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T10:45:31Z; reviewed SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d; current SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d; hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybutyrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI anion identity, beta-hydroxybutyrate alias, SSSOM row, and MicrobeDecoder occurrence provenance pass; stale advisory rows remain.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-285f5ddd0f32ebe1 | data/ingredients/mapped/3-hydroxybutyrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2111],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37054","line":2113,"mapping_status":"MAPPED","ontology_id":"CHEBI:37054","preferred_term":"3-hydroxybutyrate"}],"identifier":"CHEBI:37054","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":391,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production&#124;BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37054","ontology_label":"3-hydroxybutyrate","ontology_source":"CHEBI"},"preferred_term":"3-hydroxybutyrate","sssom_rows":[{"data_row":145,"object_id":"CHEBI:37054","object_label":"3-hydroxybutyrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-hydroxybutyrate","synonym_count":1} |
| ev-fde62cbe8009bd3d | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2111] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-64ebb313509af9af | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:3-hydroxybutyrate; data-row positions=[145] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":145,"object_id":"CHEBI:37054","object_label":"3-hydroxybutyrate","other":"Beta-hydroxybutyrate","predicate_id":"skos:exactMatch","subject_id":"MIM:3-hydroxybutyrate","validation_method":"manual:review-ingredients&#124;APPROVED&#124;2026-08-04"}] |
| ev-6cdcbea250fb6747 | docs/data/mapped_ingredients.csv; CSV lines=[2113] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:37054","line":2113,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37054","preferred_term":"3-hydroxybutyrate","total_occurrences":"0"}] |
| ev-4b227e4b6b326926 | reports/yaml_record_review/3-hydroxybutyrate.md; &#96;data/ingredients/mapped/3-hydroxybutyrate.yaml&#96;:2; Verdict:4; Identity:11; Validation:23; Evidence:38; Completeness:54; Recommended Edits:63 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-033427f50e2c3d5a | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[121] | context_only | [{"current_record_sha256":"0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d","finding_id":"SEM:c47d980e8a6e8ca6234e","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-3-hydroxybutyrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: 3-hydroxybutyrate (data/ingredients/mapped/3-hydroxybutyrate.yaml)'
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
summary: Per-record structured review for 3-hydroxybutyrate (data/ingredients/mapped/3-hydroxybutyrate.yaml,
  record-7ddaae0e8b094eac, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/3-hydroxybutyrate.yaml
    sha256: 0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d
    role: target
  - path: reviews/structured/20261011T024630Z-mim-reconcile-all-batch-02/review.yaml
    sha256: 799a1a80fa398851bced286dd0f68a97e6a22f7090d53677678dc13b92c6f076
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
  - path: reports/yaml_record_review/3-hydroxybutyrate.md
    sha256: fbf5eada2fb406c21a6e22eac370d62f44d4fca9ca22d069efb89f5e597ab4b4
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7ddaae0e8b094eac
  path: data/ingredients/mapped/3-hydroxybutyrate.yaml
  label: 3-hydroxybutyrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybutyrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/3-hydroxybutyrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/3-hydroxybutyrate.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7ddaae0e8b094eac
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7ddaae0e8b094eac
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-7ddaae0e8b094eac
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024630Z-mim-reconcile-all-batch-02
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7ddaae0e8b094eac
evidence:
- evidence_id: ev-285f5ddd0f32ebe1
  kind: record_content
  reference: data/ingredients/mapped/3-hydroxybutyrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2111],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:37054","line":2113,"mapping_status":"MAPPED","ontology_id":"CHEBI:37054","preferred_term":"3-hydroxybutyrate"}],"identifier":"CHEBI:37054","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":391,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production|BacDive_Metabolite_utilization"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:37054","ontology_label":"3-hydroxybutyrate","ontology_source":"CHEBI"},"preferred_term":"3-hydroxybutyrate","sssom_rows":[{"data_row":145,"object_id":"CHEBI:37054","object_label":"3-hydroxybutyrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:3-hydroxybutyrate","synonym_count":1}'
  snapshot_sha256: 0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d
- evidence_id: ev-fde62cbe8009bd3d
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2111]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-64ebb313509af9af
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:3-hydroxybutyrate; data-row positions=[145]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":145,"object_id":"CHEBI:37054","object_label":"3-hydroxybutyrate","other":"Beta-hydroxybutyrate","predicate_id":"skos:exactMatch","subject_id":"MIM:3-hydroxybutyrate","validation_method":"manual:review-ingredients|APPROVED|2026-08-04"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6cdcbea250fb6747
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2113]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:37054","line":2113,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:37054","preferred_term":"3-hydroxybutyrate","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4b227e4b6b326926
  kind: prior_review
  reference: reports/yaml_record_review/3-hydroxybutyrate.md
  locator: '`data/ingredients/mapped/3-hydroxybutyrate.yaml`:2; Verdict:4; Identity:11;
    Validation:23; Evidence:38; Completeness:54; Recommended Edits:63'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: fbf5eada2fb406c21a6e22eac370d62f44d4fca9ca22d069efb89f5e597ab4b4
  quote: "Recommended Edits:\n- No curated-record edits are needed.\n- If `mappings/record_research_validation.tsv`\
    \ is still used as a live queue,\n  clear the stale `3-hydroxybutyrate` P1/P3\
    \ rows or regenerate that advisory\n  table from the current record."
- evidence_id: ev-033427f50e2c3d5a
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[121]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d","finding_id":"SEM:c47d980e8a6e8ca6234e","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c1f205846c73040b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7ddaae0e8b094eac
  evidence_ids:
  - ev-285f5ddd0f32ebe1
  - ev-fde62cbe8009bd3d
  - ev-64ebb313509af9af
  - ev-6cdcbea250fb6747
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9b75a1be333945f4
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7ddaae0e8b094eac
  evidence_ids:
  - ev-4b227e4b6b326926
  - ev-285f5ddd0f32ebe1
  - ev-033427f50e2c3d5a
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T10:45:31Z;
    reviewed SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d;
    current SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d;
    hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybutyrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI anion identity, beta-hydroxybutyrate alias, SSSOM row, and MicrobeDecoder
    occurrence provenance pass; stale advisory rows remain.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4b227e4b6b326926
    - ev-285f5ddd0f32ebe1
  - name: legacy-native-ids
    value: '["SEM:c47d980e8a6e8ca6234e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-285f5ddd0f32ebe1
    - ev-4b227e4b6b326926
    - ev-033427f50e2c3d5a
findings:
- finding_id: rec-f-54959c7c0ace740e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-7ddaae0e8b094eac
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: 3-hydroxybutyrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T10:45:31Z;
    reviewed SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d;
    current SHA-256=0d7f1b890394b6c09192e6f3de4b9c13aa996d59a0b2c1dbceef578d4b712d9d;
    hash_changed=False. Reports=["reports/yaml_record_review/3-hydroxybutyrate.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    CHEBI anion identity, beta-hydroxybutyrate alias, SSSOM row, and MicrobeDecoder
    occurrence provenance pass; stale advisory rows remain.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7ddaae0e8b094eac
  evidence_ids:
  - ev-4b227e4b6b326926
  - ev-285f5ddd0f32ebe1
  - ev-033427f50e2c3d5a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/3-hydroxybutyrate.yaml
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
  with lineage to 20261011T024630Z-mim-reconcile-all-batch-02.
```
