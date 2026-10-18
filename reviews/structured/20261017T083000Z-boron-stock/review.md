# Per-record structured review: Boron_Stock (data/ingredients/mapped/Boron_Stock.yaml)

- Review: 20261017T083000Z-boron-stock
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Boron_Stock (data/ingredients/mapped/Boron_Stock.yaml, record-bbe291ffc749a2d3, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Boron_Stock.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Boron_Stock.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-bbe291ffc749a2d3 | data/ingredients/mapped/Boron_Stock.yaml | maintained | Boron_Stock |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-bbe291ffc749a2d3 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-bbe291ffc749a2d3 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-bbe291ffc749a2d3 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-bbe291ffc749a2d3.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-bbe291ffc749a2d3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:07:33Z; reviewed SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d; current SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d; hash_changed=False. Reports=["reports/yaml_record_review/Boron_Stock.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity, mapped aggregate copy, and registry SSSOM row pass, but the active unmapped complex-media collection still carries a stale Boron Stock placeholder.

## Findings

### rec-f-405065995aa10a51: Historical review coverage and residual narrative: Boron_Stock

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-bbe291ffc749a2d3.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:07:33Z; reviewed SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d; current SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d; hash_changed=False. Reports=["reports/yaml_record_review/Boron_Stock.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local stock identity, mapped aggregate copy, and registry SSSOM row pass, but the active unmapped complex-media collection still carries a stale Boron Stock placeholder.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-01ae572c371467ce | data/ingredients/mapped/Boron_Stock.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[109],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:boron_stock","line":111,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:boron_stock","preferred_term":"Boron Stock"}],"identifier":"kgmicrobe.ingredient:boron_stock","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:boron_stock","ontology_label":"Boron Stock","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Boron Stock","sssom_rows":[{"data_row":571,"object_id":"kgmicrobe.ingredient:boron_stock","object_label":"Boron Stock","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Boron_Stock","synonym_count":1} |
| ev-1beff99641e8f532 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [109] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f06c585468b5cbff | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Boron_Stock; data-row positions=[571] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":571,"object_id":"kgmicrobe.ingredient:boron_stock","object_label":"Boron Stock","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Boron_Stock","validation_method":"manual:promote_resolved_unmapped&#124;PROMOTED&#124;2026-08-06"}] |
| ev-8584c714a2a385f3 | docs/data/mapped_ingredients.csv; CSV lines=[111] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:boron_stock","line":111,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:boron_stock","preferred_term":"Boron Stock","total_occurrences":"1"}] |
| ev-82cff62e87ba57a0 | reports/yaml_record_review/Boron_Stock.md; &#96;data/ingredients/mapped/Boron_Stock.yaml&#96;:2; Verdict:4; Identity:11; Validation:24; Evidence:35; Completeness:53; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d3db41fb27c2630b | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[325] | context_only | [{"current_record_sha256":"46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d","finding_id":"SEM:cfea8ea92e9717fbc468","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-boron-stock
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Boron_Stock (data/ingredients/mapped/Boron_Stock.yaml)'
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
summary: Per-record structured review for Boron_Stock (data/ingredients/mapped/Boron_Stock.yaml,
  record-bbe291ffc749a2d3, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Boron_Stock.yaml
    sha256: 46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d
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
  - path: reports/yaml_record_review/Boron_Stock.md
    sha256: 1b2fbc68bf0fcc8d49f745749884edd254b81fcb9da89478a157f8382e2c4c68
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-bbe291ffc749a2d3
  path: data/ingredients/mapped/Boron_Stock.yaml
  label: Boron_Stock
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Boron_Stock.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Boron_Stock.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Boron_Stock.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-bbe291ffc749a2d3
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-bbe291ffc749a2d3
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-bbe291ffc749a2d3
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-bbe291ffc749a2d3
evidence:
- evidence_id: ev-01ae572c371467ce
  kind: record_content
  reference: data/ingredients/mapped/Boron_Stock.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[109],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.ingredient:boron_stock","line":111,"mapping_status":"MAPPED","ontology_id":"kgmicrobe.ingredient:boron_stock","preferred_term":"Boron
    Stock"}],"identifier":"kgmicrobe.ingredient:boron_stock","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":1,"total_occurrences":1},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"kgmicrobe.ingredient:boron_stock","ontology_label":"Boron
    Stock","ontology_source":"kgmicrobe.ingredient"},"preferred_term":"Boron Stock","sssom_rows":[{"data_row":571,"object_id":"kgmicrobe.ingredient:boron_stock","object_label":"Boron
    Stock","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Boron_Stock","synonym_count":1}'
  snapshot_sha256: 46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d
- evidence_id: ev-1beff99641e8f532
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [109]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f06c585468b5cbff
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Boron_Stock; data-row positions=[571]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":571,"object_id":"kgmicrobe.ingredient:boron_stock","object_label":"Boron
    Stock","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Boron_Stock","validation_method":"manual:promote_resolved_unmapped|PROMOTED|2026-08-06"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-8584c714a2a385f3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[111]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.ingredient:boron_stock","line":111,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"1","ontology_id":"kgmicrobe.ingredient:boron_stock","preferred_term":"Boron
    Stock","total_occurrences":"1"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-82cff62e87ba57a0
  kind: prior_review
  reference: reports/yaml_record_review/Boron_Stock.md
  locator: '`data/ingredients/mapped/Boron_Stock.yaml`:2; Verdict:4; Identity:11;
    Validation:24; Evidence:35; Completeness:53; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1b2fbc68bf0fcc8d49f745749884edd254b81fcb9da89478a157f8382e2c4c68
  quote: "Recommended Edits:\n- Major: remove the stale `UNMAPPED_0064` `Boron Stock`\
    \ row from the\n  maintained unmapped complex-media collection, regenerate\n \
    \ `data/curated/UNMAPPED_COMPLEX_MEDIA.md`, and rerun strict validation plus\n\
    \  the round-trip/category checks that cover these curated collection files."
- evidence_id: ev-d3db41fb27c2630b
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[325]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d","finding_id":"SEM:cfea8ea92e9717fbc468","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-947c736db05b82c7
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-bbe291ffc749a2d3
  evidence_ids:
  - ev-01ae572c371467ce
  - ev-1beff99641e8f532
  - ev-f06c585468b5cbff
  - ev-8584c714a2a385f3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-00a829681ed43914
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bbe291ffc749a2d3
  evidence_ids:
  - ev-82cff62e87ba57a0
  - ev-01ae572c371467ce
  - ev-d3db41fb27c2630b
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:07:33Z;
    reviewed SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d;
    current SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d;
    hash_changed=False. Reports=["reports/yaml_record_review/Boron_Stock.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local stock
    identity, mapped aggregate copy, and registry SSSOM row pass, but the active unmapped
    complex-media collection still carries a stale Boron Stock placeholder.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-82cff62e87ba57a0
    - ev-01ae572c371467ce
  - name: legacy-native-ids
    value: '["SEM:cfea8ea92e9717fbc468"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-01ae572c371467ce
    - ev-82cff62e87ba57a0
    - ev-d3db41fb27c2630b
findings:
- finding_id: rec-f-405065995aa10a51
  issue_key: mim-reconciliation-historical-review-coverage-and-r-bbe291ffc749a2d3
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Boron_Stock'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T10:07:33Z;
    reviewed SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d;
    current SHA-256=46932663b39d601cce45de7e57c451a868711fe533d4194c02d997516b1aff9d;
    hash_changed=False. Reports=["reports/yaml_record_review/Boron_Stock.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local stock
    identity, mapped aggregate copy, and registry SSSOM row pass, but the active unmapped
    complex-media collection still carries a stale Boron Stock placeholder.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-bbe291ffc749a2d3
  evidence_ids:
  - ev-82cff62e87ba57a0
  - ev-01ae572c371467ce
  - ev-d3db41fb27c2630b
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Boron_Stock.yaml
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
