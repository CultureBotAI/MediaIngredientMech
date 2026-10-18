# Per-record structured review: Lignin_Alkali (data/ingredients/mapped/Lignin_Alkali.yaml)

- Review: 20261017T083000Z-lignin-alkali
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Lignin_Alkali (data/ingredients/mapped/Lignin_Alkali.yaml, record-f8916c308f942f48, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Lignin_Alkali.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Lignin_Alkali.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f8916c308f942f48 | data/ingredients/mapped/Lignin_Alkali.yaml | maintained | Lignin_Alkali |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f8916c308f942f48 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f8916c308f942f48 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f8916c308f942f48 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f8916c308f942f48.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f8916c308f942f48.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:25:32Z; reviewed SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726; current SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726; hash_changed=False. Reports=["reports/yaml_record_review/Lignin_Alkali.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local CAS fallback row for alkali lignin is honest, but the structure block is from unrelated PubChem CID 175586.

## Findings

### rec-f-2d9577b31df23550: Historical review coverage and residual narrative: Lignin_Alkali

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-f8916c308f942f48.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:25:32Z; reviewed SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726; current SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726; hash_changed=False. Reports=["reports/yaml_record_review/Lignin_Alkali.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local CAS fallback row for alkali lignin is honest, but the structure block is from unrelated PubChem CID 175586.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cbeea4be4921cfea | data/ingredients/mapped/Lignin_Alkali.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1302],"raw_equal":true},"docs_rows":[{"identifier":"cas:8068-05-1","line":1304,"mapping_status":"MAPPED","ontology_id":"cas:8068-05-1","preferred_term":"Lignin alkali"}],"identifier":"cas:8068-05-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:8068-05-1","ontology_label":"Lignin alkali","ontology_source":"CAS"},"preferred_term":"Lignin alkali","sssom_rows":[{"data_row":1694,"object_id":"cas:8068-05-1","object_label":"Lignin alkali","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lignin_Alkali","synonym_count":0} |
| ev-4c4bb7fcfbb5fd33 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1302] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-9edf2d6d1500daa4 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Lignin_Alkali; data-row positions=[1694] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1694,"object_id":"cas:8068-05-1","object_label":"Lignin alkali","other":"CAS:8068-05-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Lignin_Alkali","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-743a9a254de8958b | docs/data/mapped_ingredients.csv; CSV lines=[1304] | supports | Published identity and count rows inspected: [{"identifier":"cas:8068-05-1","line":1304,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:8068-05-1","preferred_term":"Lignin alkali","total_occurrences":"0"}] |
| ev-250d8a4e317a37de | reports/yaml_record_review/Lignin_Alkali.md; &#96;data/ingredients/mapped/Lignin_Alkali.yaml&#96;:2; Verdict:4; Identity:10; Validation:20; Evidence:29; Completeness:44; Recommended Edits:51 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-21d794bfb6b3ff76 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[863] | context_only | [{"current_record_sha256":"3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726","finding_id":"SEM:a2797b1a4e414ed5c176","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-lignin-alkali
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Lignin_Alkali (data/ingredients/mapped/Lignin_Alkali.yaml)'
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
summary: Per-record structured review for Lignin_Alkali (data/ingredients/mapped/Lignin_Alkali.yaml,
  record-f8916c308f942f48, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Lignin_Alkali.yaml
    sha256: 3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726
    role: target
  - path: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
    sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
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
  - path: reports/yaml_record_review/Lignin_Alkali.md
    sha256: b3f89c30eb8d30560d98ca1c05cb49e46c8a84214ee0aea5265fa9d7d542a81a
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f8916c308f942f48
  path: data/ingredients/mapped/Lignin_Alkali.yaml
  label: Lignin_Alkali
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lignin_Alkali.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Lignin_Alkali.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Lignin_Alkali.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f8916c308f942f48
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f8916c308f942f48
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f8916c308f942f48
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f8916c308f942f48
evidence:
- evidence_id: ev-cbeea4be4921cfea
  kind: record_content
  reference: data/ingredients/mapped/Lignin_Alkali.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1302],"raw_equal":true},"docs_rows":[{"identifier":"cas:8068-05-1","line":1304,"mapping_status":"MAPPED","ontology_id":"cas:8068-05-1","preferred_term":"Lignin
    alkali"}],"identifier":"cas:8068-05-1","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"FALLBACK_REGISTRY","ontology_id":"cas:8068-05-1","ontology_label":"Lignin
    alkali","ontology_source":"CAS"},"preferred_term":"Lignin alkali","sssom_rows":[{"data_row":1694,"object_id":"cas:8068-05-1","object_label":"Lignin
    alkali","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Lignin_Alkali","synonym_count":0}'
  snapshot_sha256: 3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726
- evidence_id: ev-4c4bb7fcfbb5fd33
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1302]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-9edf2d6d1500daa4
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Lignin_Alkali; data-row positions=[1694]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1694,"object_id":"cas:8068-05-1","object_label":"Lignin
    alkali","other":"CAS:8068-05-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Lignin_Alkali","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-743a9a254de8958b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1304]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"cas:8068-05-1","line":1304,"mapping_quality":"FALLBACK_REGISTRY","mapping_status":"MAPPED","media_count":"0","ontology_id":"cas:8068-05-1","preferred_term":"Lignin
    alkali","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-250d8a4e317a37de
  kind: prior_review
  reference: reports/yaml_record_review/Lignin_Alkali.md
  locator: '`data/ingredients/mapped/Lignin_Alkali.yaml`:2; Verdict:4; Identity:10;
    Validation:20; Evidence:29; Completeness:44; Recommended Edits:51'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: b3f89c30eb8d30560d98ca1c05cb49e46c8a84214ee0aea5265fa9d7d542a81a
  quote: "Recommended Edits:\n- Major: remove the CID `175586` formula, SMILES, InChI,\
    \ and `pubchem_cid` from\n  `data/ingredients/mapped/Lignin_Alkali.yaml` unless\
    \ a curator can prove those\n  values denote CAS `8068-05-1`.\n- Retain the `cas:8068-05-1`\
    \ fallback identity unless a more specific active\n  ontology term is found.\n\
    - Sync the aggregate copy and regenerate derived products after the YAML\n  change;\
    \ rerun strict, round-trip, component, and SSSOM validation."
- evidence_id: ev-21d794bfb6b3ff76
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[863]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726","finding_id":"SEM:a2797b1a4e414ed5c176","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-79253961b5fd98f0
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f8916c308f942f48
  evidence_ids:
  - ev-cbeea4be4921cfea
  - ev-4c4bb7fcfbb5fd33
  - ev-9edf2d6d1500daa4
  - ev-743a9a254de8958b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-a20057d4594051c9
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f8916c308f942f48
  evidence_ids:
  - ev-250d8a4e317a37de
  - ev-cbeea4be4921cfea
  - ev-21d794bfb6b3ff76
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:25:32Z;
    reviewed SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726;
    current SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726;
    hash_changed=False. Reports=["reports/yaml_record_review/Lignin_Alkali.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local CAS fallback
    row for alkali lignin is honest, but the structure block is from unrelated PubChem
    CID 175586.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-250d8a4e317a37de
    - ev-cbeea4be4921cfea
  - name: legacy-native-ids
    value: '["SEM:a2797b1a4e414ed5c176"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cbeea4be4921cfea
    - ev-250d8a4e317a37de
    - ev-21d794bfb6b3ff76
findings:
- finding_id: rec-f-2d9577b31df23550
  issue_key: mim-reconciliation-historical-review-coverage-and-r-f8916c308f942f48
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Lignin_Alkali'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T00:25:32Z;
    reviewed SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726;
    current SHA-256=3d8bfb7313ed44bc036d7c804a66bb062d68ad9110b312fc0fd85e4cf38ce726;
    hash_changed=False. Reports=["reports/yaml_record_review/Lignin_Alkali.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The local CAS fallback
    row for alkali lignin is honest, but the structure block is from unrelated PubChem
    CID 175586.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f8916c308f942f48
  evidence_ids:
  - ev-250d8a4e317a37de
  - ev-cbeea4be4921cfea
  - ev-21d794bfb6b3ff76
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Lignin_Alkali.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
