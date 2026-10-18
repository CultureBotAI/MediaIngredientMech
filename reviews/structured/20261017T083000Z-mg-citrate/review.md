# Per-record structured review: Mg-citrate (data/ingredients/mapped/Mg-citrate.yaml)

- Review: 20261017T083000Z-mg-citrate
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Mg-citrate (data/ingredients/mapped/Mg-citrate.yaml, record-70af0a8b45e93427, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Mg-citrate.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Mg-citrate.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-70af0a8b45e93427 | data/ingredients/mapped/Mg-citrate.yaml | maintained | Mg-citrate |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-70af0a8b45e93427 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-70af0a8b45e93427 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-70af0a8b45e93427 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-70af0a8b45e93427.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-70af0a8b45e93427.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:03:27Z; reviewed SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f; current SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f; hash_changed=False. Reports=["reports/yaml_record_review/Mg-citrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-based CHEBI:131391 trimagnesium dicitrate regrounding passes, but stale chemistry and stale final SSSOM other tokens still describe the old CHEBI:131389 1:1 salt.

## Findings

### rec-f-7c7842e1e77e8a1d: Historical review coverage and residual narrative: Mg-citrate

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-70af0a8b45e93427.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:03:27Z; reviewed SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f; current SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f; hash_changed=False. Reports=["reports/yaml_record_review/Mg-citrate.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CAS-based CHEBI:131391 trimagnesium dicitrate regrounding passes, but stale chemistry and stale final SSSOM other tokens still describe the old CHEBI:131389 1:1 salt.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-d929e183f248eeed | data/ingredients/mapped/Mg-citrate.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1391],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131391","line":1393,"mapping_status":"MAPPED","ontology_id":"CHEBI:131391","preferred_term":"Mg-citrate"}],"identifier":"CHEBI:131391","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:131391","ontology_label":"trimagnesium dicitrate","ontology_source":"CHEBI"},"preferred_term":"Mg-citrate","sssom_rows":[{"data_row":1858,"object_id":"CHEBI:131391","object_label":"trimagnesium dicitrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mg-citrate","synonym_count":4} |
| ev-f17a4da8865aa0ae | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1391] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-8b1e908bba63b35a | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Mg-citrate; data-row positions=[1858] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1858,"object_id":"CHEBI:131391","object_label":"trimagnesium dicitrate","other":"E345&#124;Magnesium citrate dibasic&#124;Magnesium hydrogen citrate&#124;magnesium 3-carboxy-3-hydroxypentanedioate&#124;CAS:3344-18-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Mg-citrate","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-b4d5166cf7826226 | docs/data/mapped_ingredients.csv; CSV lines=[1393] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131391","line":1393,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:131391","preferred_term":"Mg-citrate","total_occurrences":"5"}] |
| ev-2609809c1fca5d7e | reports/yaml_record_review/Mg-citrate.md; &#96;data/ingredients/mapped/Mg-citrate.yaml&#96;:2; Verdict:4; Identity:14; Validation:25; Evidence:32; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-3ac546ceaf948300 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[928] | context_only | [{"current_record_sha256":"6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f","finding_id":"SEM:82a09a69b0b818e596db","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-mg-citrate
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Mg-citrate (data/ingredients/mapped/Mg-citrate.yaml)'
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
summary: Per-record structured review for Mg-citrate (data/ingredients/mapped/Mg-citrate.yaml,
  record-70af0a8b45e93427, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Mg-citrate.yaml
    sha256: 6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f
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
  - path: reports/yaml_record_review/Mg-citrate.md
    sha256: cc445f6464decb53b6d651ac4ba75db084f434772187b350175e02f5c015f65d
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-70af0a8b45e93427
  path: data/ingredients/mapped/Mg-citrate.yaml
  label: Mg-citrate
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mg-citrate.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Mg-citrate.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Mg-citrate.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-70af0a8b45e93427
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-70af0a8b45e93427
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-70af0a8b45e93427
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-70af0a8b45e93427
evidence:
- evidence_id: ev-d929e183f248eeed
  kind: record_content
  reference: data/ingredients/mapped/Mg-citrate.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1391],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131391","line":1393,"mapping_status":"MAPPED","ontology_id":"CHEBI:131391","preferred_term":"Mg-citrate"}],"identifier":"CHEBI:131391","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":5,"edge_count":5,"occurrences":5},"occurrence_statistics":{"media_count":5,"total_occurrences":5},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:131391","ontology_label":"trimagnesium
    dicitrate","ontology_source":"CHEBI"},"preferred_term":"Mg-citrate","sssom_rows":[{"data_row":1858,"object_id":"CHEBI:131391","object_label":"trimagnesium
    dicitrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Mg-citrate","synonym_count":4}'
  snapshot_sha256: 6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f
- evidence_id: ev-f17a4da8865aa0ae
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1391]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-8b1e908bba63b35a
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Mg-citrate; data-row positions=[1858]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1858,"object_id":"CHEBI:131391","object_label":"trimagnesium
    dicitrate","other":"E345|Magnesium citrate dibasic|Magnesium hydrogen citrate|magnesium
    3-carboxy-3-hydroxypentanedioate|CAS:3344-18-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Mg-citrate","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-b4d5166cf7826226
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1393]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131391","line":1393,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"5","ontology_id":"CHEBI:131391","preferred_term":"Mg-citrate","total_occurrences":"5"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-2609809c1fca5d7e
  kind: prior_review
  reference: reports/yaml_record_review/Mg-citrate.md
  locator: '`data/ingredients/mapped/Mg-citrate.yaml`:2; Verdict:4; Identity:14; Validation:25;
    Evidence:32; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: cc445f6464decb53b6d651ac4ba75db084f434772187b350175e02f5c015f65d
  quote: "Recommended Edits:\n- Major: backfill `chemical_properties.molecular_formula`,\
    \ `smiles`, and\n  `inchi` from the active `CHEBI:131391` or PubChem CID 6099959\
    \ structure.\n- Major: remove or replace the four `CHEBI:131389` `kg_microbe`\
    \ synonyms so the\n  final SSSOM `other` field exports only names that are exact\
    \ for\n  trimagnesium dicitrate."
- evidence_id: ev-3ac546ceaf948300
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[928]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f","finding_id":"SEM:82a09a69b0b818e596db","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-731a7450ac28ce02
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-70af0a8b45e93427
  evidence_ids:
  - ev-d929e183f248eeed
  - ev-f17a4da8865aa0ae
  - ev-8b1e908bba63b35a
  - ev-b4d5166cf7826226
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-f13f042f38d74b7b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-70af0a8b45e93427
  evidence_ids:
  - ev-2609809c1fca5d7e
  - ev-d929e183f248eeed
  - ev-3ac546ceaf948300
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:03:27Z;
    reviewed SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f;
    current SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f;
    hash_changed=False. Reports=["reports/yaml_record_review/Mg-citrate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-based CHEBI:131391
    trimagnesium dicitrate regrounding passes, but stale chemistry and stale final
    SSSOM other tokens still describe the old CHEBI:131389 1:1 salt.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-2609809c1fca5d7e
    - ev-d929e183f248eeed
  - name: legacy-native-ids
    value: '["SEM:82a09a69b0b818e596db"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-d929e183f248eeed
    - ev-2609809c1fca5d7e
    - ev-3ac546ceaf948300
findings:
- finding_id: rec-f-7c7842e1e77e8a1d
  issue_key: mim-reconciliation-historical-review-coverage-and-r-70af0a8b45e93427
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Mg-citrate'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T03:03:27Z;
    reviewed SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f;
    current SHA-256=6601f382062758877609574deeb7a2d72d9f0c6d693139b55ac031cfc6e2fb1f;
    hash_changed=False. Reports=["reports/yaml_record_review/Mg-citrate.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The CAS-based CHEBI:131391
    trimagnesium dicitrate regrounding passes, but stale chemistry and stale final
    SSSOM other tokens still describe the old CHEBI:131389 1:1 salt.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-70af0a8b45e93427
  evidence_ids:
  - ev-2609809c1fca5d7e
  - ev-d929e183f248eeed
  - ev-3ac546ceaf948300
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Mg-citrate.yaml
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
