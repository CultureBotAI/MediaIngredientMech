# Per-record structured review: Maltose (data/ingredients/mapped/Maltose.yaml)

- Review: 20261017T083000Z-maltose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Maltose (data/ingredients/mapped/Maltose.yaml, record-e30fba07cf1daca8, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Maltose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Maltose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-e30fba07cf1daca8 | data/ingredients/mapped/Maltose.yaml | maintained | Maltose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-e30fba07cf1daca8 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-e30fba07cf1daca8 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-e30fba07cf1daca8 | Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-e30fba07cf1daca8.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-e30fba07cf1daca8.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:27:59Z; reviewed SHA-256=d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1; current SHA-256=d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1; hash_changed=False. Reports=["reports/yaml_record_review/Maltose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The maltose identity, CAS, structure, and CultureMech CARBON_SOURCE pass, but final SSSOM still exports hydrate/alpha-anomer labels and ENERGY_SOURCE is provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-e30fba07cf1daca8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-701533d59dabe2ee: Reassess prediction-only role support: Maltose

major / open / confirmed; issue key: mim-reconciliation-role-support-e30fba07cf1daca8.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-701533d59dabe2ee

Reassess prediction-only role support: Maltose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-7c26321955c8340b | data/ingredients/mapped/Maltose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1341],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17306","line":1343,"mapping_status":"MAPPED","ontology_id":"CHEBI:17306","preferred_term":"Maltose"}],"identifier":"CHEBI:17306","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":188,"edge_count":188,"occurrences":189},"occurrence_statistics":{"media_count":188,"total_occurrences":189},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17306","ontology_label":"maltose","ontology_source":"CHEBI"},"preferred_term":"Maltose","sssom_rows":[{"data_row":1768,"object_id":"CHEBI:17306","object_label":"maltose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltose","synonym_count":26} |
| ev-dfa2fc3354479067 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [1341] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-701c724d7f3dc06c | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Maltose; data-row positions=[1768] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1768,"object_id":"CHEBI:17306","object_label":"maltose","other":"Maltose Hydrate&#124;1-alpha-D-Glucopyranosyl-4-alpha-D-glucopyranose&#124;4-(alpha-D-glucosido)-D-glucose&#124;4-O-alpha-D-glucopyranosyl-D-glucopyranose&#124;4-O-alpha-D-glucopyranosyl-alpha-D-glucopyranose&#124;Cextromaltose&#124;D-(+)-maltose&#124;D-maltose (maltose)&#124;Glca1-4Glca&#124;Glcalpha1-4Glca&#124;Glcalpha1-4Glcalpha&#124;Malt sugar&#124;Malzzucker&#124;alpha-D-Glcp-(1-&gt;4)-D-Glcp&#124;alpha-D-Glcp-(1-&gt;4)-alpha-D-Glcp&#124;alpha-D-Glucopyranosyl-(1-&gt;4)-D-glucopyranose&#124;alpha-D-glucopyranosyl-(1-&gt;4)-D-glucose&#124;D-Maltose&#124;Alpha-maltose&#124;alpha-D-glucopyranosyl-(1-&gt;4)-alpha-D-glucopyranose&#124;CAS:69-79-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Maltose","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-03a5089c7a0c9ed7 | docs/data/mapped_ingredients.csv; CSV lines=[1343] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:17306","line":1343,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"188","ontology_id":"CHEBI:17306","preferred_term":"Maltose","total_occurrences":"189"}] |
| ev-40a6d9c805e6d81f | reports/yaml_record_review/Maltose.md; &#96;data/ingredients/mapped/Maltose.yaml&#96;:2; Verdict:4; Identity:13; Validation:24; Evidence:31; Completeness:43; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-c2fb77335ce2d3af | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[895,1559] | context_only | [{"current_record_sha256":"d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1","finding_id":"SEM:53f11e1a1286fd6915f9","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1","finding_id":"SEM:5325840279eaa1487ee0","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-54a50e1ceec3f707 | data/ingredients/mapped/Maltose.yaml; nutritional_roles[1] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}] |
| ev-6dd9b92957db5a37 | reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml; findings[finding_id=f-701533d59dabe2ee] | context_only | Predecessor structured review finding f-701533d59dabe2ee in 20261011T024636Z-mim-reconcile-all-batch-08 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-maltose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Maltose (data/ingredients/mapped/Maltose.yaml)'
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
summary: Per-record structured review for Maltose (data/ingredients/mapped/Maltose.yaml,
  record-e30fba07cf1daca8, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Maltose.yaml
    sha256: d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1
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
  - path: reports/yaml_record_review/Maltose.md
    sha256: 2500cc5d76c05eec576707e0bcf369fefabb268132edde2eeca1751083729541
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-e30fba07cf1daca8
  path: data/ingredients/mapped/Maltose.yaml
  label: Maltose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Maltose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Maltose.yaml selected from full-corpus
    review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-e30fba07cf1daca8
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-e30fba07cf1daca8
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-e30fba07cf1daca8
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024636Z-mim-reconcile-all-batch-08
    and semantic review dispositions on HEAD.
  target_ids:
  - record-e30fba07cf1daca8
evidence:
- evidence_id: ev-7c26321955c8340b
  kind: record_content
  reference: data/ingredients/mapped/Maltose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[1341],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:17306","line":1343,"mapping_status":"MAPPED","ontology_id":"CHEBI:17306","preferred_term":"Maltose"}],"identifier":"CHEBI:17306","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":188,"edge_count":188,"occurrences":189},"occurrence_statistics":{"media_count":188,"total_occurrences":189},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:17306","ontology_label":"maltose","ontology_source":"CHEBI"},"preferred_term":"Maltose","sssom_rows":[{"data_row":1768,"object_id":"CHEBI:17306","object_label":"maltose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Maltose","synonym_count":26}'
  snapshot_sha256: d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1
- evidence_id: ev-dfa2fc3354479067
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [1341]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-701c724d7f3dc06c
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Maltose; data-row positions=[1768]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1768,"object_id":"CHEBI:17306","object_label":"maltose","other":"Maltose
    Hydrate|1-alpha-D-Glucopyranosyl-4-alpha-D-glucopyranose|4-(alpha-D-glucosido)-D-glucose|4-O-alpha-D-glucopyranosyl-D-glucopyranose|4-O-alpha-D-glucopyranosyl-alpha-D-glucopyranose|Cextromaltose|D-(+)-maltose|D-maltose
    (maltose)|Glca1-4Glca|Glcalpha1-4Glca|Glcalpha1-4Glcalpha|Malt sugar|Malzzucker|alpha-D-Glcp-(1->4)-D-Glcp|alpha-D-Glcp-(1->4)-alpha-D-Glcp|alpha-D-Glucopyranosyl-(1->4)-D-glucopyranose|alpha-D-glucopyranosyl-(1->4)-D-glucose|D-Maltose|Alpha-maltose|alpha-D-glucopyranosyl-(1->4)-alpha-D-glucopyranose|CAS:69-79-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Maltose","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-03a5089c7a0c9ed7
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[1343]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:17306","line":1343,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"188","ontology_id":"CHEBI:17306","preferred_term":"Maltose","total_occurrences":"189"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-40a6d9c805e6d81f
  kind: prior_review
  reference: reports/yaml_record_review/Maltose.md
  locator: '`data/ingredients/mapped/Maltose.yaml`:2; Verdict:4; Identity:13; Validation:24;
    Evidence:31; Completeness:43; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 2500cc5d76c05eec576707e0bcf369fefabb268132edde2eeca1751083729541
  quote: "Recommended Edits:\n- Reject or relocate the hydrate and alpha-anomer surface\
    \ forms so final SSSOM\n  only emits exact synonyms of anomer-agnostic maltose.\n\
    - Remove `ENERGY_SOURCE` unless source-backed evidence can be attached."
- evidence_id: ev-c2fb77335ce2d3af
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[895,1559]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1","finding_id":"SEM:53f11e1a1286fd6915f9","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1","finding_id":"SEM:5325840279eaa1487ee0","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-54a50e1ceec3f707
  kind: record_content
  reference: data/ingredients/mapped/Maltose.yaml
  locator: nutritional_roles[1]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[1]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    ENERGY_SOURCE added alongside CARBON_SOURCE; review recommended.","reference_text":"Canonical
    energy substrate (catabolised for energy)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"ENERGY_SOURCE"}}]'
  snapshot_sha256: d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1
- evidence_id: ev-6dd9b92957db5a37
  kind: prior_review
  reference: reviews/structured/20261011T024636Z-mim-reconcile-all-batch-08/review.yaml
  locator: findings[finding_id=f-701533d59dabe2ee]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-701533d59dabe2ee in 20261011T024636Z-mim-reconcile-all-batch-08
  snapshot_sha256: 4dd969b7020555cc2250a236d6fded134bedf3add1e1c5c72d269e98f9ae001b
assessments:
- assessment_id: a-7635deedd297f53f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-e30fba07cf1daca8
  evidence_ids:
  - ev-7c26321955c8340b
  - ev-dfa2fc3354479067
  - ev-701c724d7f3dc06c
  - ev-03a5089c7a0c9ed7
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-6adef4c0b6c3d927
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-e30fba07cf1daca8
  evidence_ids:
  - ev-40a6d9c805e6d81f
  - ev-7c26321955c8340b
  - ev-c2fb77335ce2d3af
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T01:27:59Z;
    reviewed SHA-256=d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1;
    current SHA-256=d57baa8b44a5e79c14f2f31e9571a9d51fda170e95dce58ab46d1e0114b783d1;
    hash_changed=False. Reports=["reports/yaml_record_review/Maltose.md"]. Full reports,
    including older originals behind refresh floors, are hashed inputs. Repeated refresh
    allegations are not counted as new defects. The narrative group is not a count
    of distinct scientific findings. Latest manifest note: The maltose identity, CAS,
    structure, and CultureMech CARBON_SOURCE pass, but final SSSOM still exports hydrate/alpha-anomer
    labels and ENERGY_SOURCE is provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-40a6d9c805e6d81f
    - ev-7c26321955c8340b
  - name: legacy-native-ids
    value: '["SEM:53f11e1a1286fd6915f9","SEM:5325840279eaa1487ee0"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-7c26321955c8340b
    - ev-40a6d9c805e6d81f
    - ev-c2fb77335ce2d3af
- assessment_id: a-54a50e1ceec3f707
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e30fba07cf1daca8
  evidence_ids:
  - ev-40a6d9c805e6d81f
  - ev-54a50e1ceec3f707
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-40a6d9c805e6d81f
    - ev-54a50e1ceec3f707
findings:
- finding_id: rec-f-701533d59dabe2ee
  issue_key: mim-reconciliation-role-support-e30fba07cf1daca8
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Maltose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-e30fba07cf1daca8
  evidence_ids:
  - ev-40a6d9c805e6d81f
  - ev-54a50e1ceec3f707
  - ev-6dd9b92957db5a37
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltose.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
  previous_occurrences:
  - repository: CultureBotAI/MediaIngredientMech
    review_id: 20261011T024636Z-mim-reconcile-all-batch-08
    finding_id: f-701533d59dabe2ee
actions:
- action_id: rec-action-701533d59dabe2ee
  description: 'Reassess prediction-only role support: Maltose'
  finding_ids:
  - rec-f-701533d59dabe2ee
  target_ids:
  - record-e30fba07cf1daca8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Maltose.yaml
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
  with lineage to 20261011T024636Z-mim-reconcile-all-batch-08.
```
