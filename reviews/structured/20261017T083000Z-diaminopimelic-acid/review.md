# Per-record structured review: Diaminopimelic_Acid (data/ingredients/mapped/Diaminopimelic_Acid.yaml)

- Review: 20261017T083000Z-diaminopimelic-acid
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Diaminopimelic_Acid (data/ingredients/mapped/Diaminopimelic_Acid.yaml, record-c474af502c25f61c, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Diaminopimelic_Acid.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Diaminopimelic_Acid.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-c474af502c25f61c | data/ingredients/mapped/Diaminopimelic_Acid.yaml | maintained | Diaminopimelic_Acid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-c474af502c25f61c | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-c474af502c25f61c | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-c474af502c25f61c | Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-c474af502c25f61c.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-c474af502c25f61c.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:35:13Z; reviewed SHA-256=b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352; current SHA-256=b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352; hash_changed=False. Reports=["reports/yaml_record_review/Diaminopimelic_Acid.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact ChEBI synonym identity and final SSSOM payload pass, but the amino-acid-source role is computational.

### Historical provisional-role concern

evidence: concern. Targets: record-c474af502c25f61c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-cb221f347ac16e78: Reassess prediction-only role support: Diaminopimelic acid

major / open / confirmed; issue key: mim-reconciliation-role-support-c474af502c25f61c.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-cb221f347ac16e78

Reassess prediction-only role support: Diaminopimelic acid

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-26bd3a66e5ec46c9 | data/ingredients/mapped/Diaminopimelic_Acid.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[882],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:23673","line":884,"mapping_status":"MAPPED","ontology_id":"CHEBI:23673","preferred_term":"Diaminopimelic acid"}],"identifier":"CHEBI:23673","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:23673","ontology_label":"2,6-diaminopimelic acid","ontology_source":"CHEBI"},"preferred_term":"Diaminopimelic acid","sssom_rows":[{"data_row":1029,"object_id":"CHEBI:23673","object_label":"2,6-diaminopimelic acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Diaminopimelic_Acid","synonym_count":1} |
| ev-b2eef466ce53d773 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [882] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-717f48ed7767536d | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Diaminopimelic_Acid; data-row positions=[1029] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":1029,"object_id":"CHEBI:23673","object_label":"2,6-diaminopimelic acid","other":"2,6-diaminoheptanedioic acid&#124;CAS:583-93-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Diaminopimelic_Acid","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-3a3078cadfe726f0 | docs/data/mapped_ingredients.csv; CSV lines=[884] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:23673","line":884,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:23673","preferred_term":"Diaminopimelic acid","total_occurrences":"6"}] |
| ev-8cb48e4502f02e51 | reports/yaml_record_review/Diaminopimelic_Acid.md; &#96;data/ingredients/mapped/Diaminopimelic_Acid.yaml&#96;:2; Verdict:4; Identity:11; Validation:25; Evidence:38; Completeness:54; Recommended Edits:61 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-6be15c2b669623d8 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[533,1444] | context_only | [{"current_record_sha256":"b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352","finding_id":"SEM:5f3fab885497d5a50ab8","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352","finding_id":"SEM:4775276e6060398ef4bd","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-fe6e767f1f71a033 | data/ingredients/mapped/Diaminopimelic_Acid.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}] |
| ev-1d89410525eec53e | reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml; findings[finding_id=f-cb221f347ac16e78] | context_only | Predecessor structured review finding f-cb221f347ac16e78 in 20261011T024633Z-mim-reconcile-all-batch-05 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-diaminopimelic-acid
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Diaminopimelic_Acid (data/ingredients/mapped/Diaminopimelic_Acid.yaml)'
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
summary: Per-record structured review for Diaminopimelic_Acid (data/ingredients/mapped/Diaminopimelic_Acid.yaml,
  record-c474af502c25f61c, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Diaminopimelic_Acid.yaml
    sha256: b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352
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
  - path: reports/yaml_record_review/Diaminopimelic_Acid.md
    sha256: 9dc02ef6da64eef3caf857bc18f0139271e4b66f2168c3e408e3ea720f1a09e8
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-c474af502c25f61c
  path: data/ingredients/mapped/Diaminopimelic_Acid.yaml
  label: Diaminopimelic_Acid
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Diaminopimelic_Acid.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Diaminopimelic_Acid.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Diaminopimelic_Acid.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-c474af502c25f61c
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-c474af502c25f61c
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-c474af502c25f61c
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024633Z-mim-reconcile-all-batch-05
    and semantic review dispositions on HEAD.
  target_ids:
  - record-c474af502c25f61c
evidence:
- evidence_id: ev-26bd3a66e5ec46c9
  kind: record_content
  reference: data/ingredients/mapped/Diaminopimelic_Acid.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[882],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:23673","line":884,"mapping_status":"MAPPED","ontology_id":"CHEBI:23673","preferred_term":"Diaminopimelic
    acid"}],"identifier":"CHEBI:23673","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":6,"edge_count":6,"occurrences":6},"occurrence_statistics":{"media_count":6,"total_occurrences":6},"ontology_mapping":{"mapping_quality":"SYNONYM_MATCH","ontology_id":"CHEBI:23673","ontology_label":"2,6-diaminopimelic
    acid","ontology_source":"CHEBI"},"preferred_term":"Diaminopimelic acid","sssom_rows":[{"data_row":1029,"object_id":"CHEBI:23673","object_label":"2,6-diaminopimelic
    acid","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Diaminopimelic_Acid","synonym_count":1}'
  snapshot_sha256: b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352
- evidence_id: ev-b2eef466ce53d773
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [882]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-717f48ed7767536d
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Diaminopimelic_Acid; data-row positions=[1029]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":1029,"object_id":"CHEBI:23673","object_label":"2,6-diaminopimelic
    acid","other":"2,6-diaminoheptanedioic acid|CAS:583-93-7","predicate_id":"skos:exactMatch","subject_id":"MIM:Diaminopimelic_Acid","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-3a3078cadfe726f0
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[884]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:23673","line":884,"mapping_quality":"SYNONYM_MATCH","mapping_status":"MAPPED","media_count":"6","ontology_id":"CHEBI:23673","preferred_term":"Diaminopimelic
    acid","total_occurrences":"6"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-8cb48e4502f02e51
  kind: prior_review
  reference: reports/yaml_record_review/Diaminopimelic_Acid.md
  locator: '`data/ingredients/mapped/Diaminopimelic_Acid.yaml`:2; Verdict:4; Identity:11;
    Validation:25; Evidence:38; Completeness:54; Recommended Edits:61'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 9dc02ef6da64eef3caf857bc18f0139271e4b66f2168c3e408e3ea720f1a09e8
  quote: "Recommended Edits:\n- Major: source or remove `nutritional_roles.AMINO_ACID_SOURCE`\
    \ in\n  `data/ingredients/mapped/Diaminopimelic_Acid.yaml`, then synchronize\n\
    \  `data/curated/mapped_ingredients.yaml`."
- evidence_id: ev-6be15c2b669623d8
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[533,1444]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352","finding_id":"SEM:5f3fab885497d5a50ab8","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352","finding_id":"SEM:4775276e6060398ef4bd","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-fe6e767f1f71a033
  kind: record_content
  reference: data/ingredients/mapped/Diaminopimelic_Acid.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:33709 (amino acid)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"AMINO_ACID_SOURCE"}}]'
  snapshot_sha256: b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352
- evidence_id: ev-1d89410525eec53e
  kind: prior_review
  reference: reviews/structured/20261011T024633Z-mim-reconcile-all-batch-05/review.yaml
  locator: findings[finding_id=f-cb221f347ac16e78]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-cb221f347ac16e78 in 20261011T024633Z-mim-reconcile-all-batch-05
  snapshot_sha256: 7549030a5b50ed98868ff3497507fdfbfecd07cd858c76738f734521fa9d3603
assessments:
- assessment_id: a-e2d5a926920ffd46
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-c474af502c25f61c
  evidence_ids:
  - ev-26bd3a66e5ec46c9
  - ev-b2eef466ce53d773
  - ev-717f48ed7767536d
  - ev-3a3078cadfe726f0
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ced329ac8daf29a6
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-c474af502c25f61c
  evidence_ids:
  - ev-8cb48e4502f02e51
  - ev-26bd3a66e5ec46c9
  - ev-6be15c2b669623d8
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T14:35:13Z;
    reviewed SHA-256=b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352;
    current SHA-256=b83e338a6f3ddffdd2f713708857efab65602294afcfe43a6a053b96a54fe352;
    hash_changed=False. Reports=["reports/yaml_record_review/Diaminopimelic_Acid.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The exact
    ChEBI synonym identity and final SSSOM payload pass, but the amino-acid-source
    role is computational.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8cb48e4502f02e51
    - ev-26bd3a66e5ec46c9
  - name: legacy-native-ids
    value: '["SEM:5f3fab885497d5a50ab8","SEM:4775276e6060398ef4bd"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-26bd3a66e5ec46c9
    - ev-8cb48e4502f02e51
    - ev-6be15c2b669623d8
- assessment_id: a-fe6e767f1f71a033
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c474af502c25f61c
  evidence_ids:
  - ev-8cb48e4502f02e51
  - ev-fe6e767f1f71a033
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-8cb48e4502f02e51
    - ev-fe6e767f1f71a033
findings:
- finding_id: rec-f-cb221f347ac16e78
  issue_key: mim-reconciliation-role-support-c474af502c25f61c
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Diaminopimelic acid'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-c474af502c25f61c
  evidence_ids:
  - ev-8cb48e4502f02e51
  - ev-fe6e767f1f71a033
  - ev-1d89410525eec53e
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Diaminopimelic_Acid.yaml
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
    review_id: 20261011T024633Z-mim-reconcile-all-batch-05
    finding_id: f-cb221f347ac16e78
actions:
- action_id: rec-action-cb221f347ac16e78
  description: 'Reassess prediction-only role support: Diaminopimelic acid'
  finding_ids:
  - rec-f-cb221f347ac16e78
  target_ids:
  - record-c474af502c25f61c
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Diaminopimelic_Acid.yaml
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
  with lineage to 20261011T024633Z-mim-reconcile-all-batch-05.
```
