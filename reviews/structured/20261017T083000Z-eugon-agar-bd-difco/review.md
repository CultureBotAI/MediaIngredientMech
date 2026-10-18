# Per-record structured review: Eugon_agar_BD-Difco (data/ingredients/mapped/Eugon_agar_BD-Difco.yaml)

- Review: 20261017T083000Z-eugon-agar-bd-difco
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Eugon_agar_BD-Difco (data/ingredients/mapped/Eugon_agar_BD-Difco.yaml, record-0fa48eb224d0e588, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Eugon_agar_BD-Difco.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Eugon_agar_BD-Difco.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0fa48eb224d0e588 | data/ingredients/mapped/Eugon_agar_BD-Difco.yaml | maintained | Eugon_agar_BD-Difco |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0fa48eb224d0e588 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-0fa48eb224d0e588 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0fa48eb224d0e588 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0fa48eb224d0e588.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0fa48eb224d0e588.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:01:41Z; reviewed SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b; current SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b; hash_changed=False. Reports=["reports/yaml_record_review/Eugon_agar_BD-Difco.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO Eugon agar identity and final SSSOM row pass, but ingredient_type should be backfilled.

## Findings

### rec-f-b93ed7c15ba24f0c: Historical review coverage and residual narrative: Eugon_agar_BD-Difco

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-0fa48eb224d0e588.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:01:41Z; reviewed SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b; current SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b; hash_changed=False. Reports=["reports/yaml_record_review/Eugon_agar_BD-Difco.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO Eugon agar identity and final SSSOM row pass, but ingredient_type should be backfilled.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-285aea9e6466c608 | data/ingredients/mapped/Eugon_agar_BD-Difco.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2562],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001358","line":2564,"mapping_status":"MAPPED","ontology_id":"MICRO:0001358","preferred_term":"Eugon agar (BD-Difco)"}],"identifier":"MICRO:0001358","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"MICRO:0001358","ontology_label":"Eugon agar","ontology_source":"MICRO"},"preferred_term":"Eugon agar (BD-Difco)","sssom_rows":[{"data_row":1154,"object_id":"MICRO:0001358","object_label":"Eugon agar","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Eugon_agar_BD-Difco","synonym_count":0} |
| ev-6b4e60e4b5c50eea | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2562] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-4407e349dc1666fc | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Eugon_agar_BD-Difco; data-row positions=[1154] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1154,"object_id":"MICRO:0001358","object_label":"Eugon agar","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Eugon_agar_BD-Difco","validation_method":"manual:claude_culturemech_residual_grounding&#124;CREATED&#124;2026-08-30"}] |
| ev-7e1e367b2dc9ed30 | docs/data/mapped_ingredients.csv; CSV lines=[2564] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0001358","line":2564,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"MICRO:0001358","preferred_term":"Eugon agar (BD-Difco)","total_occurrences":"1"}] |
| ev-3c8038582b040114 | reports/yaml_record_review/Eugon_agar_BD-Difco.md; &#96;data/ingredients/mapped/Eugon_agar_BD-Difco.yaml&#96;:2; Verdict:4; Identity:10; Validation:22; Evidence:29; Completeness:43; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c3dcc4aaca939af7 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[578] | context_only | [{"current_record_sha256":"532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b","finding_id":"SEM:e46cbbef982805442c7a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-eugon-agar-bd-difco
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Eugon_agar_BD-Difco (data/ingredients/mapped/Eugon_agar_BD-Difco.yaml)'
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
summary: Per-record structured review for Eugon_agar_BD-Difco (data/ingredients/mapped/Eugon_agar_BD-Difco.yaml,
  record-0fa48eb224d0e588, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Eugon_agar_BD-Difco.yaml
    sha256: 532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b
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
  - path: reports/yaml_record_review/Eugon_agar_BD-Difco.md
    sha256: 19b10eb0c3468a30406275477fbe329d0abd4bfbb1223c5d5b5e042c6643328f
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0fa48eb224d0e588
  path: data/ingredients/mapped/Eugon_agar_BD-Difco.yaml
  label: Eugon_agar_BD-Difco
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Eugon_agar_BD-Difco.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Eugon_agar_BD-Difco.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Eugon_agar_BD-Difco.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0fa48eb224d0e588
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0fa48eb224d0e588
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-0fa48eb224d0e588
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0fa48eb224d0e588
evidence:
- evidence_id: ev-285aea9e6466c608
  kind: record_content
  reference: data/ingredients/mapped/Eugon_agar_BD-Difco.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2562],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0001358","line":2564,"mapping_status":"MAPPED","ontology_id":"MICRO:0001358","preferred_term":"Eugon
    agar (BD-Difco)"}],"identifier":"MICRO:0001358","ingredient_type":null,"mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","match_level":"NORMALIZED","ontology_id":"MICRO:0001358","ontology_label":"Eugon
    agar","ontology_source":"MICRO"},"preferred_term":"Eugon agar (BD-Difco)","sssom_rows":[{"data_row":1154,"object_id":"MICRO:0001358","object_label":"Eugon
    agar","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Eugon_agar_BD-Difco","synonym_count":0}'
  snapshot_sha256: 532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b
- evidence_id: ev-6b4e60e4b5c50eea
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2562]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-4407e349dc1666fc
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Eugon_agar_BD-Difco; data-row positions=[1154]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1154,"object_id":"MICRO:0001358","object_label":"Eugon
    agar","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Eugon_agar_BD-Difco","validation_method":"manual:claude_culturemech_residual_grounding|CREATED|2026-08-30"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-7e1e367b2dc9ed30
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2564]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0001358","line":2564,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"1","ontology_id":"MICRO:0001358","preferred_term":"Eugon
    agar (BD-Difco)","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-3c8038582b040114
  kind: prior_review
  reference: reports/yaml_record_review/Eugon_agar_BD-Difco.md
  locator: '`data/ingredients/mapped/Eugon_agar_BD-Difco.yaml`:2; Verdict:4; Identity:10;
    Validation:22; Evidence:29; Completeness:43; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 19b10eb0c3468a30406275477fbe329d0abd4bfbb1223c5d5b5e042c6643328f
  quote: "Recommended Edits:\n- Minor: set `ingredient_type: NAMED_MEDIUM` on\n  `data/ingredients/mapped/Eugon_agar_BD-Difco.yaml`,\
    \ sync\n  `data/curated/mapped_ingredients.yaml`, and rerun strict validation."
- evidence_id: ev-c3dcc4aaca939af7
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[578]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b","finding_id":"SEM:e46cbbef982805442c7a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bf075fa10b2b3540
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0fa48eb224d0e588
  evidence_ids:
  - ev-285aea9e6466c608
  - ev-6b4e60e4b5c50eea
  - ev-4407e349dc1666fc
  - ev-7e1e367b2dc9ed30
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-eceb897ee45b50df
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0fa48eb224d0e588
  evidence_ids:
  - ev-3c8038582b040114
  - ev-285aea9e6466c608
  - ev-c3dcc4aaca939af7
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:01:41Z;
    reviewed SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b;
    current SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b;
    hash_changed=False. Reports=["reports/yaml_record_review/Eugon_agar_BD-Difco.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO Eugon agar identity and final SSSOM row pass, but ingredient_type should
    be backfilled.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-3c8038582b040114
    - ev-285aea9e6466c608
  - name: legacy-native-ids
    value: '["SEM:e46cbbef982805442c7a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-285aea9e6466c608
    - ev-3c8038582b040114
    - ev-c3dcc4aaca939af7
findings:
- finding_id: rec-f-b93ed7c15ba24f0c
  issue_key: mim-reconciliation-historical-review-coverage-and-r-0fa48eb224d0e588
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Eugon_agar_BD-Difco'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T16:01:41Z;
    reviewed SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b;
    current SHA-256=532b790c14461f0524e1307e87e36168d794360f1aa60dd371ff18984d0b8d1b;
    hash_changed=False. Reports=["reports/yaml_record_review/Eugon_agar_BD-Difco.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO Eugon agar identity and final SSSOM row pass, but ingredient_type should
    be backfilled.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0fa48eb224d0e588
  evidence_ids:
  - ev-3c8038582b040114
  - ev-285aea9e6466c608
  - ev-c3dcc4aaca939af7
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Eugon_agar_BD-Difco.yaml
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
