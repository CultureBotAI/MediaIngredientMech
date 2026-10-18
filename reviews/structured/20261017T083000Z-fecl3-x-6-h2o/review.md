# Per-record structured review: Fecl3_X_6_H2o (data/ingredients/mapped/Fecl3_X_6_H2o.yaml)

- Review: 20261017T083000Z-fecl3-x-6-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fecl3_X_6_H2o (data/ingredients/mapped/Fecl3_X_6_H2o.yaml, record-65f8736d67a46416, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fecl3_X_6_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fecl3_X_6_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-65f8736d67a46416 | data/ingredients/mapped/Fecl3_X_6_H2o.yaml | maintained | Fecl3_X_6_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-65f8736d67a46416 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-65f8736d67a46416 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-65f8736d67a46416 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-65f8736d67a46416.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-65f8736d67a46416.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:19:32Z; reviewed SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979; current SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979; hash_changed=False. Reports=["reports/yaml_record_review/Fecl3_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ferric chloride hexahydrate identity and role pass, but concentration and EDTA mixture strings still export as SSSOM synonyms.

## Findings

### rec-f-97121899d38a28ef: Historical review coverage and residual narrative: Fecl3_X_6_H2o

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-65f8736d67a46416.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:19:32Z; reviewed SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979; current SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979; hash_changed=False. Reports=["reports/yaml_record_review/Fecl3_X_6_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ferric chloride hexahydrate identity and role pass, but concentration and EDTA mixture strings still export as SSSOM synonyms.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-2bfd0e579e89e5d0 | data/ingredients/mapped/Fecl3_X_6_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[989],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86254","line":991,"mapping_status":"MAPPED","ontology_id":"CHEBI:86254","preferred_term":"FeCl3 x 6 H2O"}],"identifier":"CHEBI:86254","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":618,"edge_count":618,"occurrences":618},"occurrence_statistics":{"media_count":618,"total_occurrences":618},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:86254","ontology_label":"iron trichloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"FeCl3 x 6 H2O","sssom_rows":[{"data_row":1183,"object_id":"CHEBI:86254","object_label":"iron trichloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl3_X_6_H2o","synonym_count":18} |
| ev-cec03bcf76f84901 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [989] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-f329535af924f871 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fecl3_X_6_H2o; data-row positions=[1183] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1183,"object_id":"CHEBI:86254","object_label":"iron trichloride hexahydrate","other":"FeCl3\u00b76H2O&#124;FeCl3.6H2O&#124;Ferric chloride hexahydrate&#124;Iron (III) chloride hexahydrate&#124;trichloroiron--water (1/6)&#124;FeCl3 . 6H2O&#124;FeCl3 x 6 H2O (0.1% w/v in 0.2 N HCl)&#124;FeCl3 x 6 H2O (0.5%)&#124;FeCl3 x 6 H2O (w/v=1%)&#124;FeCl3 x 6 H2O NaEDTA&#124;FeCl3 x 6 H2O solution (2%)&#124;FeCl3 x6H2O&#124;FeCl3*6 H2O&#124;CAS:10025-77-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Fecl3_X_6_H2o","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-845548fd89124d96 | docs/data/mapped_ingredients.csv; CSV lines=[991] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:86254","line":991,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"618","ontology_id":"CHEBI:86254","preferred_term":"FeCl3 x 6 H2O","total_occurrences":"618"}] |
| ev-bd1cf36af4a06657 | reports/yaml_record_review/Fecl3_X_6_H2o.md; &#96;data/ingredients/mapped/Fecl3_X_6_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:28; Evidence:38; Completeness:68; Recommended Edits:76 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-120afdd0d962e330 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[595] | context_only | [{"current_record_sha256":"a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979","finding_id":"SEM:4c30741278662e8f2ff1","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fecl3-x-6-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fecl3_X_6_H2o (data/ingredients/mapped/Fecl3_X_6_H2o.yaml)'
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
summary: Per-record structured review for Fecl3_X_6_H2o (data/ingredients/mapped/Fecl3_X_6_H2o.yaml,
  record-65f8736d67a46416, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fecl3_X_6_H2o.yaml
    sha256: a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979
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
  - path: reports/yaml_record_review/Fecl3_X_6_H2o.md
    sha256: 1f185c4a6998eb60b123419b7799393d47fb663ef6c002456cae8be7c5c1a490
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-65f8736d67a46416
  path: data/ingredients/mapped/Fecl3_X_6_H2o.yaml
  label: Fecl3_X_6_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl3_X_6_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fecl3_X_6_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fecl3_X_6_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-65f8736d67a46416
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-65f8736d67a46416
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-65f8736d67a46416
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-65f8736d67a46416
evidence:
- evidence_id: ev-2bfd0e579e89e5d0
  kind: record_content
  reference: data/ingredients/mapped/Fecl3_X_6_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[989],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:86254","line":991,"mapping_status":"MAPPED","ontology_id":"CHEBI:86254","preferred_term":"FeCl3
    x 6 H2O"}],"identifier":"CHEBI:86254","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":618,"edge_count":618,"occurrences":618},"occurrence_statistics":{"media_count":618,"total_occurrences":618},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:86254","ontology_label":"iron
    trichloride hexahydrate","ontology_source":"CHEBI"},"preferred_term":"FeCl3 x
    6 H2O","sssom_rows":[{"data_row":1183,"object_id":"CHEBI:86254","object_label":"iron
    trichloride hexahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fecl3_X_6_H2o","synonym_count":18}'
  snapshot_sha256: a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979
- evidence_id: ev-cec03bcf76f84901
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [989]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-f329535af924f871
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fecl3_X_6_H2o; data-row positions=[1183]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1183,"object_id":"CHEBI:86254","object_label":"iron
    trichloride hexahydrate","other":"FeCl3\u00b76H2O|FeCl3.6H2O|Ferric chloride hexahydrate|Iron
    (III) chloride hexahydrate|trichloroiron--water (1/6)|FeCl3 . 6H2O|FeCl3 x 6 H2O
    (0.1% w/v in 0.2 N HCl)|FeCl3 x 6 H2O (0.5%)|FeCl3 x 6 H2O (w/v=1%)|FeCl3 x 6
    H2O NaEDTA|FeCl3 x 6 H2O solution (2%)|FeCl3 x6H2O|FeCl3*6 H2O|CAS:10025-77-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Fecl3_X_6_H2o","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-845548fd89124d96
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[991]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:86254","line":991,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"618","ontology_id":"CHEBI:86254","preferred_term":"FeCl3
    x 6 H2O","total_occurrences":"618"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-bd1cf36af4a06657
  kind: prior_review
  reference: reports/yaml_record_review/Fecl3_X_6_H2o.md
  locator: '`data/ingredients/mapped/Fecl3_X_6_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:28; Evidence:38; Completeness:68; Recommended Edits:76'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 1f185c4a6998eb60b123419b7799393d47fb663ef6c002456cae8be7c5c1a490
  quote: "Recommended Edits:\n- Major: remove or filter the concentration-bearing\
    \ `FeCl3 x 6 H2O` strings\n  and `FeCl3 x 6 H2O NaEDTA` from exact final SSSOM\
    \ `other` export, sync\n  `data/curated/mapped_ingredients.yaml`, regenerate\n\
    \  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus\n\
    \  the final SSSOM invariant gates."
- evidence_id: ev-120afdd0d962e330
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[595]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979","finding_id":"SEM:4c30741278662e8f2ff1","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-0f8f82515486c5c9
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-65f8736d67a46416
  evidence_ids:
  - ev-2bfd0e579e89e5d0
  - ev-cec03bcf76f84901
  - ev-f329535af924f871
  - ev-845548fd89124d96
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d515fd013b696a0c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-65f8736d67a46416
  evidence_ids:
  - ev-bd1cf36af4a06657
  - ev-2bfd0e579e89e5d0
  - ev-120afdd0d962e330
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:19:32Z;
    reviewed SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979;
    current SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979;
    hash_changed=False. Reports=["reports/yaml_record_review/Fecl3_X_6_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ferric
    chloride hexahydrate identity and role pass, but concentration and EDTA mixture
    strings still export as SSSOM synonyms.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-bd1cf36af4a06657
    - ev-2bfd0e579e89e5d0
  - name: legacy-native-ids
    value: '["SEM:4c30741278662e8f2ff1"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-2bfd0e579e89e5d0
    - ev-bd1cf36af4a06657
    - ev-120afdd0d962e330
findings:
- finding_id: rec-f-97121899d38a28ef
  issue_key: mim-reconciliation-historical-review-coverage-and-r-65f8736d67a46416
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Fecl3_X_6_H2o'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:19:32Z;
    reviewed SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979;
    current SHA-256=a77cd844d1d5ec5f1deb35d0ca1eff1ee5b73b17cd140be3524fc057f0f30979;
    hash_changed=False. Reports=["reports/yaml_record_review/Fecl3_X_6_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact ferric
    chloride hexahydrate identity and role pass, but concentration and EDTA mixture
    strings still export as SSSOM synonyms.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-65f8736d67a46416
  evidence_ids:
  - ev-bd1cf36af4a06657
  - ev-2bfd0e579e89e5d0
  - ev-120afdd0d962e330
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fecl3_X_6_H2o.yaml
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
