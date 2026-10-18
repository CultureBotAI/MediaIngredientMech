# Per-record structured review: Glycine (data/ingredients/mapped/Glycine.yaml)

- Review: 20261017T083000Z-glycine
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Glycine (data/ingredients/mapped/Glycine.yaml, record-d00cebff5a183f91, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Glycine.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Glycine.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-d00cebff5a183f91 | data/ingredients/mapped/Glycine.yaml | maintained | Glycine |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-d00cebff5a183f91 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-d00cebff5a183f91 | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-d00cebff5a183f91 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-d00cebff5a183f91.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-d00cebff5a183f91.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:16:29Z; reviewed SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57; current SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57; hash_changed=False. Reports=["reports/yaml_record_review/Glycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glycine identity and source-backed nitrogen role pass, but final SSSOM exports Glycine 1% as a synonym.

## Findings

### rec-f-8fd436e57eb3f475: Historical review coverage and residual narrative: Glycine

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-d00cebff5a183f91.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:16:29Z; reviewed SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57; current SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57; hash_changed=False. Reports=["reports/yaml_record_review/Glycine.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact glycine identity and source-backed nitrogen role pass, but final SSSOM exports Glycine 1% as a synonym.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-979cf1c3cd0cf4ef | data/ingredients/mapped/Glycine.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1074],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15428","line":1076,"mapping_status":"MAPPED","ontology_id":"CHEBI:15428","preferred_term":"Glycine"}],"identifier":"CHEBI:15428","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":161,"edge_count":161,"occurrences":161},"occurrence_statistics":{"media_count":161,"total_occurrences":161},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15428","ontology_label":"glycine","ontology_source":"CHEBI"},"preferred_term":"Glycine","sssom_rows":[{"data_row":1341,"object_id":"CHEBI:15428","object_label":"glycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycine","synonym_count":15} |
| ev-e3b52b3723547606 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1074] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-476cfb4a97144fea | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Glycine; data-row positions=[1341] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1341,"object_id":"CHEBI:15428","object_label":"glycine","other":"Aminoacetic acid&#124;Aminoessigsaeure&#124;Gly&#124;Glycocoll&#124;Glykokoll&#124;Glyzin&#124;H2N-CH2-COOH&#124;Hgly&#124;Leimzucker&#124;aminoethanoic acid&#124;Glycine 1%&#124;CAS:56-40-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycine","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-07be19c0781082eb | docs/data/mapped_ingredients.csv; CSV lines=[1076] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:15428","line":1076,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"161","ontology_id":"CHEBI:15428","preferred_term":"Glycine","total_occurrences":"161"}] |
| ev-872a757fd3595e15 | reports/yaml_record_review/Glycine.md; &#96;data/ingredients/mapped/Glycine.yaml&#96;:2; Verdict:4; Identity:12; Validation:22; Evidence:29; Completeness:59; Recommended Edits:67 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-bcdbe9c9b47bb75f | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[693] | context_only | [{"current_record_sha256":"a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57","finding_id":"SEM:39374b3af6f13c0c64d4","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-glycine
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Glycine (data/ingredients/mapped/Glycine.yaml)'
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
summary: Per-record structured review for Glycine (data/ingredients/mapped/Glycine.yaml,
  record-d00cebff5a183f91, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Glycine.yaml
    sha256: a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57
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
  - path: reports/yaml_record_review/Glycine.md
    sha256: a393b33934cfb1dfcbe250fc080a7b62698382ded620953248160f690e431073
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-d00cebff5a183f91
  path: data/ingredients/mapped/Glycine.yaml
  label: Glycine
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycine.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Glycine.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Glycine.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-d00cebff5a183f91
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-d00cebff5a183f91
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-d00cebff5a183f91
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-d00cebff5a183f91
evidence:
- evidence_id: ev-979cf1c3cd0cf4ef
  kind: record_content
  reference: data/ingredients/mapped/Glycine.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1074],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:15428","line":1076,"mapping_status":"MAPPED","ontology_id":"CHEBI:15428","preferred_term":"Glycine"}],"identifier":"CHEBI:15428","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":161,"edge_count":161,"occurrences":161},"occurrence_statistics":{"media_count":161,"total_occurrences":161},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:15428","ontology_label":"glycine","ontology_source":"CHEBI"},"preferred_term":"Glycine","sssom_rows":[{"data_row":1341,"object_id":"CHEBI:15428","object_label":"glycine","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Glycine","synonym_count":15}'
  snapshot_sha256: a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57
- evidence_id: ev-e3b52b3723547606
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1074]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-476cfb4a97144fea
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Glycine; data-row positions=[1341]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1341,"object_id":"CHEBI:15428","object_label":"glycine","other":"Aminoacetic
    acid|Aminoessigsaeure|Gly|Glycocoll|Glykokoll|Glyzin|H2N-CH2-COOH|Hgly|Leimzucker|aminoethanoic
    acid|Glycine 1%|CAS:56-40-6","predicate_id":"skos:exactMatch","subject_id":"MIM:Glycine","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-07be19c0781082eb
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1076]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:15428","line":1076,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"161","ontology_id":"CHEBI:15428","preferred_term":"Glycine","total_occurrences":"161"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-872a757fd3595e15
  kind: prior_review
  reference: reports/yaml_record_review/Glycine.md
  locator: '`data/ingredients/mapped/Glycine.yaml`:2; Verdict:4; Identity:12; Validation:22;
    Evidence:29; Completeness:59; Recommended Edits:67'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: a393b33934cfb1dfcbe250fc080a7b62698382ded620953248160f690e431073
  quote: "Recommended Edits:\n- Major: retype `Glycine 1%` in `data/ingredients/mapped/Glycine.yaml`\
    \ as a\n  non-resolving rejected label, or teach the synonym policy to filter\n\
    \  concentration-qualified raw labels, then rebuild the final SSSOM so\n  `MIM:Glycine`\
    \ no longer exports `Glycine 1%` in `other`."
- evidence_id: ev-bcdbe9c9b47bb75f
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[693]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57","finding_id":"SEM:39374b3af6f13c0c64d4","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-b4bf9f3d015a7487
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-d00cebff5a183f91
  evidence_ids:
  - ev-979cf1c3cd0cf4ef
  - ev-e3b52b3723547606
  - ev-476cfb4a97144fea
  - ev-07be19c0781082eb
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-8ce81e107185eb6f
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d00cebff5a183f91
  evidence_ids:
  - ev-872a757fd3595e15
  - ev-979cf1c3cd0cf4ef
  - ev-bcdbe9c9b47bb75f
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:16:29Z;
    reviewed SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57;
    current SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycine.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact glycine identity
    and source-backed nitrogen role pass, but final SSSOM exports Glycine 1% as a
    synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-872a757fd3595e15
    - ev-979cf1c3cd0cf4ef
  - name: legacy-native-ids
    value: '["SEM:39374b3af6f13c0c64d4"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-979cf1c3cd0cf4ef
    - ev-872a757fd3595e15
    - ev-bcdbe9c9b47bb75f
findings:
- finding_id: rec-f-8fd436e57eb3f475
  issue_key: mim-reconciliation-historical-review-coverage-and-r-d00cebff5a183f91
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Glycine'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T18:16:29Z;
    reviewed SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57;
    current SHA-256=a3f7af80526ce763ef05d032ef7c31caa28203bbd1ed4b788bf6b921c70f5a57;
    hash_changed=False. Reports=["reports/yaml_record_review/Glycine.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The exact glycine identity
    and source-backed nitrogen role pass, but final SSSOM exports Glycine 1% as a
    synonym.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-d00cebff5a183f91
  evidence_ids:
  - ev-872a757fd3595e15
  - ev-979cf1c3cd0cf4ef
  - ev-bcdbe9c9b47bb75f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Glycine.yaml
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
