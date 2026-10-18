# Per-record structured review: Fe_Nh42_So42_X_7_H2o (data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml)

- Review: 20261017T083000Z-fe-nh42-so42-x-7-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Fe_Nh42_So42_X_7_H2o (data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml, record-efa8f3ce848e6134, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-efa8f3ce848e6134 | data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml | maintained | Fe_Nh42_So42_X_7_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-efa8f3ce848e6134 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-efa8f3ce848e6134 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-efa8f3ce848e6134 | Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-efa8f3ce848e6134.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-efa8f3ce848e6134.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:10:53Z; reviewed SHA-256=2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47; current SHA-256=2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47; hash_changed=False. Reports=["reports/yaml_record_review/Fe_Nh42_So42_X_7_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact heptahydrate identity and final SSSOM row pass, but TRACE_ELEMENT is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-efa8f3ce848e6134.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-0a507e686eb653f1: Reassess prediction-only role support: Fe(NH4)2(SO4)2 x 7 H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-efa8f3ce848e6134.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-0a507e686eb653f1

Reassess prediction-only role support: Fe(NH4)2(SO4)2 x 7 H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-74f2da9e4b43fa45 | data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[982],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131378","line":984,"mapping_status":"MAPPED","ontology_id":"CHEBI:131378","preferred_term":"Fe(NH4)2(SO4)2 x 7 H2O"}],"identifier":"CHEBI:131378","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":34,"edge_count":34,"occurrences":34},"occurrence_statistics":{"media_count":34,"total_occurrences":34},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131378","ontology_label":"ferrous ammonium sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"Fe(NH4)2(SO4)2 x 7 H2O","sssom_rows":[{"data_row":1173,"object_id":"CHEBI:131378","object_label":"ferrous ammonium sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fe_Nh42_So42_X_7_H2o","synonym_count":6} |
| ev-7b0502ac265239c4 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [982] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-0cbc6992d35a550b | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Fe_Nh42_So42_X_7_H2o; data-row positions=[1173] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1173,"object_id":"CHEBI:131378","object_label":"ferrous ammonium sulfate heptahydrate","other":"Fe(NH4)2(SO4)2 . 7H2O&#124;Fe(NH4)2(SO4)2 x 7H2O&#124;Fe(NH4)2(SO4)2x7H2O&#124;Fe(NH4)2(SO4)2\u00b77H2O&#124;ammonium iron(II) sulfate heptahydrate","predicate_id":"skos:exactMatch","subject_id":"MIM:Fe_Nh42_So42_X_7_H2o","validation_method":"OAK+OLS:chebi&#124;SYNONYM_ENRICH&#124;2026-07-07"}] |
| ev-9f10b7b96bad56e3 | docs/data/mapped_ingredients.csv; CSV lines=[984] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:131378","line":984,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"34","ontology_id":"CHEBI:131378","preferred_term":"Fe(NH4)2(SO4)2 x 7 H2O","total_occurrences":"34"}] |
| ev-4cb2fb1ee7a02d28 | reports/yaml_record_review/Fe_Nh42_So42_X_7_H2o.md; &#96;data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml&#96;:2; Verdict:4; Identity:11; Validation:22; Evidence:29; Completeness:50; Recommended Edits:57 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-afd54377fca0bb61 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[589,1518] | context_only | [{"current_record_sha256":"2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47","finding_id":"SEM:5e5d1e0aa9a20652a72b","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47","finding_id":"SEM:a5ccd4b621cdf8846abf","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-f6907f71ec66b4c1 | data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-c6ffbd3d08623d97 | reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml; findings[finding_id=f-0a507e686eb653f1] | context_only | Predecessor structured review finding f-0a507e686eb653f1 in 20261011T024634Z-mim-reconcile-all-batch-06 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024634Z-mim-reconcile-all-batch-06.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-fe-nh42-so42-x-7-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Fe_Nh42_So42_X_7_H2o (data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml)'
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
summary: Per-record structured review for Fe_Nh42_So42_X_7_H2o (data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml,
  record-efa8f3ce848e6134, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
    sha256: 2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47
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
  - path: reports/yaml_record_review/Fe_Nh42_So42_X_7_H2o.md
    sha256: 8486f67f9122835c97ab60281de548c2c01cc667c92792f5cde08d35fb9768df
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-efa8f3ce848e6134
  path: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
  label: Fe_Nh42_So42_X_7_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-efa8f3ce848e6134
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-efa8f3ce848e6134
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-efa8f3ce848e6134
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024634Z-mim-reconcile-all-batch-06
    and semantic review dispositions on HEAD.
  target_ids:
  - record-efa8f3ce848e6134
evidence:
- evidence_id: ev-74f2da9e4b43fa45
  kind: record_content
  reference: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[982],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:131378","line":984,"mapping_status":"MAPPED","ontology_id":"CHEBI:131378","preferred_term":"Fe(NH4)2(SO4)2
    x 7 H2O"}],"identifier":"CHEBI:131378","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":34,"edge_count":34,"occurrences":34},"occurrence_statistics":{"media_count":34,"total_occurrences":34},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:131378","ontology_label":"ferrous
    ammonium sulfate heptahydrate","ontology_source":"CHEBI"},"preferred_term":"Fe(NH4)2(SO4)2
    x 7 H2O","sssom_rows":[{"data_row":1173,"object_id":"CHEBI:131378","object_label":"ferrous
    ammonium sulfate heptahydrate","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Fe_Nh42_So42_X_7_H2o","synonym_count":6}'
  snapshot_sha256: 2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47
- evidence_id: ev-7b0502ac265239c4
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [982]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-0cbc6992d35a550b
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Fe_Nh42_So42_X_7_H2o; data-row positions=[1173]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1173,"object_id":"CHEBI:131378","object_label":"ferrous
    ammonium sulfate heptahydrate","other":"Fe(NH4)2(SO4)2 . 7H2O|Fe(NH4)2(SO4)2 x
    7H2O|Fe(NH4)2(SO4)2x7H2O|Fe(NH4)2(SO4)2\u00b77H2O|ammonium iron(II) sulfate heptahydrate","predicate_id":"skos:exactMatch","subject_id":"MIM:Fe_Nh42_So42_X_7_H2o","validation_method":"OAK+OLS:chebi|SYNONYM_ENRICH|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-9f10b7b96bad56e3
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[984]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:131378","line":984,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"34","ontology_id":"CHEBI:131378","preferred_term":"Fe(NH4)2(SO4)2
    x 7 H2O","total_occurrences":"34"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-4cb2fb1ee7a02d28
  kind: prior_review
  reference: reports/yaml_record_review/Fe_Nh42_So42_X_7_H2o.md
  locator: '`data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml`:2; Verdict:4; Identity:11;
    Validation:22; Evidence:29; Completeness:50; Recommended Edits:57'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 8486f67f9122835c97ab60281de548c2c01cc667c92792f5cde08d35fb9768df
  quote: "Recommended Edits:\n- Major: either replace the provisional `TRACE_ELEMENT`\
    \ inference with\n  source-backed evidence or remove the role facet.\n- Minor:\
    \ attach primary source evidence for the exact heptahydrate phase if\n  it is\
    \ available from the 34 CultureMech occurrences.\n- Sync `data/curated/mapped_ingredients.yaml`,\
    \ regenerate downstream artifacts\n  if the role changes, and rerun strict validation."
- evidence_id: ev-afd54377fca0bb61
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[589,1518]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47","finding_id":"SEM:5e5d1e0aa9a20652a72b","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47","finding_id":"SEM:a5ccd4b621cdf8846abf","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-f6907f71ec66b4c1
  kind: record_content
  reference: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47
- evidence_id: ev-c6ffbd3d08623d97
  kind: prior_review
  reference: reviews/structured/20261011T024634Z-mim-reconcile-all-batch-06/review.yaml
  locator: findings[finding_id=f-0a507e686eb653f1]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-0a507e686eb653f1 in 20261011T024634Z-mim-reconcile-all-batch-06
  snapshot_sha256: 14c3200be95fdc87fca16bb71628432f3c9aaf8a65356ed494efc776ebe8aa11
assessments:
- assessment_id: a-e7de2752782bbb36
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-efa8f3ce848e6134
  evidence_ids:
  - ev-74f2da9e4b43fa45
  - ev-7b0502ac265239c4
  - ev-0cbc6992d35a550b
  - ev-9f10b7b96bad56e3
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ee0bc5254406b2db
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-efa8f3ce848e6134
  evidence_ids:
  - ev-4cb2fb1ee7a02d28
  - ev-74f2da9e4b43fa45
  - ev-afd54377fca0bb61
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T16:10:53Z;
    reviewed SHA-256=2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47;
    current SHA-256=2b8903a5c84016c972e3aae7778a54f6226f46a03ebbcf54cb8ac0dfcdad7b47;
    hash_changed=False. Reports=["reports/yaml_record_review/Fe_Nh42_So42_X_7_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    heptahydrate identity and final SSSOM row pass, but TRACE_ELEMENT is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4cb2fb1ee7a02d28
    - ev-74f2da9e4b43fa45
  - name: legacy-native-ids
    value: '["SEM:5e5d1e0aa9a20652a72b","SEM:a5ccd4b621cdf8846abf"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-74f2da9e4b43fa45
    - ev-4cb2fb1ee7a02d28
    - ev-afd54377fca0bb61
- assessment_id: a-f6907f71ec66b4c1
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-efa8f3ce848e6134
  evidence_ids:
  - ev-4cb2fb1ee7a02d28
  - ev-f6907f71ec66b4c1
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-4cb2fb1ee7a02d28
    - ev-f6907f71ec66b4c1
findings:
- finding_id: rec-f-0a507e686eb653f1
  issue_key: mim-reconciliation-role-support-efa8f3ce848e6134
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Fe(NH4)2(SO4)2 x 7 H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-efa8f3ce848e6134
  evidence_ids:
  - ev-4cb2fb1ee7a02d28
  - ev-f6907f71ec66b4c1
  - ev-c6ffbd3d08623d97
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
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
    finding_id: f-0a507e686eb653f1
actions:
- action_id: rec-action-0a507e686eb653f1
  description: 'Reassess prediction-only role support: Fe(NH4)2(SO4)2 x 7 H2O'
  finding_ids:
  - rec-f-0a507e686eb653f1
  target_ids:
  - record-efa8f3ce848e6134
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Fe_Nh42_So42_X_7_H2o.yaml
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
