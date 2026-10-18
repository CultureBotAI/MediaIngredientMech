# Per-record structured review: Gentamicin (data/ingredients/mapped/Gentamicin.yaml)

- Review: 20261017T083000Z-gentamicin
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Gentamicin (data/ingredients/mapped/Gentamicin.yaml, record-522dde2d7d878285, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Gentamicin.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Gentamicin.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-522dde2d7d878285 | data/ingredients/mapped/Gentamicin.yaml | maintained | Gentamicin |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-522dde2d7d878285 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-522dde2d7d878285 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-522dde2d7d878285 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-522dde2d7d878285.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-522dde2d7d878285.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z; reviewed SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0; current SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0; hash_changed=False. Reports=["reports/yaml_record_review/Gentamicin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The curator-ratified CHEBI gentamycin identity passes, but final SSSOM exports conditional recipe text.

## Findings

### rec-f-aa3f50caf0a058ff: Historical review coverage and residual narrative: Gentamicin

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-522dde2d7d878285.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z; reviewed SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0; current SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0; hash_changed=False. Reports=["reports/yaml_record_review/Gentamicin.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The curator-ratified CHEBI gentamycin identity passes, but final SSSOM exports conditional recipe text.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-36401bdfe4f4c120 | data/ingredients/mapped/Gentamicin.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[217],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17833","line":219,"mapping_status":"MAPPED","ontology_id":"CHEBI:17833","preferred_term":"Gentamicin"}],"identifier":"CHEBI:17833","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"source_occurrences":[{"count":638,"source":"microbedecoder","source_columns":"BacDive_Antibiotic_resistance&#124;BacDive_Antibiotic_sensitivity&#124;BacDive_Metabolite_production"}],"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:17833","ontology_label":"gentamycin","ontology_source":"CHEBI"},"preferred_term":"Gentamicin","sssom_rows":[{"data_row":1289,"object_id":"CHEBI:17833","object_label":"gentamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gentamicin","synonym_count":1} |
| ev-518d878f73a4d003 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [217] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f1bd9abb0a46955c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Gentamicin; data-row positions=[1289] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1289,"object_id":"CHEBI:17833","object_label":"gentamycin","other":"gentamicin (if needed)","predicate_id":"skos:exactMatch","subject_id":"MIM:Gentamicin","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-6a4aeffc230c58cd | docs/data/mapped_ingredients.csv; CSV lines=[219] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17833","line":219,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:17833","preferred_term":"Gentamicin","total_occurrences":"2"}] |
| ev-f489bf12ab414303 | reports/yaml_record_review/Gentamicin.md; &#96;data/ingredients/mapped/Gentamicin.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:32; Completeness:57; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6cc1ea6b5314b191 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[656] | context_only | [{"current_record_sha256":"f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0","finding_id":"SEM:f815478a76701ad02d2c","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-gentamicin
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Gentamicin (data/ingredients/mapped/Gentamicin.yaml)'
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
summary: Per-record structured review for Gentamicin (data/ingredients/mapped/Gentamicin.yaml,
  record-522dde2d7d878285, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Gentamicin.yaml
    sha256: f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0
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
  - path: reports/yaml_record_review/Gentamicin.md
    sha256: c2eeac5c50f5f69c4c5eb010e59ff18b3eb8fdda69b114fc7e5ce3657388d259
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-522dde2d7d878285
  path: data/ingredients/mapped/Gentamicin.yaml
  label: Gentamicin
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gentamicin.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Gentamicin.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Gentamicin.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-522dde2d7d878285
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-522dde2d7d878285
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-522dde2d7d878285
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-522dde2d7d878285
evidence:
- evidence_id: ev-36401bdfe4f4c120
  kind: record_content
  reference: data/ingredients/mapped/Gentamicin.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[217],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17833","line":219,"mapping_status":"MAPPED","ontology_id":"CHEBI:17833","preferred_term":"Gentamicin"}],"identifier":"CHEBI:17833","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2,"edge_count":2,"occurrences":2},"occurrence_statistics":{"media_count":2,"source_occurrences":[{"count":638,"source":"microbedecoder","source_columns":"BacDive_Antibiotic_resistance|BacDive_Antibiotic_sensitivity|BacDive_Metabolite_production"}],"total_occurrences":2},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:17833","ontology_label":"gentamycin","ontology_source":"CHEBI"},"preferred_term":"Gentamicin","sssom_rows":[{"data_row":1289,"object_id":"CHEBI:17833","object_label":"gentamycin","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Gentamicin","synonym_count":1}'
  snapshot_sha256: f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0
- evidence_id: ev-518d878f73a4d003
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [217]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f1bd9abb0a46955c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Gentamicin; data-row positions=[1289]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1289,"object_id":"CHEBI:17833","object_label":"gentamycin","other":"gentamicin
    (if needed)","predicate_id":"skos:exactMatch","subject_id":"MIM:Gentamicin","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-6a4aeffc230c58cd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[219]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17833","line":219,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"2","ontology_id":"CHEBI:17833","preferred_term":"Gentamicin","total_occurrences":"2"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-f489bf12ab414303
  kind: prior_review
  reference: reports/yaml_record_review/Gentamicin.md
  locator: '`data/ingredients/mapped/Gentamicin.yaml`:2; Verdict:4; Identity:10; Validation:20;
    Evidence:32; Completeness:57; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: c2eeac5c50f5f69c4c5eb010e59ff18b3eb8fdda69b114fc7e5ce3657388d259
  quote: "Recommended Edits:\n- Major: remove or retag `gentamicin (if needed)` so\
    \ final SSSOM stops\n  exporting conditional recipe text as a synonym.\n- Minor:\
    \ update the first mapping-evidence note so it no longer says\n  `CHEBI:759884`\
    \ does not resolve in ChEBI at all, while preserving the final\n  issue `#207`\
    \ curator ruling."
- evidence_id: ev-6cc1ea6b5314b191
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[656]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0","finding_id":"SEM:f815478a76701ad02d2c","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-21f3a8f6b4f1af0f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-522dde2d7d878285
  evidence_ids:
  - ev-36401bdfe4f4c120
  - ev-518d878f73a4d003
  - ev-f1bd9abb0a46955c
  - ev-6a4aeffc230c58cd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-7ed061285e433704
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-522dde2d7d878285
  evidence_ids:
  - ev-f489bf12ab414303
  - ev-36401bdfe4f4c120
  - ev-6cc1ea6b5314b191
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z;
    reviewed SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0;
    current SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0;
    hash_changed=False. Reports=["reports/yaml_record_review/Gentamicin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The curator-ratified
    CHEBI gentamycin identity passes, but final SSSOM exports conditional recipe text.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-f489bf12ab414303
    - ev-36401bdfe4f4c120
  - name: legacy-native-ids
    value: '["SEM:f815478a76701ad02d2c"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-36401bdfe4f4c120
    - ev-f489bf12ab414303
    - ev-6cc1ea6b5314b191
findings:
- finding_id: rec-f-aa3f50caf0a058ff
  issue_key: mim-reconciliation-historical-review-coverage-and-r-522dde2d7d878285
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Gentamicin'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T17:34:39Z;
    reviewed SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0;
    current SHA-256=f7624a1884f865e2cd2ba0c1826099e4dfe0bf06e6705aa081018108b82c0fb0;
    hash_changed=False. Reports=["reports/yaml_record_review/Gentamicin.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The curator-ratified
    CHEBI gentamycin identity passes, but final SSSOM exports conditional recipe text.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-522dde2d7d878285
  evidence_ids:
  - ev-f489bf12ab414303
  - ev-36401bdfe4f4c120
  - ev-6cc1ea6b5314b191
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Gentamicin.yaml
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
