# Per-record structured review: Caso4_X_2_H2o (data/ingredients/mapped/Caso4_X_2_H2o.yaml)

- Review: 20261017T083000Z-caso4-x-2-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Caso4_X_2_H2o (data/ingredients/mapped/Caso4_X_2_H2o.yaml, record-82e48b7fb01661f9, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Caso4_X_2_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Caso4_X_2_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-82e48b7fb01661f9 | data/ingredients/mapped/Caso4_X_2_H2o.yaml | maintained | Caso4_X_2_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-82e48b7fb01661f9 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-82e48b7fb01661f9 | Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-82e48b7fb01661f9 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-82e48b7fb01661f9.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-82e48b7fb01661f9.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:13:09Z; reviewed SHA-256=4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977; current SHA-256=4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977; hash_changed=False. Reports=["reports/yaml_record_review/Caso4_X_2_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI calcium sulfate dihydrate identity passes, but MINERAL_SOURCE has an empty evidence list.

### Historical provisional-role concern

evidence: concern. Targets: record-82e48b7fb01661f9.

Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION or empty evidence lists and require source-backed curation support.

## Findings

### rec-f-role-82e48b7fb01661f9: Reassess prediction-only or empty role support: Caso4_X_2_H2o

major / open / confirmed; issue key: mim-reconciliation-role-support-82e48b7fb01661f9.

Prediction-only or empty evidence payloads remain on the named current role assertions (nutritional_roles[1]). This confirms the local evidence gap, not that the biological role is false.

## Recommended Actions And Acceptance Checks

### rec-act-role-82e48b7fb01661f9

Reassess prediction-only or empty role support: Caso4_X_2_H2o

- Address the exact role fields and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-cda75278b54727dc | data/ingredients/mapped/Caso4_X_2_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[667],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32583","line":669,"mapping_status":"MAPPED","ontology_id":"CHEBI:32583","preferred_term":"CaSO4 x 2 H2O"}],"identifier":"CHEBI:32583","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":158,"edge_count":158,"occurrences":158},"occurrence_statistics":{"media_count":158,"total_occurrences":158},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32583","ontology_label":"calcium sulfate dihydrate","ontology_source":"CHEBI"},"preferred_term":"CaSO4 x 2 H2O","sssom_rows":[{"data_row":665,"object_id":"CHEBI:32583","object_label":"calcium sulfate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caso4_X_2_H2o","synonym_count":40} |
| ev-70d48337b1edc4e2 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [667] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-226fc77a4c08c65e | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Caso4_X_2_H2o; data-row positions=[665] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":665,"object_id":"CHEBI:32583","object_label":"calcium sulfate dihydrate","other":"CaSO4 . 2H2O&#124;CaSO4 x 2H2O&#124;CaSO4 x2H2O&#124;CaSO4 \u00b7 2 H2O&#124;CaSO4 \u00b7 2H2O&#124;CaSO4.2H2O&#124;CaSO4\u00b72H2O&#124;CaSO4\u30fb2H2O&#124;calcium(II) sulfate, dihydrate (1:1:2)&#124;sulfuric acid, calcium salt (1:1), dihydrate&#124;sulfuric acid, calcium(2+) salt, dihydrate&#124;CaSO4\u20222H2O&#124;CaSO4\u20222H2O(Mallinckroft 4300)&#124;calcium sulfate--water (1/2)&#124;CAS:10101-41-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Caso4_X_2_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-5cfd01ca5911a1fd | docs/data/mapped_ingredients.csv; CSV lines=[669] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:32583","line":669,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"158","ontology_id":"CHEBI:32583","preferred_term":"CaSO4 x 2 H2O","total_occurrences":"158"}] |
| ev-6742f827be299930 | reports/yaml_record_review/Caso4_X_2_H2o.md; &#96;data/ingredients/mapped/Caso4_X_2_H2o.yaml&#96;:2; Verdict:4; Identity:10; Validation:26; Evidence:41; Completeness:55; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-2c57c7923b9899d5 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[372,1793] | context_only | [{"current_record_sha256":"4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977","finding_id":"SEM:1905268196be592526b7","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977","finding_id":"SEM:a0838203ea18770fa603","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-42ab2d816d8816d8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; current_record=data/ingredients/mapped/Caso4_X_2_H2o.yaml | context_only | Semantic review finding dispositions ledger |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-caso4-x-2-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Caso4_X_2_H2o (data/ingredients/mapped/Caso4_X_2_H2o.yaml)'
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
summary: Per-record structured review for Caso4_X_2_H2o (data/ingredients/mapped/Caso4_X_2_H2o.yaml,
  record-82e48b7fb01661f9, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Caso4_X_2_H2o.yaml
    sha256: 4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977
    role: target
  - path: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
    sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
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
  - path: reports/yaml_record_review/Caso4_X_2_H2o.md
    sha256: 8679833cd603764285591238873dc9316bac9ae2e4695125d132db14606d9214
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-82e48b7fb01661f9
  path: data/ingredients/mapped/Caso4_X_2_H2o.yaml
  label: Caso4_X_2_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caso4_X_2_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Caso4_X_2_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Caso4_X_2_H2o.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-82e48b7fb01661f9
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-82e48b7fb01661f9
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-82e48b7fb01661f9
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-82e48b7fb01661f9
evidence:
- evidence_id: ev-cda75278b54727dc
  kind: record_content
  reference: data/ingredients/mapped/Caso4_X_2_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[667],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:32583","line":669,"mapping_status":"MAPPED","ontology_id":"CHEBI:32583","preferred_term":"CaSO4
    x 2 H2O"}],"identifier":"CHEBI:32583","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":158,"edge_count":158,"occurrences":158},"occurrence_statistics":{"media_count":158,"total_occurrences":158},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:32583","ontology_label":"calcium
    sulfate dihydrate","ontology_source":"CHEBI"},"preferred_term":"CaSO4 x 2 H2O","sssom_rows":[{"data_row":665,"object_id":"CHEBI:32583","object_label":"calcium
    sulfate dihydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Caso4_X_2_H2o","synonym_count":40}'
  snapshot_sha256: 4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977
- evidence_id: ev-70d48337b1edc4e2
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [667]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-226fc77a4c08c65e
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Caso4_X_2_H2o; data-row positions=[665]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":665,"object_id":"CHEBI:32583","object_label":"calcium
    sulfate dihydrate","other":"CaSO4 . 2H2O|CaSO4 x 2H2O|CaSO4 x2H2O|CaSO4 \u00b7
    2 H2O|CaSO4 \u00b7 2H2O|CaSO4.2H2O|CaSO4\u00b72H2O|CaSO4\u30fb2H2O|calcium(II)
    sulfate, dihydrate (1:1:2)|sulfuric acid, calcium salt (1:1), dihydrate|sulfuric
    acid, calcium(2+) salt, dihydrate|CaSO4\u20222H2O|CaSO4\u20222H2O(Mallinckroft
    4300)|calcium sulfate--water (1/2)|CAS:10101-41-4","predicate_id":"skos:exactMatch","subject_id":"MIM:Caso4_X_2_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-5cfd01ca5911a1fd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[669]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:32583","line":669,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"158","ontology_id":"CHEBI:32583","preferred_term":"CaSO4
    x 2 H2O","total_occurrences":"158"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-6742f827be299930
  kind: prior_review
  reference: reports/yaml_record_review/Caso4_X_2_H2o.md
  locator: '`data/ingredients/mapped/Caso4_X_2_H2o.yaml`:2; Verdict:4; Identity:10;
    Validation:26; Evidence:41; Completeness:55; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8679833cd603764285591238873dc9316bac9ae2e4695125d132db14606d9214
  quote: "Recommended Edits:\n- Major: add inspected evidence to\n  `nutritional_roles.MINERAL_SOURCE`\
    \ in\n  `data/ingredients/mapped/Caso4_X_2_H2o.yaml`, or remove the role if the\n\
    \  bulk-cation assertion is not supported for calcium sulfate dihydrate, then\n\
    \  rerun strict validation, SSSOM QC, aggregate roundtrip, and\n  `git diff --check`."
- evidence_id: ev-2c57c7923b9899d5
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[372,1793]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977","finding_id":"SEM:1905268196be592526b7","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977","finding_id":"SEM:a0838203ea18770fa603","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-42ab2d816d8816d8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: current_record=data/ingredients/mapped/Caso4_X_2_H2o.yaml
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Semantic review finding dispositions ledger
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
assessments:
- assessment_id: a-573f294aa1c85033
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-82e48b7fb01661f9
  evidence_ids:
  - ev-cda75278b54727dc
  - ev-70d48337b1edc4e2
  - ev-226fc77a4c08c65e
  - ev-5cfd01ca5911a1fd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-aa798afd64f28e3c
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-82e48b7fb01661f9
  evidence_ids:
  - ev-6742f827be299930
  - ev-cda75278b54727dc
  - ev-2c57c7923b9899d5
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:13:09Z;
    reviewed SHA-256=4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977;
    current SHA-256=4cc423aef35c4897c90464aeef3d58467556ca3b12ffa25b70a57817581c6977;
    hash_changed=False. Reports=["reports/yaml_record_review/Caso4_X_2_H2o.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    calcium sulfate dihydrate identity passes, but MINERAL_SOURCE has an empty evidence
    list.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-6742f827be299930
    - ev-cda75278b54727dc
  - name: legacy-native-ids
    value: '["SEM:1905268196be592526b7","SEM:a0838203ea18770fa603"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-cda75278b54727dc
    - ev-6742f827be299930
    - ev-2c57c7923b9899d5
- assessment_id: a-role-82e48b7fb01661f9
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Current role assertions on nutritional_roles[1] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence lists and require source-backed curation support.
  target_ids:
  - record-82e48b7fb01661f9
  evidence_ids:
  - ev-cda75278b54727dc
  - ev-42ab2d816d8816d8
  dimensions:
  - name: legacy-disposition
    value: still_present
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-cda75278b54727dc
    - ev-42ab2d816d8816d8
findings:
- finding_id: rec-f-role-82e48b7fb01661f9
  issue_key: mim-reconciliation-role-support-82e48b7fb01661f9
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only or empty role support: Caso4_X_2_H2o'
  description: Prediction-only or empty evidence payloads remain on the named current
    role assertions (nutritional_roles[1]). This confirms the local evidence gap,
    not that the biological role is false.
  target_ids:
  - record-82e48b7fb01661f9
  evidence_ids:
  - ev-cda75278b54727dc
  - ev-42ab2d816d8816d8
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caso4_X_2_H2o.yaml
    role: maintained ingredient
  field_paths:
  - nutritional_roles[1]
  tags:
  - reconciliation
  - bundle-by-owner
  - role-support
  external_issues:
  - https://github.com/CultureBotAI/MediaIngredientMech/issues/718
actions:
- action_id: rec-act-role-82e48b7fb01661f9
  description: 'Reassess prediction-only or empty role support: Caso4_X_2_H2o'
  finding_ids:
  - rec-f-role-82e48b7fb01661f9
  target_ids:
  - record-82e48b7fb01661f9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Caso4_X_2_H2o.yaml
    role: maintained ingredient
  acceptance_checks:
  - Address the exact role fields and evidence gap described in this finding; preserve
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
