# Per-record structured review: Distilled_Water (data/ingredients/mapped/Distilled_Water.yaml)

- Review: 20261017T083000Z-distilled-water
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Distilled_Water (data/ingredients/mapped/Distilled_Water.yaml, record-45114f77631f0385, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Distilled_Water.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Distilled_Water.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-45114f77631f0385 | data/ingredients/mapped/Distilled_Water.yaml | maintained | Distilled_Water |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-45114f77631f0385 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-45114f77631f0385 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-45114f77631f0385 | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-45114f77631f0385.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-45114f77631f0385.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T15:06:45Z; reviewed SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56; current SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56; hash_changed=False. Reports=["reports/yaml_record_review/Distilled_Water.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The broadened CHEBI water identity and final SSSOM synonyms pass; only weak auto-proposed PubMed evidence remains.

## Findings

### rec-f-dc7f2993f58316da: Historical review coverage and residual narrative: Distilled_Water

minor / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-45114f77631f0385.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T15:06:45Z; reviewed SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56; current SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56; hash_changed=False. Reports=["reports/yaml_record_review/Distilled_Water.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The broadened CHEBI water identity and final SSSOM synonyms pass; only weak auto-proposed PubMed evidence remains.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-faa417d28777cf76 | data/ingredients/mapped/Distilled_Water.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[907],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15377","line":909,"mapping_status":"MAPPED","ontology_id":"CHEBI:15377","preferred_term":"Distilled water"}],"identifier":"CHEBI:15377","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6825,"edge_count":6825,"occurrences":6872},"occurrence_statistics":{"media_count":6825,"total_occurrences":6872},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15377","ontology_label":"water","ontology_source":"CHEBI"},"preferred_term":"Distilled water","sssom_rows":[{"data_row":1069,"object_id":"CHEBI:15377","object_label":"water","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Distilled_Water","synonym_count":34} |
| ev-743d0baddf94eeb5 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [907] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-c244d1357ecdd7eb | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Distilled_Water; data-row positions=[1069] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1069,"object_id":"CHEBI:15377","object_label":"water","other":"H(2)O&#124;H2O&#124;HOH&#124;Wasser&#124;[OH2]&#124;acqua&#124;agua&#124;aqua&#124;dH2O&#124;Distiled water&#124;dihydridooxygen&#124;dihydrogen oxide&#124;eau&#124;hydrogen hydroxide&#124;oxidane&#124;Distilled water (for liquid medium)&#124;Distilled water (for solid medium)&#124;CAS:7732-18-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Distilled_Water","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-cf1fe4140e3a2036 | docs/data/mapped_ingredients.csv; CSV lines=[909] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15377","line":909,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6825","ontology_id":"CHEBI:15377","preferred_term":"Distilled water","total_occurrences":"6872"}] |
| ev-e60d7e5ed8130623 | reports/yaml_record_review/Distilled_Water.md; &#96;data/ingredients/mapped/Distilled_Water.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:40; Completeness:61; Recommended Edits:71 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-b70a1d27650a33ca | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[546] | context_only | [{"current_record_sha256":"458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56","finding_id":"SEM:e6bab7eac7e0378c8941","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-distilled-water
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Distilled_Water (data/ingredients/mapped/Distilled_Water.yaml)'
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
summary: Per-record structured review for Distilled_Water (data/ingredients/mapped/Distilled_Water.yaml,
  record-45114f77631f0385, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Distilled_Water.yaml
    sha256: 458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56
    role: target
  - path: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
    sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
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
  - path: reports/yaml_record_review/Distilled_Water.md
    sha256: 34a3de15f425dfcbfa44412985924abf273ddf3618b946dd9af115d8f12c6b6b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-45114f77631f0385
  path: data/ingredients/mapped/Distilled_Water.yaml
  label: Distilled_Water
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Distilled_Water.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Distilled_Water.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Distilled_Water.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-45114f77631f0385
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-45114f77631f0385
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-45114f77631f0385
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-45114f77631f0385
evidence:
- evidence_id: ev-faa417d28777cf76
  kind: record_content
  reference: data/ingredients/mapped/Distilled_Water.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[907],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15377","line":909,"mapping_status":"MAPPED","ontology_id":"CHEBI:15377","preferred_term":"Distilled
    water"}],"identifier":"CHEBI:15377","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6825,"edge_count":6825,"occurrences":6872},"occurrence_statistics":{"media_count":6825,"total_occurrences":6872},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15377","ontology_label":"water","ontology_source":"CHEBI"},"preferred_term":"Distilled
    water","sssom_rows":[{"data_row":1069,"object_id":"CHEBI:15377","object_label":"water","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Distilled_Water","synonym_count":34}'
  snapshot_sha256: 458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56
- evidence_id: ev-743d0baddf94eeb5
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [907]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-c244d1357ecdd7eb
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Distilled_Water; data-row positions=[1069]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1069,"object_id":"CHEBI:15377","object_label":"water","other":"H(2)O|H2O|HOH|Wasser|[OH2]|acqua|agua|aqua|dH2O|Distiled
    water|dihydridooxygen|dihydrogen oxide|eau|hydrogen hydroxide|oxidane|Distilled
    water (for liquid medium)|Distilled water (for solid medium)|CAS:7732-18-5","predicate_id":"skos:exactMatch","subject_id":"MIM:Distilled_Water","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-cf1fe4140e3a2036
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[909]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15377","line":909,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"6825","ontology_id":"CHEBI:15377","preferred_term":"Distilled
    water","total_occurrences":"6872"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e60d7e5ed8130623
  kind: prior_review
  reference: reports/yaml_record_review/Distilled_Water.md
  locator: '`data/ingredients/mapped/Distilled_Water.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:40; Completeness:61; Recommended Edits:71'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 34a3de15f425dfcbfa44412985924abf273ddf3618b946dd9af115d8f12c6b6b
  quote: "Recommended Edits:\n- Minor: remove the auto-proposed PubMed evidence from\n\
    \  `data/ingredients/mapped/Distilled_Water.yaml`, or replace it with an explicit\n\
    \  source note explaining why the distilled-water source surface is intentionally\n\
    \  represented by broad `CHEBI:15377`; then synchronize\n  `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-b70a1d27650a33ca
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[546]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56","finding_id":"SEM:e6bab7eac7e0378c8941","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-6256d4589e8f822a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-45114f77631f0385
  evidence_ids:
  - ev-faa417d28777cf76
  - ev-743d0baddf94eeb5
  - ev-c244d1357ecdd7eb
  - ev-cf1fe4140e3a2036
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9ae423c5693af066
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-45114f77631f0385
  evidence_ids:
  - ev-e60d7e5ed8130623
  - ev-faa417d28777cf76
  - ev-b70a1d27650a33ca
  details: 'Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T15:06:45Z;
    reviewed SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56;
    current SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56;
    hash_changed=False. Reports=["reports/yaml_record_review/Distilled_Water.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The broadened
    CHEBI water identity and final SSSOM synonyms pass; only weak auto-proposed PubMed
    evidence remains.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e60d7e5ed8130623
    - ev-faa417d28777cf76
  - name: legacy-native-ids
    value: '["SEM:e6bab7eac7e0378c8941"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-faa417d28777cf76
    - ev-e60d7e5ed8130623
    - ev-b70a1d27650a33ca
findings:
- finding_id: rec-f-dc7f2993f58316da
  issue_key: mim-reconciliation-historical-review-coverage-and-r-45114f77631f0385
  category: provenance
  severity: minor
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Distilled_Water'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=pass_with_minor_issues; severity=minor; reviewed_at=2026-09-16T15:06:45Z;
    reviewed SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56;
    current SHA-256=458e87161555bb11415b5155a30085120b121c07ee6612f8d7a5b6f0eb22ff56;
    hash_changed=False. Reports=["reports/yaml_record_review/Distilled_Water.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The broadened
    CHEBI water identity and final SSSOM synonyms pass; only weak auto-proposed PubMed
    evidence remains.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-45114f77631f0385
  evidence_ids:
  - ev-e60d7e5ed8130623
  - ev-faa417d28777cf76
  - ev-b70a1d27650a33ca
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Distilled_Water.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
