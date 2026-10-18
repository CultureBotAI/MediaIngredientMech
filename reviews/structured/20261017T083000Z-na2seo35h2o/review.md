# Per-record structured review: Na2seo35h2o (data/ingredients/mapped/Na2seo35h2o.yaml)

- Review: 20261017T083000Z-na2seo35h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Na2seo35h2o (data/ingredients/mapped/Na2seo35h2o.yaml, record-f46d08e37ba3d370, mapping_status=REJECTED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Na2seo35h2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Na2seo35h2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-f46d08e37ba3d370 | data/ingredients/mapped/Na2seo35h2o.yaml | maintained | Na2seo35h2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-f46d08e37ba3d370 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-f46d08e37ba3d370 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-f46d08e37ba3d370 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-f46d08e37ba3d370.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-f46d08e37ba3d370.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T05:35:01Z; reviewed SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b; current SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b; hash_changed=False. Reports=["reports/yaml_record_review/Na2seo35h2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected disodium selenite pentahydrate tombstone emits no final SSSOM row but still carries stale anhydrous CAS and structure fields.

## Findings

### rec-f-12146ff9f4356530: Historical review coverage and residual narrative: Na2seo35h2o

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-f46d08e37ba3d370.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T05:35:01Z; reviewed SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b; current SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b; hash_changed=False. Reports=["reports/yaml_record_review/Na2seo35h2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The rejected disodium selenite pentahydrate tombstone emits no final SSSOM row but still carries stale anhydrous CAS and structure fields.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-aea11f9b34e3a3da | data/ingredients/mapped/Na2seo35h2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1504],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131361","line":1506,"mapping_status":"REJECTED","ontology_id":"CHEBI:131361","preferred_term":"Na2SeO3\u00b75H2O"}],"identifier":"CHEBI:131361","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1617,"edge_count":1617,"occurrences":1622},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131361","ontology_label":"disodium selenite pentahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2SeO3\u00b75H2O","sssom_rows":[],"sssom_subject":"MIM:Na2seo35h2o","synonym_count":6} |
| ev-cc2ffb65e2bb9a17 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1504] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6cd40567d8b8df6a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Na2seo35h2o; data-row positions=[] | context_only | Current exact-subject rows, including complete other payload: [] |
| ev-5363c07bc0db30db | docs/data/mapped_ingredients.csv; CSV lines=[1506] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131361","line":1506,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:131361","preferred_term":"Na2SeO3\u00b75H2O","total_occurrences":"0"}] |
| ev-e931d709d8a5e32e | reports/yaml_record_review/Na2seo35h2o.md; &#96;data/ingredients/mapped/Na2seo35h2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:43; Recommended Edits:50 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3d14252d165effac | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1010] | context_only | [{"current_record_sha256":"889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b","finding_id":"SEM:897ce2e659a7e3938e62","kind":"existing_record_review","resolution_reason":"Source record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-na2seo35h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Na2seo35h2o (data/ingredients/mapped/Na2seo35h2o.yaml)'
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
native_verdict: mapping_status=REJECTED; open=0; deferred=1
scientific_review: false
summary: Per-record structured review for Na2seo35h2o (data/ingredients/mapped/Na2seo35h2o.yaml,
  record-f46d08e37ba3d370, mapping_status=REJECTED). Records 0 open finding(s) and
  1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Na2seo35h2o.yaml
    sha256: 889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b
    role: target
  - path: reviews/structured/20261011T024637Z-mim-reconcile-all-batch-09/review.yaml
    sha256: cf46750874f1303863883723934bbe8b09ece8d62b1785ceab64bb0342a3cf11
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
  - path: reports/yaml_record_review/Na2seo35h2o.md
    sha256: 6747ff56513c667184dbafd37ea56bc8dec41aac9610c5feeccec8915ac08bb0
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-f46d08e37ba3d370
  path: data/ingredients/mapped/Na2seo35h2o.yaml
  label: Na2seo35h2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2seo35h2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Na2seo35h2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Na2seo35h2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-f46d08e37ba3d370
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-f46d08e37ba3d370
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-f46d08e37ba3d370
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-f46d08e37ba3d370
evidence:
- evidence_id: ev-aea11f9b34e3a3da
  kind: record_content
  reference: data/ingredients/mapped/Na2seo35h2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1504],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131361","line":1506,"mapping_status":"REJECTED","ontology_id":"CHEBI:131361","preferred_term":"Na2SeO3\u00b75H2O"}],"identifier":"CHEBI:131361","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"REJECTED","membership_by_identifier":{"distinct_recipes":1617,"edge_count":1617,"occurrences":1622},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131361","ontology_label":"disodium
    selenite pentahydrate","ontology_source":"CHEBI"},"preferred_term":"Na2SeO3\u00b75H2O","sssom_rows":[],"sssom_subject":"MIM:Na2seo35h2o","synonym_count":6}'
  snapshot_sha256: 889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b
- evidence_id: ev-cc2ffb65e2bb9a17
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1504]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6cd40567d8b8df6a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Na2seo35h2o; data-row positions=[]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: []'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5363c07bc0db30db
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1506]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131361","line":1506,"mapping_quality":"EXACT_MATCH","mapping_status":"REJECTED","media_count":"0","ontology_id":"CHEBI:131361","preferred_term":"Na2SeO3\u00b75H2O","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e931d709d8a5e32e
  kind: prior_review
  reference: reports/yaml_record_review/Na2seo35h2o.md
  locator: '`data/ingredients/mapped/Na2seo35h2o.yaml`:2; Verdict:4; Identity:11;
    Validation:21; Evidence:28; Completeness:43; Recommended Edits:50'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 6747ff56513c667184dbafd37ea56bc8dec41aac9610c5feeccec8915ac08bb0
  quote: "Recommended Edits:\n- Minor: in `data/ingredients/mapped/Na2seo35h2o.yaml`,\
    \ either remove the\n  `chemical_properties` block from the rejected tombstone\
    \ or refresh its CAS RN,\n  InChI, and SMILES from `CHEBI:131361` so every retained\
    \ field denotes the\n  pentahydrate. Rerun strict validation after the tombstone\
    \ cleanup."
- evidence_id: ev-3d14252d165effac
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1010]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b","finding_id":"SEM:897ce2e659a7e3938e62","kind":"existing_record_review","resolution_reason":"Source
    record is explicitly rejected and absent from active graph.","resolution_status":"EXCLUDED_REJECTED"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-fa3ef5b4cb27278a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-f46d08e37ba3d370
  evidence_ids:
  - ev-aea11f9b34e3a3da
  - ev-cc2ffb65e2bb9a17
  - ev-6cd40567d8b8df6a
  - ev-5363c07bc0db30db
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-e7253bf74827cb74
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f46d08e37ba3d370
  evidence_ids:
  - ev-e931d709d8a5e32e
  - ev-aea11f9b34e3a3da
  - ev-3d14252d165effac
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T05:35:01Z;
    reviewed SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b;
    current SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2seo35h2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected disodium
    selenite pentahydrate tombstone emits no final SSSOM row but still carries stale
    anhydrous CAS and structure fields.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e931d709d8a5e32e
    - ev-aea11f9b34e3a3da
  - name: legacy-native-ids
    value: '["SEM:897ce2e659a7e3938e62"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-aea11f9b34e3a3da
    - ev-e931d709d8a5e32e
    - ev-3d14252d165effac
findings:
- finding_id: rec-f-12146ff9f4356530
  issue_key: mim-reconciliation-historical-review-coverage-and-r-f46d08e37ba3d370
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Na2seo35h2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-17T05:35:01Z;
    reviewed SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b;
    current SHA-256=889d9d25040aba6b22659bbb6ef5cd372966b448997258423ce5aa8b1864966b;
    hash_changed=False. Reports=["reports/yaml_record_review/Na2seo35h2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The rejected disodium
    selenite pentahydrate tombstone emits no final SSSOM row but still carries stale
    anhydrous CAS and structure fields.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-f46d08e37ba3d370
  evidence_ids:
  - ev-e931d709d8a5e32e
  - ev-aea11f9b34e3a3da
  - ev-3d14252d165effac
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Na2seo35h2o.yaml
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
  with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.
```
