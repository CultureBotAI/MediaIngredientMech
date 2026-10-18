# Per-record structured review: Actinomycin_X (data/ingredients/mapped/Actinomycin_X.yaml)

- Review: 20261017T083000Z-actinomycin-x
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Actinomycin_X (data/ingredients/mapped/Actinomycin_X.yaml, record-15a7132c299ae32b, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Actinomycin_X.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Actinomycin_X.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-15a7132c299ae32b | data/ingredients/mapped/Actinomycin_X.yaml | maintained | Actinomycin_X |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-15a7132c299ae32b | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-15a7132c299ae32b | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-15a7132c299ae32b | Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-15a7132c299ae32b.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-15a7132c299ae32b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:17:53Z; reviewed SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c; current SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c; hash_changed=False. Reports=["reports/yaml_record_review/Actinomycin_X.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MicrobeDecoder occurrence is traceable, but advisory research rows dispute mesh:C041783 as the wrong actinomycin X sense and the record still has stale promotion notes.

## Findings

### rec-f-1fa42c8925f71b61: Historical review coverage and residual narrative: Actinomycin_X

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-15a7132c299ae32b.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:17:53Z; reviewed SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c; current SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c; hash_changed=False. Reports=["reports/yaml_record_review/Actinomycin_X.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The MicrobeDecoder occurrence is traceable, but advisory research rows dispute mesh:C041783 as the wrong actinomycin X sense and the record still has stale promotion notes.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-39817c4e3e002142 | data/ingredients/mapped/Actinomycin_X.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[171],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C041783","line":173,"mapping_status":"MAPPED","ontology_id":"mesh:C041783","preferred_term":"Actinomycin X"}],"identifier":"mesh:C041783","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":2,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C041783","ontology_label":"actinomycin X","ontology_source":"MESH"},"preferred_term":"Actinomycin X","sssom_rows":[{"data_row":299,"object_id":"mesh:C041783","object_label":"actinomycin X","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Actinomycin_X","synonym_count":1} |
| ev-93154db66cda621e | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [171] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a1eb1e88f22f5f24 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Actinomycin_X; data-row positions=[299] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":299,"object_id":"mesh:C041783","object_label":"actinomycin X","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Actinomycin_X","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-d15d6332f6f9fb7b | docs/data/mapped_ingredients.csv; CSV lines=[173] | supports | Published identity and count rows inspected: [{"identifier":"mesh:C041783","line":173,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C041783","preferred_term":"Actinomycin X","total_occurrences":"0"}] |
| ev-ad0deb9651147ded | reports/yaml_record_review/Actinomycin_X.md; &#96;data/ingredients/mapped/Actinomycin_X.yaml&#96;:2; Verdict:4; Identity:10; Validation:23; Evidence:38; Completeness:58; Recommended Edits:66 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3d8fe04d3a46180f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[208] | context_only | [{"current_record_sha256":"e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c","finding_id":"SEM:287fc57ad3fd7894f96b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024631Z-mim-reconcile-all-batch-03.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-actinomycin-x
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Actinomycin_X (data/ingredients/mapped/Actinomycin_X.yaml)'
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
summary: Per-record structured review for Actinomycin_X (data/ingredients/mapped/Actinomycin_X.yaml,
  record-15a7132c299ae32b, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Actinomycin_X.yaml
    sha256: e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c
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
  - path: reports/yaml_record_review/Actinomycin_X.md
    sha256: 5eba796e92814f0194f4f8d2c4788f17b61f298590f9c4675cd88de4d13e1102
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-15a7132c299ae32b
  path: data/ingredients/mapped/Actinomycin_X.yaml
  label: Actinomycin_X
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinomycin_X.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Actinomycin_X.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Actinomycin_X.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-15a7132c299ae32b
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-15a7132c299ae32b
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-15a7132c299ae32b
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024631Z-mim-reconcile-all-batch-03
    and semantic review dispositions on HEAD.
  target_ids:
  - record-15a7132c299ae32b
evidence:
- evidence_id: ev-39817c4e3e002142
  kind: record_content
  reference: data/ingredients/mapped/Actinomycin_X.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[171],"raw_equal":true},"docs_rows":[{"identifier":"mesh:C041783","line":173,"mapping_status":"MAPPED","ontology_id":"mesh:C041783","preferred_term":"Actinomycin
    X"}],"identifier":"mesh:C041783","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"source_occurrences":[{"count":2,"source":"microbedecoder","source_columns":"BacDive_Metabolite_production"}],"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"mesh:C041783","ontology_label":"actinomycin
    X","ontology_source":"MESH"},"preferred_term":"Actinomycin X","sssom_rows":[{"data_row":299,"object_id":"mesh:C041783","object_label":"actinomycin
    X","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Actinomycin_X","synonym_count":1}'
  snapshot_sha256: e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c
- evidence_id: ev-93154db66cda621e
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [171]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a1eb1e88f22f5f24
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Actinomycin_X; data-row positions=[299]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":299,"object_id":"mesh:C041783","object_label":"actinomycin
    X","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Actinomycin_X","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d15d6332f6f9fb7b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[173]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"mesh:C041783","line":173,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"mesh:C041783","preferred_term":"Actinomycin
    X","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-ad0deb9651147ded
  kind: prior_review
  reference: reports/yaml_record_review/Actinomycin_X.md
  locator: '`data/ingredients/mapped/Actinomycin_X.yaml`:2; Verdict:4; Identity:10;
    Validation:23; Evidence:38; Completeness:58; Recommended Edits:66'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 5eba796e92814f0194f4f8d2c4788f17b61f298590f9c4675cd88de4d13e1102
  quote: "Recommended Edits:\n- In `data/ingredients/mapped/Actinomycin_X.yaml`, replace\
    \ `mesh:C041783` with a\n  better parent or local identity, or mark the record\
    \ unresolved if no exact\n  family term exists.\n- Remove or rewrite the `#213`\
    \ evidence note so it no longer claims that the\n  checked ChEBI hierarchy lacked\
    \ a broad actinomycin family term.\n- Refresh the stale top-level `notes`."
- evidence_id: ev-3d8fe04d3a46180f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[208]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c","finding_id":"SEM:287fc57ad3fd7894f96b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-48ebd0b07013ac38
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-15a7132c299ae32b
  evidence_ids:
  - ev-39817c4e3e002142
  - ev-93154db66cda621e
  - ev-a1eb1e88f22f5f24
  - ev-d15d6332f6f9fb7b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ce018bccb2324c8c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-15a7132c299ae32b
  evidence_ids:
  - ev-ad0deb9651147ded
  - ev-39817c4e3e002142
  - ev-3d8fe04d3a46180f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:17:53Z;
    reviewed SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c;
    current SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c;
    hash_changed=False. Reports=["reports/yaml_record_review/Actinomycin_X.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The MicrobeDecoder
    occurrence is traceable, but advisory research rows dispute mesh:C041783 as the
    wrong actinomycin X sense and the record still has stale promotion notes.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-ad0deb9651147ded
    - ev-39817c4e3e002142
  - name: legacy-native-ids
    value: '["SEM:287fc57ad3fd7894f96b"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-39817c4e3e002142
    - ev-ad0deb9651147ded
    - ev-3d8fe04d3a46180f
findings:
- finding_id: rec-f-1fa42c8925f71b61
  issue_key: mim-reconciliation-historical-review-coverage-and-r-15a7132c299ae32b
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Actinomycin_X'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T07:17:53Z;
    reviewed SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c;
    current SHA-256=e7031e55669a22fb5ef64719a4e2c6e74e1304ea37efdb918dd568aa9f825d8c;
    hash_changed=False. Reports=["reports/yaml_record_review/Actinomycin_X.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The MicrobeDecoder
    occurrence is traceable, but advisory research rows dispute mesh:C041783 as the
    wrong actinomycin X sense and the record still has stale promotion notes.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-15a7132c299ae32b
  evidence_ids:
  - ev-ad0deb9651147ded
  - ev-39817c4e3e002142
  - ev-3d8fe04d3a46180f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Actinomycin_X.yaml
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
