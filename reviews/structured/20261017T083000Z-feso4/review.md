# Per-record structured review: Feso4 (data/ingredients/mapped/Feso4.yaml)

- Review: 20261017T083000Z-feso4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Feso4 (data/ingredients/mapped/Feso4.yaml, record-304abec7d1ee7b56, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Feso4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Feso4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-304abec7d1ee7b56 | data/ingredients/mapped/Feso4.yaml | maintained | Feso4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-304abec7d1ee7b56 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-304abec7d1ee7b56 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-304abec7d1ee7b56 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-304abec7d1ee7b56.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-304abec7d1ee7b56.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:31:10Z; reviewed SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11; current SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11; hash_changed=False. Reports=["reports/yaml_record_review/Feso4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous ferrous sulfate identity and role pass, but a malformed hydrate token still exports as a SSSOM synonym.

## Findings

### rec-f-4225fad82da0ce4a: Historical review coverage and residual narrative: Feso4

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-304abec7d1ee7b56.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:31:10Z; reviewed SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11; current SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11; hash_changed=False. Reports=["reports/yaml_record_review/Feso4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact anhydrous ferrous sulfate identity and role pass, but a malformed hydrate token still exports as a SSSOM synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-ccc5fc3fca919492 | data/ingredients/mapped/Feso4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[997],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75832","line":999,"mapping_status":"MAPPED","ontology_id":"CHEBI:75832","preferred_term":"FeSO4"}],"identifier":"CHEBI:75832","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":267,"edge_count":267,"occurrences":267},"occurrence_statistics":{"media_count":267,"total_occurrences":267},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:75832","ontology_label":"iron(2+) sulfate (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"FeSO4","sssom_rows":[{"data_row":1198,"object_id":"CHEBI:75832","object_label":"iron(2+) sulfate (anhydrous)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Feso4","synonym_count":14} |
| ev-a76af9cc0c2bbeeb | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [997] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-78c5c745d399332d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Feso4; data-row positions=[1198] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1198,"object_id":"CHEBI:75832","object_label":"iron(2+) sulfate (anhydrous)","other":"Ferrous sulfate&#124;Iron(II) sulfate&#124;Fe(II)SO4&#124;FeSO .7H O&#124;ferrous sulfate (anh.)&#124;iron sulfate (1:1)&#124;iron(2+) sulfate&#124;iron(2+) sulfate (anh.)&#124;iron(II) sulfate (1:1)&#124;CAS:7720-78-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Feso4","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f2a18a4bbba9ad5d | docs/data/mapped_ingredients.csv; CSV lines=[999] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:75832","line":999,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"267","ontology_id":"CHEBI:75832","preferred_term":"FeSO4","total_occurrences":"267"}] |
| ev-16bef6a08d37e7e9 | reports/yaml_record_review/Feso4.md; &#96;data/ingredients/mapped/Feso4.yaml&#96;:2; Verdict:4; Identity:12; Validation:26; Evidence:36; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-cf96e1020f8aba36 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[607] | context_only | [{"current_record_sha256":"22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11","finding_id":"SEM:a97180c5f181da08a6d3","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-feso4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Feso4 (data/ingredients/mapped/Feso4.yaml)'
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
summary: Per-record structured review for Feso4 (data/ingredients/mapped/Feso4.yaml,
  record-304abec7d1ee7b56, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Feso4.yaml
    sha256: 22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11
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
  - path: reports/yaml_record_review/Feso4.md
    sha256: 9fe21b4c31303fc9c7511305555f613d7e889789dd9c4c4ddf50819085bb29e7
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-304abec7d1ee7b56
  path: data/ingredients/mapped/Feso4.yaml
  label: Feso4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Feso4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Feso4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-304abec7d1ee7b56
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-304abec7d1ee7b56
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-304abec7d1ee7b56
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-304abec7d1ee7b56
evidence:
- evidence_id: ev-ccc5fc3fca919492
  kind: record_content
  reference: data/ingredients/mapped/Feso4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[997],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:75832","line":999,"mapping_status":"MAPPED","ontology_id":"CHEBI:75832","preferred_term":"FeSO4"}],"identifier":"CHEBI:75832","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":267,"edge_count":267,"occurrences":267},"occurrence_statistics":{"media_count":267,"total_occurrences":267},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:75832","ontology_label":"iron(2+)
    sulfate (anhydrous)","ontology_source":"CHEBI"},"preferred_term":"FeSO4","sssom_rows":[{"data_row":1198,"object_id":"CHEBI:75832","object_label":"iron(2+)
    sulfate (anhydrous)","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Feso4","synonym_count":14}'
  snapshot_sha256: 22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11
- evidence_id: ev-a76af9cc0c2bbeeb
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [997]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-78c5c745d399332d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Feso4; data-row positions=[1198]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1198,"object_id":"CHEBI:75832","object_label":"iron(2+)
    sulfate (anhydrous)","other":"Ferrous sulfate|Iron(II) sulfate|Fe(II)SO4|FeSO
    .7H O|ferrous sulfate (anh.)|iron sulfate (1:1)|iron(2+) sulfate|iron(2+) sulfate
    (anh.)|iron(II) sulfate (1:1)|CAS:7720-78-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Feso4","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f2a18a4bbba9ad5d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[999]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:75832","line":999,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"267","ontology_id":"CHEBI:75832","preferred_term":"FeSO4","total_occurrences":"267"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-16bef6a08d37e7e9
  kind: prior_review
  reference: reports/yaml_record_review/Feso4.md
  locator: '`data/ingredients/mapped/Feso4.yaml`:2; Verdict:4; Identity:12; Validation:26;
    Evidence:36; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9fe21b4c31303fc9c7511305555f613d7e889789dd9c4c4ddf50819085bb29e7
  quote: "Recommended Edits:\n- Major: remove or retype `FeSO .7H O` in\n  `data/ingredients/mapped/Feso4.yaml`\
    \ so it no longer exports as an exact\n  synonym, sync `data/curated/mapped_ingredients.yaml`,\
    \ regenerate\n  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation\
    \ plus\n  the final SSSOM invariant gates."
- evidence_id: ev-cf96e1020f8aba36
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[607]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11","finding_id":"SEM:a97180c5f181da08a6d3","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-c94f16d75c375363
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-304abec7d1ee7b56
  evidence_ids:
  - ev-ccc5fc3fca919492
  - ev-a76af9cc0c2bbeeb
  - ev-78c5c745d399332d
  - ev-f2a18a4bbba9ad5d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ff57a836c75708ec
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-304abec7d1ee7b56
  evidence_ids:
  - ev-16bef6a08d37e7e9
  - ev-ccc5fc3fca919492
  - ev-cf96e1020f8aba36
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:31:10Z;
    reviewed SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11;
    current SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11;
    hash_changed=False. Reports=["reports/yaml_record_review/Feso4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous ferrous
    sulfate identity and role pass, but a malformed hydrate token still exports as
    a SSSOM synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-16bef6a08d37e7e9
    - ev-ccc5fc3fca919492
  - name: legacy-native-ids
    value: '["SEM:a97180c5f181da08a6d3"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-ccc5fc3fca919492
    - ev-16bef6a08d37e7e9
    - ev-cf96e1020f8aba36
findings:
- finding_id: rec-f-4225fad82da0ce4a
  issue_key: mim-reconciliation-historical-review-coverage-and-r-304abec7d1ee7b56
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Feso4'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:31:10Z;
    reviewed SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11;
    current SHA-256=22819bce32758595debdedcbbb2eb44948208ade151974e53fdb922d856baf11;
    hash_changed=False. Reports=["reports/yaml_record_review/Feso4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact anhydrous ferrous
    sulfate identity and role pass, but a malformed hydrate token still exports as
    a SSSOM synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-304abec7d1ee7b56
  evidence_ids:
  - ev-16bef6a08d37e7e9
  - ev-ccc5fc3fca919492
  - ev-cf96e1020f8aba36
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Feso4.yaml
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
