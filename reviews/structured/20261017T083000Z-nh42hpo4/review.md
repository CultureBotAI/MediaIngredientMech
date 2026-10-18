# Per-record structured review: Nh42hpo4 (data/ingredients/mapped/Nh42hpo4.yaml)

- Review: 20261017T083000Z-nh42hpo4
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Nh42hpo4 (data/ingredients/mapped/Nh42hpo4.yaml, record-e33fc743979ad297, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Nh42hpo4.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Nh42hpo4.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e33fc743979ad297 | data/ingredients/mapped/Nh42hpo4.yaml | maintained | Nh42hpo4 |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e33fc743979ad297 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-e33fc743979ad297 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e33fc743979ad297 | Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e33fc743979ad297.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e33fc743979ad297.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:25:03Z; reviewed SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51; current SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51; hash_changed=False. Reports=["reports/yaml_record_review/Nh42hpo4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63051 diammonium hydrogen phosphate identity passes, but final other has a Fisher catalog label.

## Findings

### rec-f-191214643e022044: Historical review coverage and residual narrative: Nh42hpo4

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-e33fc743979ad297.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:25:03Z; reviewed SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51; current SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51; hash_changed=False. Reports=["reports/yaml_record_review/Nh42hpo4.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI:63051 diammonium hydrogen phosphate identity passes, but final other has a Fisher catalog label.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-0304442f761c46fb | data/ingredients/mapped/Nh42hpo4.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1545],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63051","line":1547,"mapping_status":"MAPPED","ontology_id":"CHEBI:63051","preferred_term":"(NH4)2HPO4"}],"identifier":"CHEBI:63051","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":35,"edge_count":35,"occurrences":35},"occurrence_statistics":{"media_count":35,"total_occurrences":35},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63051","ontology_label":"diammonium hydrogen phosphate","ontology_source":"CHEBI"},"preferred_term":"(NH4)2HPO4","sssom_rows":[{"data_row":2066,"object_id":"CHEBI:63051","object_label":"diammonium hydrogen phosphate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nh42hpo4","synonym_count":5} |
| ev-04d3995e3207ef47 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1545] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-5557c20bcc720727 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Nh42hpo4; data-row positions=[2066] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2066,"object_id":"CHEBI:63051","object_label":"diammonium hydrogen phosphate","other":"(NH4)2HPO4(Fisher A686)&#124;diazanium hydrogen phosphate&#124;Ammonium phosphate&#124;CAS:7783-28-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Nh42hpo4","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-f5db0f2fb98e4d1b | docs/data/mapped_ingredients.csv; CSV lines=[1547] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:63051","line":1547,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"35","ontology_id":"CHEBI:63051","preferred_term":"(NH4)2HPO4","total_occurrences":"35"}] |
| ev-c66dda2ebc4c6503 | reports/yaml_record_review/Nh42hpo4.md; &#96;data/ingredients/mapped/Nh42hpo4.yaml&#96;:2; Verdict:4; Identity:11; Validation:21; Evidence:28; Completeness:42; Recommended Edits:49 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-342924b630650cb6 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1043] | context_only | [{"current_record_sha256":"c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51","finding_id":"SEM:9348c16febad3412f57a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024637Z-mim-reconcile-all-batch-09.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-nh42hpo4
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Nh42hpo4 (data/ingredients/mapped/Nh42hpo4.yaml)'
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
summary: Per-record structured review for Nh42hpo4 (data/ingredients/mapped/Nh42hpo4.yaml,
  record-e33fc743979ad297, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Nh42hpo4.yaml
    sha256: c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51
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
  - path: reports/yaml_record_review/Nh42hpo4.md
    sha256: f445c2155b7fa7799884e42ac9abe2ac76ab60522c5687a242cb090138ba6680
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e33fc743979ad297
  path: data/ingredients/mapped/Nh42hpo4.yaml
  label: Nh42hpo4
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nh42hpo4.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Nh42hpo4.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Nh42hpo4.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e33fc743979ad297
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e33fc743979ad297
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-e33fc743979ad297
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024637Z-mim-reconcile-all-batch-09
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e33fc743979ad297
evidence:
- evidence_id: ev-0304442f761c46fb
  kind: record_content
  reference: data/ingredients/mapped/Nh42hpo4.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1545],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:63051","line":1547,"mapping_status":"MAPPED","ontology_id":"CHEBI:63051","preferred_term":"(NH4)2HPO4"}],"identifier":"CHEBI:63051","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":35,"edge_count":35,"occurrences":35},"occurrence_statistics":{"media_count":35,"total_occurrences":35},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:63051","ontology_label":"diammonium
    hydrogen phosphate","ontology_source":"CHEBI"},"preferred_term":"(NH4)2HPO4","sssom_rows":[{"data_row":2066,"object_id":"CHEBI:63051","object_label":"diammonium
    hydrogen phosphate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Nh42hpo4","synonym_count":5}'
  snapshot_sha256: c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51
- evidence_id: ev-04d3995e3207ef47
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1545]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-5557c20bcc720727
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Nh42hpo4; data-row positions=[2066]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2066,"object_id":"CHEBI:63051","object_label":"diammonium
    hydrogen phosphate","other":"(NH4)2HPO4(Fisher A686)|diazanium hydrogen phosphate|Ammonium
    phosphate|CAS:7783-28-0","predicate_id":"skos:exactMatch","subject_id":"MIM:Nh42hpo4","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f5db0f2fb98e4d1b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1547]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:63051","line":1547,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"35","ontology_id":"CHEBI:63051","preferred_term":"(NH4)2HPO4","total_occurrences":"35"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-c66dda2ebc4c6503
  kind: prior_review
  reference: reports/yaml_record_review/Nh42hpo4.md
  locator: '`data/ingredients/mapped/Nh42hpo4.yaml`:2; Verdict:4; Identity:11; Validation:21;
    Evidence:28; Completeness:42; Recommended Edits:49'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f445c2155b7fa7799884e42ac9abe2ac76ab60522c5687a242cb090138ba6680
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Nh42hpo4.yaml`,\
    \ reject or demote\n  `(NH4)2HPO4(Fisher A686)`, then rebuild final SSSOM so vendor/catalog\
    \ labels\n  are no longer exported as exact synonyms."
- evidence_id: ev-342924b630650cb6
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1043]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51","finding_id":"SEM:9348c16febad3412f57a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-35fb4e10e303698b
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e33fc743979ad297
  evidence_ids:
  - ev-0304442f761c46fb
  - ev-04d3995e3207ef47
  - ev-5557c20bcc720727
  - ev-f5db0f2fb98e4d1b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d6f83887e6a7c190
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e33fc743979ad297
  evidence_ids:
  - ev-c66dda2ebc4c6503
  - ev-0304442f761c46fb
  - ev-342924b630650cb6
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:25:03Z;
    reviewed SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51;
    current SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51;
    hash_changed=False. Reports=["reports/yaml_record_review/Nh42hpo4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:63051 diammonium
    hydrogen phosphate identity passes, but final other has a Fisher catalog label.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-c66dda2ebc4c6503
    - ev-0304442f761c46fb
  - name: legacy-native-ids
    value: '["SEM:9348c16febad3412f57a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-0304442f761c46fb
    - ev-c66dda2ebc4c6503
    - ev-342924b630650cb6
findings:
- finding_id: rec-f-191214643e022044
  issue_key: mim-reconciliation-historical-review-coverage-and-r-e33fc743979ad297
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Nh42hpo4'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T06:25:03Z;
    reviewed SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51;
    current SHA-256=c37e0483f009037bdbe46a6da11fdd48c528a51b1847e824f1bba1a614b77e51;
    hash_changed=False. Reports=["reports/yaml_record_review/Nh42hpo4.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact CHEBI:63051 diammonium
    hydrogen phosphate identity passes, but final other has a Fisher catalog label.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e33fc743979ad297
  evidence_ids:
  - ev-c66dda2ebc4c6503
  - ev-0304442f761c46fb
  - ev-342924b630650cb6
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Nh42hpo4.yaml
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
