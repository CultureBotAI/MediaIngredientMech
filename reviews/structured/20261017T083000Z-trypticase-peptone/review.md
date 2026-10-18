# Per-record structured review: Trypticase_Peptone (data/ingredients/mapped/Trypticase_Peptone.yaml)

- Review: 20261017T083000Z-trypticase-peptone
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Trypticase_Peptone (data/ingredients/mapped/Trypticase_Peptone.yaml, record-36912a2cbd109e55, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Trypticase_Peptone.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Trypticase_Peptone.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-36912a2cbd109e55 | data/ingredients/mapped/Trypticase_Peptone.yaml | maintained | Trypticase_Peptone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-36912a2cbd109e55 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-36912a2cbd109e55 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-36912a2cbd109e55 | Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-36912a2cbd109e55.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-36912a2cbd109e55.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:59:28Z; reviewed SHA-256=88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c; current SHA-256=88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c; hash_changed=False. Reports=["reports/yaml_record_review/Trypticase_Peptone.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact MICRO identity and catalog variants pass, but PROTEIN_SOURCE is provisional name-pattern evidence.

### Historical provisional-role concern

evidence: concern. Targets: record-36912a2cbd109e55.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-bc6dceb790baa9d8: Reassess prediction-only role support: Trypticase peptone

major / open / confirmed; issue key: mim-reconciliation-role-support-36912a2cbd109e55.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-bc6dceb790baa9d8

Reassess prediction-only role support: Trypticase peptone

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-e3c3d1568ca0f5dc | data/ingredients/mapped/Trypticase_Peptone.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2007],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000175","line":2009,"mapping_status":"MAPPED","ontology_id":"MICRO:0000175","preferred_term":"Trypticase peptone"}],"identifier":"MICRO:0000175","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":785,"edge_count":785,"occurrences":785},"occurrence_statistics":{"media_count":785,"total_occurrences":785},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000175","ontology_label":"Trypticase peptone","ontology_source":"MICRO"},"preferred_term":"Trypticase peptone","sssom_rows":[{"data_row":2843,"object_id":"MICRO:0000175","object_label":"Trypticase peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trypticase_Peptone","synonym_count":6} |
| ev-8b11c874663c9ef0 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [2007] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-3a2eed21045c3aba | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Trypticase_Peptone; data-row positions=[2843] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":2843,"object_id":"MICRO:0000175","object_label":"Trypticase peptone","other":"Trypticase peptone (BD-BBL)&#124;Trypticase peptone (BD BBL)&#124;Trypticase Peptone (BBL)&#124;Trypticase Peptone (BD 211921)&#124;Tripticase peptone","predicate_id":"skos:exactMatch","subject_id":"MIM:Trypticase_Peptone","validation_method":"none&#124;UNKNOWN_TERM&#124;2026-07-07"}] |
| ev-0b586aa0aa00902b | docs/data/mapped_ingredients.csv; CSV lines=[2009] | supports | Published identity and count rows inspected: [{"identifier":"MICRO:0000175","line":2009,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"785","ontology_id":"MICRO:0000175","preferred_term":"Trypticase peptone","total_occurrences":"785"}] |
| ev-536dd1391c9e81c0 | reports/yaml_record_review/Trypticase_Peptone.md; &#96;data/ingredients/mapped/Trypticase_Peptone.yaml&#96;:2; Verdict:4; Identity:10; Validation:21; Evidence:29; Issues:40; Major: &#96;PROTEIN_SOURCE&#96; is provisional name-pattern evidence:42; Completeness:59; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-89095f4cb54692bb | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[1320,2027] | context_only | [{"current_record_sha256":"88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c","finding_id":"SEM:9d5cc3687eec672dc660","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c","finding_id":"SEM:e036d1ef042fdede0c9e","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-ec620736f336fa27 | data/ingredients/mapped/Trypticase_Peptone.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional role from a curated name-pattern rule; review recommended.","reference_text":"Inferred from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}] |
| ev-4aef88a9c005cfa9 | reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml; findings[finding_id=f-bc6dceb790baa9d8] | context_only | Predecessor structured review finding f-bc6dceb790baa9d8 in 20261011T024639Z-mim-reconcile-all-batch-12 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.

## Complete Structured Record

The sibling review.yaml is authoritative.

````yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-trypticase-peptone
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Trypticase_Peptone (data/ingredients/mapped/Trypticase_Peptone.yaml)'
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
summary: Per-record structured review for Trypticase_Peptone (data/ingredients/mapped/Trypticase_Peptone.yaml,
  record-36912a2cbd109e55, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Trypticase_Peptone.yaml
    sha256: 88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c
    role: target
  - path: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
    sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
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
  - path: reports/yaml_record_review/Trypticase_Peptone.md
    sha256: 532f121d9f9eff2528a1007098d909cdf09e418bed6ba083f68fc67520458776
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-36912a2cbd109e55
  path: data/ingredients/mapped/Trypticase_Peptone.yaml
  label: Trypticase_Peptone
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trypticase_Peptone.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Trypticase_Peptone.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Trypticase_Peptone.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-36912a2cbd109e55
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-36912a2cbd109e55
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-36912a2cbd109e55
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024639Z-mim-reconcile-all-batch-12
    and semantic review dispositions on HEAD.
  target_ids:
  - record-36912a2cbd109e55
evidence:
- evidence_id: ev-e3c3d1568ca0f5dc
  kind: record_content
  reference: data/ingredients/mapped/Trypticase_Peptone.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[2007],"raw_equal":true},"docs_rows":[{"identifier":"MICRO:0000175","line":2009,"mapping_status":"MAPPED","ontology_id":"MICRO:0000175","preferred_term":"Trypticase
    peptone"}],"identifier":"MICRO:0000175","ingredient_type":"UNDEFINED_MIXTURE","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":785,"edge_count":785,"occurrences":785},"occurrence_statistics":{"media_count":785,"total_occurrences":785},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"MICRO:0000175","ontology_label":"Trypticase
    peptone","ontology_source":"MICRO"},"preferred_term":"Trypticase peptone","sssom_rows":[{"data_row":2843,"object_id":"MICRO:0000175","object_label":"Trypticase
    peptone","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Trypticase_Peptone","synonym_count":6}'
  snapshot_sha256: 88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c
- evidence_id: ev-8b11c874663c9ef0
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [2007]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-3a2eed21045c3aba
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Trypticase_Peptone; data-row positions=[2843]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":2843,"object_id":"MICRO:0000175","object_label":"Trypticase
    peptone","other":"Trypticase peptone (BD-BBL)|Trypticase peptone (BD BBL)|Trypticase
    Peptone (BBL)|Trypticase Peptone (BD 211921)|Tripticase peptone","predicate_id":"skos:exactMatch","subject_id":"MIM:Trypticase_Peptone","validation_method":"none|UNKNOWN_TERM|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-0b586aa0aa00902b
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[2009]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"MICRO:0000175","line":2009,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"785","ontology_id":"MICRO:0000175","preferred_term":"Trypticase
    peptone","total_occurrences":"785"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-536dd1391c9e81c0
  kind: prior_review
  reference: reports/yaml_record_review/Trypticase_Peptone.md
  locator: '`data/ingredients/mapped/Trypticase_Peptone.yaml`:2; Verdict:4; Identity:10;
    Validation:21; Evidence:29; Issues:40; Major: `PROTEIN_SOURCE` is provisional
    name-pattern evidence:42; Completeness:59; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 532f121d9f9eff2528a1007098d909cdf09e418bed6ba083f68fc67520458776
  quote: "Issues:\n\n\nMajor: `PROTEIN_SOURCE` is provisional name-pattern evidence:\n\
    The only role assertion is:\n\n```yaml\nnutritional_roles:\n- role: PROTEIN_SOURCE\n\
    \  confidence: 0.8\n  evidence:\n  - reference_type: COMPUTATIONAL_PREDICTION\n\
    \    reference_text: Inferred from curated media-role name pattern\n    curator_note:\
    \ Provisional role from a curated name-pattern rule; review recommended.\n```\n\
    \nThe exact MICRO identity does not independently curate the protein-source\n\
    role.\n\nRecommended Edits:\n- Replace the `PROTEIN_SOURCE` computational prediction\
    \ with curated\n  database/literature evidence, or remove `nutritional_roles`\
    \ until such\n  support is added."
- evidence_id: ev-89095f4cb54692bb
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[1320,2027]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c","finding_id":"SEM:9d5cc3687eec672dc660","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c","finding_id":"SEM:e036d1ef042fdede0c9e","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-ec620736f336fa27
  kind: record_content
  reference: data/ingredients/mapped/Trypticase_Peptone.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.8,"evidence":[{"curator_note":"Provisional
    role from a curated name-pattern rule; review recommended.","reference_text":"Inferred
    from curated media-role name pattern","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"PROTEIN_SOURCE"}}]'
  snapshot_sha256: 88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c
- evidence_id: ev-4aef88a9c005cfa9
  kind: prior_review
  reference: reviews/structured/20261011T024639Z-mim-reconcile-all-batch-12/review.yaml
  locator: findings[finding_id=f-bc6dceb790baa9d8]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-bc6dceb790baa9d8 in 20261011T024639Z-mim-reconcile-all-batch-12
  snapshot_sha256: 20e55e956f704a8c90164bf2749b9ddf6c35d94cdcbab538776d0675aa150899
assessments:
- assessment_id: a-58ee5893f2f58cce
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-36912a2cbd109e55
  evidence_ids:
  - ev-e3c3d1568ca0f5dc
  - ev-8b11c874663c9ef0
  - ev-3a2eed21045c3aba
  - ev-0b586aa0aa00902b
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-9e0ca96612965af3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-36912a2cbd109e55
  evidence_ids:
  - ev-536dd1391c9e81c0
  - ev-e3c3d1568ca0f5dc
  - ev-89095f4cb54692bb
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-17T19:59:28Z;
    reviewed SHA-256=88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c;
    current SHA-256=88e513d4f6e6fa153ae508047b9a654922dad2bab84d4624cca2a17ade2b742c;
    hash_changed=False. Reports=["reports/yaml_record_review/Trypticase_Peptone.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    MICRO identity and catalog variants pass, but PROTEIN_SOURCE is provisional name-pattern
    evidence.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-536dd1391c9e81c0
    - ev-e3c3d1568ca0f5dc
  - name: legacy-native-ids
    value: '["SEM:9d5cc3687eec672dc660","SEM:e036d1ef042fdede0c9e"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-e3c3d1568ca0f5dc
    - ev-536dd1391c9e81c0
    - ev-89095f4cb54692bb
- assessment_id: a-ec620736f336fa27
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-36912a2cbd109e55
  evidence_ids:
  - ev-536dd1391c9e81c0
  - ev-ec620736f336fa27
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-536dd1391c9e81c0
    - ev-ec620736f336fa27
findings:
- finding_id: rec-f-bc6dceb790baa9d8
  issue_key: mim-reconciliation-role-support-36912a2cbd109e55
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Trypticase peptone'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-36912a2cbd109e55
  evidence_ids:
  - ev-536dd1391c9e81c0
  - ev-ec620736f336fa27
  - ev-4aef88a9c005cfa9
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trypticase_Peptone.yaml
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
    review_id: 20261011T024639Z-mim-reconcile-all-batch-12
    finding_id: f-bc6dceb790baa9d8
actions:
- action_id: rec-action-bc6dceb790baa9d8
  description: 'Reassess prediction-only role support: Trypticase peptone'
  finding_ids:
  - rec-f-bc6dceb790baa9d8
  target_ids:
  - record-36912a2cbd109e55
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Trypticase_Peptone.yaml
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
  with lineage to 20261011T024639Z-mim-reconcile-all-batch-12.
````
