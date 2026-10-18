# Per-record structured review: Sodium_Carbonate_Solution (data/ingredients/mapped/Sodium_Carbonate_Solution.yaml)

- Review: 20261017T083000Z-sodium-carbonate-solution
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Sodium_Carbonate_Solution (data/ingredients/mapped/Sodium_Carbonate_Solution.yaml, record-7d775f5a978e86f9, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Sodium_Carbonate_Solution.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Sodium_Carbonate_Solution.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-7d775f5a978e86f9 | data/ingredients/mapped/Sodium_Carbonate_Solution.yaml | maintained | Sodium_Carbonate_Solution |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-7d775f5a978e86f9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-7d775f5a978e86f9 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-7d775f5a978e86f9 | Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-7d775f5a978e86f9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-7d775f5a978e86f9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:54:52Z; reviewed SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6; current SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Carbonate_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI:29377 solute and buffer role pass, but final SSSOM exports malformed formula, supplier-specific, and buffer-system labels.

## Findings

### rec-f-1fa67e7a38523bdd: Historical review coverage and residual narrative: Sodium_Carbonate_Solution

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-7d775f5a978e86f9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:54:52Z; reviewed SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6; current SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6; hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Carbonate_Solution.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The CHEBI:29377 solute and buffer role pass, but final SSSOM exports malformed formula, supplier-specific, and buffer-system labels.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b9957d1da99a460f | data/ingredients/mapped/Sodium_Carbonate_Solution.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1823],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29377","line":1825,"mapping_status":"MAPPED","ontology_id":"CHEBI:29377","preferred_term":"Sodium carbonate solution"}],"identifier":"CHEBI:29377","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1751,"edge_count":1751,"occurrences":1751},"occurrence_statistics":{"media_count":1751,"total_occurrences":1751},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:29377","ontology_label":"sodium carbonate","ontology_source":"CHEBI"},"preferred_term":"Sodium carbonate solution","sssom_rows":[{"data_row":2545,"object_id":"CHEBI:29377","object_label":"sodium carbonate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Carbonate_Solution","synonym_count":9} |
| ev-cdbd7b8c548d490b | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1823] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-e07c5a9a8aacbcaa | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Sodium_Carbonate_Solution; data-row positions=[2545] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2545,"object_id":"CHEBI:29377","object_label":"sodium carbonate","other":"disodium trioxidocarbonate&#124;Na CO&#124;Na2CO&#124;Na2CO3 anhydrous&#124;Na2CO3(Baker 3604)&#124;Na2CO3-CO2 buffer&#124;NaCO3","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Carbonate_Solution","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-bb0f2797d260132d | docs/data/mapped_ingredients.csv; CSV lines=[1825] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:29377","line":1825,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"1751","ontology_id":"CHEBI:29377","preferred_term":"Sodium carbonate solution","total_occurrences":"1751"}] |
| ev-7e8e9189f49ec8e2 | reports/yaml_record_review/Sodium_Carbonate_Solution.md; &#96;data/ingredients/mapped/Sodium_Carbonate_Solution.yaml&#96;:2 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-f2bb98a715b67b17 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1208] | context_only | [{"current_record_sha256":"537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6","finding_id":"SEM:c493990865c65b528958","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-sodium-carbonate-solution
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Sodium_Carbonate_Solution (data/ingredients/mapped/Sodium_Carbonate_Solution.yaml)'
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
summary: Per-record structured review for Sodium_Carbonate_Solution (data/ingredients/mapped/Sodium_Carbonate_Solution.yaml,
  record-7d775f5a978e86f9, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
    sha256: 537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6
    role: target
  - path: reviews/structured/20261011T024638Z-mim-reconcile-all-batch-11/review.yaml
    sha256: a417d1bfc777756925990a4ecae1a6b539746c3606d042df7e1c29a218c62f8b
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
  - path: reports/yaml_record_review/Sodium_Carbonate_Solution.md
    sha256: e3e3a0c3a85e980aae795456893eb6f68448b54b2d64fbaaf43611c41ac75937
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-7d775f5a978e86f9
  path: data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
  label: Sodium_Carbonate_Solution
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
    selected from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-7d775f5a978e86f9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-7d775f5a978e86f9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-7d775f5a978e86f9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024638Z-mim-reconcile-all-batch-11
    and semantic review dispositions on HEAD.
  target_ids:
  - record-7d775f5a978e86f9
evidence:
- evidence_id: ev-b9957d1da99a460f
  kind: record_content
  reference: data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1823],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:29377","line":1825,"mapping_status":"MAPPED","ontology_id":"CHEBI:29377","preferred_term":"Sodium
    carbonate solution"}],"identifier":"CHEBI:29377","ingredient_type":"STOCK_SOLUTION","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":1751,"edge_count":1751,"occurrences":1751},"occurrence_statistics":{"media_count":1751,"total_occurrences":1751},"ontology_mapping":{"mapping_quality":"LEXICAL_MATCH","ontology_id":"CHEBI:29377","ontology_label":"sodium
    carbonate","ontology_source":"CHEBI"},"preferred_term":"Sodium carbonate solution","sssom_rows":[{"data_row":2545,"object_id":"CHEBI:29377","object_label":"sodium
    carbonate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Sodium_Carbonate_Solution","synonym_count":9}'
  snapshot_sha256: 537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6
- evidence_id: ev-cdbd7b8c548d490b
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1823]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-e07c5a9a8aacbcaa
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Sodium_Carbonate_Solution; data-row positions=[2545]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2545,"object_id":"CHEBI:29377","object_label":"sodium
    carbonate","other":"disodium trioxidocarbonate|Na CO|Na2CO|Na2CO3 anhydrous|Na2CO3(Baker
    3604)|Na2CO3-CO2 buffer|NaCO3","predicate_id":"skos:exactMatch","subject_id":"MIM:Sodium_Carbonate_Solution","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-bb0f2797d260132d
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1825]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:29377","line":1825,"mapping_quality":"LEXICAL_MATCH","mapping_status":"MAPPED","media_count":"1751","ontology_id":"CHEBI:29377","preferred_term":"Sodium
    carbonate solution","total_occurrences":"1751"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-7e8e9189f49ec8e2
  kind: prior_review
  reference: reports/yaml_record_review/Sodium_Carbonate_Solution.md
  locator: '`data/ingredients/mapped/Sodium_Carbonate_Solution.yaml`:2'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: e3e3a0c3a85e980aae795456893eb6f68448b54b2d64fbaaf43611c41ac75937
- evidence_id: ev-f2bb98a715b67b17
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1208]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6","finding_id":"SEM:c493990865c65b528958","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-ebdd4e0c2a384872
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-7d775f5a978e86f9
  evidence_ids:
  - ev-b9957d1da99a460f
  - ev-cdbd7b8c548d490b
  - ev-e07c5a9a8aacbcaa
  - ev-bb0f2797d260132d
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-4774088604f4d9ed
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7d775f5a978e86f9
  evidence_ids:
  - ev-7e8e9189f49ec8e2
  - ev-b9957d1da99a460f
  - ev-f2bb98a715b67b17
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:54:52Z;
    reviewed SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6;
    current SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Carbonate_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI:29377
    solute and buffer role pass, but final SSSOM exports malformed formula, supplier-specific,
    and buffer-system labels.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-7e8e9189f49ec8e2
    - ev-b9957d1da99a460f
  - name: legacy-native-ids
    value: '["SEM:c493990865c65b528958"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b9957d1da99a460f
    - ev-7e8e9189f49ec8e2
    - ev-f2bb98a715b67b17
findings:
- finding_id: rec-f-1fa67e7a38523bdd
  issue_key: mim-reconciliation-historical-review-coverage-and-r-7d775f5a978e86f9
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Sodium_Carbonate_Solution'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T14:54:52Z;
    reviewed SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6;
    current SHA-256=537baefadff4ad57ce2f405300b09f74b82962990fb4e6f5673a406ac83e00d6;
    hash_changed=False. Reports=["reports/yaml_record_review/Sodium_Carbonate_Solution.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The CHEBI:29377
    solute and buffer role pass, but final SSSOM exports malformed formula, supplier-specific,
    and buffer-system labels.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-7d775f5a978e86f9
  evidence_ids:
  - ev-7e8e9189f49ec8e2
  - ev-b9957d1da99a460f
  - ev-f2bb98a715b67b17
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Sodium_Carbonate_Solution.yaml
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
  with lineage to 20261011T024638Z-mim-reconcile-all-batch-11.
```
