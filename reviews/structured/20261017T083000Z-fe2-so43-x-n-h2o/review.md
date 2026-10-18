# Per-record structured review: Fe2_So43_X_N_H2o (data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml)

- Review: 20261017T083000Z-fe2-so43-x-n-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fe2_So43_X_N_H2o (data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml, record-0342a970229031a5, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-0342a970229031a5 | data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml | maintained | Fe2_So43_X_N_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-0342a970229031a5 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-0342a970229031a5 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-0342a970229031a5 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-0342a970229031a5.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-0342a970229031a5.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:08:06Z; reviewed SHA-256=5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447; current SHA-256=5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447; hash_changed=False. Reports=["reports/yaml_record_review/Fe2_So43_X_N_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The variable hydrate identity passes, but TRACE_ELEMENT is computational and a malformed hydrate surface still exports as a synonym.

### Historical provisional-role concern

evidence: concern. Targets: record-0342a970229031a5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-3c6f9ac33d890e2e: Reassess prediction-only role support: Fe2(SO4)3 x n H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-0342a970229031a5.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-3c6f9ac33d890e2e

Reassess prediction-only role support: Fe2(SO4)3 x n H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-b68f71699f11b322 | data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[976],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","line":978,"mapping_status":"MAPPED","ontology_id":"CHEBI:53438","preferred_term":"Fe2(SO4)3 x n H2O"}],"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":43,"edge_count":43,"occurrences":43},"occurrence_statistics":{"media_count":43,"total_occurrences":43},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:53438","ontology_label":"iron(3+) sulfate","ontology_source":"CHEBI"},"preferred_term":"Fe2(SO4)3 x n H2O","sssom_rows":[{"data_row":1166,"object_id":"CHEBI:53438","object_label":"iron(3+) sulfate","predicate_id":"skos:broadMatch"},{"data_row":1167,"object_id":"kgmicrobe.compound:fe2_so43_x_n_h2o","object_label":"Fe2(SO4)3 x n H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fe2_So43_X_N_H2o","synonym_count":1} |
| ev-f01c40cee56843f9 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [976] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-70d7bffa5e352c69 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fe2_So43_X_N_H2o; data-row positions=[1166, 1167] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1166,"object_id":"CHEBI:53438","object_label":"iron(3+) sulfate","other":"Fe(SO4)3 x n H2O","predicate_id":"skos:broadMatch","subject_id":"MIM:Fe2_So43_X_N_H2o","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":1167,"object_id":"kgmicrobe.compound:fe2_so43_x_n_h2o","object_label":"Fe2(SO4)3 x n H2O","other":"Fe(SO4)3 x n H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Fe2_So43_X_N_H2o","validation_method":""}] |
| ev-41e5d79b968d6e1f | docs/data/mapped_ingredients.csv; CSV lines=[978] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","line":978,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"43","ontology_id":"CHEBI:53438","preferred_term":"Fe2(SO4)3 x n H2O","total_occurrences":"43"}] |
| ev-b510d193b46de9a4 | reports/yaml_record_review/Fe2_So43_X_N_H2o.md; &#96;data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:31; Completeness:54; Recommended Edits:62 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-7faac96d48532f73 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[584,1876] | context_only | [{"current_record_sha256":"5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447","finding_id":"SEM:fc4b5653e0833949616a","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447","finding_id":"SEM:b219be966290c01a9537","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-a9792434ee2ca76a | data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml; nutritional_roles[0] | supports | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[976],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","line":978,"mapping_status":"MAPPED","ontology_id":"CHEBI:53438","preferred_term":"Fe2(SO4)3 x n H2O"}],"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":43,"edge_count":43,"occurrences":43},"occurrence_statistics":{"media_count":43,"total_occurrences":43},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:53438","ontology_label":"iron(3+) sulfate","ontology_source":"CHEBI"},"preferred_term":"Fe2(SO4)3 x n H2O","sssom_rows":[{"data_row":1166,"object_id":"CHEBI:53438","object_label":"iron(3+) sulfate","predicate_id":"skos:broadMatch"},{"data_row":1167,"object_id":"kgmicrobe.compound:fe2_so43_x_n_h2o","object_label":"Fe2(SO4)3 x n H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fe2_So43_X_N_H2o","synonym_count":1} |
| ev-81cf1cabc8171d72 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-3c6f9ac33d890e2e] | context_only | Predecessor structured review finding f-3c6f9ac33d890e2e in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fe2-so43-x-n-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fe2_So43_X_N_H2o (data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml)'
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
native_verdict: mapping_status=MAPPED; open=1; deferred=0
scientific_review: false
summary: Per-record structured review for Fe2_So43_X_N_H2o (data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml,
  record-0342a970229031a5, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
    sha256: 5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447
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
  - path: reports/yaml_record_review/Fe2_So43_X_N_H2o.md
    sha256: 24dd7f3cc8ad8e384371e104bbee4ffeecbb0a9d6270155285e1357b9ca1be0b
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-0342a970229031a5
  path: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
  label: Fe2_So43_X_N_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-0342a970229031a5
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b68f71699f11b322
  - ev-f01c40cee56843f9
  - ev-70d7bffa5e352c69
  - ev-41e5d79b968d6e1f
  - ev-a9792434ee2ca76a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b68f71699f11b322
  - ev-7faac96d48532f73
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b510d193b46de9a4
  - ev-7faac96d48532f73
  - ev-81cf1cabc8171d72
evidence:
- evidence_id: ev-b68f71699f11b322
  kind: record_content
  reference: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-17T08:30:00Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[976],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","line":978,"mapping_status":"MAPPED","ontology_id":"CHEBI:53438","preferred_term":"Fe2(SO4)3
    x n H2O"}],"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":43,"edge_count":43,"occurrences":43},"occurrence_statistics":{"media_count":43,"total_occurrences":43},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:53438","ontology_label":"iron(3+)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Fe2(SO4)3 x n H2O","sssom_rows":[{"data_row":1166,"object_id":"CHEBI:53438","object_label":"iron(3+)
    sulfate","predicate_id":"skos:broadMatch"},{"data_row":1167,"object_id":"kgmicrobe.compound:fe2_so43_x_n_h2o","object_label":"Fe2(SO4)3
    x n H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fe2_So43_X_N_H2o","synonym_count":1}'
  snapshot_sha256: 5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447
- evidence_id: ev-f01c40cee56843f9
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [976]'
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-70d7bffa5e352c69
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fe2_So43_X_N_H2o; data-row positions=[1166, 1167]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1166,"object_id":"CHEBI:53438","object_label":"iron(3+)
    sulfate","other":"Fe(SO4)3 x n H2O","predicate_id":"skos:broadMatch","subject_id":"MIM:Fe2_So43_X_N_H2o","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":1167,"object_id":"kgmicrobe.compound:fe2_so43_x_n_h2o","object_label":"Fe2(SO4)3
    x n H2O","other":"Fe(SO4)3 x n H2O","predicate_id":"skos:exactMatch","subject_id":"MIM:Fe2_So43_X_N_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-41e5d79b968d6e1f
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[978]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","line":978,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"43","ontology_id":"CHEBI:53438","preferred_term":"Fe2(SO4)3
    x n H2O","total_occurrences":"43"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-b510d193b46de9a4
  kind: prior_review
  reference: reports/yaml_record_review/Fe2_So43_X_N_H2o.md
  locator: '`data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:31; Completeness:54; Recommended Edits:62'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 24dd7f3cc8ad8e384371e104bbee4ffeecbb0a9d6270155285e1357b9ca1be0b
  quote: "Recommended Edits:\n- Major: remove `Fe(SO4)3 x n H2O` from the active synonym\
    \ set or exclude it\n  from final SSSOM `other` export, unless source review proves\
    \ it is a real\n  synonym rather than a malformed formula.\n- Major: either replace\
    \ the provisional `TRACE_ELEMENT` inference with\n  source-backed evidence or\
    \ remove the role facet.\n- Sync `data/curated/mapped_ingredients.yaml`, regenerate\n\
    \  `mappings/ingredient_mappings.sssom.tsv`, and rerun strict validation plus\n\
    \  the final SSSOM invariant gates."
- evidence_id: ev-7faac96d48532f73
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[584,1876]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: '[{"current_record_sha256":"5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447","finding_id":"SEM:fc4b5653e0833949616a","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447","finding_id":"SEM:b219be966290c01a9537","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-a9792434ee2ca76a
  kind: record_content
  reference: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: supports
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[976],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","line":978,"mapping_status":"MAPPED","ontology_id":"CHEBI:53438","preferred_term":"Fe2(SO4)3
    x n H2O"}],"identifier":"kgmicrobe.compound:fe2_so43_x_n_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":43,"edge_count":43,"occurrences":43},"occurrence_statistics":{"media_count":43,"total_occurrences":43},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:53438","ontology_label":"iron(3+)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Fe2(SO4)3 x n H2O","sssom_rows":[{"data_row":1166,"object_id":"CHEBI:53438","object_label":"iron(3+)
    sulfate","predicate_id":"skos:broadMatch"},{"data_row":1167,"object_id":"kgmicrobe.compound:fe2_so43_x_n_h2o","object_label":"Fe2(SO4)3
    x n H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fe2_So43_X_N_H2o","synonym_count":1}'
  snapshot_sha256: 5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447
- evidence_id: ev-81cf1cabc8171d72
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-3c6f9ac33d890e2e]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-3c6f9ac33d890e2e in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-f2a7ad669507499a
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b68f71699f11b322
  - ev-f01c40cee56843f9
  - ev-70d7bffa5e352c69
  - ev-41e5d79b968d6e1f
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-c21a64d11e795ca0
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b510d193b46de9a4
  - ev-b68f71699f11b322
  - ev-7faac96d48532f73
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:08:06Z;
    reviewed SHA-256=5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447;
    current SHA-256=5b98fed8eddbde07bfd8e8e4dd9263cd56d7ecb494691d4d5f55fedd3a405447;
    hash_changed=False. Reports=["reports/yaml_record_review/Fe2_So43_X_N_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The variable
    hydrate identity passes, but TRACE_ELEMENT is computational and a malformed hydrate
    surface still exports as a synonym.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b510d193b46de9a4
    - ev-b68f71699f11b322
  - name: legacy-native-ids
    value: '["SEM:fc4b5653e0833949616a","SEM:b219be966290c01a9537"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-b68f71699f11b322
    - ev-b510d193b46de9a4
    - ev-7faac96d48532f73
- assessment_id: a-a9792434ee2ca76a
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b510d193b46de9a4
  - ev-a9792434ee2ca76a
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-b510d193b46de9a4
    - ev-a9792434ee2ca76a
findings:
- finding_id: rec-f-3c6f9ac33d890e2e
  issue_key: mim-reconciliation-role-support-0342a970229031a5
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Fe2(SO4)3 x n H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-0342a970229031a5
  evidence_ids:
  - ev-b510d193b46de9a4
  - ev-a9792434ee2ca76a
  - ev-81cf1cabc8171d72
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[0]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024634Z-mim-reconcile-all-batch-06
    finding_id: f-3c6f9ac33d890e2e
actions:
- action_id: rec-action-3c6f9ac33d890e2e
  description: 'Reassess prediction-only role support: Fe2(SO4)3 x n H2O'
  finding_ids:
  - rec-f-3c6f9ac33d890e2e
  target_ids:
  - record-0342a970229031a5
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fe2_So43_X_N_H2o.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact fields/tokens and evidence gap described in this finding; preserve
    unrelated source labels and audit history.
  - Inspect the original preparation, organism, or mapping evidence where needed;
    do not promote a label/name-pattern inference to proof.
  - For an authorized fix, synchronize maintained surfaces, run focused validation,
    and save an evidence-backed successor citing this finding.
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
