# Per-record structured review: Glucuronamide (data/ingredients/mapped/Glucuronamide.yaml)

- Review: 20261017T083000Z-glucuronamide
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glucuronamide (data/ingredients/mapped/Glucuronamide.yaml, record-ebe8b5c743271224, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glucuronamide.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glucuronamide.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-ebe8b5c743271224 | data/ingredients/mapped/Glucuronamide.yaml | maintained | Glucuronamide |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-ebe8b5c743271224 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-ebe8b5c743271224 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-ebe8b5c743271224 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-ebe8b5c743271224.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-ebe8b5c743271224.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z; reviewed SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458; current SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458; hash_changed=False. Reports=["reports/yaml_record_review/Glucuronamide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI and CAS registry rows pass, but stale CultureBotHT evidence prose needs cleanup.

## Findings

### rec-f-0ece4c8f03af982c: Historical review coverage and residual narrative: Glucuronamide

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-ebe8b5c743271224.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z; reviewed SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458; current SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458; hash_changed=False. Reports=["reports/yaml_record_review/Glucuronamide.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI and CAS registry rows pass, but stale CultureBotHT evidence prose needs cleanup.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e0beaa0f40783b5d | data/ingredients/mapped/Glucuronamide.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1060],"raw_equal":true},"docs_rows":[{"identifier":"cas:3789-97-7","line":1062,"mapping_status":"MAPPED","ontology_id":"CHEBI:32323","preferred_term":"Glucuronamide"}],"identifier":"cas:3789-97-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:32323","ontology_label":"beta-D-glucuronamide","ontology_source":"CHEBI"},"preferred_term":"Glucuronamide","sssom_rows":[{"data_row":1317,"object_id":"CHEBI:32323","object_label":"beta-D-glucuronamide","predicate_id":"skos:exactMatch"},{"data_row":1318,"object_id":"cas:3789-97-7","object_label":"Glucuronamide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucuronamide","synonym_count":2} |
| ev-d30ddf7bd1c7d36c | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1060] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-39904bbcdb52bc8d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glucuronamide; data-row positions=[1317,1318] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1317,"object_id":"CHEBI:32323","object_label":"beta-D-glucuronamide","other":"D-Glucuronamide&#124;beta-D-glucopyranuronamide&#124;CAS:3789-97-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucuronamide","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"},{"data_row":1318,"object_id":"cas:3789-97-7","object_label":"Glucuronamide","other":"CAS:3789-97-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucuronamide","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-b9e7addb9e53057e | docs/data/mapped_ingredients.csv; CSV lines=[1062] | supports | Published identity and count rows inspected: [{"identifier":"cas:3789-97-7","line":1062,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:32323","preferred_term":"Glucuronamide","total_occurrences":"0"}] |
| ev-345a67f0ee492baa | reports/yaml_record_review/Glucuronamide.md; &#96;data/ingredients/mapped/Glucuronamide.yaml&#96;:2; Verdict:4; Identity:13; Validation:23; Evidence:37; Completeness:67; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-ec64d6ace3f7b31f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[677] | context_only | [{"current_record_sha256":"848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458","finding_id":"SEM:5311ff230bef8cfcb149","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glucuronamide
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glucuronamide (data/ingredients/mapped/Glucuronamide.yaml)'
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
summary: Per-record structured review for Glucuronamide (data/ingredients/mapped/Glucuronamide.yaml,
  record-ebe8b5c743271224, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glucuronamide.yaml
    sha256: 848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458
    role: target
  - path: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
    sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
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
  - path: reports/yaml_record_review/Glucuronamide.md
    sha256: 8454b03284e0d4da46286ea2b460fe75c257053779ed17b6d00f5d63c6286697
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-ebe8b5c743271224
  path: data/ingredients/mapped/Glucuronamide.yaml
  label: Glucuronamide
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucuronamide.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glucuronamide.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glucuronamide.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-ebe8b5c743271224
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-ebe8b5c743271224
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-ebe8b5c743271224
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-ebe8b5c743271224
evidence:
- evidence_id: ev-e0beaa0f40783b5d
  kind: record_content
  reference: data/ingredients/mapped/Glucuronamide.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1060],"raw_equal":true},"docs_rows":[{"identifier":"cas:3789-97-7","line":1062,"mapping_status":"MAPPED","ontology_id":"CHEBI:32323","preferred_term":"Glucuronamide"}],"identifier":"cas:3789-97-7","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:32323","ontology_label":"beta-D-glucuronamide","ontology_source":"CHEBI"},"preferred_term":"Glucuronamide","sssom_rows":[{"data_row":1317,"object_id":"CHEBI:32323","object_label":"beta-D-glucuronamide","predicate_id":"skos:exactMatch"},{"data_row":1318,"object_id":"cas:3789-97-7","object_label":"Glucuronamide","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glucuronamide","synonym_count":2}'
  snapshot_sha256: 848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458
- evidence_id: ev-d30ddf7bd1c7d36c
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1060]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-39904bbcdb52bc8d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glucuronamide; data-row positions=[1317,1318]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1317,"object_id":"CHEBI:32323","object_label":"beta-D-glucuronamide","other":"D-Glucuronamide|beta-D-glucopyranuronamide|CAS:3789-97-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucuronamide","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"},{"data_row":1318,"object_id":"cas:3789-97-7","object_label":"Glucuronamide","other":"CAS:3789-97-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Glucuronamide","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b9e7addb9e53057e
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1062]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:3789-97-7","line":1062,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:32323","preferred_term":"Glucuronamide","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-345a67f0ee492baa
  kind: prior_review
  reference: reports/yaml_record_review/Glucuronamide.md
  locator: '`data/ingredients/mapped/Glucuronamide.yaml`:2; Verdict:4; Identity:13;
    Validation:23; Evidence:37; Completeness:67; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8454b03284e0d4da46286ea2b460fe75c257053779ed17b6d00f5d63c6286697
  quote: "Recommended Edits:\n- Minor: rephrase `ontology_mapping.evidence[0].notes`\
    \ in\n  `data/ingredients/mapped/Glucuronamide.yaml` so it preserves the CultureBotHT\n\
    \  CAS fallback provenance without saying the current mapping still lacks a\n\
    \  ChEBI grounding."
- evidence_id: ev-ec64d6ace3f7b31f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[677]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458","finding_id":"SEM:5311ff230bef8cfcb149","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-e138faa9ff864d7d
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-ebe8b5c743271224
  evidence_ids:
  - ev-e0beaa0f40783b5d
  - ev-d30ddf7bd1c7d36c
  - ev-39904bbcdb52bc8d
  - ev-b9e7addb9e53057e
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d8395e673b173577
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ebe8b5c743271224
  evidence_ids:
  - ev-345a67f0ee492baa
  - ev-e0beaa0f40783b5d
  - ev-ec64d6ace3f7b31f
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z;
    reviewed SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458;
    current SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucuronamide.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ChEBI
    and CAS registry rows pass, but stale CultureBotHT evidence prose needs cleanup.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-345a67f0ee492baa
    - ev-e0beaa0f40783b5d
  - name: legacy-native-ids
    value: '["SEM:5311ff230bef8cfcb149"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e0beaa0f40783b5d
    - ev-345a67f0ee492baa
    - ev-ec64d6ace3f7b31f
findings:
- finding_id: rec-f-0ece4c8f03af982c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-ebe8b5c743271224
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glucuronamide'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T17:54:08Z;
    reviewed SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458;
    current SHA-256=848e41f6a504664b56e47f076bbb59e8c9e888487355df65b5d121d7a1974458;
    hash_changed=False. Reports=["reports/yaml_record_review/Glucuronamide.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ChEBI
    and CAS registry rows pass, but stale CultureBotHT evidence prose needs cleanup.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-ebe8b5c743271224
  evidence_ids:
  - ev-345a67f0ee492baa
  - ev-e0beaa0f40783b5d
  - ev-ec64d6ace3f7b31f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glucuronamide.yaml
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
  with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.
```
