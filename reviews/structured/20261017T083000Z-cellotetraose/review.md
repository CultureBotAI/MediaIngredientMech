# Per-record structured review: Cellotetraose (data/ingredients/mapped/Cellotetraose.yaml)

- Review: 20261017T083000Z-cellotetraose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cellotetraose (data/ingredients/mapped/Cellotetraose.yaml, record-6b497733fd0e0372, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cellotetraose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cellotetraose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-6b497733fd0e0372 | data/ingredients/mapped/Cellotetraose.yaml | maintained | Cellotetraose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-6b497733fd0e0372 | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-6b497733fd0e0372 | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-6b497733fd0e0372 | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-6b497733fd0e0372.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-6b497733fd0e0372.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:34:31Z; reviewed SHA-256=fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a; current SHA-256=fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a; hash_changed=False. Reports=["reports/yaml_record_review/Cellotetraose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cellotetraose identity, structure fields, zero occurrence count, SSSOM row, and aggregate copy pass, but CARBON_SOURCE is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-6b497733fd0e0372.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-f052be68797cfc18: Reassess prediction-only role support: Cellotetraose

major / open / confirmed; issue key: mim-reconciliation-role-support-6b497733fd0e0372.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-f052be68797cfc18

Reassess prediction-only role support: Cellotetraose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-906c5277344cbcdc | data/ingredients/mapped/Cellotetraose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[688],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62974","line":690,"mapping_status":"MAPPED","ontology_id":"CHEBI:62974","preferred_term":"Cellotetraose"}],"identifier":"CHEBI:62974","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:62974","ontology_label":"cellotetraose","ontology_source":"CHEBI"},"preferred_term":"Cellotetraose","sssom_rows":[{"data_row":711,"object_id":"CHEBI:62974","object_label":"cellotetraose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cellotetraose","synonym_count":1} |
| ev-eecd1baffa2732ad | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [688] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6f905192680cb981 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cellotetraose; data-row positions=[711] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":711,"object_id":"CHEBI:62974","object_label":"cellotetraose","other":"beta-D-glucopyranosyl-(1-&gt;4)-beta-D-glucoopyranosyl-(1-&gt;4)-beta-D-glucoopyranosyl-(1-&gt;4)-D-glucoopyranose&#124;CAS:38819-01-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Cellotetraose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-47a52d6b887bb9dd | docs/data/mapped_ingredients.csv; CSV lines=[690] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:62974","line":690,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:62974","preferred_term":"Cellotetraose","total_occurrences":"0"}] |
| ev-171c1aca4a36f02e | reports/yaml_record_review/Cellotetraose.md; &#96;data/ingredients/mapped/Cellotetraose.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:41; Completeness:57; Recommended Edits:65 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-325eac95346580e3 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[389,2031] | context_only | [{"current_record_sha256":"fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a","finding_id":"SEM:5514ae697e3ef1231122","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a","finding_id":"SEM:5185a89ce4a5b796f22a","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-1f89cae3d5b835c1 | data/ingredients/mapped/Cellotetraose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-252375aa14f1f6c3 | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-f052be68797cfc18] | context_only | Predecessor structured review finding f-f052be68797cfc18 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cellotetraose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cellotetraose (data/ingredients/mapped/Cellotetraose.yaml)'
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
summary: Per-record structured review for Cellotetraose (data/ingredients/mapped/Cellotetraose.yaml,
  record-6b497733fd0e0372, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cellotetraose.yaml
    sha256: fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a
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
  - path: reports/yaml_record_review/Cellotetraose.md
    sha256: 00d169a46c52d88886a46fd004202654c06c36269084131684675bc0e4c0dcd2
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-6b497733fd0e0372
  path: data/ingredients/mapped/Cellotetraose.yaml
  label: Cellotetraose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellotetraose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cellotetraose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cellotetraose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-6b497733fd0e0372
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-6b497733fd0e0372
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-6b497733fd0e0372
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-6b497733fd0e0372
evidence:
- evidence_id: ev-906c5277344cbcdc
  kind: record_content
  reference: data/ingredients/mapped/Cellotetraose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[688],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:62974","line":690,"mapping_status":"MAPPED","ontology_id":"CHEBI:62974","preferred_term":"Cellotetraose"}],"identifier":"CHEBI:62974","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:62974","ontology_label":"cellotetraose","ontology_source":"CHEBI"},"preferred_term":"Cellotetraose","sssom_rows":[{"data_row":711,"object_id":"CHEBI:62974","object_label":"cellotetraose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cellotetraose","synonym_count":1}'
  snapshot_sha256: fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a
- evidence_id: ev-eecd1baffa2732ad
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [688]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6f905192680cb981
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cellotetraose; data-row positions=[711]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":711,"object_id":"CHEBI:62974","object_label":"cellotetraose","other":"beta-D-glucopyranosyl-(1->4)-beta-D-glucoopyranosyl-(1->4)-beta-D-glucoopyranosyl-(1->4)-D-glucoopyranose|CAS:38819-01-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Cellotetraose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-47a52d6b887bb9dd
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[690]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:62974","line":690,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:62974","preferred_term":"Cellotetraose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-171c1aca4a36f02e
  kind: prior_review
  reference: reports/yaml_record_review/Cellotetraose.md
  locator: '`data/ingredients/mapped/Cellotetraose.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:41; Completeness:57; Recommended Edits:65'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 00d169a46c52d88886a46fd004202654c06c36269084131684675bc0e4c0dcd2
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ with inspected\n  evidence for cellotetraose as a carbon source in media, or\
    \ remove the role,\n  then rerun strict validation, SSSOM QC, aggregate roundtrip,\
    \ and\n  `git diff --check`."
- evidence_id: ev-325eac95346580e3
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[389,2031]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a","finding_id":"SEM:5514ae697e3ef1231122","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a","finding_id":"SEM:5185a89ce4a5b796f22a","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-1f89cae3d5b835c1
  kind: record_content
  reference: data/ingredients/mapped/Cellotetraose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a
- evidence_id: ev-252375aa14f1f6c3
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-f052be68797cfc18]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-f052be68797cfc18 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-c418987f7220f86f
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-6b497733fd0e0372
  evidence_ids:
  - ev-906c5277344cbcdc
  - ev-eecd1baffa2732ad
  - ev-6f905192680cb981
  - ev-47a52d6b887bb9dd
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-ef4be62bd6a574f3
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-6b497733fd0e0372
  evidence_ids:
  - ev-171c1aca4a36f02e
  - ev-906c5277344cbcdc
  - ev-325eac95346580e3
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:34:31Z;
    reviewed SHA-256=fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a;
    current SHA-256=fcc75737b8a2ef59b23520cc623bdcb7da4bdf6a0c7e2c5f1933facc251aaa4a;
    hash_changed=False. Reports=["reports/yaml_record_review/Cellotetraose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    cellotetraose identity, structure fields, zero occurrence count, SSSOM row, and
    aggregate copy pass, but CARBON_SOURCE is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-171c1aca4a36f02e
    - ev-906c5277344cbcdc
  - name: legacy-native-ids
    value: '["SEM:5514ae697e3ef1231122","SEM:5185a89ce4a5b796f22a"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-906c5277344cbcdc
    - ev-171c1aca4a36f02e
    - ev-325eac95346580e3
- assessment_id: a-1f89cae3d5b835c1
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6b497733fd0e0372
  evidence_ids:
  - ev-171c1aca4a36f02e
  - ev-1f89cae3d5b835c1
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-171c1aca4a36f02e
    - ev-1f89cae3d5b835c1
findings:
- finding_id: rec-f-f052be68797cfc18
  issue_key: mim-reconciliation-role-support-6b497733fd0e0372
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cellotetraose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-6b497733fd0e0372
  evidence_ids:
  - ev-171c1aca4a36f02e
  - ev-1f89cae3d5b835c1
  - ev-252375aa14f1f6c3
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellotetraose.yaml
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
    finding_id: f-f052be68797cfc18
actions:
- action_id: rec-action-f052be68797cfc18
  description: 'Reassess prediction-only role support: Cellotetraose'
  finding_ids:
  - rec-f-f052be68797cfc18
  target_ids:
  - record-6b497733fd0e0372
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellotetraose.yaml
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
