# Per-record structured review: Folic_Acid (data/ingredients/mapped/Folic_Acid.yaml)

- Review: 20261017T083000Z-folic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Folic_Acid (data/ingredients/mapped/Folic_Acid.yaml, record-fc2f1c8e1973820c, mapping_status=MAPPED). Records 0 open finding(s) and 1 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Folic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Folic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-fc2f1c8e1973820c | data/ingredients/mapped/Folic_Acid.yaml | maintained | Folic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-fc2f1c8e1973820c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | passed | True | record-fc2f1c8e1973820c | All populated role assertions on this record carry non-prediction evidence or no role array defects were detected. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-fc2f1c8e1973820c | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-fc2f1c8e1973820c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-fc2f1c8e1973820c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:52:12Z; reviewed SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615; current SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615; hash_changed=False. Reports=["reports/yaml_record_review/Folic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact folic acid identity passes, but one different folate and one concentration label leak into final SSSOM other.

## Findings

### rec-f-530396e11116620e: Historical review coverage and residual narrative: Folic_Acid

major / deferred / provisional; issue key: mim-reconciliation-historical-review-coverage-and-r-fc2f1c8e1973820c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment. Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:52:12Z; reviewed SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615; current SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615; hash_changed=False. Reports=["reports/yaml_record_review/Folic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact folic acid identity passes, but one different folate and one concentration label leak into final SSSOM other.

Disposition: The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-6f9f5d1a9f9bcd42 | data/ingredients/mapped/Folic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1015],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27470","line":1017,"mapping_status":"MAPPED","ontology_id":"CHEBI:27470","preferred_term":"Folic acid"}],"identifier":"CHEBI:27470","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2108,"edge_count":2108,"occurrences":2111},"occurrence_statistics":{"media_count":2108,"total_occurrences":2111},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27470","ontology_label":"folic acid","ontology_source":"CHEBI"},"preferred_term":"Folic acid","sssom_rows":[{"data_row":1225,"object_id":"CHEBI:27470","object_label":"folic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Folic_Acid","synonym_count":24} |
| ev-5bb9616fc542b9dc | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1015] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-626cddc2f6661864 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Folic_Acid; data-row positions=[1225] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1225,"object_id":"CHEBI:27470","object_label":"folic acid","other":"Folate&#124;(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic acid&#124;Acfol&#124;Folicet&#124;Folinic acid (citrovorum)&#124;Folsaeure&#124;N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic acid&#124;N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic acid&#124;N-pteroyl-L-glutamic acid&#124;PGA&#124;PteGlu&#124;acide folique&#124;acido folico&#124;acidum folicum&#124;pteroyl-L-glutamic acid&#124;pteroyl-L-monoglutamic acid&#124;pteroylglutamic acid&#124;pteroylmonoglutamic acid&#124;vitamin B11&#124;vitamin B9&#124;Folic acid (5 \u03bcg/\u03bcL)&#124;CAS:59-30-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Folic_Acid","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-d069c10d3a229267 | docs/data/mapped_ingredients.csv; CSV lines=[1017] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:27470","line":1017,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2108","ontology_id":"CHEBI:27470","preferred_term":"Folic acid","total_occurrences":"2111"}] |
| ev-a034d48d5df9bcf8 | reports/yaml_record_review/Folic_Acid.md; &#96;data/ingredients/mapped/Folic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:32; Completeness:63; Recommended Edits:70 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c1b66733be2277f3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[624] | context_only | [{"current_record_sha256":"df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615","finding_id":"SEM:d2370682344a15f3d338","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-folic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Folic_Acid (data/ingredients/mapped/Folic_Acid.yaml)'
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
summary: Per-record structured review for Folic_Acid (data/ingredients/mapped/Folic_Acid.yaml,
  record-fc2f1c8e1973820c, mapping_status=MAPPED). Records 0 open finding(s) and 1
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Folic_Acid.yaml
    sha256: df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615
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
  - path: reports/yaml_record_review/Folic_Acid.md
    sha256: 33ccd4e17e2fcdc426b7f73485dc43b5183d95fc0ed0a08234daf29872428e27
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-fc2f1c8e1973820c
  path: data/ingredients/mapped/Folic_Acid.yaml
  label: Folic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Folic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Folic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Folic_Acid.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-fc2f1c8e1973820c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-fc2f1c8e1973820c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: passed
  required: true
  summary: All populated role assertions on this record carry non-prediction evidence
    or no role array defects were detected.
  target_ids:
  - record-fc2f1c8e1973820c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-fc2f1c8e1973820c
evidence:
- evidence_id: ev-6f9f5d1a9f9bcd42
  kind: record_content
  reference: data/ingredients/mapped/Folic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1015],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:27470","line":1017,"mapping_status":"MAPPED","ontology_id":"CHEBI:27470","preferred_term":"Folic
    acid"}],"identifier":"CHEBI:27470","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":2108,"edge_count":2108,"occurrences":2111},"occurrence_statistics":{"media_count":2108,"total_occurrences":2111},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:27470","ontology_label":"folic
    acid","ontology_source":"CHEBI"},"preferred_term":"Folic acid","sssom_rows":[{"data_row":1225,"object_id":"CHEBI:27470","object_label":"folic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Folic_Acid","synonym_count":24}'
  snapshot_sha256: df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615
- evidence_id: ev-5bb9616fc542b9dc
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1015]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-626cddc2f6661864
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Folic_Acid; data-row positions=[1225]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1225,"object_id":"CHEBI:27470","object_label":"folic
    acid","other":"Folate|(2S)-2-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzamido)pentanedioic
    acid|Acfol|Folicet|Folinic acid (citrovorum)|Folsaeure|N-(4-{[(2-amino-4-oxo-3,4-dihydropteridin-6-yl)methyl]amino}benzoyl)-L-glutamic
    acid|N-[(4-{[(2-amino-4-oxo-1,4-dihydropteridin-6-yl)methyl]amino}phenyl)carbonyl]-L-glutamic
    acid|N-pteroyl-L-glutamic acid|PGA|PteGlu|acide folique|acido folico|acidum folicum|pteroyl-L-glutamic
    acid|pteroyl-L-monoglutamic acid|pteroylglutamic acid|pteroylmonoglutamic acid|vitamin
    B11|vitamin B9|Folic acid (5 \u03bcg/\u03bcL)|CAS:59-30-3","predicate_id":"skos:exactMatch","subject_id":"MIM:Folic_Acid","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-d069c10d3a229267
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1017]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:27470","line":1017,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"2108","ontology_id":"CHEBI:27470","preferred_term":"Folic
    acid","total_occurrences":"2111"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-a034d48d5df9bcf8
  kind: prior_review
  reference: reports/yaml_record_review/Folic_Acid.md
  locator: '`data/ingredients/mapped/Folic_Acid.yaml`:2; Verdict:4; Identity:11; Validation:22;
    Evidence:32; Completeness:63; Recommended Edits:70'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 33ccd4e17e2fcdc426b7f73485dc43b5183d95fc0ed0a08234daf29872428e27
  quote: "Recommended Edits:\n- Major: remove or demote `Folinic acid (citrovorum)`\
    \ in\n  `data/ingredients/mapped/Folic_Acid.yaml`, sync\n  `data/curated/mapped_ingredients.yaml`,\
    \ regenerate\n  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation\
    \ plus\n  the final SSSOM invariant gates.\n- Major: move the concentration-bearing\
    \ CultureMech alias out of active\n  resolving synonyms so final SSSOM no longer\
    \ publishes it as `other`, then\n  rerun the SSSOM synonym gates.\n- Major: remove\
    \ the unrelated PMID `20415580` ontology-mapping evidence entry\n  unless a future\
    \ curator inspects the article and attaches it to a narrower\n  claim it actually\
    \ supports."
- evidence_id: ev-c1b66733be2277f3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[624]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615","finding_id":"SEM:d2370682344a15f3d338","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-bca93d99167a8708
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-fc2f1c8e1973820c
  evidence_ids:
  - ev-6f9f5d1a9f9bcd42
  - ev-5bb9616fc542b9dc
  - ev-626cddc2f6661864
  - ev-d069c10d3a229267
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-0cc726f6e4b8e4b6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fc2f1c8e1973820c
  evidence_ids:
  - ev-a034d48d5df9bcf8
  - ev-6f9f5d1a9f9bcd42
  - ev-c1b66733be2277f3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:52:12Z;
    reviewed SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615;
    current SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615;
    hash_changed=False. Reports=["reports/yaml_record_review/Folic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact folic
    acid identity passes, but one different folate and one concentration label leak
    into final SSSOM other.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-a034d48d5df9bcf8
    - ev-6f9f5d1a9f9bcd42
  - name: legacy-native-ids
    value: '["SEM:d2370682344a15f3d338"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-6f9f5d1a9f9bcd42
    - ev-a034d48d5df9bcf8
    - ev-c1b66733be2277f3
findings:
- finding_id: rec-f-530396e11116620e
  issue_key: mim-reconciliation-historical-review-coverage-and-r-fc2f1c8e1973820c
  category: provenance
  severity: major
  status: deferred
  certainty: provisional
  title: 'Historical review coverage and residual narrative: Folic_Acid'
  description: 'The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
    Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:52:12Z;
    reviewed SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615;
    current SHA-256=df85938271ec8f32a6d756f5213ba9661c9a7530822f333d2e02493b9f92e615;
    hash_changed=False. Reports=["reports/yaml_record_review/Folic_Acid.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact folic
    acid identity passes, but one different folate and one concentration label leak
    into final SSSOM other.'
  disposition_reason: The legacy concern set remains only partially reconciled. Specific
    dispositions below apply solely to their named subclaims; other identity, source,
    component, synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-fc2f1c8e1973820c
  evidence_ids:
  - ev-a034d48d5df9bcf8
  - ev-6f9f5d1a9f9bcd42
  - ev-c1b66733be2277f3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Folic_Acid.yaml
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
