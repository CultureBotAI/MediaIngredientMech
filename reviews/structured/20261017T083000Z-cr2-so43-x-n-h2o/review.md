# Per-record structured review: Cr2_So43_X_N_H2o (data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml)

- Review: 20261017T083000Z-cr2-so43-x-n-h2o
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cr2_So43_X_N_H2o (data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml, record-4e80df1ec775dd84, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-4e80df1ec775dd84 | data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml | maintained | Cr2_So43_X_N_H2o |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-4e80df1ec775dd84 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-4e80df1ec775dd84 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-4e80df1ec775dd84 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-4e80df1ec775dd84.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-4e80df1ec775dd84.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:36:40Z; reviewed SHA-256=0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504; current SHA-256=0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504; hash_changed=False. Reports=["reports/yaml_record_review/Cr2_So43_X_N_H2o.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The local variable chromium sulfate hydrate identity and 3/3 count pass, but its trace-element role is only computationally supported.

### Historical provisional-role concern

evidence: concern. Targets: record-4e80df1ec775dd84.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-994fe54e17a908f0: Reassess prediction-only role support: Cr2(SO4)3 x n H2O

major / open / confirmed; issue key: mim-reconciliation-role-support-4e80df1ec775dd84.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-994fe54e17a908f0

Reassess prediction-only role support: Cr2(SO4)3 x n H2O

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-637407deee126d43 | data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[763],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cr2_so43_x_n_h2o","line":765,"mapping_status":"MAPPED","ontology_id":"CHEBI:53471","preferred_term":"Cr2(SO4)3 x n H2O"}],"identifier":"kgmicrobe.compound:cr2_so43_x_n_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:53471","ontology_label":"chromium(III) sulfate","ontology_source":"CHEBI"},"preferred_term":"Cr2(SO4)3 x n H2O","sssom_rows":[{"data_row":823,"object_id":"CHEBI:53471","object_label":"chromium(III) sulfate","predicate_id":"skos:broadMatch"},{"data_row":824,"object_id":"kgmicrobe.compound:cr2_so43_x_n_h2o","object_label":"Cr2(SO4)3 x n H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cr2_So43_X_N_H2o","synonym_count":0} |
| ev-17056796790c72da | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [763] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-a8099c3f5b1d0ede | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cr2_So43_X_N_H2o; data-row positions=[823,824] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":823,"object_id":"CHEBI:53471","object_label":"chromium(III) sulfate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Cr2_So43_X_N_H2o","validation_method":"manual:reconcile_sssom&#124;PREDICATE&#124;2026-09-20"},{"data_row":824,"object_id":"kgmicrobe.compound:cr2_so43_x_n_h2o","object_label":"Cr2(SO4)3 x n H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cr2_So43_X_N_H2o","validation_method":""}] |
| ev-f3d169eb4345e803 | docs/data/mapped_ingredients.csv; CSV lines=[765] | supports | Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cr2_so43_x_n_h2o","line":765,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:53471","preferred_term":"Cr2(SO4)3 x n H2O","total_occurrences":"3"}] |
| ev-e8ccf517ed5a09e8 | reports/yaml_record_review/Cr2_So43_X_N_H2o.md; &#96;data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml&#96;:2; Verdict:4; Identity:13; Validation:28; Evidence:49; Completeness:67; Recommended Edits:74 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-4043779687f114ad | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[444,1832] | context_only | [{"current_record_sha256":"0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504","finding_id":"SEM:c0c5cead9cc97c75f5ad","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504","finding_id":"SEM:ab6bbaddf9d46a07815f","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-266fe5371479edc3 | data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional in-session LLM role assignment; review recommended.","reference_text":"Assigned by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}] |
| ev-790ac0cd522220e4 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-994fe54e17a908f0] | context_only | Predecessor structured review finding f-994fe54e17a908f0 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cr2-so43-x-n-h2o
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cr2_So43_X_N_H2o (data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml)'
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
summary: Per-record structured review for Cr2_So43_X_N_H2o (data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml,
  record-4e80df1ec775dd84, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
    sha256: 0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504
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
  - path: reports/yaml_record_review/Cr2_So43_X_N_H2o.md
    sha256: f1d9b5a1b143f620f8fd53591e8b73dea10ad9680fad473040a3cc37335051c6
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-4e80df1ec775dd84
  path: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
  label: Cr2_So43_X_N_H2o
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml selected
    from full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-4e80df1ec775dd84
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-4e80df1ec775dd84
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-4e80df1ec775dd84
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-4e80df1ec775dd84
evidence:
- evidence_id: ev-637407deee126d43
  kind: record_content
  reference: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[763],"raw_equal":true},"docs_rows":[{"identifier":"kgmicrobe.compound:cr2_so43_x_n_h2o","line":765,"mapping_status":"MAPPED","ontology_id":"CHEBI:53471","preferred_term":"Cr2(SO4)3
    x n H2O"}],"identifier":"kgmicrobe.compound:cr2_so43_x_n_h2o","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":3,"edge_count":3,"occurrences":3},"occurrence_statistics":{"media_count":3,"total_occurrences":3},"ontology_mapping":{"mapping_quality":"NARROW_MATCH","ontology_id":"CHEBI:53471","ontology_label":"chromium(III)
    sulfate","ontology_source":"CHEBI"},"preferred_term":"Cr2(SO4)3 x n H2O","sssom_rows":[{"data_row":823,"object_id":"CHEBI:53471","object_label":"chromium(III)
    sulfate","predicate_id":"skos:broadMatch"},{"data_row":824,"object_id":"kgmicrobe.compound:cr2_so43_x_n_h2o","object_label":"Cr2(SO4)3
    x n H2O","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cr2_So43_X_N_H2o","synonym_count":0}'
  snapshot_sha256: 0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504
- evidence_id: ev-17056796790c72da
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [763]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-a8099c3f5b1d0ede
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cr2_So43_X_N_H2o; data-row positions=[823,824]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":823,"object_id":"CHEBI:53471","object_label":"chromium(III)
    sulfate","other":"","predicate_id":"skos:broadMatch","subject_id":"MIM:Cr2_So43_X_N_H2o","validation_method":"manual:reconcile_sssom|PREDICATE|2026-09-20"},{"data_row":824,"object_id":"kgmicrobe.compound:cr2_so43_x_n_h2o","object_label":"Cr2(SO4)3
    x n H2O","other":"","predicate_id":"skos:exactMatch","subject_id":"MIM:Cr2_So43_X_N_H2o","validation_method":""}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-f3d169eb4345e803
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[765]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"kgmicrobe.compound:cr2_so43_x_n_h2o","line":765,"mapping_quality":"NARROW_MATCH","mapping_status":"MAPPED","media_count":"3","ontology_id":"CHEBI:53471","preferred_term":"Cr2(SO4)3
    x n H2O","total_occurrences":"3"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e8ccf517ed5a09e8
  kind: prior_review
  reference: reports/yaml_record_review/Cr2_So43_X_N_H2o.md
  locator: '`data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`:2; Verdict:4; Identity:13;
    Validation:28; Evidence:49; Completeness:67; Recommended Edits:74'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: f1d9b5a1b143f620f8fd53591e8b73dea10ad9680fad473040a3cc37335051c6
  quote: "Recommended Edits:\n- Major: in `data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml`,\
    \ either replace\n  `nutritional_roles.TRACE_ELEMENT` with inspected evidence\
    \ for chromium(III)\n  sulfate hydrate as a trace element in this media scope,\
    \ or remove the role.\n- Regenerate synchronized products and rerun strict validation,\
    \ SSSOM QC,\n  aggregate roundtrip, and `git diff --check`."
- evidence_id: ev-4043779687f114ad
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[444,1832]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504","finding_id":"SEM:c0c5cead9cc97c75f5ad","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504","finding_id":"SEM:ab6bbaddf9d46a07815f","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-266fe5371479edc3
  kind: record_content
  reference: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.6,"evidence":[{"curator_note":"Provisional
    in-session LLM role assignment; review recommended.","reference_text":"Assigned
    by in-session Claude reasoning (no external API)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"TRACE_ELEMENT"}}]'
  snapshot_sha256: 0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504
- evidence_id: ev-790ac0cd522220e4
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-994fe54e17a908f0]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-994fe54e17a908f0 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-dc2bc1118b626fdc
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-4e80df1ec775dd84
  evidence_ids:
  - ev-637407deee126d43
  - ev-17056796790c72da
  - ev-a8099c3f5b1d0ede
  - ev-f3d169eb4345e803
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-d94a2f12d15e4e8a
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-4e80df1ec775dd84
  evidence_ids:
  - ev-e8ccf517ed5a09e8
  - ev-637407deee126d43
  - ev-4043779687f114ad
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T12:36:40Z;
    reviewed SHA-256=0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504;
    current SHA-256=0b7e77f7f4f3d09677a869564b459ba02dc82699ff142dfe20b7fc873c0a3504;
    hash_changed=False. Reports=["reports/yaml_record_review/Cr2_So43_X_N_H2o.md"].
    Full reports, including older originals behind refresh floors, are hashed inputs.
    Repeated refresh allegations are not counted as new defects. The narrative group
    is not a count of distinct scientific findings. Latest manifest note: The local
    variable chromium sulfate hydrate identity and 3/3 count pass, but its trace-element
    role is only computationally supported.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e8ccf517ed5a09e8
    - ev-637407deee126d43
  - name: legacy-native-ids
    value: '["SEM:c0c5cead9cc97c75f5ad","SEM:ab6bbaddf9d46a07815f"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-637407deee126d43
    - ev-e8ccf517ed5a09e8
    - ev-4043779687f114ad
- assessment_id: a-266fe5371479edc3
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4e80df1ec775dd84
  evidence_ids:
  - ev-e8ccf517ed5a09e8
  - ev-266fe5371479edc3
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e8ccf517ed5a09e8
    - ev-266fe5371479edc3
findings:
- finding_id: rec-f-994fe54e17a908f0
  issue_key: mim-reconciliation-role-support-4e80df1ec775dd84
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cr2(SO4)3 x n H2O'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-4e80df1ec775dd84
  evidence_ids:
  - ev-e8ccf517ed5a09e8
  - ev-266fe5371479edc3
  - ev-790ac0cd522220e4
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
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
    review_id: 20261011T024632Z-mim-reconcile-all-batch-04
    finding_id: f-994fe54e17a908f0
actions:
- action_id: rec-action-994fe54e17a908f0
  description: 'Reassess prediction-only role support: Cr2(SO4)3 x n H2O'
  finding_ids:
  - rec-f-994fe54e17a908f0
  target_ids:
  - record-4e80df1ec775dd84
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cr2_So43_X_N_H2o.yaml
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
  with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.
```
