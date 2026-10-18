# Per-record structured review: Cellotriose (data/ingredients/mapped/Cellotriose.yaml)

- Review: 20261017T083000Z-cellotriose
- Repository: CultureBotAI/MediaIngredientMech
- Started UTC: 2026-10-17T08:25:00Z
- Finished UTC: 2026-10-17T08:30:00Z
- Reviewer: Antigravity (independent)
- Completion: partial
- Verdict: needs_curation
- Scientific review: false

## Summary

Per-record structured review for Cellotriose (data/ingredients/mapped/Cellotriose.yaml, record-857c99ee53adfa6a, mapping_status=MAPPED). Records 1 open finding(s) and 0 deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).

## Scope And Provenance

Per-record structured review of data/ingredients/mapped/Cellotriose.yaml covering current record state, role evidence support, published surfaces, and residual historical review claims.

Selection: Single record data/ingredients/mapped/Cellotriose.yaml selected from full-corpus review of all 2,953 ingredient records on HEAD.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 3751d80fbd916de878be918aa481371020cc75bb.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| record-857c99ee53adfa6a | data/ingredients/mapped/Cellotriose.yaml | maintained | Cellotriose |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Current record and published surface consistency | passed | True | record-857c99ee53adfa6a | Verified current YAML against maintained aggregates, exact-subject SSSOM rows, and published CSV exports. |
| Role evidence and plausibility check | failed | True | record-857c99ee53adfa6a | Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION or empty evidence. |
| Predecessor structured review and semantic disposition reconciliation | passed | True | record-857c99ee53adfa6a | Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04 and semantic review dispositions on HEAD. |

## Scientific And Domain Assessments

### Current record and published surfaces

consistency: supported. Targets: record-857c99ee53adfa6a.

Current YAML and its maintained aggregate agree under the documented overlay exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export gates pass within their stated limits.

Membership summaries are keyed by identifier, not record address: duplicate records and tombstones may share an identity. They are not evidence that counts should be copied between records.

### Historical review coverage and residual narrative

provenance: unknown. Targets: record-857c99ee53adfa6a.

The legacy concern set remains only partially reconciled. Specific dispositions below apply solely to their named subclaims; other identity, source, component, synonym, and conditional recommendations still need targeted reassessment.

Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:34:31Z; reviewed SHA-256=e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f; current SHA-256=e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f; hash_changed=False. Reports=["reports/yaml_record_review/Cellotriose.md"]. Full reports, including older originals behind refresh floors, are hashed inputs. Repeated refresh allegations are not counted as new defects. The narrative group is not a count of distinct scientific findings. Latest manifest note: The exact CHEBI cellotriose identity, structure fields, zero occurrence count, SSSOM row, and aggregate copy pass, but CARBON_SOURCE is only provisional.

### Historical provisional-role concern

evidence: concern. Targets: record-857c99ee53adfa6a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Findings

### rec-f-098a886cd42589c6: Reassess prediction-only role support: Cellotriose

major / open / confirmed; issue key: mim-reconciliation-role-support-857c99ee53adfa6a.

Prediction-only payloads remain on the named current role assertions. This confirms the local evidence gap, not that the biological role is false. Native positive context receipts=[].

## Recommended Actions And Acceptance Checks

### rec-action-098a886cd42589c6

Reassess prediction-only role support: Cellotriose

- Address the exact fields/tokens and evidence gap described in this finding; preserve unrelated source labels and audit history.
- Inspect the original preparation, organism, or mapping evidence where needed; do not promote a label/name-pattern inference to proof.
- For an authorized fix, synchronize maintained surfaces, run focused validation, and save an evidence-backed successor citing this finding.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev-8d0100911d64c4f7 | data/ingredients/mapped/Cellotriose.yaml; Complete YAML parsed; identity, roles, synonyms, occurrences, history and optional payloads inspected by bounded checks. | partial | {"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[689],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3528","line":691,"mapping_status":"MAPPED","ontology_id":"CHEBI:3528","preferred_term":"Cellotriose"}],"identifier":"CHEBI:3528","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3528","ontology_label":"cellotriose","ontology_source":"CHEBI"},"preferred_term":"Cellotriose","sssom_rows":[{"data_row":712,"object_id":"CHEBI:3528","object_label":"cellotriose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cellotriose","synonym_count":2} |
| ev-b39d52e9456bac20 | data/curated/mapped_ingredients.yaml; ingredients positions (zero-based): [689] | supports | Exactly one (identifier, preferred_term) row; semantic equality after excluding only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True. |
| ev-6073784a1c7af637 | mappings/ingredient_mappings.sssom.tsv; subject_id=MIM:Cellotriose; data-row positions=[712] | context_only | Current exact-subject rows, including complete other payload: [{"data_row":712,"object_id":"CHEBI:3528","object_label":"cellotriose","other":"beta-D-glucopyranosyl-(1-&gt;4)-beta-D-glucopyranosyl-(1-&gt;4)-D-glucopyranose&#124;beta-D-glucopyranosyl-(1-&gt;4)-beta-D-glucopyranosyl-(1-&gt;4)-D-glucose&#124;CAS:33404-34-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Cellotriose","validation_method":"OAK+OLS:chebi&#124;CONFIRMED&#124;2026-07-07"}] |
| ev-94f6f2999567b588 | docs/data/mapped_ingredients.csv; CSV lines=[691] | supports | Published identity and count rows inspected: [{"identifier":"CHEBI:3528","line":691,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3528","preferred_term":"Cellotriose","total_occurrences":"0"}] |
| ev-e5a54ebdde86d054 | reports/yaml_record_review/Cellotriose.md; &#96;data/ingredients/mapped/Cellotriose.yaml&#96;:2; Verdict:4; Identity:12; Validation:24; Evidence:41; Completeness:56; Recommended Edits:64 | context_only | Whole historical report loaded, including evidence, caveats and follow-up sections. Original allegations and recommendations below are historical, not new instructions or verified conclusions. |
| ev-d4081a255c913916 | reports/semantic_review_20260921/resolution/finding-dispositions.tsv; lines=[390,1505] | context_only | [{"current_record_sha256":"e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f","finding_id":"SEM:36fdb0b326d696fbe13d","kind":"existing_record_review","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f","finding_id":"SEM:3da0ae1e7d2c5715ea61","kind":"role_evidence","resolution_reason":"Historical finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}] |
| ev-94bc7c53c6e013d0 | data/ingredients/mapped/Cellotriose.yaml; nutritional_roles[0] | supports | Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION: [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}] |
| ev-7bfcc620bffc327f | reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml; findings[finding_id=f-098a886cd42589c6] | context_only | Predecessor structured review finding f-098a886cd42589c6 in 20261011T024632Z-mim-reconcile-all-batch-04 |

## Limits And Additional Notes

- Read-only per-record structured review (scientific_review: false); no ingredient YAML, curated aggregate, or SSSOM files were modified.
- Confirmed local evidence gaps and structural issues are recorded as open with bounded remediation actions; historical or source-context claims requiring primary recipe/literature verification remain deferred (provisional).
- Derived from full-corpus review on HEAD (3751d80fbd916de878be918aa481371020cc75bb) with lineage to 20261011T024632Z-mim-reconcile-all-batch-04.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261017T083000Z-cellotriose
kind: record
repository: CultureBotAI/MediaIngredientMech
title: 'Per-record structured review: Cellotriose (data/ingredients/mapped/Cellotriose.yaml)'
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
summary: Per-record structured review for Cellotriose (data/ingredients/mapped/Cellotriose.yaml,
  record-857c99ee53adfa6a, mapping_status=MAPPED). Records 1 open finding(s) and 0
  deferred finding(s) bound to current HEAD (3751d80fbd916de878be918aa481371020cc75bb).
source:
  git_revision: 3751d80fbd916de878be918aa481371020cc75bb
  state: working_tree
  inputs:
  - path: data/ingredients/mapped/Cellotriose.yaml
    sha256: e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f
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
  - path: reports/yaml_record_review/Cellotriose.md
    sha256: 398f926ca15733944c253fefba1272f3769962541172d864c47e45204b1d783c
    role: context
  - path: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
    sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
    role: context
targets:
- target_id: record-857c99ee53adfa6a
  path: data/ingredients/mapped/Cellotriose.yaml
  label: Cellotriose
  kind: maintained
  record_class: IngredientRecord
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellotriose.yaml
    role: maintained ingredient
scope:
  description: Per-record structured review of data/ingredients/mapped/Cellotriose.yaml
    covering current record state, role evidence support, published surfaces, and
    residual historical review claims.
  selection: Single record data/ingredients/mapped/Cellotriose.yaml selected from
    full-corpus review of all 2,953 ingredient records on HEAD.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - record-857c99ee53adfa6a
checks:
- check_id: surface-consistency
  name: Current record and published surface consistency
  status: passed
  required: true
  summary: Verified current YAML against maintained aggregates, exact-subject SSSOM
    rows, and published CSV exports.
  target_ids:
  - record-857c99ee53adfa6a
- check_id: role-evidence-audit
  name: Role evidence and plausibility check
  status: failed
  required: true
  summary: Role assertions on nutritional_roles[0] rely only on COMPUTATIONAL_PREDICTION
    or empty evidence.
  target_ids:
  - record-857c99ee53adfa6a
- check_id: predecessor-reconciliation
  name: Predecessor structured review and semantic disposition reconciliation
  status: passed
  required: true
  summary: Reconciled against predecessor batch review 20261011T024632Z-mim-reconcile-all-batch-04
    and semantic review dispositions on HEAD.
  target_ids:
  - record-857c99ee53adfa6a
evidence:
- evidence_id: ev-8d0100911d64c4f7
  kind: record_content
  reference: data/ingredients/mapped/Cellotriose.yaml
  locator: Complete YAML parsed; identity, roles, synonyms, occurrences, history and
    optional payloads inspected by bounded checks.
  accessed_at: '2026-10-11T02:46:28Z'
  support: partial
  summary: '{"aggregate":{"equal":true,"excluded_overlay_fields":["discussions"],"matching_rows":1,"path":"data/curated/mapped_ingredients.yaml","positions":[689],"raw_equal":true},"docs_rows":[{"identifier":"CHEBI:3528","line":691,"mapping_status":"MAPPED","ontology_id":"CHEBI:3528","preferred_term":"Cellotriose"}],"identifier":"CHEBI:3528","ingredient_type":"SINGLE_INGREDIENT","mapping_status":"MAPPED","membership_by_identifier":{"distinct_recipes":0,"edge_count":0,"occurrences":0},"occurrence_statistics":{"media_count":0,"total_occurrences":0},"ontology_mapping":{"mapping_quality":"EXACT_MATCH","ontology_id":"CHEBI:3528","ontology_label":"cellotriose","ontology_source":"CHEBI"},"preferred_term":"Cellotriose","sssom_rows":[{"data_row":712,"object_id":"CHEBI:3528","object_label":"cellotriose","predicate_id":"skos:exactMatch"}],"sssom_subject":"MIM:Cellotriose","synonym_count":2}'
  snapshot_sha256: e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f
- evidence_id: ev-b39d52e9456bac20
  kind: validation
  reference: data/curated/mapped_ingredients.yaml
  locator: 'ingredients positions (zero-based): [689]'
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: Exactly one (identifier, preferred_term) row; semantic equality after excluding
    only exporter-declared PER_RECORD_AUTHORED_FIELDS=["discussions"]. Raw equality=True.
  snapshot_sha256: 4ff96cd6d6728db6d5d35c03e9adf03ff994de6fe092ae2266a9f7bf13a6886b
- evidence_id: ev-6073784a1c7af637
  kind: record_content
  reference: mappings/ingredient_mappings.sssom.tsv
  locator: subject_id=MIM:Cellotriose; data-row positions=[712]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: 'Current exact-subject rows, including complete other payload: [{"data_row":712,"object_id":"CHEBI:3528","object_label":"cellotriose","other":"beta-D-glucopyranosyl-(1->4)-beta-D-glucopyranosyl-(1->4)-D-glucopyranose|beta-D-glucopyranosyl-(1->4)-beta-D-glucopyranosyl-(1->4)-D-glucose|CAS:33404-34-1","predicate_id":"skos:exactMatch","subject_id":"MIM:Cellotriose","validation_method":"OAK+OLS:chebi|CONFIRMED|2026-07-07"}]'
  snapshot_sha256: 89ec9cbd634e958ab07cfae5021594834dfc49a584365f3917da136505e400b9
- evidence_id: ev-94f6f2999567b588
  kind: record_content
  reference: docs/data/mapped_ingredients.csv
  locator: CSV lines=[691]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Published identity and count rows inspected: [{"identifier":"CHEBI:3528","line":691,"mapping_quality":"EXACT_MATCH","mapping_status":"MAPPED","media_count":"0","ontology_id":"CHEBI:3528","preferred_term":"Cellotriose","total_occurrences":"0"}]'
  snapshot_sha256: c15ebf8ca7ab0fe780c57cb696337c454c9232bafccd57cd9bf2abd582290474
- evidence_id: ev-e5a54ebdde86d054
  kind: prior_review
  reference: reports/yaml_record_review/Cellotriose.md
  locator: '`data/ingredients/mapped/Cellotriose.yaml`:2; Verdict:4; Identity:12;
    Validation:24; Evidence:41; Completeness:56; Recommended Edits:64'
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: Whole historical report loaded, including evidence, caveats and follow-up
    sections. Original allegations and recommendations below are historical, not new
    instructions or verified conclusions.
  snapshot_sha256: 398f926ca15733944c253fefba1272f3769962541172d864c47e45204b1d783c
  quote: "Recommended Edits:\n- Major: either replace `nutritional_roles.CARBON_SOURCE`\
    \ with inspected\n  evidence for cellotriose as a carbon source in media, or remove\
    \ the role,\n  then rerun strict validation, SSSOM QC, aggregate roundtrip, and\n\
    \  `git diff --check`."
- evidence_id: ev-d4081a255c913916
  kind: prior_review
  reference: reports/semantic_review_20260921/resolution/finding-dispositions.tsv
  locator: lines=[390,1505]
  accessed_at: '2026-10-11T02:46:28Z'
  support: context_only
  summary: '[{"current_record_sha256":"e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f","finding_id":"SEM:36fdb0b326d696fbe13d","kind":"existing_record_review","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"},{"current_record_sha256":"e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f","finding_id":"SEM:3da0ae1e7d2c5715ea61","kind":"role_evidence","resolution_reason":"Historical
    finding remains unresolved; no blanket approval.","resolution_status":"OPEN"}]'
  snapshot_sha256: abc3299188d9e666ca7f0df1fad03ece80827c4e007634a41ced296e6bdc5989
- evidence_id: ev-94bc7c53c6e013d0
  kind: record_content
  reference: data/ingredients/mapped/Cellotriose.yaml
  locator: nutritional_roles[0]
  accessed_at: '2026-10-11T02:46:28Z'
  support: supports
  summary: 'Every evidence entry on these current assertions is COMPUTATIONAL_PREDICTION:
    [{"field":"nutritional_roles[0]","role":{"confidence":0.7,"evidence":[{"curator_note":"Provisional
    role inferred from CHEBI is_a/has_role closure; review recommended.","reference_text":"Inferred
    from CHEBI ancestry: subclass/has_role of CHEBI:16646 (carbohydrate)","reference_type":"COMPUTATIONAL_PREDICTION"}],"role":"CARBON_SOURCE"}}]'
  snapshot_sha256: e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f
- evidence_id: ev-7bfcc620bffc327f
  kind: prior_review
  reference: reviews/structured/20261011T024632Z-mim-reconcile-all-batch-04/review.yaml
  locator: findings[finding_id=f-098a886cd42589c6]
  accessed_at: '2026-10-17T08:30:00Z'
  support: context_only
  summary: Predecessor structured review finding f-098a886cd42589c6 in 20261011T024632Z-mim-reconcile-all-batch-04
  snapshot_sha256: 304aa2f246d52fcfef2fb5165e9b4c0995c263df5e818c23b30e9d76e3ec55e3
assessments:
- assessment_id: a-700e48848c0ba2a5
  area: consistency
  topic: Current record and published surfaces
  outcome: supported
  summary: Current YAML and its maintained aggregate agree under the documented overlay
    exclusion. Exact-subject SSSOM and published CSV rows were inspected; corpus structural/export
    gates pass within their stated limits.
  target_ids:
  - record-857c99ee53adfa6a
  evidence_ids:
  - ev-8d0100911d64c4f7
  - ev-b39d52e9456bac20
  - ev-6073784a1c7af637
  - ev-94f6f2999567b588
  details: 'Membership summaries are keyed by identifier, not record address: duplicate
    records and tombstones may share an identity. They are not evidence that counts
    should be copied between records.'
- assessment_id: a-984548c68f54696b
  area: provenance
  topic: Historical review coverage and residual narrative
  outcome: unknown
  summary: The legacy concern set remains only partially reconciled. Specific dispositions
    below apply solely to their named subclaims; other identity, source, component,
    synonym, and conditional recommendations still need targeted reassessment.
  target_ids:
  - record-857c99ee53adfa6a
  evidence_ids:
  - ev-e5a54ebdde86d054
  - ev-8d0100911d64c4f7
  - ev-d4081a255c913916
  details: 'Latest manifest verdict=needs_curation; severity=major; reviewed_at=2026-09-16T11:34:31Z;
    reviewed SHA-256=e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f;
    current SHA-256=e8fdd559e5b4b015d6def5e031a80f3dd2c0e54f145b95c25c403308ddecd87f;
    hash_changed=False. Reports=["reports/yaml_record_review/Cellotriose.md"]. Full
    reports, including older originals behind refresh floors, are hashed inputs. Repeated
    refresh allegations are not counted as new defects. The narrative group is not
    a count of distinct scientific findings. Latest manifest note: The exact CHEBI
    cellotriose identity, structure fields, zero occurrence count, SSSOM row, and
    aggregate copy pass, but CARBON_SOURCE is only provisional.'
  dimensions:
  - name: legacy-disposition
    value: needs_reassessment
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e5a54ebdde86d054
    - ev-8d0100911d64c4f7
  - name: legacy-native-ids
    value: '["SEM:36fdb0b326d696fbe13d","SEM:3da0ae1e7d2c5715ea61"]'
    definition: Existing SEM ledger identities retained for handoff, not common structured
      previous_occurrences.
    evidence_ids:
    - ev-8d0100911d64c4f7
    - ev-e5a54ebdde86d054
    - ev-d4081a255c913916
- assessment_id: a-94bc7c53c6e013d0
  area: evidence
  topic: Historical provisional-role concern
  outcome: concern
  summary: Prediction-only payloads remain on the named current role assertions. This
    confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-857c99ee53adfa6a
  evidence_ids:
  - ev-e5a54ebdde86d054
  - ev-94bc7c53c6e013d0
  dimensions:
  - name: legacy-disposition
    value: still_open
    definition: Disposition of this explicitly bounded allegation or narrative group
      only; not whole-record approval.
    evidence_ids:
    - ev-e5a54ebdde86d054
    - ev-94bc7c53c6e013d0
findings:
- finding_id: rec-f-098a886cd42589c6
  issue_key: mim-reconciliation-role-support-857c99ee53adfa6a
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: 'Reassess prediction-only role support: Cellotriose'
  description: Prediction-only payloads remain on the named current role assertions.
    This confirms the local evidence gap, not that the biological role is false. Native
    positive context receipts=[].
  target_ids:
  - record-857c99ee53adfa6a
  evidence_ids:
  - ev-e5a54ebdde86d054
  - ev-94bc7c53c6e013d0
  - ev-7bfcc620bffc327f
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellotriose.yaml
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
    finding_id: f-098a886cd42589c6
actions:
- action_id: rec-action-098a886cd42589c6
  description: 'Reassess prediction-only role support: Cellotriose'
  finding_ids:
  - rec-f-098a886cd42589c6
  target_ids:
  - record-857c99ee53adfa6a
  owner_paths:
  - repository: CultureBotAI/MediaIngredientMech
    path: data/ingredients/mapped/Cellotriose.yaml
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
